cart = []

price = {
	'Apple' : 0.60,
	'Banana' : 0.80,
	'Coconut' : 1.00,
	'Durian' : 10.00,
}



def displayProducts():
	for item in price:
		print item + " " + str(price[item])

def addProduct(product):
	cart.append(product)

def calcTotal():
	total = 0.00
	for item in cart:
		total = total + price[item]

	return total


def showCart():
	print "Items in cart: "
	for item in cart:
		print item
		print price[item]
		print "----------"
	print "total is: "
	print calcTotal()


def main():

	print "Welcome to FruitBay  \n The World's Best Fruit Seller!"

	print "**************************************************"

	cont = 'y'
	while cont =='y':
		print "1) Purchase"
		print "2) Show Cart"
		print "3) Checkout"
		choice = raw_input("What would you like to do? : ")
		if choice == '1':
			displayProducts()
			product = raw_input("Product name: ")
			addProduct(product)
		elif choice == '2':
			showCart()
		elif choice == '3':
			print "Please pay RM:"
			print calcTotal()
			print "THANK YOU!"
		else :
			print "WRONG INPUT!"
		cont = raw_input('Continue: y/n ?: ')
	print "\n \n \n \n\n\n\n\n\n\n\n\n\n\n\n"


main()

