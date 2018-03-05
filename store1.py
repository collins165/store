import uuid
import random
import string
randomItems = ["Playstation 4", "Iphone 10", "Samsung Galaxy S9", "LG Smart TV", "Gaming PC",
"Speakers", "Headphones", "Nothing3", "Nothing2", "Nothing1"]
list1 = ["butter", "cheese", "milk", "bread", "eggs", "sugar"] #shopping cart items
refferal = str("".join(random.choice(string.hexdigits.upper())for i in range(7)))

class Customer(object):
    def __init__(self, firstname, lastname, street, housenumber, postalCode,
     city, country, telephone, email, credit):
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.housenumber = housenumber
        self.postalCode = postalCode
        self.city = city
        self.country = country
        self.telephone = telephone
        self.email = email
        self.credit = credit
    def addCredit(self):
        conversionRate = 3
        euro = 2500
        print("how much credit do you want to add?")
        self.credit = self.credit + (conversionRate * euro) #converting and adding credit to the balance
        print("We have added " + str(conversionRate * euro) + " credits to your account")
        print("your total balance is now: " + str(self.credit))
    def showInfo(self):
        print("Name: " + self.firstname + " " + self.lastname)
        print("Address: " + "" + self.street, self.housenumber + "\n" +
        "\t" + " " + self.postalCode + " "+ self.city + ", " + self.country)
        print("Phone number: " + self.telephone)
        print("E-mail: " + self.email)
        print("Credit balance: " + str(self.credit))
        print("User ID: " + str(uuid.uuid4()))
        print("Refferal code: " + refferal) #With random choice pick random hexdigits and make them uppercase, do that 7 times and join them)
    def randomSpin(self):
        print("You will now insert 1500 coins for a random spin where you can receive a random item")
        print("Available balance: " + str(self.credit))
        print("How many times do you want to spin?")
        spinAmount = 4
        if self.credit >= 1500 * spinAmount:
            self.credit -= 1500 * spinAmount
            for i in range(spinAmount):
                list1.append("".join(random.choice(randomItems)))
            print("Available balance left: " + str(self.credit))
            print("Your shopping cart now contains: " + ", ".join(list1) + "\n")
        else:
            print("You do not have sufficient credit for a random spin, please top up your credit" + "\n")




class ShoppingCart(Customer):
    def __init__(self, items):
        self.items = items
    def buy(self):
        new_items = ["cookies", "candy", "chocolate"]
        print("What do you want to add to the shopping cart?")
        for i in new_items:
            list1.append(i) #append each element of the newly made list to the first one
        print("you have added: " + ", ".join(new_items)) #printing them as words instead of a list
        print("Your shopping cart now consists of: " + ", ".join(list1)) #printing the entire shopping cart
    def displayCart(self):
        print("Your shopping cart now consists of: " + ", ".join(list1)) #printing the entire shopping cart

customer1 = Customer("Collins", "Woodbleach", "Vaandrigstraat", "25c", "3034PX",
 "Rotterdam", "The Netherlands", "+31642076846", "collins.woodbleach@gmail.com",
 10500)

customer1_shoppingCart = ShoppingCart(list1)



#printing statements
#customer1.addCredit()
#customer1.showInfo()
customer1.randomSpin()
customer1.randomSpin()
customer1.randomSpin()
