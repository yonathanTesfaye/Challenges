def count_substring(string, sub_string):
    pos = string.find(sub_string)
    counter = 0
    for num in range(pos,len(string)):
        new_str = string[num:num + len(sub_string)]
        if new_str == sub_string:
            counter +=1
    return  counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
