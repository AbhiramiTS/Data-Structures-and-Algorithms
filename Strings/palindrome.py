def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

# Test Case 1: Palindrome string
str1 = "Malayalam"
assert is_palindrome(str1) == True, f"Test Case 1 failed: {str1} is a palindrome."

# Test Case 2: Non-palindrome string
str2 = "Hello"
assert is_palindrome(str2) == False, f"Test Case 2 failed: {str2} is not a palindrome."

# Test Case 3: Empty string
str3 = ""
assert is_palindrome(str3) == True, "Test Case 3 failed: Empty string is a palindrome."

# Test Case 4: Palindrome with spaces
str4 = "A man a plan a canal Panama"
assert is_palindrome(str4) == True, f"Test Case 4 failed: {str4} is a palindrome."

# Test Case 5: Palindrome with mixed case
str5 = "Able was I ere I saw Elba"
assert is_palindrome(str5) == True, f"Test Case 5 failed: {str5} is a palindrome."

print("All test cases passed.")
