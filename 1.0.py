from colorama import init 
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Fore.CYAN )

print("█▄▀ ▄▀█ █░░ █▄▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█")
print("█░█ █▀█ █▄▄ █░█ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄")

print ( Back.BLACK )
print ( Fore.RED )
name = input ("----nickname----:")
password = input ("----password----:")

if password == "gg":
	print ("----hello " + name + ", good morning =D----")
else:
	print("Неверный пароль")
	exit()

 
what = input ("что делаем ? (+,-,*): " )

a = float( input("----пожалуйста введите цифру----: ") )
b = float( input("----пожалуйста введите цифру----: ") )

if what == "+":
	c = a + b
	print("----ваш результат: " + str(c) + "----")
elif what == "-":
	c = a - b
	print("----ваш результат: " + str(c) + "----")
elif what == "*":
	c = a * b
	print("----ваш результат: " + str(c) + "----")
else:
	print("----ты дебил----")
