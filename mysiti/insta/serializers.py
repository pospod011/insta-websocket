from django.contrib.auth import authenticate
from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  ]
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_date):
        user = UserProfile.objects.create_user(**validated_date)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),

        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Не верный пароль или логин ")


    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),

        }




class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['image', 'video']






class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['like']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'text']



class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'



class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'


class SaveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveItem
        fields = '__all__'



class PostDetailSerializer(serializers.ModelSerializer):
    post_like = PostLikeSerializer(many=True, read_only=True)
    post_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['image', 'video', 'description', 'created_at', 'post_like', 'post_comment', 'hashtag']

