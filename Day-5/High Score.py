student_scores = input("Enter the scores of all of the students : ").split()
max = 0
for score in student_scores:
    if int(score) > max:
        max = int(score)
print(f'The highest score in the list is {max}')