import random

with open('outfile.txt') as f:
  lines = f.read().splitlines()
  
print(lines[random.randint(0,len(lines)-1)])
