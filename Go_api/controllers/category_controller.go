package controllers

import (
    "Go_api/models"
    "net/http"

    "github.com/gin-gonic/gin"
    "Go_api/database"
)

func GetCategory(c *gin.Context) {
    var categories []models.Category
    database.DB.Find(&categories)
    c.JSON(http.StatusOK, categories)
}

func CreateCategory(c *gin.Context) {
    var category models.Category
    if err := c.ShouldBindJSON(&category); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    database.DB.Create(&category)
    c.JSON(http.StatusCreated, category)
}