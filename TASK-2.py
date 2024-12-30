def calculate_letter_grade(average):
    """Return the letter grade based on the average score."""
    if average >= 90:
        return 'O'
    elif average >= 80:
        return 'A+'
    elif average >= 70:
        return 'A'
    elif average >= 60:
        return 'B+'
    elif average >= 50:
        return 'B'
    elif average >= 40:
        return 'C'
    else:
        return 'F'

def calculate_gpa(average):
    if average >= 95:
        return 10.0
    elif average >= 90:
        return 9.0
    elif average >= 80:
        return 8.0
    elif average >= 70:
        return 7.0
    elif average >= 60:
        return 6.0
    elif average >= 50:
        return 5.0
    elif average >= 40:
        return 4.0
    elif average >= 60:
        return 3.0
    elif average >= 60:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

def get_grade_input():
    grades = []
    while True:
        grade_input = input("Enter grade (or type 'done' to finish): ")
        if grade_input.lower() == 'done':
            break
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    return grades

def main():
    print("Student Grade Tracker!")
    
    grades = get_grade_input()
    
    if grades:
        # Calculate average grade
        average = sum(grades) / len(grades)
        
        # Calculate letter grade and GPA
        letter_grade = calculate_letter_grade(average)
        gpa = calculate_gpa(average)
        
        # Display the results
        print("\nResults:")
        print(f"Grades entered: {grades}")
        print(f"Average grade: {average:.2f}")
        print(f"Letter grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")
    else:
        print("No grades entered. Exiting the program.")

if __name__ == "__main__":
    main()
