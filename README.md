# E-commerce Backend API

This document outlines the endpoints for an e-commerce backend API, providing functionalities for user management, product and category management, order processing, cart operations, payment handling, reviews, wishlists, and administrative tasks.

## Table of Contents
- [User Management](#user-management)
- [Category Management](#category-management)
- [Product Management](#product-management)
- [Payment Management](#payment-management)
- [Order Management](#order-management)
- [Cart Management](#cart-management)
- [Review and Rating Management](#review-and-rating-management)
- [Wishlist Management](#wishlist-management)
- [Admin Management](#admin-management)

## User Management

### POST /register
Register a new user

**Request Body:**
```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "testpassword"
}
```

### POST /login
User login

**Request Body:**
```json
{
  "username": "testuser",
  "password": "testpassword"
}
```

**Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

### POST /token/refresh/
Refresh access token when it expires

**Request Body:**
```json
{
  "refresh": "<refresh_token>"
}
```

### PUT /users/{id}
Update user profile

### DELETE /users/{id}
Delete user account

## Category Management

### POST /categories
Add a new category

**Request Body:**
```json
{
  "name": "Clothes"
}
```

### GET /categories
Retrieve a list of all categories

**Response:**
```json
[
  {
    "id": 1,
    "name": "vegetables"
  },
  {
    "id": 2,
    "name": "Canned food"
  },
  {
    "id": 4,
    "name": "Clothes"
  },
  {
    "id": 3,
    "name": "Electronics"
  }
]
```

### GET /categories/{id}/
Retrieve details of a specific category

### PUT /categories/{id}/
Update a specific category

**Request Body:**
```json
{
  "name": "Updated category"
}
```

### DELETE /categories/{id}/
Delete a specific category

## Product Management

### POST /products
Add a new product

**Request Body:**
```json
{
  "name": "T-shirt",
  "description": "A comfortable cotton T-shirt",
  "price": 19.99,
  "qty_stock": 100,
  "category": 1
}
```

### GET /products
Retrieve a list of all products

**Response:**
```json
[
  {
    "id": 1,
    "name": "T-shirt",
    "description": "A comfortable cotton T-shirt",
    "price": 19.99,
    "qty_stock": 100,
    "category": {
      "id": 1,
      "name": "vegetables"
    }
  },
  {
    "id": 3,
    "name": "T-shirt",
    "description": "A comfortable cotton T-shirt",
    "price": 19.99,
    "qty_stock": 100,
    "category": {
      "id": 1,
      "name": "vegetables"
    }
  },
  {
    "id": 4,
    "name": "Hoodie",
    "description": "A warm and stylish hoodie",
    "price": 29.99,
    "qty_stock": 50,
    "category": {
      "id": 2,
      "name": "Canned food"
    }
  }
]
```

### GET /products/{id}/
Retrieve details of a specific product

### PUT /products/{id}/
Update details of a specific product

### DELETE /products/{id}/
Delete a specific product

### GET /products/category/{categoryId}
Retrieve products by category

## Payment Management

### POST /payments
Process a payment

**Request Body:**
```json
{
  "order_id": 1234,
  "amount": 59.98,
  "payment_method": "credit_card",
  "card_number": "4111111111111111",
  "expiry_date": "12/25",
  "cvv": "123"
}
```

### GET /payments/{orderId}
Retrieve payment details for a specific order

### POST /refunds
Process a refund

**Request Body:**
```json
{
  "order_id": 1234,
  "amount": 59.98,
  "reason": "Product damaged during shipping"
}
```

### GET /refunds/{orderId}
Retrieve refund details for a specific order

## Order Management

### POST /orders
Create a new order

**Request Body:**
```json
{
  "user_id": 1,
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 3,
      "quantity": 1
    }
  ],
  "shipping_address": {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345",
    "country": "USA"
  }
}
```

### GET /orders
Retrieve a list of all orders

### GET /orders/{id}
Retrieve details of a specific order

### PUT /orders/{id}
Update details of a specific order

**Request Body:**
```json
{
  "status": "shipped",
  "tracking_number": "1Z999AA1123456789"
}
```

### DELETE /orders/{id}
Delete a specific order

### GET /orders/user/{userId}
Retrieve orders by user

## Cart Management

### POST /cart
Add item to cart

**Request Body:**
```json
{
  "user_id": 1,
  "product_id": 2,
  "quantity": 1
}
```

### GET /cart/{userId}
Retrieve the cart for a specific user

### PUT /cart/{userId}/item/{itemId}
Update quantity of a specific item in the cart

**Request Body:**
```json
{
  "quantity": 3
}
```

### DELETE /cart/{userId}/item/{itemId}
Remove an item from the cart

### DELETE /cart/{userId}
Clear the cart for a specific user

## Review and Rating Management

### POST /products/{productId}/reviews
Add a review for a product

**Request Body:**
```json
{
  "user_id": 1,
  "rating": 4,
  "comment": "Great product, very comfortable!"
}
```

### GET /products/{productId}/reviews
Retrieve reviews for a specific product

### PUT /products/{productId}/reviews/{reviewId}
Update a specific review

**Request Body:**
```json
{
  "rating": 5,
  "comment": "Even better than I initially thought!"
}
```

### DELETE /products/{productId}/reviews/{reviewId}
Delete a specific review

## Wishlist Management

### POST /wishlist/{userId}
Add an item to the wishlist

**Request Body:**
```json
{
  "product_id": 4
}
```

### GET /wishlist/{userId}
Retrieve the wishlist for a specific user

### DELETE /wishlist/{userId}/item/{itemId}
Remove an item from the wishlist

## Admin Management

### GET /admin/users
Retrieve a list of all users

### GET /admin/orders
Retrieve a list of all orders

### GET /admin/products
Retrieve a list of all products

### GET /admin/reports/sales
Retrieve sales reports

**Query Parameters:**
```json
{
  "start_date": "2023-01-01",
  "end_date": "2023-12-31"
}
```

### GET /admin/reports/inventory
Retrieve inventory reports

**Query Parameters:**
```json
{
  "low_stock_threshold": 10
}
```

This API provides a comprehensive set of functionalities to manage an e-commerce platform, including user authentication, product and category management, order processing, cart operations, payment handling, reviews, wishlists, and administrative tasks.

## Class Diagram
![drawSQL-image-export-2024-07-20](https://github.com/user-attachments/assets/2099a1e4-2d2b-4c04-9a48-9173984e34be)