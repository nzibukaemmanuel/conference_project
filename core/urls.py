from django.urls import path
from .views import *
urlpatterns = [
    path('index', index, name='index'),
    path('create_meeting', create_meeting, name='create_meeting'),
    path('conference/<int:conference_id>/', conference_detail, name='conference_detail'),
    path('update_meeting/<int:meeting_id>/', update_meeting, name='update_meeting'),
    path('delete_meeting/<int:conference_id>/', delete_meeting, name='delete_meeting'),
]
