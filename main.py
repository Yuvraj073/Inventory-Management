from fastapi import FastAPI

app = FastAPI()

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

product = Product(id=5, name="Chair", description="A comfortable chair", price=89.99, quantity=15)

@app.get("/produts")
def get_all_produts ():
    return products

@app.get("/produts/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

@app.post("/products")
def add_product():
