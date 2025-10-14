** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    # 1) Guard: at most 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes_line = []
    results_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must have two operands and an operator."

        left, operator, right = parts

        # 2) Operator must be + or -
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # 3) Digits only
        if not (left.isdigit() and right.isdigit()):
            return "Error: Numbers must only contain digits."

        # 4) Max 4 digits each
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # 5) Width for alignment
        width = max(len(left), len(right)) + 2

        # 6) Build lines
        first_line.append(left.rjust(width))
        second_line.append(operator + right.rjust(width - 1))
        dashes_line.append("-" * width)

        if show_answers:
            if operator == "+":
                val = int(left) + int(right)
            else:
                val = int(left) - int(right)
            results_line.append(str(val).rjust(width))

    arranged = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes_line)
    )

    if show_answers:
        arranged += "\n" + "    ".join(results_line)

    return arranged


** end of main.py **

