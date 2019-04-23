import sys

# input problems
problems_len = int(sys.stdin.readline()[:-1])
problems = list(sys.stdin.readline()[:-1])
s_per_problem = 100 // problems_len # each problrm's score

# input students
students_len = int(sys.stdin.readline()[:-1])
for student in sys.stdin:
    student = student[:-1]

    # your turn
