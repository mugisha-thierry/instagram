from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('signup/',views.signup , name='signup'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('follow/<pk>', views.follow, name='follow'),
    path('unfollow/<pk>',views.unfollow, name='unfollow'),
    path('post/<pk>', views.comment, name='comment'),
    path('search',views.search_image,name = 'search_image'),
    path('like/<int:pk>',views.likeView,name='like_post'),
    # path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    # path('api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    # path('like', like, name='like_post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)