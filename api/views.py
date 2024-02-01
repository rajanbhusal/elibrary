from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User, Book, BorrowedBooks, BookDetails
from rest_framework.response import Response
from .serializers import BookSerializer, BorrowedBooksSerializer, BookDetailsSerializer

# User APIs.
# create user
@api_view(['POST'])
def create_user(request):
    name = request.data.get('name')
    email = request.data.get('email')
    membershipDate = request.data.get('membershipDate')
    if not name or not email or not membershipDate:
        return Response({"message": "Please provide all the required fields"}, status=400)
    user = User.objects.create(name=name, email=email, membershipDate=membershipDate)
    if not user:
        return Response({"message": "Something went wrong"}, status=500)
    return Response({"message": "User created successfully"}, status=201)

#get all users
@api_view(['GET'])
def all_users(request):
    users = User.objects.all()
    if not users:
        return Response({"message": "No users found"}, status=404)
    return Response({"users": users.values()}, status=200)

#get users by their id
@api_view(['POST'])
def get_user(request):
    userid = request.data.get('userid')
    if not userid:
        return Response({"message": "Please provide the userid"}, status=400)
    user = User.objects.filter(userid=userid)
    if not user:
        return Response({"message": "No user found"}, status=404)
    return Response({"user": user.values()}, status=200)

#Book APIs.
# add a new book
@api_view(['POST'])
def add_book(request):
    title = request.data.get('title')
    userid = request.data.get('userid')
    borrower = User.objects.filter(userid=userid)
    isbn = request.data.get('isbn')
    publishedDate = request.data.get('publishedDate')
    genre = request.data.get('genre')
    if not title or not borrower or not isbn or not publishedDate or not genre:
        return Response({"message": "Please provide all the required fields"}, status=400)
    book = Book.objects.create(title=title, borrower=borrower[0], isbn=isbn, publishedDate=publishedDate, genre=genre)
    if not book:
        return Response({"message": "Something went wrong"}, status=500)
    return Response({"message": "Book added successfully"}, status=201)

# get all books
@api_view(['GET'])
def all_books(request):
    books = Book.objects.all()
    if not books:
        return Response({"message": "No books found"}, status=404)
    return Response({"books": books.values()}, status=200)

# get books by their id
@api_view(['POST'])
def get_book(request):
    bookID = request.data.get('bookID')
    if not bookID:
        return Response({"message": "Please provide the bookid"}, status=400)
    book = Book.objects.filter(bookID=bookID)
    if not book:
        return Response({"message": "No book found"}, status=404)
    return Response({"book": book.values()}, status=200)

#assign or update book details
@api_view(['POST'])
def update_book(request):
    id = request.data.get('id')
    if not id:
        return Response({"message": "Please provide the bookid"}, status=400)
    book = Book.objects.filter(bookID=id)
    book_details,created = BookDetails.objects.update_or_create(
        book=book[0],
        numberOfPages=request.data.get('numberOfPages'),
        publisher=request.data.get('publisher'),
        language=request.data.get('language')
    )
    if not book_details:
        return Response({"message": "Something went wrong"}, status=500)
    serializer = BookDetailsSerializer(data=request.data,instance=book_details)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#borrowed books APIs.
#borrow a book
@api_view(['POST'])
def borrow_book(request):
    userid = request.data.get('userid')
    bookid = request.data.get('bookid')
    borrowedDate = request.data.get('borrowedDate')
    returnDate = request.data.get('returnDate')
    if not userid or not bookid or not borrowedDate:
        return Response({"message": "Please provide all the required fields"}, status=400)
    user = User.objects.filter(userid=userid)
    if not user:
        return Response({"message": "No user found"}, status=404)
    book = Book.objects.filter(bookID=bookid)
    if not book:
        return Response({"message": "No book found"}, status=404)
    borrowedBook = BorrowedBooks.objects.create(userID=user[0], bookID=book[0], borrowedDate=borrowedDate, returnDate=returnDate)
    if not borrowedBook:
        return Response({"message": "Something went wrong"}, status=500)
    return Response({"message": "Book borrowed successfully"}, status=201)
    
#list borrowed books
@api_view(['GET'])
def borrowed_books(request):
    borrowedBooks = BorrowedBooks.objects.all()
    if not borrowedBooks:
        return Response({"message": "No books found"}, status=404)
    borrowed_books = BorrowedBooksSerializer(borrowedBooks, many=True)
    return Response({"borrowedBooks": borrowed_books.data}, status=200)