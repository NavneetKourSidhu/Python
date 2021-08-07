def palindrome(number):
	reverse = number[::-1]
	if reverse == number:
		print("Palindrome")
	else:
		print("not a palindrome")
print(palindrome("helloolleh"))
