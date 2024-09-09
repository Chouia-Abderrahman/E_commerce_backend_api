# E-commerce Backend API

## User Management
- **POST /register**: Register a new user, with a request like this
    ````
    {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "testpassword"
    }
    ````
- **POST /login**: User login
    ````
    {
      "username": "testuser",
      "password": "testpassword"
    }
    ````
  and returns the access token and a refresh token to refresh the access token when it expires
    ````
    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
  ````
- **POST token/refresh/**: Refresh access token when it expires
    ````
    {
      "refresh": "<refresh_token>"
    }
    ````
- **PUT /users/{id}**: Update user profile
- **DELETE /users/{id}**: Delete user account

## Product Management
- **POST /products**: Add a new product
- **GET /products**: Retrieve a list of all products
- **GET /products/{id}**: Retrieve details of a specific product
- **PUT /products/{id}**: Update details of a specific product
- **DELETE /products/{id}**: Delete a specific product
- **GET /products/category/{categoryId}**: Retrieve products by category

## Category Management
- **POST /categories**: Add a new category
- **GET /categories**: Retrieve a list of all categories
- **GET /categories/{id}**: Retrieve details of a specific category
- **PUT /categories/{id}**: Update a specific category
- **DELETE /categories/{id}**: Delete a specific category

## Order Management
- **POST /orders**: Create a new order
- **GET /orders**: Retrieve a list of all orders
- **GET /orders/{id}**: Retrieve details of a specific order
- **PUT /orders/{id}**: Update details of a specific order
- **DELETE /orders/{id}**: Delete a specific order
- **GET /orders/user/{userId}**: Retrieve orders by user

## Cart Management
- **POST /cart**: Add item to cart
- **GET /cart/{userId}**: Retrieve the cart for a specific user
- **PUT /cart/{userId}/item/{itemId}**: Update quantity of a specific item in the cart
- **DELETE /cart/{userId}/item/{itemId}**: Remove an item from the cart
- **DELETE /cart/{userId}**: Clear the cart for a specific user

## Payment Management
- **POST /payments**: Process a payment
- **GET /payments/{orderId}**: Retrieve payment details for a specific order
- **POST /refunds**: Process a refund
- **GET /refunds/{orderId}**: Retrieve refund details for a specific order

## Review and Rating Management
- **POST /products/{productId}/reviews**: Add a review for a product
- **GET /products/{productId}/reviews**: Retrieve reviews for a specific product
- **PUT /products/{productId}/reviews/{reviewId}**: Update a specific review
- **DELETE /products/{productId}/reviews/{reviewId}**: Delete a specific review

## Wishlist Management
- **POST /wishlist/{userId}**: Add an item to the wishlist
- **GET /wishlist/{userId}**: Retrieve the wishlist for a specific user
- **DELETE /wishlist/{userId}/item/{itemId}**: Remove an item from the wishlist

## Admin Management
- **GET /admin/users**: Retrieve a list of all users
- **GET /admin/orders**: Retrieve a list of all orders
- **GET /admin/products**: Retrieve a list of all products
- **GET /admin/reports/sales**: Retrieve sales reports
- **GET /admin/reports/inventory**: Retrieve inventory reports

These endpoints provide a comprehensive set of functionalities to manage an e-commerce platform, including user authentication, product and category management, order processing, cart operations, payment handling, reviews, wishlists, and administrative tasks.

## Class Diagram
![drawSQL-image-export-2024-07-20](https://github.com/user-attachments/assets/2099a1e4-2d2b-4c04-9a48-9173984e34be)
