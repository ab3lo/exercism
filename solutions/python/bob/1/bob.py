def response(msg):
    msg = msg.strip()
    if(msg == "" ):
        return("Fine. Be that way!")
    last=msg[-1]
    if(last=='?'and are_yelling(msg)==False):
        return("Sure.")
    elif(are_yelling(msg)==True and last!="?"):
        return("Whoa, chill out!")
    elif( (last=='?') and (are_yelling(msg)==True) ):
        return("Calm down, I know what I'm doing!")
    else:
        return("Whatever.")


def are_yelling(string):
    return string.isupper()

