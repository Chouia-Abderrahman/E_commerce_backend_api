// models/models.go
package models

import (
	"gorm.io/gorm"
)

type Wishlist struct {
	gorm.Model
	UserID uint
	User   User `gorm:"foreignKey:UserID"`
	Items  []WishlistItem
}

type Review struct {
	gorm.Model
	UserID    uint
	User      User `gorm:"foreignKey:UserID"`
	ProductID uint
	Product   Product `gorm:"foreignKey:ProductID"`
	Rating    int
	Comment   string
}

type Category struct {
	gorm.Model
	Name     string `gorm:"unique;not null"`
	Products []Product
}

type CartItem struct {
	gorm.Model
	CartID    uint
	Cart      Cart `gorm:"foreignKey:CartID"`
	ProductID uint
	Product   Product `gorm:"foreignKey:ProductID"`
	Quantity  int
}

type Product struct {
	gorm.Model
	Name        string  `gorm:"not null"`
	Description string  `gorm:"not null"`
	Price       float64 `gorm:"not null"`
	QtyStock    int     `gorm:"not null"`
	CategoryID  uint
	Category    Category `gorm:"foreignKey:CategoryID"`
	Reviews     []Review
	CartItems   []CartItem
}

type User struct {
	gorm.Model
	UserID    uint
	Username  string
	Email     string
	Password  string
	Wishlists []Wishlist
	Reviews   []Review
	Orders    []Order
	Carts     []Cart
	Address   string
	Phone     string
}

type Payment struct {
	gorm.Model
	Amount        float64
	PaymentMethod string
	PaymentStatus string
	Orders        []Order
}

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

type OrderItem struct {
	gorm.Model
	OrderID   uint
	Order     Order `gorm:"foreignKey:OrderID"`
	ProductID uint
	Product   Product `gorm:"foreignKey:ProductID"`
	Quantity  int
	Price     float64
}

type WishlistItem struct {
	gorm.Model
	WishlistID uint
	Wishlist   Wishlist `gorm:"foreignKey:WishlistID"`
	ProductID  uint
	Product    Product `gorm:"foreignKey:ProductID"`
}

type Cart struct {
	gorm.Model
	UserID uint
	User   User `gorm:"foreignKey:UserID"`
	Items  []CartItem
}
