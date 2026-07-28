#name = "hassan"

#print(name[0])
#print(name[5])
#print(name[3])
#print(name[0:3])



sentence = input("Enter a sentence: ")



print("Uppercase: " , sentence.upper())
print("Lowercase: " , sentence.lower())
print("Title Case: " , sentence.title())
print("Capitalized Form:", sentence.capitalize())


char_count = len(sentence)
word_count = len(sentence.split())


print("Total number of characters:", [char_count])
print("Total number of words: ",[word_count])


