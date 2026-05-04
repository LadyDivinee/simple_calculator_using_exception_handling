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