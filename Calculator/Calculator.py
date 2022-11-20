'''Calculator'''
print(" Calculator")
option = 0
while (option !=3):
	print("Choose mode:")
	print("-Scientific press 1")
	print("-Programmer press 2")
	print("-To exit calculator press 3")
	option = int(input())
	while option == 1:
		print("Scientific Mode")
		print("Enter input1 , operation , input2")
		print("Example: 2 + 3")
		print ("1-Add press '+'\n2-Sub press '-'\n3-Division press '/'")
		print("4-Multiply press '*'\n5-Modolus press '%'\n6-Power press '^'")
		num1 , operation , num2 = input().split()
		num1 = int(num1)
		num2 = int(num2)
		if operation == '+':
			result = num1 + num2
		elif operation == '-':
			result = num1 - num2
		elif operation == '\/':
		 	result = num1 / num2
		elif operation == '*':
			result = num1 * num2
		elif operation == '%':
			result = num1 % num2
		elif operation == '^':
			result = num1 ** num2
		print(end="\r")
		print(num1,operation,num2,"=",result)
		##print(end =" ","=",result)
		print("-To exit scientific mode press 0\n-To continue press 1")
		option = int(input())
	while option == 2:
		print("Programmer Mode")
		print("Choose operation")
		print ("1-AND \n2-OR \n3-NOT \n4-XOR \n5-Shift Left \n6-Shift Right \n7-Convert Numeric System")
		operation = input()
		if operation == '1':
			num1 = int(input("Num1 = "))
			num2 = int(input("Num2 = "))
			operant = '&'
			result = num1 & num2
			print(num1,operant,num2,"=",result)
			print(bin(num1),operant,bin(num2),"=",bin(result))
		elif operation == '2':
			num1 = int(input("Num1 = "))
			num2 = int(input("Num2 = "))
			operant = '|'
			result = num1 | num2
			print(num1,operant,num2,"=",result)
			print(bin(num1),operant,bin(num2),"=",bin(result))
		elif operation == '3':
			num1 = int(input("Num = "))
			operant = '~'
			result = ~num1
			print(operant,num1,"=",result)
			print(operant,bin(num1),"=",bin(result))
		elif operation == '4':
			num1 = int(input("Num1 = "))
			num2 = int(input("Num2 = "))
			operant = '^'
			result = num1 ^ num2
			print(num1,operant,num2,"=",result)
			print(bin(num1),operant,bin(num2),"=",bin(result))
		elif operation == '5':
			num1 = int(input("Num = "))
			num2 = int(input("n = "))
			operant = '<<'
			result = num1 << num2
			print(num1,operant,num2,"=",result)
			print(bin(num1),operant,num2,"=",bin(result))
		elif operation == '6':
			num1 = int(input("Num = "))
			num2 = int(input("n = "))
			operant = '>>'
			result = num1 >> num2
			print(num1,operant,num2,"=",result)
			print(bin(num1),operant,num2,"=",bin(result))
		elif operation == '7':
			print("1-Decimal to Binary\n2-Binary to Decimal\n3-Decimal to Hex\n4-Hex to Decimal")
			print("5-Decimal to Oct\n6-Oct to Decimal")
			conversion = input ()
			num1 = input("Num = ")
			if (conversion == '1'):
				num1 = int(num1)
				result = bin(num1)
				print("bin(",num1,") = ",result)
			elif(conversion == '2'):
				num1 = int(num1,2)
				result = int(num1)
				print("Dec(",bin(num1),") = ",result)
			elif(conversion == '3'):
				num1 = int(num1)
				result = hex(num1)
				print("hex(",num1,") = ",result)
			elif(conversion == '4'):
				num1 = int(num1,16)
				result = int(num1)
				print("Dec(",hex(num1),") = ",result)
			elif(conversion == '5'):
				num1 = int(num1)
				result = oct(num1)
				print("oct(",num1,") = ",result)
			elif(conversion == '6'):
				num1 = int(num1,8)
				result = int(num1)
				print("Dec(",oct(num1),") = ",result)
		print(end="\r")
		print("-To exit Programmer mode press 0\n-To continue press 2")
		option = int(input())
	
	