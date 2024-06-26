from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDeleteAPIView, \
    PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    # CRUD habit
    path('list/', HabitListAPIView.as_view(), name='habit-list'),
    path('list/public/', PublicHabitListAPIView.as_view(), name='habit-list-public'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit-delete'),

]
