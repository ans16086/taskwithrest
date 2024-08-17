from rest_framework import serializers
from userprof.models import *


class PostaddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'addressUser')
        model = userprofilee





class PostdeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'deleteq',)
        model = deletebutton
