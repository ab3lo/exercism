def steps(number):
    steps = 0
    if ( number < 1):
        raise ValueError("Only positive integers are allowed")
    else:
        while(number != 1):
            steps+=1
            if (number %2 ==0):
                number = int(number//2)
            else:
                number = (3*number) +1
    return steps
        