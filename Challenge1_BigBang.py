import json

result = []
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        result.append("BIGBANG")
    elif num % 3 == 0:
        result.append("BIG")
    elif num % 5 == 0:
        result.append("BANG")
    else:
        result.append(str(num))

with open('output.json', 'w') as file:
    json.dump(result, file)