def main():
    start = 136818
    finish = 685979
    #start = 100000
    #finish = 200000
    counter = 0
    possible_passwords = list()
    for i in range(start, finish+1):
        password = comparison(i)
        if(checkpassword(password)):
            counter += 1
            possible_passwords.append(password)
            #print(password)
    print("Solution part 1: ",counter)

    counter = 0
    for i in range(0,len(possible_passwords)):
        password = possible_passwords[i]
        if (checkpassword_parttwo(password)):
            counter += 1
            # print(password)
    print("Solution part 2: ", counter)

def comparison(password):
    password_string = str(password)
    password_numbers = list()
    for i in range(0,len(password_string)):
        password_numbers.append(password_string[i])
    #print(password_numbers)
    return password_numbers

def checkpassword(password):
    if(password[5] >= password[4]):
        if(password[4] >= password[3]):
            if (password[3] >= password[2]):
                if (password[2] >= password[1]):
                    if (password[1] >= password[0]):
                        if(password[0] == password[1] or password[1] == password[2] or password[2] == password[3] or password[3] == password[4] or password[4] == password[5]):
                            return 1
                        return 0
                    return 0
                return 0
            return 0
        return 0
    return 0

######### PART 2 #########
def checkpassword_parttwo(password):
    for i in range(0, len(password)):
        counter = 0
        for j in range(0, len(password)):
            if(password[i] == password[j]):
                counter += 1
        if(counter == 2):
            return 1
    return 0
main()