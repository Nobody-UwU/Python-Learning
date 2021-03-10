string = "malayalam"
reverse_string = ""
for x in string:
    reverse_string = x + reverse_string
if string == reverse_string:
    print("Yes, the word is a palindrome")
else:
    print("No, the word is not a palindrome")