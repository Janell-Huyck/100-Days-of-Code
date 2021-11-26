from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculate():
  print(logo)

  keep_calculating = "yes"
  num1 = int(input("What's the first number? "))

  while keep_calculating == "yes":
    for operation in operations:
      print(operation)
    operation_choice = input("Pick an operation symbol from above: ")
    num2 = int(input("What's the next number? "))

    answer = operations[operation_choice](num1, num2)
    print(f"{num1} {operation_choice} {num2} = {answer}")

    keep_calculating = input("Continue calculating?  Yes or No: ").lower()
    if keep_calculating == "yes":
      num1 = answer
    else:
      calculate()
  
calculate()
