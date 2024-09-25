from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pinch_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    filter_backends =[
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    
    #allows filtering by the profile ID
    filterset_fields = [
        'owner__username',
        'owner__profile',
        'item_name',
        'category',
        'location',
    ]
    search_fields = [
        'owner__username',
        'item_name',
        'category',
        'location'
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
        'price',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()  # Call the original queryset

        user = self.request.user
        liked = self.request.query_params.get('liked', None)  # Check if 'liked' parameter is present

        if liked and user.is_authenticated:
            # Filter to return only posts liked by the current user
            queryset = queryset.filter(likes__owner=user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')