from rest_framework import serializers
from posts.models import Post


class GetAllMemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'cover', 'category', 'created_on', 'author']


class CreateMemeSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Post
        fields = ['title', 'cover', 'category', 'author']

        def save(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.cover = validated_data.get('file', instance.cover)
            instance.category = validated_data.get('category',
                                                   instance.category)
            instance.user = validated_data.get('author', instance.author)
            instance.save()
            return instance


class UpdateMemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'cover', 'category']

        def update(self, user, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.cover = validated_data.get('file', instance.cover)
            instance.category = validated_data.get('category',
                                                   instance.category)
            instance.author = validated_data.get(user, instance.category)
            instance.save()
            return instance
