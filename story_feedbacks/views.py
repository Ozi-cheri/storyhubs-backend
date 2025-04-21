from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from storyhubs_backend.permissions import IsOwnerOrReadOnly
from .models import StoryFeedback
from .serializers import StoryFeedbackSerializer


class StoryFeedbackList(generics.ListCreateAPIView):
    serializer_class = StoryFeedbackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = StoryFeedback.objects.annotate(
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'story_title',
        'story_creator',
        'category',
    ]
    ordering_fields = [
        'likes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StoryFeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoryFeedbackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = StoryFeedback.objects.annotate(
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')