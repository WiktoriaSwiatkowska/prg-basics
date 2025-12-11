###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   result = x * y
   return result

# takes two numbers from keyboard
n1 = int(input("number1:"))
n2 = int(input("number2:"))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')