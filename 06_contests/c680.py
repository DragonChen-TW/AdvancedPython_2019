import sys

# input problems
problems_len = int(sys.stdin.readline()[:-1])
problems = list(sys.stdin.readline()[:-1])
s_per_problem = 100 // problems_len

# input students
students_len = int(sys.stdin.readline()[:-1])
for student in sys.stdin:
    student = student[:-1]
    if len(student) > problems_len:
        student = student[:problems_len]

    score = 0
    for i, s in enumerate(student):
        if s == problems[i]:
            score += s_per_problem

    print(score)
