Paragraph Search API
This is a Django REST API for managing paragraphs and performing word searches within those paragraphs.

...........................................Table of Contents
Getting Started
Prerequisites
Installation
Authentication
Endpoints
Register
Login
Create Paragraph
Word Search
Usage
Contributing
License


.............................................................Authentication
The API uses token-based authentication. To access protected endpoints, you need to include the JWT token in the request headers.

..................Endpoints
..........Register
URL: /register/
Method: POST
Parameters:
name (string, required): User's name.
email (string, required): User's email.
password (string, required): User's password.
.........Login
URL: /login/
Method: POST
Parameters:
email (string, required): User's email.
password (string, required): User's password.
Response:
jwt (string): JSON Web Token for authentication.



.......................................................Create Paragraph
URL: /paragraph/
Method: POST
Parameters:
text (string, required): Paragraph text.
Authentication: Required (JWT token).
.......................................................Word Search
URL: /wordindex/{word}/
Method: GET
Parameters:
word (string, required): Word to search for.
Authentication: Required (JWT token).
Response:
List of paragraphs containing the specified word.






