from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from callofdutyapi.models import Gun
from callofdutyapi.models import GunStat
from callofdutyapi.models import Stat
from callofdutyapi.models import CreatedClass
from callofdutyapi.models import AttachmentSlot
from callofdutyapi.models import AttachmentStat
from callofdutyapi.models import Attachment

class CreatedClasses(ViewSet):
    def retrieve(self, request, pk=None):
        # get the selected class
        created_class_selected=CreatedClass.objects.get(pk=pk)
        selected_class_serializer=CreatedClassSerlializer(
            created_class_selected, many=False, context={'request':request}
        )
        class_workable_data=selected_class_serializer.data
        
        # get the associated gunstats 
        my_gun_stats=GunStat.objects.filter(gun_id=class_workable_data['base_gun'])
        my_gun_stats_workable=GunStatSerlializer(my_gun_stats, many=True, context={'request':request})
        my_gun_stats_workable=my_gun_stats_workable.data
        
        # create a new dictionary with the keys and values of the associated gunstats
        selected_gun_with_stats={}
        for item in my_gun_stats_workable:
            selected_gun_with_stats[item['stat_id']['name']]=item['value']
        
        # getting attachments
        my_slots=AttachmentSlot.objects.filter(createdclass_id=pk)
        my_slots_workable=AttachmentSlotSerializer(my_slots, many=True, context={'request':request}).data
        list_of_attachments=[]
        for x in range(len(my_slots_workable)):
            attachment_id=my_slots_workable[x]['attachment_id']
            list_of_attachments.append(attachment_id)
        all_attachment_stats_out_of_order=[]
        for item in list_of_attachments:
            attachment_stat=AttachmentStat.objects.filter(attachment_id=item)
            attachment_stat_workable=AttachmentStatSerializer(attachment_stat, many=True, context={'request':request}).data
            all_attachment_stats_out_of_order.append(attachment_stat_workable)
        all_attachment_stats=[]
        for item in all_attachment_stats_out_of_order:
            for stat in item:
                all_attachment_stats.append(stat)
                
        # create a dictionary for attachments
        attachment_object={}
        for item in all_attachment_stats:
            if item['stat_id']['name'] not in attachment_object.keys():
                attachment_object[item['stat_id']['name']]=float(item['effect'])
            else:
                new_value=attachment_object[item['stat_id']['name']]+float(item['effect'])
                attachment_object[item['stat_id']['name']]=new_value
        
        # modify the selected guns properly
        for attachment_stat in attachment_object.keys():
            for gun_stat in selected_gun_with_stats.keys():
                if attachment_stat==gun_stat:
                    selected_gun_with_stats[gun_stat]=float(selected_gun_with_stats[gun_stat])*attachment_object[attachment_stat]+float(selected_gun_with_stats[gun_stat])
        selected_gun_with_stats['gun']=class_workable_data['base_gun']
        return Response(selected_gun_with_stats)

class GunSerlializer(serializers.ModelSerializer):
    class Meta:
        model=Gun
        fields=['name','gun_type']

class StatSerlializer(serializers.ModelSerializer):
    class Meta:
        model=Stat
        fields=['name']
        
class GunStatSerlializer(serializers.ModelSerializer):
    gun_id=GunSerlializer(many=False)
    stat_id=StatSerlializer(many=False)
    class Meta:
        model=GunStat
        fields=['gun_id','stat_id', 'value']
        
class CreatedClassSerlializer(serializers.ModelSerializer):
    # base_gun=GunSerlializer(many=False)
    class Meta:
        model=CreatedClass
        fields=['name','base_gun',]
        
class AttachmentSlotSerializer(serializers.ModelSerializer):
    attachment_id=Attachment()
    class Meta:
        model=AttachmentSlot
        fields=['name','attachment_id']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attachment
        fields=['name']

class AttachmentStatSerializer(serializers.ModelSerializer):
    stat_id=StatSerlializer(many=False)
    class Meta:
        model=AttachmentStat
        fields=['attachment_id','stat_id', 'effect']