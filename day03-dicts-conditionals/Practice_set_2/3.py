# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

word1 = "Make a lot of money"
word2 = "buy now"
word3 = "subscribe this"
word4 = "click this"

text = input("Write Comment here: ")

if (word1 in text or word2 in text or word3 in text or word4 in text):
    print("Spam")
else:
    print("Not spam")