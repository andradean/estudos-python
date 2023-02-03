num = int(input('digite numero um: '))
num2 = int(input('digite numero dois: '))
num3 = int(input('digite numero tres: '))

if num > num2 and num > num3:
    print(f"esse numero é o 100maior: {num}")
if num2 > num and num2 > num3:
    print(f"esse numero é o maior: {num2}")
if num3 > num and num3 > num2:
    print(f"esse numero é o maior: {num3}")

if num < num2 and num < num3:
    print(f"esse numero é o menor: {num}")
if num2 < num and num2 < num3:
    print(f"esse numero é o menor: {num2}")
if num3 < num and num3 < num2:
    print(f"esse numero é o menor: {num3}")





