# J.Yang, V.Bui — CS Term 3 Group Project

class Student:
    
    def __init__(self, name, year_group, grades):
        self.name = name
        self.year_group = year_group
        self.grades = grades

    def subjectavg(self, subject_name):
        scores = self.grades[subject_name]
        total = 0
        for score in scores:
            total += score
        return total / len(scores)

    def yearavg(self):
        total_avg = 0
        subject_count = 0
        for subject in self.grades:
            total_avg += self.subjectavg(subject)
            subject_count += 1
        return total_avg / subject_count

    def failcheck(self):
        failed_subjects = []
        for subject in self.grades:
            if self.subjectavg(subject) < 55:
                failed_subjects.append(subject)
        
        if len(failed_subjects) > 0:
            subjects_str = ""
            for i in range(len(failed_subjects)):
                if i == 0:
                    subjects_str += failed_subjects[i]
                else:
                    subjects_str += ", " + failed_subjects[i]
            print(f"  !! {self.name} failed: {subjects_str}")

    def writegrades(self, grade_dict):
        student_data = {}
        for subject in self.grades:
            student_data[subject] = round(self.subjectavg(subject), 2)
        
        student_data["Year Average"] = round(self.yearavg(), 2)
        grade_dict[self.name] = student_data


students = [
    Student("Allen",  10, {"Math": [72, 68, 75], "Science": [80, 85, 78], "English": [60, 65, 70]}),
    Student("Junsu Yang",    11, {"Math": [45, 50, 52], "Science": [88, 92, 85], "English": [55, 60, 58]}),
    Student("Vihn",   9, {"Math": [90, 88, 92], "Science": [78, 82, 80], "English": [85, 90, 88]}),
    Student("David Lee",    12, {"Math": [60, 55, 58], "Science": [40, 45, 48], "English": [70, 72, 68]}),
    Student("Emma Wilson",  10, {"Math": [75, 80, 78], "Science": [65, 70, 68], "English": [82, 85, 80]}),
]

all_grades = {}
for student in students:
    student.writegrades(all_grades)

sorted_students = sorted(students, key=lambda s: s.name)
for student in sorted_students:
    print(f"\nName: {student.name}")
    print(f"Year Group: {student.year_group}")
    
    subjects = ["Math", "Science", "English"]
    for subject in subjects:
        avg = student.subjectavg(subject)
        print(f"  {subject} Avg: {avg:.0f}")
        
    year_avg = student.yearavg()
    print(f"  Year Avg: {year_avg:.0f}")
    student.failcheck()

print("\n----------------------------------")

highest_avg = -1
top_student = ""

for name in all_grades:
    info = all_grades[name]
    if info["Year Average"] > highest_avg:
        highest_avg = info["Year Average"]
        top_student = name

print(f"Highest year average: {top_student} ({highest_avg:.0f})")

subjects_list = ["Math", "Science", "English"]
subject_class_avgs = {}

for subject in subjects_list:
    total_sum = 0
    for name in all_grades:
        total_sum += all_grades[name][subject]
    subject_class_avgs[subject] = total_sum / len(all_grades)

lowest_avg = 999
for subject in subject_class_avgs:
    if subject_class_avgs[subject] < lowest_avg:
        lowest_avg = subject_class_avgs[subject]

hardest_subjects = []
for subject in subject_class_avgs:
    if subject_class_avgs[subject] == lowest_avg:
        hardest_subjects.append(subject)

if len(hardest_subjects) == 1:
    print(f"Hardest subject: {hardest_subjects[0]} (class avg: {lowest_avg:.0f})")
else:
    result_str = ""
    for i in range(len(hardest_subjects)):
        if i == 0:
            result_str += hardest_subjects[i]
        else:
            result_str += ", " + hardest_subjects[i]
    print(f"Tied for hardest subject (class avg: {lowest_avg:.0f}): {result_str}")