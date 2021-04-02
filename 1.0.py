

print(colored("█▄▀ ▄▀█ █░░ █▄▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█", 'red'))
print(colored("█░█ █▀█ █▄▄ █░█ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄", 'red'))


name = input ("nickname:")
password = input ("password:")

print ("hello " + name + ", good morning =D")
 
what = input ("что делаем ? (+,-): " )

a = float( input("пожалуйста введите цифру: ") )
b = float( input("пожалуйста введите цифру: ") )

if what == "+":
	c = a + b
	print("ваш результат: " + str(c))
elif what == "-":
	c = a - b
	print("ваш результат: " + str(c))
else:
	print("ты дебил")
