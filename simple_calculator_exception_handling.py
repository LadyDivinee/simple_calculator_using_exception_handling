#parent class constructor
class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
#to display the result
    def final_answer(self, operation, answer):
        print("Selected Operation: ", operation)
        print("Answer: ", answer)
#child class inherited from Calculator
class CalculatorOperations(Calculator):
    #addition operation
    def addition(self):
        return self.first_number + self.second_number
    #for subtraction operation
    def subtraction(self):
        return self.first_number - self.second_number
    #for multiplication operation
    def multiplication(self):
        return self.first_number * self.second_number
    #for division operation
    def division(self):
        return self.first_number / self.second_number
#main program
def calculator_system():
    #exception handling
    while True:
        print("+++ Simple Calculator by Lady Divine OTG <3 +++")
        try:
            num_1 = float(input("Enter first number: "))
            num_2 = float(input("Enter second number: "))
            simple_calculator = CalculatorOperations(num_1, num_2)
            print("""
                ==============================
                |      S E L E C T I O N     |
                |----------------------------|
                | 1. Add                     |
                | 2. Subtract                |
                | 3. Multiply                |
                | 4. Divide                  |
                |============================|
                """)
            input_operation = input("Number of your choice: ")

            if input_operation == '1':
                simple_calculator.final_answer("Addition", simple_calculator.addition())

            elif input_operation == '2':
                simple_calculator.final_answer("Subtraction", simple_calculator.subtraction())

            elif input_operation == '3':
                simple_calculator.final_answer("Multiplication", simple_calculator.multiplication())

            elif input_operation == '4':
                simple_calculator.final_answer("Division", simple_calculator.division())

            else:
                print("Invalid selection.")
        #error handling for input problems
        except ValueError:
            print("Only numerical values are accepted.")
        #error handling to prevent crash when dividing by 0
        except ZeroDivisionError:
            print("Error: You are dividing by zero.")
        #to run the program
        finally:
            print("--- Calculation process completed ---")
        #asks the user if they want to continue
        if input("You want to try again? (yes/no): ") != 'yes':
            print("Thank you!")
            break