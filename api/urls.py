from django.urls import path
from .views import Movies,DetailMovie,GroupMovie,GroupMovieLists,GetComment,PostComment,SearchMovie,SignUpUser,GetUserDetail


urlpatterns = [
    path("movies/",Movies.as_view(),name="movies"),
    path("movie/<pk>",DetailMovie,name="movie"),
    path("movies/search/<pk>",SearchMovie,name="moviesearch"),
    path("list/",GroupMovieLists,name="lists"),
    path("list/<pk>",GroupMovie,name="list"),
    path("comment/<pk>",GetComment,name="comment"),
    path("post-comment/",PostComment,name="addcomment"),
    path("signup/",SignUpUser.as_view(),name="signup"),
    path("get-user/<pk>",GetUserDetail,name='user')

]















