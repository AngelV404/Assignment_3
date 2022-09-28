def sum(*,list):
    total = 0
    for x in list:
        total = total + x
    return total

def average(*,list):
    total = 0
    for x in list:
        total = total + x
    mean = total / len(list)
    return mean