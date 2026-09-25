print("Enter the passcode of eight characters")
passcode = input("Enter passcode: ")
while len(passcode) != 8:
	print("Passcode should be exactly 8 characters.")
	passcode = input("Re-enter passcode: ")
print("Valid passcode:", passcode)