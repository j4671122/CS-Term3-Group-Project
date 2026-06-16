# CS-Term3-Group-Project
Computer Science Take Home Assignment (Term 3)
The following is a group assignment for Teams of 2. You may work alone, but this will not change rubric or how the assignment is graded. The assignment is due by end of day 19/6/2026. This is the project for term 3 and worth 30% of your final grade for the term (3). You are responsible writing your code, documenting your design process, and understanding every line of code that is submitted. You are strictly not permitted to use AI tools for generating code. To verify this, there will be an oral exam component that will be completed in person, on campus and individually. In this oral you may be asked details about project 1 or project 2 so be prepared.
Deliverables:
•	Code submitted as a .py file to moodle with you and your partner’s names(first initial and last name, for example JJonker), a file should be formatted for example: JJonker_SJonker_CS_Project2_code.py
o	Make sure to comment code with what it does do NOT comment every line but leave comments for what an object or class is designed to do, what a function or method is designed to do, and if there are any algorithms or problem solving methods highlight what code is supposed to do
o	Include the names of all who contributed as a comment on line 1
o	DO NOT COMMENT EVERY LINE
•	Each student is expected to submit a brief write up (500 words) describing what your code does and what choices your team made, make sure to specify what portion of the assignment you personally contributed to. Include pictures of your code working (show test cases)
o	Make sure to upload your write up to Moodle as a docx with first initial last name present for example JJonker_CS_Project2_writeup.docx
•	You are responsible for finding your groupmate
 
Rubric:
•	Functionality (30%): Code presented solves the assigned task, choices made are clear and make sense (10% for solving the task completely). Deductions occur if there are semantic errors or specific cases that cause errors or the wrong results to display (up to 20% deductions). Grading is done case by case. If the code returns an error when run in python, then you will not receive credit for these criteria, for clarity if the code does not run due to syntax or other fundamental errors. 
•	Readability and Design (20%): Code should be easy to follow. Generic or vague names for objects, methods, functions, data structures, variables, etc are not acceptable. Names should be unique and describe purpose or function. I do not want to see x= or FunctionName(arg) or classname for example. Classes, methods, functions, and logic should be used when appropriate and within reason. Code should also be commented to explain what objects, methods, and functions do. Full credit would have code that is well organized with functions and methods being implemented to use code that would otherwise be repeated. Logic, when used, should be comprehensive but not redundant. Comments are present with purpose. 
•	Documentation (20%): This will be assessed in combination with the writeup and any comments provided. If there are no comments expect a 10% deduction. The write up should briefly describe how you solved the problem and your personal contributions.
•	Testing and Debugging (10%): Include examples of your code running in the write up document. Include at least 3 test cases and include screenshots. If something does not work talk about it in the write up document.
•	Oral component (20%): You will be interviewed individually regarding your contributions and understanding. This component is worth up to 20 points. Failing to make an appointment however will result in a 0 for the entire assignment for a given individual.  

A school wants to manage student information using both classes and dictionaries. You have been provided with each student’s grades for math, science, and English for terms 1, 2, and 3. You are tasked with writing code that presents the grades of each student in alphabetical order as well as some important statistics. The following are the rules and requirements in detail. You must demonstrate your code works for 4 or more students.

Each student has:
•	A name
•	A year group
•	A dictionary of subjects and scores 

For this project you can assume:
•	Each student has a unique name
•	The year group is a number 9, 10, 11 or 12.
•	The subjects are Math, English and Science.  The scores are a number between 0 and 100
o	Grades are given to you based on each term
Program Requirements
Main program:
•	Create an instance of class “Student” for each unique student. Each instance of the class should contain all identifying information: (name, year group, dictionary of grades). This class also contains the raw scores for each subject as a dictionary with the keys being the name of each subject and the values being a list of each term’s final grades for example {‘Math’:[55, 60, 77], ‘Science’:[70, 25, 90], ‘English’:[59, 70, 82]}
o	The class should have methods that can do the following
	Return the average score for a specific subject [Student.subjectavg(subjectname)]
	Return the average score for the year for the specific student [Student.yearavg()]
	Checks if a student failed one or more classes, a student fails if they score below a 55 [Student.failcheck()] and communicate if they did by printing a message
	Write the average grades into a dictionary [Student.writegrades(dictionaryname)] *dictionaryname is a placeholder
•	Create a dictionary that contains all the students end of year information, the keys should be the student name
o	The value should be average grades for each class and end of year average
•	Print all student information in alphabetical order, your program should display:
 
for each student and in alphabetical order
•	Print a message for which student had the highest average for the year, you must account for if two or more students have the same highest average
•	Print a message for which class is the hardest based off which class had the lowest average score across all 3 terms. You must account for if two or more classes have the same lowest average score.

Your program must:
1.	Display all student information in alphabetical order. (Name, group number, average scores for each class). 
2.	A student fails if the average for any specific course has lower than a 55, have the program print if a specific student failed 1 or more subjects.
3.	Find and display the student(s) with the highest overall average. Your code must account for if two students share the same highest score.
4.	Determine and display the subject(s) that are the most difficult. The more difficult the subject the lower the average score. Your code must account for if two or more subjects share the same lowest average.
Your code must make use of classes, methods, and dictionaries, or you will get a 0.



<img width="523" height="755" alt="image" src="https://github.com/user-attachments/assets/d87fac27-86c6-4745-9e73-3e7031489c17" />
