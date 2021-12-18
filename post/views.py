from rest_framework.response import Response
from rest_framework import generics
from django.db.models import F
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-votes_total")
    serializer_class = PostSerializer


class PostDetailedAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpvoteAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # increase total votes on this particular instance
        Post.objects.filter(pk=instance.id).update(votes_total=F("votes_total") + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        return self.queryset.filter(post=id)
