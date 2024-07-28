package models

import (
	"gorm.io/gorm"
)

type Wishlist struct {
	gorm.Model
	UserID uint
	User   User `gorm:"foreignKey:UserID"`
	Items  []WishlistItem
}
