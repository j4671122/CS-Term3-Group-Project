class student:
    def __init__(self, name, year_group, grades):
        self.name = name
        self.year_group = year_group  
        self.grades = grades


name_input = input("Enter the name of the student: ")
year_input = int(input("Enter the year group of the student (9-12): "))

grades_input = {}
subjects = ['Math', 'Science', 'English']