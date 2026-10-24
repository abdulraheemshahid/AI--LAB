"""Rule-based example: all numeric thresholds are synthetic lab assumptions."""


def check_application(score, documents_complete, attendance, age):
    if score < 70:
        return "FAIL", "Score is below the synthetic lab threshold of 70."
    if not documents_complete:
        return "FAIL", "Documents are incomplete."
    if attendance < 75:  # Named condition 1: minimum attendance.
        return "FAIL", "Attendance is below the synthetic lab threshold of 75%."
    if age < 18:  # Named condition 2: minimum age.
        return "FAIL", "Age is below the synthetic lab threshold of 18."
    return "PASS", "All conditions are satisfied."


def run_case(number, description, inputs, expected):
    actual, reason = check_application(**inputs)
    print(f"Test Case {number}: {description}")
    print("Input:", inputs)
    print("Expected Result:", expected)
    print("Actual Result:", actual)
    print("Reason:", reason)
    print()


cases = [
    ("All requirements met", {"score": 85, "documents_complete": True, "attendance": 80, "age": 20}, "PASS"),
    ("Failure of named condition 1: minimum attendance", {"score": 85, "documents_complete": True, "attendance": 74, "age": 20}, "FAIL"),
    ("Failure of named condition 2: minimum age", {"score": 85, "documents_complete": True, "attendance": 80, "age": 17}, "FAIL"),
    ("Threshold boundary: score exactly 70", {"score": 70, "documents_complete": True, "attendance": 75, "age": 18}, "PASS"),
]

for number, (description, inputs, expected) in enumerate(cases, start=1):
    run_case(number, description, inputs, expected)

print(
    "Case selection: the first case is a valid pass; cases 2 and 3 each fail "
    "one new named condition while meeting the others; case 4 uses score 70 "
    "exactly to verify that the retained score cutoff is inclusive."
)
