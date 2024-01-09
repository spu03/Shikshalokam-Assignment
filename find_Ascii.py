def transform_string(s):
    ascii_value = []
    transformed_str = list(s)
    length = len(s)
    for i in range(length):
        ascii_val = ord(s[i])

        if ascii_val % 2 == 0:
            if i < length - 1 and not transformed_str[i + 1].isdigit():
                next_ascii_val = (ascii_val % 7) + ord(s[i + 1])
                if next_ascii_val > 127:
                    next_ascii_val = 83
                transformed_str[i + 1] = chr(next_ascii_val)
        else:
            if i > 0 and not transformed_str[i - 1].isdigit():
                prev_ascii_val = ord(transformed_str[i - 1]) - (ascii_val % 5)
                if prev_ascii_val < 0:
                    prev_ascii_val = 83
                transformed_str[i - 1] = chr(prev_ascii_val)

        ascii_value.append(str(ascii_val))

    transformed_str = "".join(transformed_str)
    return transformed_str, "-".join(ascii_value)

s = input("s: ")
transformed_str, ascii_value = transform_string(s)
print("ASCII:", ascii_value)
print("Final Answer:", transformed_str)