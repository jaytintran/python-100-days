from art import logo_calculator
print(logo_calculator)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2
  
def divide(n1, n2):
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

operators = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def do_calc():
  continue_calc = True
  while continue_calc:
    first_num = float(input("What's the first number?: "))
    operator_choice = input("Pick an operation [ + | - | * | / ]: ")
    second_num = float(input("What's the next number?: "))
  
    calc_func = operators[operator_choice]
    result = calc_func(first_num, second_num)
  
    print(f"{first_num} {operator_choice} {second_num} = {result}")
    continue_calc_ask = input("Do you want to contine other calculation? Type 'yes' or 'no': ").lower()
    if continue_calc_ask == 'no':
      continue_calc = False
  do_calc()

do_calc()
# def do_calculation(first_num, second_num, operator):
#   if operator == "+":
#     result = add(first_num, second_num)
#   elif operator_choice == "-":
#     result = subtract(first_num, second_num)
#   elif operator_choice == "*":
#     result = multiply(first_num, second_num)
#   elif operator_choice == "/":
#     result = divide(first_num, second_num)
#   print(f"{first_num} {operator_choice} {second_num} = {result} ")

# do_calculation(first_num, second_num, )