package models

import (
	"gorm.io/gorm"
)

type Review struct {
	gorm.Model
	UserID    uint
	User      User `gorm:"foreignKey:UserID"`
	ProductID uint
	Product   Product `gorm:"foreignKey:ProductID"`
	Rating    int
	Comment   string
}
