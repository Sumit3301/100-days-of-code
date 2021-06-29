#Calculator
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

second=float(input("Enter your second number"))

for symbols in operations:
    operat=input("Enter your operation")
    
