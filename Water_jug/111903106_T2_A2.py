import array as arr
   
def solve_waterjug(j1, j2, z,flag):
    count = j1 + j2 #for total no. of iterations
    jug1 = arr.array('i',[0])
    jug2 = arr.array('i',[0])
    message = ["initially both jugs are empty"]
    i = 1

    if(z == 0):
        return jug1, jug2, i
    
    jug1.append(j1)
    jug2.append(0)
    if(flag == 1):
        message.append("fill jug2 till its full")
    else:
        message.append("fill jug1 till its full")
    i += 1
    while(i <= 2*count):
        if(jug1[i-1] == z):
            if(jug2[i-1] == 0):
                break
            jug1.append(z)
            jug2.append(0)
            if(flag == 1):
                message.append("empty jug1")
            else:
                message.append("empty jug2")
            i += 1
            break
        
        elif(jug2[i-1] == z):
            if(jug1[i-1] == 0):
                break
            jug1.append(0)
            jug2.append(z)
            if(flag == 1):
                message.append("empty jug2")
            else:
                message.append("empty jug1")
            i += 1
            break
        
        elif(jug1[i-1] == 0): #i.e. jug1 is empty
            jug1.append(j1)
            jug2.append(jug2[i-1])   #- jug1[i-1]
            if(flag == 1):
                message.append("Completely fill jug2")
            else:
                message.append("Completely fill jug1")
            
            
        elif(jug1[i-1] == j1):
            if(jug1[i-1] > j2):   
                jug2.append(j2)
                jug1.append(j1 - (j2 - jug2[i-1]))
                if(flag == 1):
                    message.append("Transfer from jug2 to jug1 so that jug1 is full")
                else:
                    message.append("Transfer from jug1 to jug2 so that jug2 is full")
            else:
                jug2.append(jug1[i-1])
                jug1.append(0)
                if(flag == 1):
                    message.append("Transfer water from jug2 to jug1 till it is full, now jug2 has 0litres of water")
                else:
                    message.append("Transfer water from jug1 to jug2 till it is full, now jug1 has 0litres of water")
                
            
        elif(jug2[i-1] == 0): #i.e. jug2 is empty
            if(jug1[i-1] > j2):   
                jug2.append(j2)
                jug1.append(jug1[i-1]- jug2[i])
                if(flag == 1):
                    message.append("Transfer water from jug2 to jug1 till it is full")
                else:
                    message.append("Transfer water from jug1 to jug2 till it is full")
            else:
                jug2.append(jug1[i-1])
                jug1.append(0)
                if(flag ==1):
                    message.append("Completely Transfer water from jug2 to jug1")
                else:
                    message.append("Completely Transfer water from jug1 to jug2")

        elif(jug2[i-1] == j2):
            jug2.append(0)
            jug1.append(jug1[i-1])
            if(flag == 1):
                message.append("Empty Jug1")
            else:
                message.append("Empty Jug2")
        i += 1

    if(jug1[i-1] != z and jug2[i-1] != z):
        return 0,0,0, message
    return jug1, jug2, i, message


while(1):
    print("\nType -1 to exit")
    j1 = int(input("\nEnter capacity of Jug 1: "))
    if(j1 == -1):
        break
    j2 = int(input("Enter capacity of Jug 2: "))
    z = int(input("Enter expected Volume: "))
    flag = 0

    if(j1 > j2):
        jug1, jug2, i, message = solve_waterjug(j1, j2, z, flag)
    else:
        flag = 1
        jug2, jug1, i, message = solve_waterjug(j2, j1, z, flag)

    if(i == 0):
        print("No solution possible");
    for j in range(0,i):
        print("jug1: ", jug1[j], "and jug2: ", jug2[j], "(",message[j], ")")

    print("Total Cost: ", i-1);
        

