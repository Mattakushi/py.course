def speech_reverse(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
            "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    twenties = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    hundred = "hundred"

    if num > 0 and num < 20:
        print(ones[num])
    elif num > 19 and num < 100:
        temp = list(str(num))
        print(twenties[int(temp[0])] + " " + ones[int(temp[1])])
    elif num > 99 and num < 1000:
        temp = list(str(num))
        sec_thr = (int(temp[1] + temp[2]))
        if sec_thr > 0 and sec_thr < 20:
            print(ones[int(temp[0])] + " " + hundred + " " + ones[sec_thr])
        else:
            print(ones[int(temp[0])] + " " + hundred + " " + twenties[int(temp[1])] + " " + ones[int(temp[2])])


speech_reverse(4)
speech_reverse(143)
speech_reverse(12)
speech_reverse(101)
speech_reverse(212)
speech_reverse(40)
