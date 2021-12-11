def vacuum_cleaner():
    cost = 0
    performance = 0
    remain = 2
    vacuum_pos = input("Enter Position of Vacuum Cleaner (A/B): ")
    a = input("Is room A dirty (T/F): ")
    b = input("Is room B dirty (T/F): ")
    
    if(a == 'F' and b == 'F'):
        print("Rooms are already Clean\nTotal Cost: ", cost)
        return
    while(remain > 0):
        if(vacuum_pos == 'A'):
            print("Currently Vacuum at location A")
            if(a == 'T'):
                print("Room A is being cleaned...")
                cost += 1 #cost for suck
                performance += 1
                a = 'F' #mark clean
            if(b == 'T'):
                print("Moving RIGHT to Room B...")
                vacuum_pos = 'B'
                cost += 1 #cost for moving RIGHT
                performance -= 1
        if(vacuum_pos == 'B'):
            print("Currently Vacuum at location B")
            if(b == 'T'):
                print("Room B is being cleaned...")
                cost += 1 #cost for suck
                performance += 1
                b = 'F'  #mark clean
            if(a == 'T'):
               print("Moving LEFT to Room A...")
               vacuum_pos = 'A'
               cost += 1 #cost for moving LEFT
               performance -= 1
        remain -= 1;
    print("Both rooms are cleaned\n cost: ",cost, "\n");
    #print("Both rooms are cleaned\n cost: ",cost, "performance measure: ",performance)

vacuum_cleaner()
