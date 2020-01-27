text = input("Enter text here: ")
list = text.split(' ')

print("Most common word:", max(set(list), key=list.count))
print("The longest word:", max(list, key=len))
