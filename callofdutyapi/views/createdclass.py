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
        created_class_selected=CreatedClass.objects.get(pk=pk)
        serializer=CreatedClassSerlializer(
            created_class_selected, many=False, context={'request':request}
        )
        class_workable_data=serializer.data
        print(class_workable_data)
        print(class_workable_data['base_gun'])
        my_gun_stats=GunStat.objects.filter(gun_id=class_workable_data['base_gun'])
        my_gun_stats_workable=GunStatSerlializer(my_gun_stats, many=True, context={'request':request})
        my_gun_stats_workable=my_gun_stats_workable.data
        
        print(my_gun_stats_workable[0]['stat_id']['name'])
        new_object={}
        for item in my_gun_stats_workable:
            new_object[item['stat_id']['name']]=item['value']
        print(new_object)
        
        # getting attachments
        my_slots=AttachmentSlot.objects.filter(createdclass_id=pk)
        my_slots_workable=AttachmentSlotSerializer(my_slots, many=True, context={'request':request}).data
        for item in my_slots_workable:
            attachment_id=my_slots_workable[0]['attachment_id']
            print(attachment_id)
        # get createdclass
        # get associated gun
        # get associated gun stats
        # get associated attachmentslots
        # get associated attachment
        # get associated attachment stats
        # modify value for gunstat
        return Response(serializer.data)

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
    class Meta:
        model=AttachmentSlot
        fields=['attachment_id','stat_id', 'effect']