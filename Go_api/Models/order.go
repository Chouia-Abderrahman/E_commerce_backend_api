package models

import (
	"gorm.io/gorm"
)

type Order struct {
	gorm.Model
	UserID      uint
	User        User `gorm:"foreignKey:UserID"`
	Status      string
	TotalAmount float64
	PaymentID   uint
	Payment     Payment `gorm:"foreignKey:PaymentID"`
	Items       []OrderItem
}
