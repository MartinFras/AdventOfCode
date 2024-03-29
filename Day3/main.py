def main():
    #print(readfromfile("input"))
    data = readfromfile("input") #get 2 lines in 2d array
    result = findintersection(drawline(data[0]), drawline(data[1])) #data[0] = first line, data[1] = second line
    print("Distance to closest intersection: ", result)
    result_part_two = findintersection_timesensitive(drawline(data[0]), drawline(data[1]))
    print("Lowest walking distance to an interception:", result_part_two)

def readfromfile(filename):
    file = open(filename, "r")
    firstline = file.readline().split(",") #firstline array
    secondline = file.readline().split(",") #second line array
    result = [firstline,secondline] #combine arrays into 2d array
    return result

def drawline(linedata):
    print("drawing line")
    #starting position
    current_x = 0
    current_y = 0
    coordinates = {} #dictionary of all coordinates that the line crosses # template: { 'x,y':1 } #key has to be string type for this template
    steps = 0  # steps from start

    #read 'linedata' and get direction and distance
    for i in range(0, len(linedata)):
        direction = linedata[i][0]
        distance = linedata[i][1:]


        #based on direction mark all coordinates that a line passes
        #RIGHT
        if(direction == "R"):
            for j in range(0, (int(distance))):
                key = str(current_x + j + 1) + "," + str(current_y)
                #print("key",key)
                if (key in coordinates.keys()):
                    coordinates.update({str(current_x+j+1)+","+str(current_y):coordinates[key]})#add coordinates to dictionary 'coordinates'
                else:
                    coordinates.update({str(current_x + j + 1) + "," + str(current_y): steps + 1})
                steps += 1
                print(steps, key)
            current_x += int(distance)

        #LEFT
        if(direction == "L"):
            for j in range(0, (int(distance))):
                key = str(current_x-j-1)+","+str(current_y)
                #print("key", key)
                if (key in coordinates.keys()):
                    coordinates.update({str(current_x-j-1)+","+str(current_y):coordinates[key]})
                else:
                    coordinates.update({str(current_x - j - 1) + "," + str(current_y): steps + 1})
                steps += 1
                print(steps, key)
            current_x -= int(distance)

        #UP
        if(direction == "U"):
            for j in range(0, int(distance)):
                key = str(current_x)+","+str(current_y+j+1)
                #print("key", key)
                if (key in coordinates.keys()):
                    coordinates.update({str(current_x)+","+str(current_y+j+1):coordinates[key]})
                else:
                    coordinates.update({str(current_x) + "," + str(current_y + j + 1): steps + 1})
                steps += 1
                print(steps, key)
            current_y += int(distance)

        #DOWN
        if (direction == "D"):
            for j in range(0, int(distance)):
                key = str(current_x)+","+str(current_y - j - 1)
                #print("key", key)
                if (key in coordinates.keys()):
                    coordinates.update({str(current_x)+","+str(current_y - j - 1):coordinates[key]})
                else:
                    coordinates.update({str(current_x) + "," + str(current_y - j - 1): steps + 1})
                steps += 1
                print(steps, key)
            current_y -= int(distance)

    return(coordinates)

def findintersection(first, second):
    closest = 99999 #default distance setup
    closest_coordinates = str()
    coordinates = list()

    for element in second: #
        #read both coordinates from dictionary key and calculate Manhattan distance
        current_coordinates = element.split(",")
        current_distance = abs(int(current_coordinates[0]))+abs(int(current_coordinates[1]))
        if(current_distance < closest and element in first.keys()): #if current distance is closer than closest and first line goes over coordinate (key) then intersection is closest
            closest = current_distance
            closest_coordinates = element
            #print("found a closer intersection", element)
    return closest

######### PART TWO #########
def findintersection_timesensitive(first, second):
    closest_path_distance = 99999  # default distance setup
    closest_coordinates = str()
    coordinates = list()

    for element in second:
        if (element in first.keys()):  # if current distance is closer than closest and first line goes over coordinate (key) then intersection is closestž
            current_path_distance = first[element] + second[element]
            if(current_path_distance < closest_path_distance):
                closest_path_distance = current_path_distance
                closest_coordinates = element
                #print("found a intersection with closer path", closest_coordinates)
    return closest_path_distance
main()
