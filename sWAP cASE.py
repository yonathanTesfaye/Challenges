def swap_case(s):
    new_str = str()
    for i in s:
        if i.isupper():
            new = i.lower()
        elif i.islower():
            new = i.upper()
        else:
            new = i
        new_str = new_str.__add__(new)
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
