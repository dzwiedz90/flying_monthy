from rest_framework import serializers
from comments.models import Comments


class GetAllCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'content', 'author', 'meme', 'created_on']


class CreateCommentsSerializer(serializers.ModelSerializer):
    content = serializers.CharField(write_only=True, max_length=1084)

    class Meta:
        model = Comments
        fields = ['content', 'author', 'meme']

        def save(self, instance, validated_data):
            instance.content = validated_data.get('content', instance.content)
            instance.meme = validated_data.get('meme', instance.meme)
            instance.user = validated_data.get('author', instance.author)
            instance.save()
            return instance


class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['content']

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.meme = validated_data.get('meme', instance.meme)
        instance.user = validated_data.get('author', instance.author)
        instance.save()
        return instance
