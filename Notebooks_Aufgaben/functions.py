def create_step_vector(start, end, stepwidth = 1):
    step_vector = [start]
    number_of_digits_after_decimal_point = len(str(stepwidth-int(stepwidth))[2:])
    i = start
    while i < end:
        i = round(i + stepwidth,  number_of_digits_after_decimal_point)
        step_vector.append(i)
    return step_vector 