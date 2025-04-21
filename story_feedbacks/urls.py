from django.urls import path
from story_feedbacks import views

urlpatterns = [
    path('story_feedbacks/', views.StoryFeedbackList.as_view()),
    path('story_feedbacks/<int:pk>/', views.StoryFeedbackDetail.as_view())
]