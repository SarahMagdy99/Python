def get_nth_key(dictionary , n):
    if n < 0:
        n += len(dictionary)
    for i, value in enumerate(dictionary.values()):
        if i == n:
            return value
    raise IndexError("dictionary index out of range") 
const_Password = 1234	
Cart = {}
Products = ["Apple" , "Banana" , "Cherry"]
Price = {
"Apple" : 20,
"Banana": 15,
"Cherry": 30
}

Stock = {
"Apple" : 40,
"Banana": 30,
"Cherry": 70
}
print("#Welcome to ITI shop")
while(1):
	print("Select mode :\n- For customer press 1\n- For owner press 2\n- To exist press 0")
	mode_option = int(input())
	if mode_option == 1:
		Customer_Mode = 1
		Bill = 0
		while(Customer_Mode == 1):
			print("#Customer Mode:")
			print("-To show our products press 1\n-To Buy from our products press 2")
			print("-To print the bill press 3\n-To exist customer mode press 0 ")
			customer_Option = int(input())
			if(customer_Option == 0): #Exit customer mode
				Customer_Mode = 0
				continue
			elif (customer_Option == 1): #Print products
				i = 1 
				print("Our products with prices:")
				for key, value in Price.items():
					print(i,"- " ,key, ' : ', value)
					i= i+1
			elif(customer_Option == 2): #Buy
				operation = 1
				while(operation == 1):
					index = int(input("Write product number:"))-1 
					n = int(input("How many kilos you want?"))
					Bill = Bill + n * get_nth_key(Price , index)
					p = Products[index] #Get the product name from the list
					St = Stock[p]       #Get the value of product in stock
					St = St - n
					Stock[p] = St       #Modify the value of product in stock
					for key, value in Cart.items():
						if (p == key):
							n = n + value[0]
					Cart[p] = [n,n*get_nth_key(Price , index)]
					print("Confimation: You bought ",n," kilos of ",p ," cost = ",get_nth_key(Price , index)," per kilo")
					operation = int(input("To keep buying press 1 to exit press 0"))		
			elif(customer_Option == 3): #Print bill
				print("Your cart items: ")
				i = 1 
				for key, value in Cart.items():
					print(i,"- " ,key, '     :     ', value[0]," kilos  :    price  ",value[1])
					i= i+1
				print("Total Bill: ",Bill)	
	elif mode_option == 2:
		Owner_Mode = 1
		password = int(input("Enter Password: "))
		while(password != const_Password):
			password = int(input("Enter correct Password: "))
		while (Owner_Mode == 1):
			print("#ITI Owner:")
			print("-Show Products press 1\n-Add new products press 2")
			print("-Change cost press 3\n-Delete product 4\n-To exist Owner mode press 0")
			owner_Option = int(input())
			if(owner_Option == 0): #Exit Owner mode
				Owner_Mode = 0
				continue
			elif (owner_Option == 1): #Show products with prices and amount in stock
				i = 1 
				print("Products       :   Prices   :      In Stock")
				for key, value in Price.items():
					p = Products[i-1] #Get product name from products list
					print(i,"- " ,key, '     :     ', value,'     :     ',Stock[p])
					i= i+1
			elif(owner_Option == 2): #Add new product
				operation = 1
				while(operation == 1):
					p = input("Enter product name: ")
					Products.append(p)
					cost = int(input("Enter product price:"))
					Price[p] = cost
					s = int(input("How much in the stock:"))
					Stock[p] = s
					print("Confimation: You added ",p," of price ",Price[p]," with ",Stock[p]," kilos in stock")
					operation = int(input("To add other products press 1 to exit press 0"))
			elif(owner_Option == 3): #Change cost
				operation = 1
				while(operation == 1):
					index = int(input("Write product number:"))-1
					cost = int(input("Enter the new Price"))
					p = Products[index]
					Price[p] = cost
					print("Confimation: You changed the cost of ",Products[index]," to be ",Price[p])
					operation = int(input("To change price of other products press 1 to exit press 0"))
			elif(owner_Option == 4): #Delete product
				operation = 1
				while(operation == 1):
					index = int(input("Write product number:"))-1
					p = Products[index]
					Price.pop(p)
					Stock.pop(p)
					Products.remove(p)
					print("Confimation: You are deleting the product ",p)
					operation = int(input("To delete other products press 1 to exit press 0"))
					
	elif mode_option == 0:
		break;