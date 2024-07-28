package models

import (
	"gorm.io/gorm"
)

type OrderItem struct {
	gorm.Model
	OrderID   uint
	Order     Order `gorm:"foreignKey:OrderID"`
	ProductID uint
	Product   Product `gorm:"foreignKey:ProductID"`
	Quantity  int
	Price     float64
}
