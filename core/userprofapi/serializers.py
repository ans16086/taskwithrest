from rest_framework import serializers
from userprof.models import *



class colorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['color_name']
        model = colour


class userserializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User

        

class PostaddressSerializer(serializers.ModelSerializer):
    users=userserializers()
    class Meta:
        fields = '__all__'
        model = userprofilee





class PostdeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'deleteq')
        model = deletebutton

'''
ALLAH wasta da ware ha mara naal anu
class testmodelserial(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'age')
        model = testmodel
'''       
class testomodelserial(serializers.ModelSerializer):
   
   
   #country = serializers.SerializerMethodField()
   #color= colorSerializer()
   class Meta:
        fields = ['color','username']
        model = testomodel
   
   def get_country(self,obj):
        new_color=colour.objects.get(id=obj.color.id)  
        return {'color':new_color.color_name,'hex':'001'} 
    
       