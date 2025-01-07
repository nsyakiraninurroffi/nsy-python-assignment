# 2. 1 + 2 + 3 + 4 + 5 = 15
i = 1
total = 0
output = ""
while i <= 5:
    output += str(i)
    total += i
    if i < 5:
        output += " + "
    i += 1
print(f"{output} = {total}")