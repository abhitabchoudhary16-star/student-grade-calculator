def display_welcome():
    print("=" * 55)
    print("       📚 STUDENT GRADE CALCULATOR 📚")
    print("=" * 55)
    print("Calculate grades, GPA, and performance analysis.")
    print()

def get_student_name():
    name = input("Enter Student Name: ").strip()
    return name if name else "Student"

def get_subjects():
    subjects = []
    print()
    print("Enter subject names and marks (type 'done' when finished)")
    print("Marks should be between 0 and 100")
    print()

    while True:
        subject = input("Subject name (or 'done' to finish): ").strip()
        if subject.lower() == "done":
            if len(subjects) < 1:
                print("❌ Please enter at least 1 subject.")
                continue
            break
        if not subject:
            print("❌ Subject name cannot be empty.")
            continue

        while True:
            try:
                marks = float(input(f"Marks obtained in {subject} (0-100): "))
                if 0 <= marks <= 100:
                    subjects.append({"name": subject, "marks": marks})
                    print(f"✅ {subject}: {marks} marks added.")
                    print()
                    break
                else:
                    print("❌ Marks must be between 0 and 100.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

    return subjects

def get_grade(marks):
    if marks >= 90:
        return "A+", "Outstanding"
    elif marks >= 80:
        return "A", "Excellent"
    elif marks >= 70:
        return "B", "Good"
    elif marks >= 60:
        return "C", "Average"
    elif marks >= 50:
        return "D", "Below Average"
    else:
        return "F", "Fail"

def calculate_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.7
    elif average >= 70:
        return 3.3
    elif average >= 60:
        return 3.0
    elif average >= 50:
        return 2.0
    else:
        return 0.0

def display_results(student_name, subjects):
    total_marks = sum(s["marks"] for s in subjects)
    average = total_marks / len(subjects)
    grade, performance = get_grade(average)
    gpa = calculate_gpa(average)
    highest = max(subjects, key=lambda x: x["marks"])
    lowest = min(subjects, key=lambda x: x["marks"])

    print()
    print("=" * 55)
    print(f"         📊 RESULT CARD — {student_name.upper()}")
    print("=" * 55)
    print()

    print(f"{'Subject':<25} {'Marks':>8} {'Grade':>8} {'Status':>12}")
    print("-" * 55)

    for s in subjects:
        g, status = get_grade(s["marks"])
        print(f"{s['name']:<25} {s['marks']:>8.1f} {g:>8} {status:>12}")

    print("-" * 55)
    print()
    print(f"  📌 Total Marks     : {total_marks:.1f} / {len(subjects) * 100}")
    print(f"  📌 Average Marks   : {average:.2f}%")
    print(f"  📌 Overall Grade   : {grade}")
    print(f"  📌 GPA             : {gpa:.1f} / 4.0")
    print(f"  📌 Performance     : {performance}")
    print()
    print(f"  🏆 Best Subject    : {highest['name']} ({highest['marks']:.1f})")
    print(f"  📉 Needs Work      : {lowest['name']} ({lowest['marks']:.1f})")
    print()

    if grade == "F":
        print("  ⚠️  Result: FAIL — Keep working hard!")
    else:
        print("  ✅ Result: PASS — Great job!")

    print("=" * 55)

def main():
    display_welcome()
    student_name = get_student_name()
    subjects = get_subjects()
    display_results(student_name, subjects)

    print()
    again = input("🔄 Calculate for another student? (yes/no): ").strip().lower()
    if again in ["yes", "y"]:
        print()
        main()
    else:
        print()
        print("Thank you for using Student Grade Calculator! 👋")

if __name__ == "__main__":
    main()
