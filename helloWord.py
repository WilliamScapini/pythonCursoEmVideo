# print("Hello World!")
romanos = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
print(type(sorted(romanos.items(), key=lambda item: item[0], reverse=True)))
