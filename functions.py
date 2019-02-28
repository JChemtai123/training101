# a function is a block of code that is used to perform a related action
# creating/ defining a function
# def chapisha(sth):
#     print(sth)
# # calling/using a function
# chapisha("Actely")
#
# chapisha("Kiki")
def totalmarks (math,eng, kis, sci,ssr):
    totalmarks = math+eng+kis+sci+ssr
    return totalmarks

def average (total):
    avg = total/5
    return avg

def findgrade (average ):
    if average >= 80 and average < 100:
        return "A"
    elif average>= 70 and average < 80:
        return "B"
    elif average >= 60 and average < 70:
        return "C"
    elif average >= 50 and average < 60:
        return "D"
    else:
        return "E"
