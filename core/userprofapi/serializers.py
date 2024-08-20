
#from rest_framework import serializers
from userprof.models import *
from django.contrib.auth.models import User
from rest_framework import serializers
#from .models import User, userprofilee


class colorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['color_name']
        model = colour


class userserializers(serializers.ModelSerializer):
    class Meta:
        fields = ['username','email','password']
        model = User
  

        


'''
class PostaddressSerializer(serializers.ModelSerializer):
    user=userserializers()
    class Meta:
        fields = ['addressUser','user']
        model = userprofilee
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user, created = User.objects.get_or_create(**user_data)  # Retrieve or create the user

        # If multiple addresses are provided, handle them
        if isinstance(validated_data['addressUser'], list):
            addresses = validated_data.pop('addressUser')
            user_profiles = [userprofilee.objects.create(user=user, addressUser=address) for address in addresses]
        else:
            # Handle single address
            user_profiles = [userprofilee.objects.create(user=user, **validated_data)]

        return user_profiles
        '''''''
        user_data = validated_data.pop('user')
        usero = User.objects.create(**user_data)
        user_profile = userprofilee.objects.create(user=usero,**validated_data)
        return user_profile

class PostaddressSerializer(serializers.ModelSerializer):
    user = userserializers()
    addressUser = MultipleAddressField()

    class Meta:
        model = userprofilee
        fields = ['addressUser', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user, created = User.objects.get_or_create(**user_data)

        addresses = validated_data.pop('addressUser')
        user_profiles = [userprofilee.objects.create(user=user, addressUser=address) for address in addresses]

        return user_profiles
'''


class MultipleAddressField(serializers.ListField):
    child = serializers.CharField()

class PostaddressSerializer(serializers.ModelSerializer):
    user = userserializers()
    addressUser = MultipleAddressField()  # Use the custom list field for addresses

    class Meta:
        model = userprofilee
        fields = ['addressUser', 'user']

    def create(self, validated_data):
        # Extract user data and addressUser data
        user_data = validated_data.pop('user')
        addresses = validated_data.pop('addressUser')

        # Create the user instance
        #usero = User.objects.create(**user_data)
        usero = User.objects.create(username = user_data['username'],email=user_data["email"])
        usero.set_password(user_data['password'])
        usero.save()


        # Create a userprofilee instance for each address
        user_profiles = []
        for address in addresses:
            user_profile = userprofilee.objects.create(user=usero, addressUser=address)
            user_profiles.append(user_profile)

        return user_profiles  # Return the list of created user profiles

    def to_representation(self, instance):
        """
        Override the to_representation method to return a list of user profiles.
        """
        if isinstance(instance, list):
            return [super().to_representation(item) for item in instance]
        return super().to_representation(instance)

  

#seconday way start


class addressSerializer(serializers.ModelSerializer):
      class Meta:
        fields = ['addressUser']
        model = userprofilee












#seconday way end
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






'''
class userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostaddressSerializer(serializers.ModelSerializer):
    user = userserializers()

    class Meta:
        model = userprofilee
        fields = ['addressUser', 'user']

    def create(self, validated_data):
        # Extract the user data
        user_data = validated_data.pop('user')
        addresses = validated_data.pop('addressUser')

        # Ensure addresses is a list
        if not isinstance(addresses, list):
            addresses = [addresses]

        # Get or create the user
        user, created = User.objects.get_or_create(**user_data)

        # Create userprofilee instances for each address
        user_profiles = []
        for address in addresses:
            user_profile = userprofilee.objects.create(user=user, addressUser=address)
            user_profiles.append(user_profile)

        return user_profiles  # Return the list of created user profiles

    def to_representation(self, instance):
        """
        Override the to_representation method to correctly serialize a list of userprofilee instances.
        """
        if isinstance(instance, list):
            return [super().to_representation(item) for item in instance]
        return super().to_representation(instance)
'''