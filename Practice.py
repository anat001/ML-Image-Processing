
# We need to initialize our variables count and val for our while loop
minimum = -1
val = int(input())

while val != 0:
    if val < minimum:
        minimum = val
    val = int(input())
print(minimum)










