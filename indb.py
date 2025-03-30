from product import Product

def generate_products():
    list_products =[]
    
    for i in range(20):
        product = Product(name=f"Product{i + 1}", price=5.98*i, quantity=2*i)
        list_products.append(product)
    return list_products
