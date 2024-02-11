from django.urls import path, include
from . import views
from chunked_upload.views import ChunkedUploadView
from chunked_upload.views import ChunkedUploadCompleteView
from django.contrib.auth import views as auth_views

#here i have mapped each tab of app to specific view function of views.py
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('log_out/', auth_views.LogoutView.as_view(), name='logout'),
    path('index', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('add_user', views.add_user, name='add_user'),
    path('add_user/', views.add_user, name='add_user'),
    path('users/delete_user <int:id>/', views.delete_user, name='delete_user'),
    path('upload_data/', views.upload_data, name='upload_data'),
    path('upload_chunked/', ChunkedUploadView.as_view(), name='upload_chunked'),
    path('upload_chunked_complete/', ChunkedUploadCompleteView.as_view(), name='upload_chunked_complete'),
    path('query_builder/', views.query_builder, name='query_builder'),
]
