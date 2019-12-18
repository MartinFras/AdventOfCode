def main():
    filename = "test"
    inputint = 3
    #print(readfromfile(filename))

    ######### PART ONE #########
    result = intcode(readfromfile(filename), inputint)
    #print("Answer PART ONE:",result[0])

    ######### PART TWO #########
    #result = searchcode(readfromfile(filename))
    #print(result)
    #print("Answer PART TWO:",(100*int(result[1])+int(result[2])))

######### PART ONE #########
def readfromfile(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    contentarray = content.split(",")
    return contentarray

def intcode(code, inputint):
    i = 0
    while(i < len(code)):
        #addition
        if(code[i] == '1'):
            firstindex = int(code[i+1])
            secondindex = int(code[i+2])
            sumindex = int(code[i+3])
            code[sumindex] = int(code[firstindex])+int(code[secondindex])
            i += 4
        #multiplication
        elif(code[i] == '2'):
            firstindex = int(code[i + 1])
            secondindex = int(code[i + 2])
            sumindex = int(code[i + 3])
            code[sumindex] = int(code[firstindex]) * int(code[secondindex])
            i += 4
        elif(code[i] == '3'):
            adress = int(code[i + 1])
            code[adress] = str(inputint)
            i += 2
        elif(code[i] == '4'):
            adress = int(code[i+1])
            print("Opcode 4 output: ", code[adress])
            i += 2
        #stop reading intcode
        elif(code[i] == '99'):
            print("Halting")
            return code

    return code

######### PART TWO #########
def searchcode(code):
    requiredoutput = 19690720
    currentoutput = 0
    for i in range(0,len(code)):
        for j in range(0, len(code)):
            tempcode = code.copy()
            tempcode[1] = i
            tempcode[2] = j
            result = intcode(tempcode)
            if(int(result[0]) == requiredoutput):
                return result
    return "erroryo"

main()