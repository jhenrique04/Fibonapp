print("Welcome to Fibonapp")
n1 = 1
n2 = 2
position = int(input("What position of the sequence do you want to print? "))
for i in range(3, position):
    aux = n1 + n2
    n1 = n2
    n2 = aux
print(f"The number contained in this position is: {n2}")