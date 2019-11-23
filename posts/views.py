from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from posts.models import Post
from posts.serializers import GetAllMemesSerializer, CreateMemeSerializer, UpdateMemeSerializer


class List(ListView):
    model = Post
    template_name = 'list.html'
    ordering = ['-created_on']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'cover']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MemeRestApi(APIView):
    def get(self, request):
        memes = Post.objects.all()
        serializer = GetAllMemesSerializer(memes, many=True)
        return Response({'memes': serializer.data})

    def post(self, request):
        serializer = CreateMemeSerializer(data=request.data)
        if request.user.id == int(request.data['author']):
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Meme created'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'Cant add meme, wrong data'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'You cant add meme as another user'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            request_id = request.data['id']
            request_user = request.user
            post = Post.post = Post.objects.get(id=request_id)
            serializer = UpdateMemeSerializer(data=request.data)
            if request_user == post.author:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'Meme modified'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'You cant change another users memes'}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response('Meme not found', status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            request_id = request.data['id']
            request_user = request.user
            post = Post.objects.get(id=request_id)
            if request_user == post.author:
                post.delete()
                return Response('Meme deleted', status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'You cant delete another user meme'},
                                status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response('Meme not found', status=status.HTTP_404_NOT_FOUND)


class GetMemesOfUser(APIView):
    def get(self, request):
        memes = Post.objects.filter(author=request.user.id)
        serializer = GetAllMemesSerializer(memes, many=True)
        return Response({'memes': serializer.data})
