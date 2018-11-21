from facebook.views import play
from facebook.views import play2
from facebook.views import profile
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import new_feed
from facebook.views import edit_feed
from facebook.views import remove_feed


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('profile/play/', play),
    path('profile/play2/', play2),
    path('profile/', profile),
    path('new/', new_feed),
    path('', newsfeed),
    path('feed/<pk>/',detail_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('feed/<pk>/remove/', remove_feed)

]
