from rest_framework import serializers
from .models import User, Book, BookDetails, BorrowedBooks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    borrower = UserSerializer(read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

class BookDetailsSerializer(serializers.ModelSerializer):
    bookID = BookSerializer(read_only=True)
    class Meta:
        model = BookDetails
        fields = '__all__'

class BorrowedBooksSerializer(serializers.ModelSerializer):
    userID = UserSerializer(read_only=True)
    bookID = BookSerializer(read_only=True)
    class Meta:
        model = BorrowedBooks
        fields = '__all__'