def roman_numeral(list):
    romans = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    total = 0
    idx = 0

    while idx < len(list):
        if idx < len(list) - 1:
            twoChar = list[idx] + (list[idx + 1] or "")

            if twoChar in romans:
                total += romans[twoChar]
                idx += 2
                continue
        
        total += romans[list[idx]]
        idx += 1

    return total

print("Expecting: 1")
print(roman_numeral("I"))

print("")

print("Expecting: 9")
print(roman_numeral("IX"))

print("")

print("Expecting: 402")
print(roman_numeral("CDII"))