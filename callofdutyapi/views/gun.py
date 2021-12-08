
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from callofdutyapi.models import Gun

class Guns(ViewSet):
    def list(self, request):
        guns=Gun.objects.all()
        serializer=GunSerlializer(
            guns, many=True, context={'request':request}
        )
        return Response(serializer.data)

class GunSerlializer(serializers.ModelSerializer):
    class Meta:
        model=Gun
        fields=['name','gun_type']