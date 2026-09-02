from fastapi import FastAPI
from models import Product
app = FastAPI()

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

product = Product(id=5, name="Chair", description="A comfortable chair", price=89.99, quantity=15)

@app.get("/products")
def get_all_produts ():
    return products

@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

@app.post("/products")
def add_product(product: Product):
    products.append()
    return product

@app.put("/product")
def update_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated successfully"
    return"Product not found"

@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del product
            return "Product deleted successfully"

    return "Product not found"

