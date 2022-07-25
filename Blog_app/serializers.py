
from dataclasses import field, fields
from rest_framework import serializers
from Blog_app.models import Author, Category , Post


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        #fields = ('id','title','content', 'date_posted', 'comment', 'likes','dislikes', 'author_post','post_category')

        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

        fields ='__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post

        fields = '__all__'
