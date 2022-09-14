def readText(): # this function is to count how many user exist, read data from txt file and store into list
    with open('user.txt') as f:
        lines = f.readlines() # every line in txt file will store in list lines
    
    count = 0
    for line in lines:
        count += 1 # to count how many user exist in this program
        
    numMem = int(count/24) # every user has 24 data

    user = [] # every 24 user's data will store in one list, 1 user has 1 list 
    user_list = [] # every list of user will store in this list

    with open('user.txt','r') as fa:

        for i in range(numMem):            
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))
            user.append(fa.readline().rstrip('\n'))

            user_list.append(user)
            user = [] # to empty the user list before append another user

    return user_list

def readPPV(): # this function is to count how many PPV exist, read data from txt file and store into list
    lines = []
    with open('ppv.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        count += 1 # to count how many PPV exist in this program
    
    numPPV = int(count/6) # every PPV has 6 data

    PPV = [] # every 6 PPV's data will store in one list, 1 PPV has 1 list 
    PPV_list = [] # every list of PPV will store in this list

    with open('ppv.txt','r') as fb:
        for i in range(numPPV):
            PPV.append(fb.readline().rstrip('\n'))
            PPV.append(fb.readline().rstrip('\n'))
            PPV.append(fb.readline().rstrip('\n'))
            PPV.append(fb.readline().rstrip('\n'))
            PPV.append(fb.readline().rstrip('\n'))
            PPV.append(fb.readline().rstrip('\n'))

            PPV_list.append(PPV)
            PPV = []

    return PPV_list

def writeText(user_list): # this function is to write the data in the list into txt file
    fh = open('user.txt','w')
    for i in user_list:  # user_list is a big list containing every user's list, so i is user's list
        for j in i: # j is every each data of user
            fh.write(j) # write every each data of user into txt file
            fh.write('\n')
            
    fh.close()

def writeText2(PPV_list): # this function is to write the data in the list into txt file
    fp = open('ppv.txt','w')
    for i in PPV_list: # PPV_list is a big list containing every PPV's list, so i is PPV's list
        for j in i: # j is every each data of PPV
            fp.write(j) # write every each data of PPV into txt file
            fp.write('\n')

    fp.close()

isQuit = True
while(isQuit):
    print("\n------G16 COVID-19 PROGRAM------")
    print("Welcome user! Please select a method to log in.")
    print("1.Sign up")
    print("2.User Login")
    print("3.Admin Login")
    print("4.Exit")

    method = input("Enter the number according to its function: ")
    while (chr(49) != method and chr(50) != method and chr(51) != method and chr(52) != method): # use chr because the program would not error when user input space
        method = input("Please enter an valid number: ")

    if chr(49) == method: # chr(49) == '1', thats mean when user input 1, the below statement will be executed
        print("\n(Press space and enter to sign up later)")
        print("--Sign up--")
        idDuplicate = False
        user_list = readText()
        name = input("name: ")

        if name == ' ':
            continue # back to main menu when user input space and enter
        
        age = input("age: ")
        id = input("ID: ")

        for i in user_list:
            if i[2] == id:
                print("This ID has already sign up.\nPress enter and try again.")
                input()
                idDuplicate = True
                break

        if(not idDuplicate):
            phone = input("phone: ")
            email = input("email: ")
            address = input("address: ")
            postcode = (input("postcode: "))
            state = input('state: ')
        
            PassIsNotSame = True

            while(PassIsNotSame):
                password = input("password: ")
                password2 = input("confirm password: ")

                if password == password2: # only when the password and confirm password input by user is same, the account will be successfully created
                    print("Account is successfull create,Login now with your ID and password")
                    print("Press enter to continue")
                    input()
                    PassIsNotSame = False

                    fh = open('user.txt','a') # append the data user input during sign up and 15 '-' as a empty space for user to store user's other data in advance such as appointment data and time into txt file
                    fh.write(name)
                    fh.write('\n')
                    fh.write(age)
                    fh.write('\n')
                    fh.write(id)
                    fh.write('\n')
                    fh.write(phone)
                    fh.write('\n')
                    fh.write(email)
                    fh.write('\n')
                    fh.write(address)
                    fh.write('\n')
                    fh.write(postcode)
                    fh.write('\n')
                    fh.write(state)
                    fh.write('\n')
                    fh.write(password)
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.write('-')
                    fh.write('\n')
                    fh.close()

                else:
                    print("Your password and confirm password are not same,please enter again.")

        

    elif chr(50) == method: # User Login

        user_list = readText() # calling function readText()
        PPV_list = readPPV() # calling funtion readPPV()

        validID = False # assume that the combination of input id and input password from user is wrong initially

        print("\n--User Login--")
        inputid = input("ID: ")
        inputpass = input("password: ")

        for i in user_list: #user_list is store list in list, eg [['lck','40','0725'],['kyy','19','1226']]
            if i[2] == inputid and i[8] == inputpass: #i already broke out from list in list, eg ['lck','40','0725'] in the next line ['kyy','19',1226']
                validID = True # when the combination is correct, for loop will be terminated
                idseq = i
                print("Combination of ID and password correct.")

        if(validID == False):
            print("Combination of ID and password incorrect.\nPress enter and try again.")
            input()

        else:

            doneop = True
            while(doneop):

                print(f"\nWelcome {idseq[0]}")
                print("1.Profile")
                print("2.Update status")
                print("3.Update medical history & occupation")
                print("4.Check appointment")
                print("5.Logout")
                user_function = input("Enter the number according to its function: ")
                while (chr(49) != user_function and chr(50) != user_function and chr(51) != user_function and chr(52) != user_function and chr(53) != user_function):
                    user_function = input("Please enter an valid number: ")

                if chr(49) == user_function: # Profile
                    print("\n",idseq[0],"'s Profile")
                    print("------Personal Details------")
                    print("name:",idseq[0])
                    print("age:",idseq[1])
                    print("id:",idseq[2])
                    print("phone:",idseq[3])
                    print("email:",idseq[4])
                    print("address:",idseq[5])
                    print("postcode:",idseq[6])
                    print("state:",idseq[7])
                    print("password:",idseq[8])

                    print("\n------Personal Status------")
                    if idseq[9] == '-':
                        print("Please update your status first.(Selection 2 in menu)")

                    else:
                        print("Are you exhibiting 2 or more symptoms as listed below?:", idseq[9])
                        print("Beside the above,are you exhibiting any of the symptoms listed below?:", idseq[10])
                        print("Have you attend any event/ areas associated with known COVID-19 cluster?:", idseq[11])
                        print("Have you travelled to any country outside Malaysia within 14 days before onset of symptoms?:", idseq[12])
                        print("Have you had close contact to confirmed or suspected case of COVID-19 witin 14 days before onset of illness?:", idseq[13])
                        print("Are you under quarantine now?:", idseq[14])

                    print("\n------Medical history------")
                    if idseq[15] == '-':
                        print("Please update your medical history first.(Selection 3 in menu)")
                    else:
                        print("Chronic disease:",idseq[15])

                    print("\n------Occupation------")
                    if idseq[16] == '-':
                        print("Please update your occupation first.(Selection 3 in menu)")
                    else:
                        print("Occupation:",idseq[16])

                    print("\n------Risk------")
                    if idseq[17] == '-':
                        print("Please update your medical history & ocuupation first.(Selection 3 in menu)")
                    else:
                        print("Risk:",idseq[17])

                    print("\n------Appointment Status------")
                    if idseq[18] == '-':
                        print("Please update your medical history & occupation first.(Selection 3 in menu)")
                    else:
                        print("Appointment:",idseq[18])

                elif chr(50) == user_function: # Update status
                    print("Please answer the question below by typing Yes or No.\nPress enter to continue.")
                    input()
                    print("Are you exhibiting 2 or more symptoms as listed below?")
                    print("-Fever\n-Chills\n-Shivering\n-Body ache\n-Headache\n-Sore throat\n-Nausea or vomiting\n-Diarrhea\n-Fatigue\n-Runny nose or nasal congestion")
                    symptoms = input("Type Yes or No: ")
                    symptoms = symptoms.lower()
                    while(symptoms != 'no' and symptoms != 'yes'):
                        symptoms = input("Please only type Yes or No: ")
                        symptoms = symptoms.lower()

                    print("\nBeside the above,are you exhibiting any of the symptoms listed below?")
                    print("-Cough\n-Difficulty breathing\n-Loss of smell\n-Loss of taste")
                    symptoms2 = input("Type Yes or No: ")
                    symptoms2 = symptoms2.lower()
                    while(symptoms2 != 'no' and symptoms2 != 'yes'):
                        symptoms2 = input("Please only type Yes or No: ")
                        symptoms2 = symptoms2.lower()

                    print("\nHave you attend any event/ areas associated with known COVID-19 cluster?")
                    area = input("Type Yes or No: ")
                    area = area.lower()
                    while(area != 'no' and area != 'yes'):
                        area = input("Please only type Yes or No: ")
                        area = area.lower()

                    print("\nHave you travelled to any country outside Malaysia within 14 days before onset of symptoms?")
                    travelled = input("Type Yes or No: ")
                    travelled = travelled.lower()
                    while(travelled != 'no' and travelled != 'yes'):
                        travelled = input("Please only type Yes or No: ")
                        travelled = travelled.lower()

                    print("\nHave you had close contact to confirmed or suspected case of COVID-19 witin 14 days before onset of illness?")
                    c_contact = input("Type Yes or No: ")
                    c_contact = c_contact.lower()
                    while(c_contact != 'no' and c_contact != 'yes'):
                        c_contact = input("Please only type Yes or No: ")
                        c_contact = c_contact.lower()

                    print("\nAre you under quarantine now?")
                    quarantine = input("Type Yes or No: ")
                    quarantine = quarantine.lower()
                    while(quarantine != 'no' and quarantine != 'yes'):
                        quarantine = input("Please only type Yes or No: ")
                        quarantine = quarantine.lower()

                    print("Your status is successfull updated,press enter to back to menu.")
                    input()

                    idseq[9] = symptoms
                    idseq[10] = symptoms2
                    idseq[11] = area
                    idseq[12] = travelled
                    idseq[13] = c_contact
                    idseq[14] = quarantine

                elif chr(51) == user_function: # Update medical history & occupation
                    print("\nPlease answer the question below.\nPress enter to continue.")
                    input()
                    print("Do you suffer any chronic disease listed below before?")
                    print("-Lung or heart disease\n-Asthma\n-Diabetes\n-Sickle cell disease\n-Immunosuppression")
                    inputdisease = input("Type Yes or No: ")
                    inputdisease = inputdisease.lower()
                    while (inputdisease != 'no' and inputdisease != 'yes'):
                        inputdisease = input("Please only type Yes or No: ")
                        inputdisease = inputdisease.lower()
                    print(("\nWhat is your occupation?\n1.Student\n2.Medical Personnel\n3.Retiree\n4.Government Functionary\n5.Others"))
                    occupation = input("Type the number according to the occupation: ")
                    while (chr(49) != occupation and chr(50) != occupation and chr(51) != occupation and chr(52) != occupation and chr(53) != occupation):
                        occupation = input("Please enter an valid number: ")
                    if chr(49) == occupation:
                        inputoccupation = "Student"
                        occupationrisk = True

                    elif chr(50) == occupation:
                        inputoccupation = "Medical Personnel"
                        occupationrisk = False

                    elif chr(51) == occupation:
                        inputoccupation = "Retiree"
                        occupationrisk = True

                    elif chr(52) == occupation:
                        inputoccupation = "Government Functionary"
                        occupationrisk = False

                    elif chr(53) == occupation:
                        print("Does your occupation meet a lot of people")
                        occupationother = input("Type Yes or No: ")
                        occupationother = occupationother.lower()

                        while (occupationother != 'no' and occupationother != 'yes'):
                            occupationother = input("Please only type Yes or No: ")
                            occupationother = occupationother.lower()

                        if occupationother == "yes":
                            inputoccupation = "Others, High"
                            occupationrisk = False

                        elif occupationother == 'no':
                            inputoccupation = "Others, Low"
                            occupationrisk = True

                    if (int(idseq[1])>=60 and occupationrisk==False and inputdisease=="yes"):
                        inputrisk = "3, High"

                    elif (int(idseq[1])>=60 and occupationrisk==False):
                        inputrisk = "2, High"

                    elif (int(idseq[1])>=60 and inputdisease=="yes"):
                        inputrisk = "2, High"

                    elif (occupationrisk==False and inputdisease=="yes"):
                        inputrisk = "2, High"

                    elif (int(idseq[1])>=60 or occupationrisk==False or inputdisease=="yes"):
                        inputrisk = "1, High"

                    else:
                        inputrisk = "0, Low"

                    print("Your medical history and occupation have updated successfully.\nPress enter to back to menu.")
                    input()

                    if idseq[18] == '-' or idseq[18] == 'no': # if a user already has appointment where his/her appointment status will become yes or confirm, but if without this statement, when the user update again his/her medical history & occupation, the user's appointment status will turn to no
                        idseq[15] = inputdisease
                        idseq[16] = inputoccupation
                        idseq[17] = inputrisk
                        idseq[18] = 'no'

                    elif idseq[18] == 'yes' or idseq[18] == 'confirm': # so with this statement, if a user already has appointment, his/her apppointment status will keep as usual which is yes or confirm
                        idseq[15] = inputdisease
                        idseq[16] = inputoccupation
                        idseq[17] = inputrisk


                elif chr(52) == user_function: # Check appointment
                    confirmapp = True
                    while(confirmapp):
                        if idseq[18] == 'yes': # if a user already received a appointment, his/her appointment status will turn to yes
                            print("\nPPV ID:",idseq[19])
                            print("PPV name:",idseq[20])
                            print("PPV date:",idseq[21])
                            print("PPV time:",idseq[22])
                            print("Type of vaccine:",idseq[23])
                            print("\nCan you attend to this appointment. \nOnce you confirm, you cannot change the time anymore.")
                            print("1.Yes\n2.No\n3.Make decision later")
                            decision = input("Enter the number according to its function: ")
                            while (chr(49) != decision and chr(50) != decision and chr(51) != decision):
                                decision = input("Please enter an valid number: ")

                            if chr(49) == decision:
                                cdecision = input("\nDo you confirm you can attend to this appointment.\n1.Yes\n2.No\nOnce you confirm, you cannot change the time anymore: ")
                                
                                while (chr(49) != cdecision and chr(50) != cdecision):
                                    cdecision = input("Please enter an valid number: ")
                                
                                if chr(49) == cdecision:    
                                    idseq[18] = 'confirm'
                                    print("You have confirmed this appointment. Remember attend to the appointment on time.\nPress enter to back to menu.")
                                    input()
                                    confirmapp = False
                                
                                elif chr(50) == cdecision:
                                    confirmapp = True
                            
                            elif chr(50) == decision:
                                c2decision = input("\nDo you confirm you want to cancel this appointment.\n1.Yes\n2.No\nOnce you cancel, you need to wait for administrator to assign to you a new appointment: ")
                                
                                while (chr(49) != c2decision and chr(50) != c2decision):
                                    c2decision = input("Please enter an valid number: ")
                                
                                if chr(49) == c2decision:
                                    deletePPVid = idseq[19]
                                    idseq[18] = 'no'
                                    idseq[19] = '-'
                                    idseq[20] = '-'
                                    idseq[21] = '-'
                                    idseq[22] = '-'
                                    idseq[23] = '-'
                                    
                                    for i in PPV_list:
                                        if i[0] == deletePPVid:
                                            i[5] = str(int(i[5])-1)
                                    
                                    print("You have cancelled this appointment successfully, please wait for administrator to assign you a new appointment.\nPress enter to back to menu")
                                    input()
                                    
                                    writeText2(PPV_list)
                                    confirmapp = False

                                elif chr(50) == c2decision:
                                    confirmapp = True

                            elif chr(51) == decision:
                                break

                        elif idseq[18] == "no": # this is where user already update his/her medical history & occupation but he/she haven't received any appointment yet
                            print("You haven't received appointment yet, please wait for admin to assign appointment to you.\nPress enter to back to menu.")
                            input()
                            confirmapp = False

                        elif idseq[18] == "-": # this is where user haven't update his/her medical history & occupation yet
                            print("You have to update your medical history & occupation first.(selection 3 in menu.)\nPress enter to back to menu.")
                            input()
                            confirmapp = False

                        elif idseq[18] == "confirm": # this is where user already confirmed his/her appointment, so that he/she cannot do changing anymore
                            print("\nPPV ID:",idseq[19])
                            print("PPV name:",idseq[20])
                            print("PPV date:",idseq[21])
                            print("PPV time:",idseq[22])
                            print("Type of vaccine:",idseq[23])
                            print("You have confirmed this appointment, no any changes will be allowed.\nPlease attend on time.")
                            confirmapp = False

                            

                elif chr(53) == user_function: # Logout account, back to main menu
                    doneop = False

    
        writeText(user_list) # calling function to write the data in the list into txt file
    

    elif chr(51) == method: # Admin Login
        print("\n--Admin Login--")
        if input("password: ") == 'group16':
            print("Password correct.")

            abc = True
            while(abc):

                user_list = readText()
                PPV_list = readPPV()

                print("\nWelcome admin!")
                print("1.User")
                print("2.PPV")
                print("3.Asign appointment")
                print("4.Logout")
                admin_function = input("Enter the number according to its function: ")
                
                while (chr(49) != admin_function and chr(50) != admin_function and chr(51) != admin_function and chr(52) != admin_function):
                    admin_function = input("Please enter an valid number: ")

                if chr(49) == admin_function: # Manage user
                    print("\n1.Check all user")
                    print("2.Delete user")
                    print("3.Back")
                    admin_user = input("Enter the number according to its function: ")

                    while (chr(49) != admin_user and chr(50) != admin_user and chr(51) != admin_user):
                        admin_user = input("Please enter an valid number: ")

                    if chr(49) == admin_user: # Check user
                        print("\n1.sort by age")
                        print("2.sort by risk")
                        sortuser = input("Enter the number according to its function: ")

                        while (chr(49) != sortuser and chr(50) != sortuser):
                            sortuser = input("Please enter an valid number: ")
                        
                        print("\nNAME                    AGE     ID              STATE           POSTCODE        RISK            APPOINTMENT STATUS      PPV ID")
                        print("---------------         ---     ------------    ------------    --------        -------         ------------------      ------")
                        
                        if chr(49) == sortuser: # Check user sort by user's age
                            user_list.sort(key = lambda x: int(x[1]),reverse=True)

                            for i in user_list:
                                if len(i[0]) > 7: # i[0] is name of user, if the name of user is more than 7 character, the layout below will be executed
                                    if len(i[7]) < 8: # i[7] is state. if the state is less than 8 character, the layout below will be executed
                                        print(f'{i[0]}\t\t{i[1]}\t{i[2]}\t{i[7]}\t\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                    else:
                                        print(f'{i[0]}\t\t{i[1]}\t{i[2]}\t{i[7]}\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                else:
                                    if len(i[7]) < 8:
                                        print(f'{i[0]}\t\t\t{i[1]}\t{i[2]}\t{i[7]}\t\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                    else:
                                        print(f'{i[0]}\t\t\t{i[1]}\t{i[2]}\t{i[7]}\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                        elif chr(50) == sortuser: # Check user sort by user's risk
                            user_list.sort(key = lambda x: x[17],reverse=True)
                            for i in user_list:
                                if len(i[0]) > 7:
                                    if len(i[7]) < 8:
                                        print(f'{i[0]}\t\t{i[1]}\t{i[2]}\t{i[7]}\t\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                    else:
                                        print(f'{i[0]}\t\t{i[1]}\t{i[2]}\t{i[7]}\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                else:
                                    if len(i[7]) < 8:
                                        print(f'{i[0]}\t\t\t{i[1]}\t{i[2]}\t{i[7]}\t\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                    else:
                                        print(f'{i[0]}\t\t\t{i[1]}\t{i[2]}\t{i[7]}\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                    elif chr(50) == admin_user: # Delete user
                        print("\nNAME                    AGE     ID              STATE           POSTCODE        RISK            APPOINTMENT STATUS      PPV ID")
                        print("---------------         ---     ------------    ------------    --------        -------         ------------------      ------")
                        
                        user_list.sort(key = lambda x: int(x[1]),reverse=True)

                        deleteUserExist = False # assume that user is not exist

                        for i in user_list: # print all user exist
                            if len(i[0]) > 7:
                                if len(i[7]) < 8:
                                    print(f'{i[0]}\t\t{i[1]}\t{i[2]}\t{i[7]}\t\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                else:
                                    print(f'{i[0]}\t\t{i[1]}\t{i[2]}\t{i[7]}\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                            else:
                                if len(i[7]) < 8:
                                    print(f'{i[0]}\t\t\t{i[1]}\t{i[2]}\t{i[7]}\t\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                else:
                                    print(f'{i[0]}\t\t\t{i[1]}\t{i[2]}\t{i[7]}\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')


                        deleteuser = input("\n(Press space and enter to delete user later) \nEnter the ID of user that you want to delete: ")
                        
                        if deleteuser == ' ':
                            abc = True

                        else:
                            for i in user_list:
                                if deleteuser == i[2]:
                                    deleteUserExist = True # when the user id was found in list, thats mean the user admin input is exist, user exist become True
                                    print(f"\nAre you sure you want to delete user {deleteuser}: ") # require double confirm from admin
                                    print("1.Yes")
                                    print("2.No")
                                    confirmdelete = input("Enter the number according to its function: ")
                                    
                                    while (chr(49) != confirmdelete and chr(50) != confirmdelete):
                                        confirmdelete = input("Please enter an valid number: ")
                                    
                                    if chr(49) == confirmdelete: # when admin confirm delete this user
                                        if i[18] == 'yes' or i[18] == 'confirm': # if user already assigned appointment
                                            deleteusers = i[19] # i[19] is the PPV id that has assigned to this user
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            for a in PPV_list:
                                                if a[0] == deleteusers: # deleteusers = i[19], typed in line 568, i[19] is PPV id
                                                    a[5] = str(int(a[5])-1) # number of people in that PPV which was assigned to user also has to -1
                                            print(f'User {deleteuser} has deleted successfully.')
                                            writeText2(PPV_list)
                                            break

                                        else: # if user haven't received any appointment, then no need delete or minus any data in PPV txt file, but only delete all data of this user
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            del i[0]
                                            print(f'User {deleteuser} has deleted successfully.')
                                            writeText2(PPV_list)
                                            break
                                        
                                    elif chr(50) == confirmdelete: # when admin dosn't confirm to delete this user, program will back to main menu
                                        abc = True

                            if not deleteUserExist:
                                print(f'User {deleteuser} does not exist.\nPress enter to back to menu')
                                input()

                    elif chr(51) == admin_user:
                        abc = True


                elif chr(50) == admin_function: # Manage PPV
                    print("\n1.Add PPV")
                    print("2.Check PPV")
                    print("3.Delete PPV")
                    print("4.Back")
                    ppvadmin = input("Enter the number according to its function: ")
                    while (chr(49) != ppvadmin and chr(50) != ppvadmin and chr(51) != ppvadmin and chr(52) != ppvadmin):
                        ppvadmin = input("Please enter an valid number: ")

                    if chr(49) == ppvadmin: # Add PPV
                        print("Press space and enter to add PPV later.")
                        ppvid = input("\nPPV ID: ")
                        if ppvid == ' ':
                            abc = True

                        else:
                            ppvname = input("PPV name: ")
                            ppvdate = input("PPV date: ")
                            ppvtime = input("PPV time: ")
                            ppvtype = input("Type of vaccine: ")

                            fg = open('ppv.txt','a')
                            fg.write(ppvid)
                            fg.write('\n')
                            fg.write(ppvname)
                            fg.write('\n')
                            fg.write(ppvdate)
                            fg.write('\n')
                            fg.write(ppvtime)
                            fg.write('\n')
                            fg.write(ppvtype)
                            fg.write('\n')
                            fg.write('0') # to count number of people, the program has to leave a space to every PPV and every PPV has 0 people at the first
                            fg.write('\n')
                            fg.close()

                            print(f'PPV {ppvid} has added successsfull')
                            print(" ")

                    elif chr(50) == ppvadmin: # Check all PPV that are exist
                        PPV_list = readPPV()
                        print("\nPPV ID          PPV NAME                PPV DATE        PPV TIME        Type of Vaccine         Number of People")
                        print("------          --------------          ---------       ----------      ---------------         ----------------")
                        PPV_list.sort(key = lambda x: x[0])
                        for i in PPV_list:
                            if len(i[1]) < 8: # i[1] is PPV name, if the name is less than 8 character like PPV UM, three tab (\t\t\t) will be used
                                print(f"{i[0]}\t\t{i[1]}\t\t\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}")

                            elif len(i[1]) >= 8 and len(i[1]) < 16: # else if the name is more than and equal to 8 and less than 16 character like PPV Cheras, two tab (\t\t) will be used
                                print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}")

                            else: # else, one tab (\t) will be used
                                print(f"{i[0]}\t\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}")
                        print("\n(Press space and enter to check later)")
                        checkuserinppv = input("Enter PPV ID that you want to check: ")

                        if checkuserinppv == ' ':
                            abc = True
                        
                        else:
                            isFoundPPVAttendees = False

                            for a in PPV_list:
                                if a[0] == checkuserinppv:
                                    
                                    isFoundPPVAttendees = True
                                    print("\nNAME                    AGE     ID              STATE           POSTCODE        RISK            APPOINTMENT STATUS      PPV ID")
                                    print("---------------         ---     ------------    ------------    --------        -------         ------------------      ------")

                                    for i in user_list:
                                        if i[19] == checkuserinppv:
                                            if len(i[0]) > 7:
                                                if len(i[7]) < 8:
                                                    print(f'{i[0]}\t\t{i[1]}\t{i[2]}\t{i[7]}\t\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                                else:
                                                    print(f'{i[0]}\t\t{i[1]}\t{i[2]}\t{i[7]}\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                            else:
                                                if len(i[7]) < 8:
                                                    print(f'{i[0]}\t\t\t{i[1]}\t{i[2]}\t{i[7]}\t\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                                                else:
                                                    print(f'{i[0]}\t\t\t{i[1]}\t{i[2]}\t{i[7]}\t{i[6]}\t\t{i[17]}\t\t{i[18]}\t\t\t{i[19]}')

                            if (not isFoundPPVAttendees):
                                print(f'PPV {checkuserinppv} does not exist.\nPress enter to back to menu')
                                input()

                    elif chr(51) == ppvadmin: # Delete PPV
                        PPV_list = readPPV()
                        print("\nPPV ID          PPV NAME                PPV DATE        PPV TIME        Type of Vaccine         Number of People")
                        print("------          --------------          ---------       ----------      ---------------         ----------------")
                        
                        ppvdeleteExist = False # assume that PPV is not exist

                        PPV_list.sort(key = lambda x: x[0])
                        for i in PPV_list:
                            if len(i[1]) < 8:
                                print(f"{i[0]}\t\t{i[1]}\t\t\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}")

                            elif len(i[1]) >= 8 and len(i[1]) < 16:
                                print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}")

                            else:
                                print(f"{i[0]}\t\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}")

                        deleteppv = input("\n(Press space and enter to delete PPV later) \nEnter PPV ID that you want to delete: ")
                        
                        if deleteppv == ' ':
                            abc = True

                        else:
                            for i in PPV_list:
                                if deleteppv == i[0]:
                                    ppvdeleteExist = True # when the PPV id was found in list, thats mean the PPV admin input is exist, PPV exist become True
                                    print(f'Are you sure you want to delete PPV {deleteppv}: ') # require double confirm from admin
                                    print("1.Yes")
                                    print("2.No")
                                    confirmdeleteppv = input("Enter the number according to its function: ")
                                    
                                    while (chr(49) != confirmdeleteppv and chr(50) != confirmdeleteppv):
                                        confirmdeleteppv = input("Please enter an valid number: ")

                                    if chr(49) == confirmdeleteppv and int(i[5]) != 0: # if the PPV is already assigned to at least 1 user, then this PPV cannot be deleted 
                                        print(f'PPV {deleteppv} cannot be deleted due to this PPV has already assigned to user.\nPress enter to back to menu.')
                                        input()
                                        abc = True
                                    
                                    elif chr(49) == confirmdeleteppv and int(i[5]) == 0: # only if the PPV is added and haven't assigned to any user, this PPV can be deleted
                                        del i[0]
                                        del i[0]
                                        del i[0]
                                        del i[0]
                                        del i[0]
                                        del i[0]
                                        print(f'PPV {deleteppv} has deleted successfully.')
                                        writeText2(PPV_list)
                                        break

                                    elif chr(50) == confirmdeleteppv:
                                        abc = True

                            if not ppvdeleteExist:
                                print(f'PPV {deleteppv} does not exist.\nPress enter to back to menu.')
                                input()

                    elif chr(52) == ppvadmin:
                        abc = True



                elif chr(51) == admin_function: # Assign appointment

                    print("\nPPV ID          PPV NAME                PPV DATE        PPV TIME        Type of Vaccine         Number of People")
                    print("------          --------------          ---------       ----------      ---------------         ----------------")
                    PPV_list.sort(key = lambda x: x[0])
                    for i in PPV_list:
                        if len(i[1]) < 8:
                            print(f"{i[0]}\t\t{i[1]}\t\t\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}")

                        elif len(i[1]) >= 8 and len(i[1]) < 16:
                            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}")

                        else:
                            print(f"{i[0]}\t\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{i[5]}") 

                    userLeft = False # assume that there is no user left need to assign appointment, where userLeft is False

                    user_list.sort(key = lambda x: x[17],reverse=True) # sort by user's risk, so that the higher risk user will be assigned appointment first
                    for a in user_list:
                        if a[18] == 'no': # only if the user's appointment status is no, only then userleft is True now
                            assgnuser = a
                            userLeft = True
                            break

                    if userLeft: # when it is True, that user's details will be shown and admin has to assign appointment to he/she with PPV id

                        print("\nUser's Details")
                        print("--------------")
                        print("ID:",assgnuser[2])
                        print("age:",assgnuser[1])
                        print("state:",assgnuser[7])
                        print("postcode:",assgnuser[6])
                        print("risk status:",assgnuser[17])
                        assgnppv = input(f"\n(Press space and enter to assign later) \nEnter PPV ID that wanted to assign to {a[2]}: ")

                        if assgnppv == ' ':
                            abc = True

                        else:
                            validPPV = False # assume that the PPV is not exist, validPPV is False now

                            for i in PPV_list:
                                if assgnppv == i[0]:
                                    print(f'Are you sure you want to assign PPV {assgnppv} to user {assgnuser[2]}?')
                                    print("1.Yes")
                                    print("2.No")
                                    confirmassignppv = input("Enter the number according to its function: ")
                                    while (chr(49) != confirmassignppv and chr(50) != confirmassignppv):
                                        confirmassignppv = input("Please enter an valid number: ")

                                    if chr(49) == confirmassignppv:
                                        print("PPV",assgnppv,"is assigned to user", assgnuser[2], "successfully")

                                        a[18] = 'yes'
                                        a[19] = i[0]
                                        a[20] = i[1]
                                        a[21] = i[2]
                                        a[22] = i[3]
                                        a[23] = i[4]
                                        i[5] = str(int(i[5])+1)

                                        writeText2(PPV_list)
                                        validPPV = True # when the PPV id was found in list, thats mean the PPV admin input is exist, validPPV become True now
                                        break

                                    elif chr(50) == confirmassignppv:
                                        abc = True
                                        break

                            else:
                                validPPV = False # if the PPV id was not found in the list, validPPV still is False, so the PPV id would not be assigned to user
                                print(f"PPV {assgnppv} do not exist. Press enter to try again.")
                                input()

                    else: # else, it is false, thats mean there is no user left need to assign
                        print("\nNo user left to assign. Press enter to back to menu")
                        input()

                elif chr(52) == admin_function: # Logout account, back to main menu
                    abc = False

                writeText(user_list) # calling function to write the data in the list into txt file

        else:
            print("Password incorrect.\nPress enter and try again.")
            input()

    elif chr(52) == method: # Terminate program
        isQuit = False
