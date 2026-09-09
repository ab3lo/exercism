def convert(n):
    sound = ""
    if n % 3 == 0:
        sound+="Pling"
    if n % 5 == 0:
        sound+="Plang"
    if n % 7 == 0:
        sound+="Plong"
        
    return str(n) if sound=="" else sound