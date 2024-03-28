## Flask JWT Authentication with SQLAlchemy

<p> This is a Flask application that provides JWT (JSON Web Token) authentication using SQLAlchemy for interacting with the database. It allows users to register, login, and access protected routes by validating JWT tokens.</p>

## Features:
1. User registration
   Users can create an account by providing a username, email, and password. <br>

2. User authentication: Registered users can log in    using their credentials. <br>
 3. JWT generation: Upon successful authentication, JWT tokens are generated and provided to users

 4. Protected routes: Certain routes are protected and can only be accessed by users with valid JWT tokens.

 5. SQLAlchemy integration: User data is stored in a SQL database, and SQLAlchemy is used for ORM.

    


