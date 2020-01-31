def check_result(result):
    letters = []
    for item in result:
        for character in item:
            letters.append(character)
    if letters[0] == letters[1] == letters[2] != '.':
        print(letters[0])
    elif letters[3] == letters[4] == letters[5] != '.':
        print(letters[3])
    elif letters[6] == letters[7] == letters[8] != '.':
        print(letters[6])
    elif letters[0] == letters[3] == letters[6] != '.':
        print(letters[0])
    elif letters[1] == letters[4] == letters[7] != '.':
        print(letters[1])
    elif letters[2] == letters[5] == letters[8] != '.':
        print(letters[2])
    elif letters[0] == letters[4] == letters[8] != '.':
        print(letters[0])
    elif letters[2] == letters[4] == letters[6] != '.':
        print(letters[2])
    else:
        print("D")
        print("D")


check_result([
    "X.O",
    "XX.",
    "XOO"]
)
check_result([
    "OO.",
    "XOX",
    "XOX"]
)
check_result([
    "OOX",
    "XXO",
    "OXX"]
)
