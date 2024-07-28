package controllers

import (
    "net/http"

    "github.com/gin-gonic/gin"
)

func CreateProduct(c *gin.Context) {
    c.JSON(http.StatusOK, gin.H{"message": "create_product"})
}

func ReadProduct(c *gin.Context) {
    c.JSON(http.StatusOK, gin.H{"message": "read_product"})
}