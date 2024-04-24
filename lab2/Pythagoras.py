print()

option = int(input ("Pythagoras’ Calculator"
                    "\n Enter 1 to Find the length of A given B and C"
                    "\n Enter 2 to Find the length of B given A and C"
                    "\n Enter 3 to Find the length of C given A and B"
                    "\n "))

if option == 1:
    B = int(input("Please enter length of side B: "))
    C = int(input("Please enter length of side C: "))
    print(f"Length of side A is {(C**2 - B**2)**0.5}")
elif option == 2:
    A = int(input("Please enter length of side A: "))
    C = int(input("Please enter length of side C: "))
    print(f"Length of side B is {(C**2 - A**2)**0.5}")
elif option == 3:
    A = int(input("Please enter length of side A: "))
    B = int(input("Please enter length of side B: "))
    print(f"Length of side C is {(A**2 + B**2)**0.5}")
else:
    print("Invalid option entered.")