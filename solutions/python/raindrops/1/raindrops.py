def convert(n):
    sound = ""
    while(True): 
        if n % 3 == 0:
            sound+="Pling"
        if n % 5 == 0:
            sound+="Plang"
        if n % 7 == 0:
            sound+="Plong"
        break
    if sound=="":
        return str(n)
    return sound