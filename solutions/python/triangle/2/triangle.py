def real_tri(sides):
    if( (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0]) ):
        return(True)
    else:
        return(False)




def equilateral(sides):
    if ( sides[0]==sides[1] and sides[1] == sides[2] and any(side !=0 for side in sides)):
        return(True)
    else:
        return(False)


def isosceles(sides):
    if ( (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]) and (real_tri(sides) != False) ):
        return(True)
    else:
        return(False)


def scalene(sides):
    if (isosceles(sides) == False and equilateral(sides)==False) and real_tri(sides) == True:
        return(True)
    else:
        return(False)