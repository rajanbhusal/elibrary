from django.db import models
import uuid

# database schema for the api
class User(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    membershipDate = models.DateField()

class Book(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    bookID = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publishedDate = models.DateField()
    genre = models.CharField(max_length=100)

class BookDetails(models.Model):
    detailsID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, null=True, blank=True)
    numberOfPages = models.PositiveIntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)

class BorrowedBooks(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowedDate = models.DateField()
    returnDate = models.DateField(null=True, blank=True)

