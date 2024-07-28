package models

import (
	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Name        string  `gorm:"not null"`
	Description string  `gorm:"not null"`
	Price       float64 `gorm:"not null"`
	QtyStock    int     `gorm:"not null"`
	CategoryID  uint
	Category    Category `gorm:"foreignKey:CategoryID"`
	Reviews     []Review
	CartItems   []CartItem
}