# ---------- Method Overriding Example ----------

# Base class
class Calculator:
    def calculate(self, a, b):
        print(f"Sum in Calculator: {a + b}")

# Derived class overriding the calculate method
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        # Method overriding: different behavior
        print(f"Advanced calculation (product): {a * b}")

# ---------- Operator Overloading Example ----------

class Number:
    def __init__(self, value):
        self.value = value


    def __add__(self, other):
        return Number(self.value + other.value)


    def __str__(self):
        return str(self.value)



# 1. Method Overriding
calc = Calculator()
adv_calc = AdvancedCalculator()

calc.calculate(5, 3)
adv_calc.calculate(5, 3)

print()

# 2. Operator Overloading
num1 = Number(10)
num2 = Number(20)
num3 = num1 + num2
print(f"Result of operator overloading: {num3}")

print()

# 3. Polymorphism Example (Same method name, different behaviors)
def perform_calculation(calc_obj, a, b):
    calc_obj.calculate(a, b)

perform_calculation(calc, 7, 2)
perform_calculation(adv_calc, 7, 2)
