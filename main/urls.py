from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post/',views.post,name='create-post'),
    path('edit-post/<int:post_id>/',views.edit_post,name='edit-post'),
    path('delete/<post_id>',views.delete_post,name='delete'),
]