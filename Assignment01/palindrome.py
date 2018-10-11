def isPalindrome(s):
    inputStr = input("Enter  string:")
    if inputStr == inputStr[::-1]:
        print("That's a palindrome.")
    else:
        print("That isn't a palindrome.")
        
isPalindrome('poop')