from django.urls import path
from myblog.views import post_list, post_detail, post_share

app_name = 'myblog'

urlpatterns = [
    path('share/<int:post_pk>', post_share, name='post_share'),
    path('', post_list, name='post_list'),
    path('post_detail/<int:post_pk>', post_detail, name='post_detail'),
    path('tag/<tag_slug>', post_list, name='post_list_by_tag'),

]
