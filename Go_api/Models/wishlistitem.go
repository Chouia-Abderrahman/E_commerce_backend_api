package models

import (
	"gorm.io/gorm"
)

type WishlistItem struct {
	gorm.Model
	WishlistID uint
	Wishlist   Wishlist `gorm:"foreignKey:WishlistID"`
	ProductID  uint
	Product    Product `gorm:"foreignKey:ProductID"`
}