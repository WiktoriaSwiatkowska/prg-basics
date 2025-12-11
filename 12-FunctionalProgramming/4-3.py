grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
nice = list(filter(lambda e: e>2, grades))
average = sum(nice)/len(nice)

# print a list …
print(average)