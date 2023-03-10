# -*- coding: utf-8 -*-
"""Pizza_Order_System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sa2lvN-EqY0NYD6SPHOgaOnreQgrhAkt
"""

#pizzaordersystem
#The project presents a menu. Pizza and sauce selection is made. Then the customer information is entered and the order is created.
#--- Doğukan Kılınç / Berna Ferudun ---


import csv
import datetime

#Pizza sınıfına ait ve sos sınıfı tarafından kullanılacak methodlar
#pizza üst sınıfı
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.sauces = []

    #sos ekleme
    def add_sauces(self, sauce):
        self.sauces.append(sauce)

    #hem pizza hem sosu alan tanım cümlesi
    def get_description(self):
        sauces = ', '.join([sauce.name for sauce in self.sauces])
        return f"Your choice pizza: {self.name} with {sauces}"

    #hem pizza hem sosu alan hesaplama 
    def get_cost(self):
        cost = self.price
        for sauce in self.sauces:
            cost += sauce.price
        return f"Your payment {cost} TL"

#alt pizza sınıfları kendilerine ait tanım ve ücretlendirme   
class Classic_pizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 60)

class Margarita_pizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza",70)

class Turkish_pizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza",50)

class Plain_pizza(Pizza):
    def __init__(self):
        super().__init__("Plain Pizza",40)

#sos üst sınıfı
class Sauce:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#alt sos sınıfları kendilerine ait tanım ve ücretlendirme   
class Olives(Sauce):
    def __init__(self):
      super().__init__("Olives", 7)

class Mushrooms(Sauce):
    def __init__(self):
      super().__init__("Mushrooms",10)

class Goat_Cheese(Sauce):
    def __init__(self):
      super().__init__("Goat Cheese",12)

class Meat(Sauce):
    def __init__(self):
      super().__init__("Meat",15)

class Onions(Sauce):
    def __init__(self):
      super().__init__("Onions",5)

class Corn(Sauce):
    def __init__(self):
      super().__init__("Corn",5)

class not_sauce(Sauce):
    def __init__(self):
      super().__init__("not sauce",0)
  

#müşteri bilgileri
def get_customer_info():
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    tc_number = input("Please enter your tc number: ")
    credit_card = input("Please enter your credit card number: ")
    password = input("please enter your password: ")
    return name, surname, tc_number, credit_card, password

#pizzaları oluşturup geri dönecek fonksiyon(--menüye dahil--)
def get_pizza_order():
    print("--- WELCOME ---")
    print("1.Classic Pizza") 
    print("2.Margarita Pizza")
    print("3.Turkish Pizza")
    print("4.Plain Pizza")
    choice = input("Your pizza choice (1-4): ")
    while choice not in  ["1","2","3","4"]:
        choice = input("Please make a choice 1-4: ")
    if choice == "1" :
        pizza = Classic_pizza()
    elif choice == "2" :
        pizza = Margarita_pizza()
    elif choice == "3" : 
        pizza = Turkish_pizza()
    else: 
        pizza = Plain_pizza()
    return pizza 

#sosları oluşturup geri dönecek fonksiyon(--menüye dahil--)
def get_sauce_order():
    print("--- Please continue ---")
    print("5. Olives") 
    print("6. Mushrooms")
    print("7. Goat Cheese")
    print("8. Meat")
    print("9. Onions")
    print("10. Corn")
    print("11. not sauce")
    sauce_choice = input("Your sauce choice (5-11): ")
    while sauce_choice not in ["5", "6", "7", "8", "9", "10", "11"]:
        sauce_choice = input("Please make a choice 5-11: ")
    if sauce_choice == "5":
        sauce = Olives()
    elif sauce_choice == "6":
        sauce = Mushrooms()
    elif sauce_choice == "7": 
        sauce = Goat_Cheese()
    elif sauce_choice == "8":
        sauce = Meat()
    elif sauce_choice == "9":
        sauce = Onions()
    elif sauce_choice == "10":
        sauce = Corn()
    else:
        sauce = not_sauce()
    return sauce

#müşteri bilgileri,pizza ismi ve tercih edilen sos,ücret ve sipariş zamanını alıp csv dosyayı yapan fonksiyon
def record_order(name, surname, tc_number, credit_card, pizza, sauce):
    now = datetime.datetime.now()
    with open("Orders_Database.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Surname", "TC Number", "Credit Card Number", "Pizza Name", "Sauces", "Cost","Time"])
        writer.writerow([name, surname, tc_number, credit_card, pizza.name, ", ".join([s.name for s in pizza.sauces]), pizza.get_cost(),now])

#akış sırası
if __name__ == '__main__':
    pizza = get_pizza_order()
    sauce = get_sauce_order()
    pizza.add_sauces(sauce)
    name, surname, tc_number, credit_card, password = get_customer_info()
    d = pizza.get_description()
    c = pizza.get_cost()
    record_order(name, surname, tc_number, credit_card, pizza, sauce)
    print("Thank you for your order, {} {}!".format(name, surname))