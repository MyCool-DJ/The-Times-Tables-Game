user_wants = int(input("Please select a times table number: "))

for i in range (11):
	answer = i * user_wants
	print(user_wants, "x", i, "=", answer)
	