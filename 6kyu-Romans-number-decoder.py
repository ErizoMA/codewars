roman = "MCMXC"
# Dictionary
romanDict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
# Sum
number = 0
# Defining which are + or -
for i in range(len(roman)-1):
    if romanDict[roman[i]] >= romanDict[roman[i+1]]:
        number += romanDict[roman[i]]
    else:
        number -= romanDict[roman[i]]

print(number + romanDict[roman[-1:]])
