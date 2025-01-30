'''
Tutorial:
Get Input from the User Write a program that asks the user to input a sentence.

Perform the Following Operations Using String Methods:

a. Convert the string to uppercase and lowercase, and print the results.

b. Find and print the length of the string.

c. Count how many times the word "the" (case-insensitive) appears in the string.

d. Check if the string ends with a punctuation mark (e.g., ., !, ?). Print True or False.

e. Replace all spaces with a hyphen (-) and print the modified string.

f. Extract and print the first word from the string.

#***SOLUTIONS****
'''
sent=input("Enter a sentence")
print('(a)Uppercase:',sent.upper())
print('(b)Length:',len(sent))
print('(c)Count:',sent.count("the"))
print('(d)Punctuation:',sent.endswith(("!", "?", ",")))
print('(e)Remove:',sent.replace(' ','-'))
print('(f)Split:',sent[0].split())
