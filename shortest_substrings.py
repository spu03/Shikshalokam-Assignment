def shortest_substring(s, x):
    substrings = []
    for i in range(len(s)):
        for j in range(i + x, len(s) + 1):
            substring = s[i:j]
            if len(substring) == x and substring[0] == substring[-1]:
                substrings.append(substring)
    return substrings

def print_shortest_substrings(s, x):
    substrings = shortest_substring(s, x)
    if not substrings:
        print("Answer: not-found")
    else:
        print("Answer:", " ".join(substrings))

s = input("string: ")
x = int(input("x: "))

print_shortest_substrings(s,x)
