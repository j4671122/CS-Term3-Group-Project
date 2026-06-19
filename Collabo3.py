# J.Yang, V.Bui — CS Term 3 Group Project

class Student:
    """Stores a student's name, year group, and term grades, and provides grade analysis methods."""

    def __init__(self, name, year_group, grades):
        self.name = name
        self.year_group = year_group
        self.grades = grades  

    def subjectavg(self, subject_name):
        """Returns the average score across all terms for the given subject."""
        scores = self.grades[subject_name]
        return sum(scores) / len(scores)

    def yearavg(self):
        """Returns the overall average across all subjects for the year."""
        subject_averages = [self.subjectavg(subject) for subject in self.grades]
        return sum(subject_averages) / len(subject_averages)

    def failcheck(self):
        """Prints a warning if the student's average in any subject is below 55."""
        failed_subjects = [subject for subject in self.grades if self.subjectavg(subject) < 55]
        if failed_subjects:
            print(f"  !! {self.name} failed: {', '.join(failed_subjects)}")

    def writegrades(self, grade_dict):
        """Writes this student's subject averages and year average into the provided dictionary."""
        grade_dict[self.name] = {subject: round(self.subjectavg(subject), 2) for subject in self.grades}
        grade_dict[self.name]["Year Average"] = round(self.yearavg(), 2)


# --- Student data (4 students minimum as required) ---
students = [
    Student("Allen",  10, {"Math": [72, 68, 75], "Science": [80, 85, 78], "English": [60, 65, 70]}),
    Student("Junsu Yang",    11, {"Math": [45, 50, 52], "Science": [88, 92, 85], "English": [55, 60, 58]}),
    Student("Vinh",   9, {"Math": [90, 88, 92], "Science": [78, 82, 80], "English": [85, 90, 88]}),
    Student("David Lee",    12, {"Math": [60, 55, 58], "Science": [40, 45, 48], "English": [70, 72, 68]}),
    Student("Emma Wilson",  10, {"Math": [75, 80, 78], "Science": [65, 70, 68], "English": [82, 85, 80]}),
]

# --- Build the school-wide grades dictionary ---
all_grades = {}
for student in students:
    student.writegrades(all_grades)

for student in sorted(students, key=lambda s: s.name):
    print(f"\nName:       {student.name}")
    print(f"Year Group: {student.year_group}")
    for subject in ["Math", "Science", "English"]:
        print(f"  {subject:10} Avg: {student.subjectavg(subject):.0f}")
    print(f"  {'Year':10} Avg: {student.yearavg():.0f}")
    student.failcheck()

#Highest overall average (handles ties)
highest_avg = max(info["Year Average"] for info in all_grades.values())
top_students = [name for name, info in all_grades.items() if info["Year Average"] == highest_avg]

if len(top_students) == 1:
    print(f"Highest year average: {top_students[0]} ({highest_avg:.0f})")
else:
    print(f"Tied for highest year average ({highest_avg:.0f}): {', '.join(top_students)}")

#Hardest subject — lowest average across all students (handles ties)
subjects = ["Math", "Science", "English"]
subject_class_avgs = {
    subject: sum(all_grades[name][subject] for name in all_grades) / len(all_grades)
    for subject in subjects
}

lowest_avg = min(subject_class_avgs.values())
hardest_subjects = [s for s, avg in subject_class_avgs.items() if avg == lowest_avg]

if len(hardest_subjects) == 1:
    print(f"Hardest subject: {hardest_subjects[0]} (class avg: {lowest_avg:.0f})")
else:
    print(f"Tied for hardest subject (class avg: {lowest_avg:.0f}): {', '.join(hardest_subjects)}")

