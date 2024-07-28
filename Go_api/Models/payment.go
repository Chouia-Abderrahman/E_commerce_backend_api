package models

import (
	"gorm.io/gorm"
)

type Payment struct {
	gorm.Model
	Amount        float64
	PaymentMethod string
	PaymentStatus string
	Orders        []Order
}