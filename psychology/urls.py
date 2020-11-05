from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    url(r'^api/post/$', views.Post_getter.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api/register-user/$', views.Register_user.as_view()),
    url(r'^api/add-comment/$', views.Comment_getter.as_view()),
    url(r'^api/get-comment/$', views.Comment_getter.as_view()),
    url(r'^api/set-profile/$', views.Add_Profile.as_view()),
    url(r'^api/get-post/(?P<pk>[0-9]+)/', views.Get_Individual_Post.as_view()),
    url(r'^api/get-userprofile/(?P<pk>[0-9]+)/', views.Get_User_Profile.as_view()),
    url(r'^api/get-comment/(?P<pk>[0-9]+)/', views.Get_Individual_Comment.as_view()),
    url(r'^api/update-userprofile/(?P<pk>[0-9]+)/', views.Update_userprofile.as_view()),
    url(r'^api/update-usersign-in/(?P<pk>[0-9]+)/', views.Register_user.as_view()), 
    url(r'^api/delete-comment/(?P<pk>[0-9]+)/', views.Get_Individual_Comment.as_view()),
    url(r'^api/delete-post/(?P<pk>[0-9]+)/', views.Get_Individual_Post.as_view()),
    url(r'^api/delete-user/(?P<pk>[0-9]+)/', views.Register_user.as_view()), 

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)