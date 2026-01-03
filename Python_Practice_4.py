# Question (Product Store): Design and create an online store for products(name,price)
# Track total products being created
# Create a staic method to calculate discount on each product based on a % parameter.

class Products:
    tracking_products = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        # We write Products.tracking_products += 1 inside the constructor (__init__) because the constructor is automatically executed every time a new product object is created. This makes it the correct place to update the total product count. A class method does not run automatically; it only runs when we explicitly call it, so using it for counting would require manual calls and could miss some creations. Therefore, the constructor handles the counting when products are created, while the class method is better used to access or display the class-level tracking data.
        Products.tracking_products += 1 #If we use self instead of Products, a separate instance attribute tracking_products will be created for each object, instead of updating the class-level counter.

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def track_products(cls):
        print(f"Total Products in store = {cls.tracking_products}")
    
    @staticmethod
    def discount(amnt,disc_percent):
        return (amnt*(disc_percent/100))
        

p1 = Products("Phone",35_000)
p2 = Products("Laptop",55_000)
p1.get_info()
p2.get_info()
Products.track_products()
print(f"Discount price is: {Products.discount(100,10)}")