from rest_framework import serializers
from .models import CustomUser 

class regserialiser(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email','password']

    def create(self,validated_data):
        user=CustomUser(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.role=2
        user.save()
        return user
    
class logserialiser(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'

    def update(self, instance, validated_data):
        if instance.is_blocked==True:
            instance.is_blocked=False
        else:
            instance.is_blocked=True
        instance.save()        
        return instance