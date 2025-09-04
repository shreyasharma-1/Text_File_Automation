"""
You have a record of n students. Each record contains the student's name, and
their percent marks in Math, Physics and Chemistry. The marks can be floating
values. You are required to save the record in a dictionary data type.

Student's name is the key. Marks stored in a list is the value. The user enters a
student's name. Output the average percentage marks obtained by that
student.

Formula: (sum of marks) / (no of subjects)

Sample input: { "Krishna" : [67, 68, 69],

"Arjun" : [70, 98, 63],

"Malika" : [52, 56, 60] }

Sample output:

Enter a name: Malika

Average percentage mark: 56

Explanation:

Marks for Malika are [52, 56, 60] whose average is (52 + 56 + 60) / 3 => 56
"""

studentRecords = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

studentName = input("Enter a name: ")

if studentName in studentRecords:
    marksList = studentRecords[studentName]
    averagePercentage = sum(marksList) / len(marksList)
    print("Average percentage mark:", int(averagePercentage))
else:
    print("Student not found.")
