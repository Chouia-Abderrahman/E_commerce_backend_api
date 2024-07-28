package models

import (
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	UserID    uint
	Username  string
	Email     string
	Password  string
	Wishlists []Wishlist
	Reviews   []Review
	Orders    []Order
	Carts     []Cart
	Address   string
	Phone     string
}
