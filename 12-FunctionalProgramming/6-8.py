arr = [37,51,44,23,78,92,39,84,83,51]
lim = [70,40,30]
def min_pts(limit):
   return lambda pts: pts >= limit

print(list(map(min_pts(lim),arr)))

