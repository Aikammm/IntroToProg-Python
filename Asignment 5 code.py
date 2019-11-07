# --------------------------------------------------# Title: <Type the name of the script here>
# Descreption: <Type a description of the script>
# ChangeLog (Who,When,What)
# <Example Dev, 01/01/2019, Created Script>
# --------------------------------------------------
#  -- Data--  #
dicRow= {}
Row1 = ("Todo: Dishwash", "Priority: 1")
Row2 = ("Todo: Vacume", "Priority: 2")
lstTable =[Row1,Row2]
for row in lstTable:
    print(row[0], row[1], sep='|')

# Get user Input
while(True):
    print("Write or Read file data, then type 'Exit' to quit!")
    strChoice = input("Choose to [W]rite or [R]ead data: ")

    # Process the data
    if (strChoice.lower() == 'exit'): break
    elif(strChoice.lower() == 'w'):
        # Process the data
        strID = input("What is your ToDo?: ")
        strName = input("What is this priority?: ")
        dicRow= {"Todo":strID, '|' +"Priority":strName}
        lstTable.append(dicRow)
        for objRow in lstTable:
            print(objRow)

    elif (strChoice.lower() == 'r'):
        # File to Listprint
        for objRow in lstTable:
            print(objRow)
    else:
        print('Please choose either W or R!')

