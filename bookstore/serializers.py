from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets

from bookstore.models import BookInstance, Book, Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', #'id',
                  'first_name', 'last_name', 'date_of_birth']

class BookSerializer(serializers.HyperlinkedModelSerializer):
   # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ['url',
                  'title', 'author', 'summary', 'isbn']


class BookInstanceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BookInstance
        fields = ['url', #'id',
                  'owner',
                  'book', 'status', 'customer', 'timestamp']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
