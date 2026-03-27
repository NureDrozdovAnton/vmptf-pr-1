from datetime import datetime

def task1():
    for i in range(1, 11):
        print(i)

def input_number(message = "Enter a number: "):
    while True:
        try:
            inp = input(message)

            if inp.lower() == 'exit':
                print("Exiting the program.")
                exit()
            num = float(inp)
            return num
        except ValueError:
            print("Invalid input. Please enter a number or 'exit' to quit.")

def task2():
    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")
    num3 = input_number("Enter third number: ")
    average = (num1 + num2 + num3) / 3
    print(f"The average is: {average}")

def task3():
    current_year = datetime.now().year
    year_of_birth = int(input_number("Enter your year of birth: "))
    
    age = current_year - year_of_birth

    if age < 0:
        print("You haven't been born yet!")
    else:
        print(f"You are {age} (or {age - 1}) years old.")

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}, author: {self.author}, year: {self.year}")

def task4():
    book = Book("1984", "George Orwell", 1949)
    book.display_info()

# task1()
# task2()
# task3()
# task4()
