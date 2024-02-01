Library Management System API using Django and django-rest-framework

#Initial Setup:

Install  virtual environment: python -m venv env 

Install django : pip install django 

Start a new django Project: django-admin startproject elibrary 

Set Up a postgres Database : pip install psycopg2-binary 

Change settings.py files to include postgres database : 

DATABASES = {

    'default': {
		
        'ENGINE': 'django.db.backends.postgresql',
				
        'NAME': 'yourdbname',
				
        'USER': 'yourdbuser',
				
        'PASSWORD': 'yourpassword',
				
        'HOST': 'localhost',
				
        'PORT': '',
				
    }
		
} 

Start a new app named api: python manage.py startapp api 

Install django-rest-framework: pip install django-rest-framework 

The initial setup is now complete 

#API Documentation

1. Create User

EndPoint => POST /create_user

Request Body Example => 

{

  "name": "John Doe",

  "email": "john.doe@example.com",

  "membershipDate": "2022-01-01"

}
Responses => 

201 Created , {"message" : "User Created Succesfully" }

400 Bad Request , {"message" : "Please Provide all the required fields" }

500 Internal Server Error , {"message": "Something went wrong"}

2. Get All Users

EndPoint => GET /all_users

Responses => 

200 OK , 

{

  "users": [

    {

      "id": 1,

      "name": "John Doe",

      "email": "john.doe@example.com",

      "membershipDate": "2022-01-01"

    },

    {

      "id": 2,

      "name": "Jane Smith",

      "email": "jane.smith@example.com",

      "membershipDate": "2022-02-01"

    }
  ]
}

3. Get User by ID

Endpoint POST /get_user

Request Body

{
  "userid": 1
}
Responses

200 OK =>

{

  "user": {

    "id": 1,

    "name": "John Doe",

    "email": "john.doe@example.com",

    "membershipDate": "2022-01-01"

  }

}

404 Not Found =>

{

  "message": "No user found"

}

400 Bad Request =>

{

  "message": "Please provide the userid"

}

Book APIs

4. Add a New Book

Endpoint => POST /add_book

Request Body

{

  "title": "Sample Book",

  "userid": 1,

  "isbn": "1234567890",

  "publishedDate": "2022-03-01",

  "genre": "Fiction"

}
Responses

201 Created => 

{

  "message": "Book added successfully"

}

400 Bad Request => 

{

  "message": "Please provide all the required fields"

}
500 Internal Server Error => 

{

  "message": "Something went wrong"

}
5. Get All Books

Endpoint => GET /all_books

Responses

200 OK => 

{

  "books": [

    {

      "id": 1,

      "title": "Sample Book",

      "borrower": {

        "id": 1,

        "name": "John Doe",

        "email": "john.doe@example.com",

        "membershipDate": "2022-01-01"

      },

      "isbn": "1234567890",

      "publishedDate": "2022-03-01",

      "genre": "Fiction"

    }

  ]

}

404 Not Found => 

{

  "message": "No books found"

}

6. Get Book by ID

Endpoint => POST /get_book

Request Body

{

  "bookID": 1

}

Responses 

200 OK => 


{

  "book": {

    "id": 1,

    "title": "Sample Book",

    "borrower": {

      "id": 1,

      "name": "John Doe",

      "email": "john.doe@example.com",

      "membershipDate": "2022-01-01"

    },

    "isbn": "1234567890",

    "publishedDate": "2022-03-01",

    "genre": "Fiction"

  }

}

404 Not Found => 

{

  "message": "No book found"

}

400 Bad Request =>

{

  "message": "Please provide the bookid"

}

7. Update Book Details

Endpoint => POST /update_book

Request Body

{

  "id": 1,

  "numberOfPages": 200,

  "publisher": "Sample Publisher",

  "language": "English"

}

Responses

200 OK => 

{
    
  "message": "Book details updated successfully"

}

400 Bad Request => 

{

  "message": "Please provide the bookid"

}

500 Internal Server Error => 

{

  "message": "Something went wrong"

}

Borrowed Books APIs

8. Borrow a Book

Endpoint => POST /borrow_book

Request Body=> 

{

  "userid": 1,

  "bookid": 1,

  "borrowedDate": "2023-01-01",

  "returnDate": "2023-02-01"

}

Responses

201 Created => 

{

  "message": "Book borrowed successfully"

}

400 Bad Request =>

{

  "message": "Please provide all the required fields"

}

404 Not Found => 

{

  "message": "No user or book found"

}

500 Internal Server Error =>

{

  "message": "Something went wrong"

}

9. List Borrowed Books

Endpoint => GET /borrowed_books

Responses 

200 OK => 

{

  "borrowedBooks": [

    {

      "id": 1,

      "book": {

        "title": "Sample Book",

        "borrower": {

          "id": 1,

          "name": "John Doe",

          "email": "john.doe@example.com",

          "membershipDate": "2022-01-01"

        },

        "isbn": "1234567890",

        "publishedDate": "2022-03-01",

        "genre": "Fiction"

      },

      "borrower": {

        "id": 1,

        "name": "John Doe",

        "email": "john.doe@example.com",

        "membershipDate": "2022-01-01"
      }
  ]
}



