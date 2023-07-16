from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,CreateAPIView
from django.contrib.auth.models import User
from rest_framework import permissions,authentication
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import AccessToken
 
#serializer
from .serializers import MovieList,Lists,CommentMovieSerializer,SignUpSerializer,UserSerializer

# models


from .models import Movie,ListMovie,Comment





@api_view(["GET"])
def GetUserDetail(request,pk):
    access_token_obj = AccessToken(pk)
    user_id=access_token_obj['user_id']
    user=User.objects.get(id=user_id)
    content =  {'user_id': user_id, 'user':user.username}
    return Response(content)




class SignUpUser(CreateAPIView):
    model = User() 
    serializer_class = SignUpSerializer

    
class Movies(ListAPIView):
    #permission_classes=[permissions.IsAuthenticated]
    queryset =Movie.objects.all()
    serializer_class=MovieList
    filter_backends =(DjangoFilterBackend,SearchFilter)
    filterset_fields =['title']
    search_fields=("title",)




@api_view(["GET"])
def DetailMovie(request,pk):
    
    movie=Movie.objects.get(title=pk)
    serializer=MovieList(movie,many=False)
    return Response(serializer.data)


@api_view(["GET"])
class SearchMovie(ListAPIView):
    queryset =Movie.objects.all()
    serializer_class=MovieList

@api_view(["GET"])
def GroupMovieLists(request):
    list=ListMovie.objects.all()
    serializer=Lists(list,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def GroupMovie(request,pk):
    list=ListMovie.objects.get(id=pk)
    serializer=Lists(list,many=False)
    return Response(serializer.data)

@api_view(["GET"])
def GetComment(request,pk):
    CommentUser=Comment.objects.filter(movie__id=pk)
    serializer=CommentMovieSerializer(CommentUser,many=True)
    return Response(serializer.data)


@api_view(["POST"])
def PostComment(request):
    serializer=CommentMovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

