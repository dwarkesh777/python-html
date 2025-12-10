class invalid(Exception):
    pass
class invalidchees(Exception):
    pass
class pizzeria:
    def __init__(self,size,toppings,cheese):
        self.size=size
        self.toppings =toppings
        self.cheese=cheese
        self.validtop()
        self.validchees()
    def price(self):
        pizzasize={"small":50,"medium":100,"large":200}
        toppingprice=20
        exotic=50
        cheeseprice=50
        total=pizzasize[self.size]
        for topping in self.toppings:
            if topping in ["broccoli", "olives", "mushroom"]:
                total+=50
            else:
                total+=20
            total+=len(self.cheese)*50
        return total
    def validtop(self):
        valid=["corn", "tomato", 'onion', "capsicum", "mushroom", "olives","broccoli"]
        for toping in self.topping:
            for i not in valid:
                raise invalid("invalid toping")
    def validchees(self):
        validch=["mozzarella","feta", "cheddar"]
        for chese in self.cheese:
            for i not in validch:
                raise invalidchees("invalid cheese")
class order:
    def __init__(self,name,cid):
        self.name=name
        self.cid=cid
        self.pizza=[]
    def order(self,pizza):
        self.pizza.append(pizza)
    def bill(self)
        totalcost=0
        print(f"order detail of {self.name} withId{self.cid}:")
        for i,pizza in enumerate(self.pizza,start=1):
            pizzacost=pizza.price()
            totalcost+=pizzacost
