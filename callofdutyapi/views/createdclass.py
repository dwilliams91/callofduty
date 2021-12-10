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
        print("dude")
        serializer=CreatedClassSerlializer(
            created_class_selected, many=False, context={'request':request}
        )
        return Response(serializer.data)


class CreatedClassSerlializer(serializers.ModelSerializer):
    class Meta:
        model=CreatedClass
        fields=['name','base_gun']