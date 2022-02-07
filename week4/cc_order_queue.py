class Queue:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)

    def enqueue(self,items):
        self.items.append(items)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
    
    def take_order(self, customer, flavor, scoops):

        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
            return

        if (scoops < 1) | (scoops > 3):
            print("Choose between 1-3 sccops")
            return
        
        print("Order Created!")
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}

        self.orders.enqueue(order)
    
    def show_all_orders(self):

        print("\nAll pending ice cream orders:")
        for order in self.orders.items:
            #print(order)
            print("Customer:", order["customer"], "--  Flavor:", order["flavor"], " -- Scoops:", order["scoops"])
            #for item in order:
            #    print(item, order[item])
        
    
    def next_order(self):
        next = self.orders.dequeue()
        print("\nNext Order Up!")
        print("Customer:", next["customer"], "--  Flavor:", next["flavor"], " -- Scoops:", next["scoops"])



shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()

        

            
