#Q3 function that takes dict of course grades of student
#and returns the name of the course with the lowest grade

def min_grade(exams):
    minn_grade = float("inf")
    min_course = ""
    for course, grade in exams.items():
        if grade < minn_grade:
            minn_grade = grade
            min_course = course
    return min_course
  

print(min_grade({"art":90, "music":92, "drama":87}))