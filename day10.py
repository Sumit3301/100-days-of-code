
#Dictionary Calculator
import pyfiglet
  
result = pyfiglet.figlet_format("Calculator")
print(result)   
def add(first, second):
  return first +second

def subtract(first, second):
  return first- second

def multiply(first, second):
  return first* second

def divide(first, second):
  return first/ second

first=float(input("Enter First number"))
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}



for symbols in operations:
  print(symbols)
operat=input("Enter your operation")
second=float(input("Enter your second number"))
func=operations[operat]
print(func(first,second))


    
