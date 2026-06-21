import math


GRADE_CUTOFFS = [
    ("A*", 0.10),
    ("A",  0.25),
    ("B",  0.45),
    ("C",  0.65),
    ("D",  0.80),
    ("E",  0.90),
    ("U",  1.00),
]


def calculate_boundaries(marks):
    sorted_marks = sorted(marks, reverse=True)
    n = len(marks)
    boundaries = {}
    for grade, cumulative_pct in GRADE_CUTOFFS:
        idx = min(math.ceil(cumulative_pct * n), n) - 1
        boundaries[grade] = sorted_marks[idx]
    return boundaries


def assign_grade(mark, boundaries):
    for grade, _ in GRADE_CUTOFFS:
        if mark >= boundaries[grade]:
            return grade
    return "U"


def get_marks_from_input():
    print("Enter student marks out of 250.")
    print("You can enter them one per line, or comma-separated. Type 'done' when finished.\n")
    marks = []
    while True:
        raw = input("> ").strip()
        if raw.lower() == "done":
            break
        entries = raw.replace(",", " ").split()
        for entry in entries:
            try:
                mark = float(entry)
                if not (0 <= mark <= 250):
                    print(f"  Skipped {entry}: must be between 0 and 250.")
                else:
                    marks.append(mark)
            except ValueError:
                if entry.lower() != "done":
                    print(f"  Skipped '{entry}': not a valid number.")
    return marks


def main():
    marks = get_marks_from_input()

    if len(marks) < 2:
        print("Need at least 2 marks to calculate boundaries.")
        return

    boundaries = calculate_boundaries(marks)

    print("\n" + "=" * 40)
    print(f"  COHORT: {len(marks)} students")
    print(f"  Highest: {max(marks):.1f}   Lowest: {min(marks):.1f}")
    avg = sum(marks) / len(marks)
    print(f"  Average: {avg:.1f}")
    print("=" * 40)

    print("\nGRADE BOUNDARIES (minimum mark to achieve grade):\n")
    grade_names = [g for g, _ in GRADE_CUTOFFS]
    for grade in grade_names[:-1]:
        print(f"  {grade:<4}  {boundaries[grade]:.1f}")
    print(f"  U     below {boundaries['E']:.1f}")

    print("\nSTUDENT RESULTS:\n")
    student_grades = [(mark, assign_grade(mark, boundaries)) for mark in marks]
    student_grades.sort(key=lambda x: x[0], reverse=True)
    for i, (mark, grade) in enumerate(student_grades, 1):
        print(f"  {i:>3}. {mark:>6.1f} / 250   ->  {grade}")

    print("\nGRADE DISTRIBUTION:\n")
    from collections import Counter
    counts = Counter(g for _, g in student_grades)
    for grade, _ in GRADE_CUTOFFS:
        count = counts.get(grade, 0)
        pct = count / len(marks) * 100
        bar = "#" * count
        print(f"  {grade:<4} {count:>3} students ({pct:4.1f}%)  {bar}")


if __name__ == "__main__":
    main()
