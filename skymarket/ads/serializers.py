from rest_framework import serializers

from .models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ('id', "image", "title", "price", "phone", "description",
                  "author_first_name", "author_last_name", "author_id")

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name

    def get_phone(self, obj):
        return obj.author.phone
