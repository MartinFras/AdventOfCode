def main():
    #print(readfromfile("input"))
    data = readfromfile("input") #get 2 lines in 2d array
    result = findintersection(drawline(data[0]), drawline(data[1])) #data[0] = first line, data[1] = second line
    print("Distance to closest intersection: ", result)

def readfromfile(filename):
    file = open(filename, "r")
    firstline = file.readline().split(",") #firstline array
    secondline = file.readline().split(",") #second line array
    result = [firstline,secondline] #combine arrays into 2d array
    return result

def drawline(linedata):
    #starting position
    current_x = 0
    current_y = 0
    coordinates = {} #dictionary of all coordinates that the line crosses # template: { 'x,y':1 } #key has to be string type for this template

    #read 'linedata' and get direction and distance
    for i in range(0, len(linedata)):
        direction = linedata[i][0]
        distance = linedata[i][1:]

        #based on direction mark all coordinates that a line passes
        #RIGHT
        if(direction == "R"):
            for j in range(0, (int(distance))):
                coordinates.update({str(current_x+j+1)+","+str(current_y):1})#add coordinates to dictionary 'coordinates'
            current_x += int(distance)
        #LEFT
        if(direction == "L"):
            for j in range(0, (int(distance))):
                coordinates.update({str(current_x-j-1)+","+str(current_y):1})
            current_x -= int(distance)
        #UP
        if(direction == "U"):
            for j in range(0, int(distance)):
                coordinates.update({str(current_x)+","+str(current_y+j+1):1})
            current_y += int(distance)
        #DOWN
        if (direction == "D"):
            for j in range(0, int(distance)):
                coordinates.update({str(current_x)+","+str(current_y - j - 1):1})
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
            print("found a closer intersection", element)
    return closest

main()
