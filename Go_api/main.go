// main.go
package main

import (
	"Go_api/models"
	"net/http"

	"github.com/gin-gonic/gin"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var db *gorm.DB
var err error

func main() {
	dsn := "host=localhost user=go password=go dbname=go_db port=5432 sslmode=disable TimeZone=Africa/Algiers"
	db, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	db.AutoMigrate(&models.Wishlist{}, &models.Review{}, &models.Category{},
		&models.CartItem{}, &models.Product{}, &models.User{}, &models.Payment{},
		&models.Order{}, &models.OrderItem{}, &models.WishlistItem{}, &models.Cart{})

	r := gin.Default()

	r.GET("/categories/", getCategory)
	r.POST("/categories/", createCategory)
	r.GET("/products/", createProduct)
	r.POST("/products/", readProduct)

	r.Run() // listen and serve on 0.0.0.0:8080
}

func getCategory(c *gin.Context) {
	var categories []models.Category
	db.Find(&categories)
	c.JSON(http.StatusOK, categories)
}

func createCategory(c *gin.Context) {
	var category models.Category
	if err := c.ShouldBindJSON(&category); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	db.Create(&category)
	c.JSON(http.StatusCreated, category)
}

func createProduct(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"message": "create_product"})
}

func readProduct(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"message": "read_product"})
}
