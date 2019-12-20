def main():
    filename = "input"
    inputint = 1
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
        parameter_opcode = str(code[i])

        if(len(parameter_opcode)>1):
            opcode = parameter_opcode[-2:]
            parameter_mode = parameter_opcode[0:-2]
            parameter_mode = parameter_mode[::-1]
            for j in range(3 - len(parameter_mode)):
                parameter_mode += '0'
        else:
            opcode = parameter_opcode
            parameter_mode = '000'
        #print("par_mode:", parameter_mode)
        #addition
        if(opcode == '01' or opcode == '1'):
            if(parameter_mode[0] == '1'):
                firstindex = i+1
            else:
                firstindex = int(code[i+1])
            if(parameter_mode[1] == '1'):
                secondindex = i+2
            else:
                secondindex = int(code[i+2])
            sumindex = int(code[i+3])
            code[sumindex] = int(code[firstindex])+int(code[secondindex])
            i += 4
        #multiplication
        elif(opcode == '02' or opcode == '2'):
            if (parameter_mode[0] == '1'):
                firstindex = i + 1
            else:
                firstindex = int(code[i + 1])
            if (parameter_mode[1] == '1'):
                secondindex = i + 2
            else:
                secondindex = int(code[i + 2])
            sumindex = int(code[i + 3])
            code[sumindex] = int(code[firstindex]) * int(code[secondindex])
            i += 4
        elif(opcode == '03' or opcode == '3'):
            adress = int(code[i + 1])
            code[adress] = str(inputint)
            i += 2
        elif(opcode == '04' or opcode == '4'):
            if (parameter_mode[0] == '1'):
                firstindex = i + 1
            else:
                firstindex = int(code[i + 1])
            print("Opcode 4 output: ", code[firstindex])
            i += 2
        #stop reading intcode
        elif(opcode == '99'):
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