"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    return(neutrons_emitted >500 and temperature < 800 and (neutrons_emitted*temperature)< 500000)
        
    


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage = (generated_power/theoretical_max_power)*100
    if(percentage >= 80):
        return('green')
    elif(percentage<80 and percentage>=60):
        return('orange')
    elif(percentage<60 and percentage>=30):
        return('red')
    elif(percentage<30):
        return('black')
    else:
        return False

                      
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    safe = temperature * neutrons_produced_per_second
    if(safe < threshold*0.9):
        return('LOW')
    elif(safe<= threshold*1.1 and safe>threshold*0.9 or safe== threshold):
        return('NORMAL')
    else:
        return('DANGER')
