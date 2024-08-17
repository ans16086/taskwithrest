from rest_framework import serializers
from userprof.models import *


class PostaddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'addressUser')
        model = userprofilee





class PostdeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'deleteq',)
        model = deletebutton

'''
class testmodelserial(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = testmodel
'''        