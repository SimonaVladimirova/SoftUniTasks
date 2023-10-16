def transform_strings(string1, string2):
    if len(string1) != len(string2):
        print("Cannot transform: the lengths of the two strings are different.")
        return

    result = list(string1)

    for i in range(len(string1)):
        if result[i] != string2[i]:
            result[i] = string2[i]
            transformed_string = ''.join(result)
            print(transformed_string)


string1 = input()
string2 = input()

transform_strings(string1, string2)
