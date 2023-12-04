from rest_framework import serializers

from .models import Paragraph, WordIndex
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id', 'text', 'created_at', 'modified_at')

class WordIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordIndex
        fields = ('paragraph', 'word')



































