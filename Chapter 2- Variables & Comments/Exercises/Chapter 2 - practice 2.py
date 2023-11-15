num_courses = int(input("Input how many courses there are: "))
total_marks = 500
total_course_marks = 0
for i in range(num_courses):
    course_marks = int(input(f"Enter marks for course {i + 1: }: "))
    total_course_marks += course_marks
average_marks = total_course_marks / num_courses
precentage = (total_course_marks / num_courses) *100
print(f"Average marks: {average_marks}")
print(f"precentage: {precentage}%")