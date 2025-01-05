def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""
    for problem in problems:
        top, operator, bottom = problem.split()
        if operator not in ['+' , '-']:
            return "Error: Operator must be '+' or '-'."
        if not top.isdigit() or not bottom.isdigit():
            return "Error: Numbers must only contain digits."
        if len(top) > 4 or len(bottom) > 4:
            return "Error: Numbers cannot be more than four digits."
        width = max(len(top), len(bottom)) + 2 
        if len(line_1) > 0:
            line_1 += 4 * " "
            line_2 += 4 * " "
            line_3 += 4 * " "
        line_1 += top.rjust(width, " ")
        line_2 += operator + (width - 1 - len(bottom)) * " " + bottom
        line_3 += width * "-"
        if answers is True:
            if len(line_4) > 0:
                line_4 = line_4 + 4 * " "
            if operator == "+":
                x = int(top) + int(bottom)
                line_4 = line_4 + str(x).rjust(width, " ")
            else:
                x = int(top) - int(bottom)
                line_4 = line_4 + str(x).rjust(width, " ")
    result = line_1 + '\n' + line_2 + '\n' + line_3
    if len(line_4) > 0: result = result + '\n' + line_4
    return result