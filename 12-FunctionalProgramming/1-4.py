# takes two numbers from keyboard
n1 = int(input("speed:"))

# define an anonymous function
mean = lambda x: x / 1000 *3600


# calculates arightmtic mean and print result
result = mean(n1)
print(f"The speed {n1} in km/h is {result}")