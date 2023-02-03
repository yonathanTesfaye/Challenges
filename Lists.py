if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        texts = list(input().split())
        if 'print' == texts[0]:
            print(lst)
        elif 'pop' == texts[0]:
            lst.pop()
        elif 'reverse' == texts[0]:
            lst.reverse()
        elif 'sort' == texts[0]:
            lst.sort()
        elif 'remove' == texts[0]:
            lst.remove(int(texts[1]))
        elif 'append' == texts[0]:
            lst.append(int(texts[1]))    
        elif 'insert' == texts[0]:
            lst.insert(int(texts[1]),int(texts[2]))
