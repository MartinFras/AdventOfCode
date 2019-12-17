def main():
    inputfilename = "input"
    dataarray = readfromtxtfile(inputfilename)
    ######### PART ONE #########
    result = calculate(dataarray)
    print("Answer PART ONE:",result)
    ######### PART TWO #########
    totalfuel = calculatetotalfuel(dataarray)
    print("Answer PART TWO:",totalfuel)

######### PART ONE #########
def readfromtxtfile(inputfilename):
    numberlist = []
    counter = 0
    file = open(inputfilename, "r")
    for line in file:
        numberlist.append(line)
    file.close()
    return numberlist


def calculate(data):
    result = 0
    for i in range(0,len(data)):
        temp = int(int(data[i])/3)-2
        result += temp
    if(result < 0):
        return 0
    return result

######### PART TWO #########
def calculatetotalfuel(data):
    result = 0
    for i in range(0,len(data)):
        temp = int(int(data[i])/3)-2
        result += temp #fuel for mass
        while (int(temp / 3) - 2 > 0):
            temp = int(temp / 3) - 2
            result += temp #add fuel for fuel mass
    return result
main()