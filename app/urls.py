from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.home_view, name='home'),
    path('search-users/', views.search_users_view, name='search_users'),

    path('user/<str:username>/', views.profile_user_view, name='user_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('follow/<str:username>/', views.follow_toggle, name='follow_toggle'),

    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('add_post/', views.add_post_view, name='add_post'),
    path('add_story/', views.add_story_view, name='add_story'),
    path('story/<int:story_id>/', views.view_story, name='view_story'),
    path('post/<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('send_post_dm/', views.send_post_dm, name='send_post_dm'),

    path('explore/', views.explore_view, name='explore'),
    path('reels/', views.reels_view, name='reels'),
    path('reels/add/', views.add_reel_view, name='add_reel'),

    path('like/<int:post_id>/', views.like_toggle_ajax, name='like_toggle_ajax'),
    path('comment/<int:post_id>/', views.add_comment_ajax, name='add_comment_ajax'),
    path('reel/like/<int:reel_id>/', views.reel_like_toggle_ajax, name='reel_like_toggle_ajax'),
    path('reel/comment/<int:reel_id>/', views.add_reel_comment_ajax, name='add_reel_comment_ajax'),
    path('share/post/<int:post_id>/', views.post_share_link, name='post_share_link'),
    path('share/reel/<int:reel_id>/', views.reel_share_link, name='reel_share_link'),

    path('chat/<int:user_id>/', views.chat_view, name='chat'),
    path('chats/', views.chat_list_view, name='chat_list'),
]
