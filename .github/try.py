def greet(name):
  """Greets the person passed in as a parameter."""
  print(f"Hello, {name}!")

def add(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

def main():
  """Main function to run the application."""
  user_name = input("Enter your name: ")
  greet(user_name)

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  sum_of_numbers = add(num1, num2)
  print(f"The sum of {num1} and {num2} is: {sum_of_numbers}")

if __name__ == "__main__":
  main()
