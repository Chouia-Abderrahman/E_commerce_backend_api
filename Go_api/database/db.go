package database

import (
    "gorm.io/driver/postgres"
    "gorm.io/gorm"
	"Go_api/models"
)

var DB *gorm.DB
var err error

func Init() {
    dsn := "host=localhost user=go password=go dbname=go_db port=5432 sslmode=disable TimeZone=Africa/Algiers"
    DB, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
    if err != nil {
        panic("failed to connect database")
    }

    DB.AutoMigrate(&models.Wishlist{}, &models.Review{}, &models.Category{},
        &models.CartItem{}, &models.Product{}, &models.User{}, &models.Payment{},
        &models.Order{}, &models.OrderItem{}, &models.WishlistItem{}, &models.Cart{})
}