def is_armstrong_number(num):
    array = list(map(int, str(num)))
    arm = 0
    j = len(array)
    for i in range(len(array)):
        arm += array[i]**j
    if (arm != num):
        return False
    return True

