package models

import (
	"gorm.io/gorm"
)

type CartItem struct {
	gorm.Model
	CartID    uint
	Cart      Cart `gorm:"foreignKey:CartID"`
	ProductID uint
	Product   Product `gorm:"foreignKey:ProductID"`
	Quantity  int
}