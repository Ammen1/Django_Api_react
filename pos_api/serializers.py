from rest_framework import serializers
from base.models import Post
from django.conf import settings




class PostSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='author.full_name', read_only=True)
    email = serializers.EmailField(source='author.email', read_only=True)
    word_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'audio', 'excerpt', 'content', 'author', 'full_name', 'email', 'word_count')




class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'full_name','phone')
        extra_kwargs = {'password': {'write_only': True}}