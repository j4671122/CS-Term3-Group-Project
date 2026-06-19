# J.Yang, V.Bui — CS Term 3 Group Project

class Student:

    def __init__(self, name, year_group, grades):
        self.name = name
        self.year_group = year_group
        self.grades = grades 

    def subjectavg(self, subject_name):
        scores = self.grades[subject_name]
        return sum(scores) / len(scores)

    def yearavg(self):
        subject_averages = []
        for subject in self.grades:
            subject_averages.append(self.subjectavg(subject))
        return sum(subject_averages) / len(subject_averages)

    def failcheck(self):
        failed_subjects = []
        for subject in self.grades:
            if self.subjectavg(subject) < 55:
                failed_subjects.append(subject)
                
        if len(failed_subjects) > 0:
            print(f"  !! {self.name} failed: {failed_subjects}")


# Student data (4 students minimum as required)
students = [
    Student("Allen",  10, {"Math": [72, 68, 75], "Science": [80, 85, 78], "English": [60, 65, 70]}),
    Student("Junsu Yang",    11, {"Math": [45, 50, 52], "Science": [88, 92, 85], "English": [55, 60, 58]}),
    Student("Vihn",   9, {"Math": [90, 88, 92], "Science": [78, 82, 80], "English": [85, 90, 88]}),
    Student("David Lee",    12, {"Math": [60, 55, 58], "Science": [40, 45, 48], "English": [70, 72, 68]}),
    Student("Emma Wilson",  10, {"Math": [75, 80, 78], "Science": [65, 70, 68], "English": [82, 85, 80]}),
]

all_grades = {}
for student in students:
    student_info = {}
    for subject in student.grades:
        student_info[subject] = round(student.subjectavg(subject), 2)
    student_info["Year Average"] = round(student.yearavg(), 2)
    
    all_grades[student.name] = student_info

for student in sorted(students, key=lambda s: s.name):
    print(f"\nName: {student.name}")
    print(f"Year Group: {student.year_group}")
    for subject in ["Math", "Science", "English"]:
        print(f"  {subject}: {student.subjectavg(subject):.0f}")
    print(f"  Year\tAvg: {student.yearavg():.0f}")
    student.failcheck()

# Highest overall average
highest_avg = -1
top_student = ""

for name, info in all_grades.items():
    if info["Year Average"] > highest_avg:
        highest_avg = info["Year Average"]
        top_student = name

print(f"Highest year average: {top_student} ({highest_avg:.0f})")

# Hardest subject 
subjects = ["Math", "Science", "English"]
subject_class_avgs = {}
for subject in subjects:
    total_score = 0
    for name in all_grades:
        total_score += all_grades[name][subject]
    subject_class_avgs[subject] = total_score / len(all_grades)

lowest_avg = 999
hardest_subject = ""

for subject, avg in subject_class_avgs.items():
    if avg < lowest_avg:
        lowest_avg = avg
        hardest_subject = subject

print(f"Hardest subject: {hardest_subject} (class avg: {lowest_avg:.0f})")