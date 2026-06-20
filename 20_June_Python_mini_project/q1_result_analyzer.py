# Aditya Kumar (20 June)

def analyze_result(name, roll, marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total:.1f}, Average: {average:.1f}")
    print(f"Grade: {grade}")

    below_40 = []

    for i in range(len(marks)):
        if marks[i] < 40:
            below_40.append(f"Subject {i + 1}")

    if len(below_40) > 0:
        print("Subjects below 40:", ", ".join(below_40))
    else:
        print("Subjects below 40: None")

# Input
name = "Aarav"
roll = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

analyze_result(name, roll, marks)
