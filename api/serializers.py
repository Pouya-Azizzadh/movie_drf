from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ListMovie, Movie, Comment, Genre
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=False)
    confirm_password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("username", "password",'confirm_password', 'token')

    def get_tokens(self, user):
        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data


    def create(self, validated_data):
        del validated_data['confirm_password']
        user = User.objects.create_user(
            **validated_data
        )
        return user

    def validate(self, value):
        if value.get('password') != value.get("confirm_password"):
            raise serializers.ValidationError("password not match")
        return value


class GenreList(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "title"]


class MovieList(serializers.ModelSerializer):
    gener = GenreList(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'poster',
                  'disk_image', 'imdb', 'story', 'gener']


class Lists(serializers.ModelSerializer):
    list = MovieList(many=True, read_only=True)

    class Meta:
        model = ListMovie
        fields = ['id', 'title', 'list']


class CommentMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'movie']
