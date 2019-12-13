def main():
    start = 136818
    finish = 685979
    #start = 100000
    #finish = 200000
    counter = 0
    for i in range(start, finish+1):
        password = comparison(i)
        if(checkpassword(password)):
            counter += 1
            #print(password)
    print("Solution part 1: ",counter)

def comparison(password):
    password_string = str(password)
    password_numbers = list()
    for i in range(0,len(password_string)):
        password_numbers.append(password_string[i])
    #print(password_numbers)
    return password_numbers

def checkpassword(password):
    if(password[0] <= password[1]):
        if(password[1] <= password[2]):
            if (password[2] <= password[3]):
                if (password[3] <= password[4]):
                    if (password[4] <= password[5]):
                        if(password[0] == password[1] or password[1] == password[2] or password[2] == password[3] or password[3] == password[4] or password[4] == password[5]):
                            return 1
                        return 0
                    return 0
                return 0
            return 0
        return 0
    return 0


main()