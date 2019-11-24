from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from comments.models import Comments
from posts.models import Post
from comments.serializers import GetAllCommentsSerializer, CreateCommentsSerializer, \
    UpdateCommentSerializer


class CommentRestApi(APIView):
    def get(self, request):
        comments = Comments.objects.all()
        serializer = GetAllCommentsSerializer(comments, many=True)
        return Response({'comments': serializer.data})

    def post(self, request):
        serializer = CreateCommentsSerializer(data=request.data)
        if request.user.id == int(request.data['author']):
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Comment added'},
                                status=status.HTTP_201_CREATED)
            return Response({'message': 'Cant add comment, wrong data'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message': 'You cant add comment as another user'},
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            request_id = request.data['id']
            request_user = request.user
            post = Comments.objects.get(id=request_id)
            serializer = UpdateCommentSerializer(request_user,
                                                 data=request.data)
            if request_user == post.author:
                if serializer.is_valid():
                    serializer.update(post, serializer.validated_data)
                    return Response({'message': 'Comment modified'},
                                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {'message': "You can't change another users comments"},
                    status=status.HTTP_400_BAD_REQUEST)
        except Comments.DoesNotExist:
            return Response('Comment not found',
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            request_id = request.data['id']
            request_user = request.user
            comment = Comments.objects.get(id=request_id)
            if request_user == comment.author:
                comment.delete()
                return Response('Comment deleted',
                                status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                    {'message': 'You cant delete another user comment'},
                    status=status.HTTP_400_BAD_REQUEST)
        except Comments.DoesNotExist:
            return Response('Comment not found',
                            status=status.HTTP_404_NOT_FOUND)


class GetCommentsOfUser(APIView):
    def get(self, request):
        comment = Comments.objects.filter(author=request.user.id)
        serializer = GetAllCommentsSerializer(comment, many=True)
        return Response({'comments': serializer.data})


# @login_required()
def add_comment(request, pk):
    if request.method == "POST":
        if request.user.username:
            data = request.POST
            if data['content']:
                Comments.objects.create(content=data.get('content'), author=request.user, meme=Post.objects.get(pk=pk))
                return redirect(request.environ['HTTP_REFERER'])
        else:
            return redirect(request.environ['HTTP_REFERER'])
