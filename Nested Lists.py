if __name__ == '__main__':
    students= list()
    scores = list()
    new_lst = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
        srted_students = sorted(students)
        scores.append(score)
        srted_score = sorted(scores)
   
    for scr in srted_score:
        if scr > min(srted_score):
            new_lst.append(scr)
    for student in srted_students:
        if student[1] == new_lst[0]:
            print(student[0])
      
