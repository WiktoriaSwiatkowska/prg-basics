###
# Calculates arithmetic mean of two integer numbers
#
def ms_to_kmh(ms):
   result = ms / 1000 * 3600
   return result

# takes two numbers from keyboard
n1 = int(input("speed:"))


# calculates arightmtic mean and print result
result = ms_to_kmh(n1)
print(f'the speed {n1} in  km/h is {result}')