print("Welcome to the Space Travel Calculator!")
distance = int(input("Enter distance to the celestial object (in light years): "))
speed = int(input("enter the spacecraft speed (in fraction of the speed of light): "))
time = (distance/speed)
print("It will take", time, "light-years to reach your dsetination")