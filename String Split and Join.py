def split_and_join(line):
    # write your code here
    new_line = line.split(' ')
    new_line = '-'.join(new_line)
    return new_line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
