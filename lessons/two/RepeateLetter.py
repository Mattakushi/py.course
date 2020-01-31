def letter(text):
    letters = ""
    for x in text:
        if x.isalpha():
            letters = "".join([letters, x])
    letters = sorted(letters.lower())
    result = max(letters, key=letters.count)
    print(result)


letter("Hello World!")
letter("How do you do?")
letter("One")
letter("Oops!")
letter("AAaooo!!!!")
letter("abe")
