package main

import (
    "Go_api/controllers"
    "Go_api/database"
    "github.com/gin-gonic/gin"
)

func main() {
    database.Init()

    router := gin.Default()

    router.GET("/categories/", controllers.GetCategory)
    router.POST("/categories/", controllers.CreateCategory)
    router.GET("/products/", controllers.CreateProduct)
    router.POST("/products/", controllers.ReadProduct)

    router.Run(":8000")
}