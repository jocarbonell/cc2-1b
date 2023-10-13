# Programmed by Jennylyn Carbonell

# Summation

# Start of the program
# Variables and Input
input_num = int(input("Input: "))
sum = 0
formula_list = []

# Functions
# Formula
while len(formula_list) < input_num:
    for i in range(1, input_num+1):
        formula_list.append(i) 
print("Formula:", "+".join(map(str, formula_list)))

# Summation
for i in range(1, input_num+1): 
    sum += i 
print("Summation:", sum)
# End of the program
