#Calculator
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2
  
#Multiply
def multiply(n1, n2):
  return n1 * n2
  
#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  calculator_on = True
  
  while calculator_on == True:
    operation_symbol = input("Choose an operation: ")
    num2 = float(input("Whats the next number?: "))
    operation_function = operations[operation_symbol]
    answer = operation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if to_continue == "n":
      calculator_on = False
      calculator()
      
    else:
      num1 = answer
    
  
calculator()
