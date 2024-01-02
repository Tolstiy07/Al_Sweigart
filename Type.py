
x,y =2,2
WIDTH =78
HEIGHT = 18



left = (x - 1) % WIDTH
right = (x + 1) % WIDTH
above = (y - 1) % HEIGHT
below = (y + 1) % HEIGHT


print (f"left-{left}")
print (f"right-{right}")
print (f"above-{above}")
print (f"below-{below}")
print()
left = (x - 1) / WIDTH
right = (x + 1) / WIDTH
above = (y - 1) / HEIGHT
below = (y + 1) / HEIGHT


print (f"left-{left}")
print (f"right-{right}")
print (f"above-{above}")
print (f"below-{below}")

print( (0-1)//78)

print(5//3)
print(5%3)
print()
print(-3//5)
print(4%5)
