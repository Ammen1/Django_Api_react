from rest_framework import serializers
from users.models import NewUser
from base.models import Post


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    

    class Meta:
        model = NewUser
        fields = ("email", "full_name", "phone", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PostSerializers(serializers.ModelSerializer):
    full_name = serializers.CharField(source='author.full_name', read_only=True)
    email = serializers.EmailField(source='author.email', read_only=True)
    word_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('id','full_name', 'email', 'word_count')