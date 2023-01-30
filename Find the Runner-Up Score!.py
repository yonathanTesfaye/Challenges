if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unum=list()
    for num in arr:
        if num in unum:
            continue
        else:
            unum.append(num)
    srt = sorted(unum, reverse=True)
    print(srt[1])
