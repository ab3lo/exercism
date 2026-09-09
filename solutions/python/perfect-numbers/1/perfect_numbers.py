def classify(num):
    if num <=0:
        raise ValueError("Classification is only possible for positive integers.")
    agg=0
    for i in range(1, num):
        if num%i==0:
            agg += i
    if agg< num:
        return "deficient"
    elif agg == num:
        return "perfect"
    else:
        return "abundant"
