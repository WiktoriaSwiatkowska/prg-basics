def avg_speed(distance,hours,minutes):
   time = hours + minutes / 60
   result = distance / time
   return result

# takes two numbers from keyboard
n1 = int(input("distance:"))
n2 = int(input("hours:"))
n3 = int(input("minutes:"))

# calculates arightmtic mean and print result
result = avg_speed(n1,n2,n3)
print(f'The average speed when {n1}km and {n2} hours and {n3} minutes is {result}')