
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from callofdutyapi.models import Gun
from callofdutyapi.models import GunStat
from callofdutyapi.models import Stat



class Guns(ViewSet):
    def list(self, request):
        guns=Gun.objects.all()
        serializer=GunSerlializer(
            guns, many=True, context={'request':request}
        )
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        gun=Gun.objects.get(pk=pk)
        gunstats=GunStat.objects.filter(gun_id=pk)
        # serializer=GunSerlializer(
        #     gun, many=False, context={'request':request}
        # )
        serializer=GunStatSerlializer(
            gunstats, many=True, context={'request':request}
        )
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