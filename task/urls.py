

from django.urls import path,include
from .views import *

urlpatterns = [

    path('quest/post/master/tasks/v1',MasterTaskDataView.as_view()),
    path('post/<uuid:pk>/',PostDetailsView.as_view(), name='post-detail'),
    path('post/<uuid:pk>/reply',replyToTaskView, name='reply'),
    path('post/<uuid:pk>/approve',approveTaskView, name='approve'),
    path('post/<uuid:pk>/reject',rejectTaskView, name='reject'),
]
