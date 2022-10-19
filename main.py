# Start of computer program
# Start of global variables

def globalVars():
 global individualdict
 global teamdict
 global individualsfile
 global teamsfile
 individualdict ={} 
 teamdict = {}
 individualsfile = "individual.txt"
 teamsfile = "team.txt"

# End of globalVars

def Menu():
    menuChoice =""
    while menuChoice !="0":
        print("""
        1) Add Teams
        2) Add Individuals
        3) Show scores
        0) Exit
        """)

        # Initialise
      
        menuChoiceOK = False

        while not menuChoiceOK:
          
        # Repeat the program until a valid value has been entered
          
            menuChoice=input("Enter number of your choice: ")
            if menuChoice=="1":
              
              # Add a team
              
                AddTeam()
                menuChoiceOK = True
            elif menuChoice=="2":
              
              # Add a individual
              
                AddIndividual()
                menuChoiceOK = True
            elif menuChoice=="3":
              
              # show all saved data
              
                showevents()
                menuChoiceOK = True
            elif menuChoice=="0": 
            
              # End the program
              
                Exit()
                menuChoiceOK = True
            else:
              
              # Invalid option chosen
              
                print("Please input only 1, 2, 3 or 0: ")
              
                # Repeat the program until a valid value has been entered

def AddTeam():
  global teamdict
  while True:
   teamtup1 =input("Enter Team name:")
   if teamtup1 and teamtup1.isalpha():
     
     # Validates if the name entered are words
     
    break
   else :
     # If a name contains numbers #
     print("Invalid Name,renter without any numbers")
   continue
    
   # Repeat the program until a valid value has been entered

  teamtup2 =input("Enter names of 5 members:")
  print("Only choose from Basketball, Football or Cricket")

  while True:
   teamtup3 =input("Enter names of events:")
   if teamtup3 and teamtup3.isalpha():
    break
   else :
     print("Enter name without numbers")
   continue
  while True:

   teamtup4 =input("Enter score of the team:")
   if teamtup4 and teamtup4.isdigit():
     # Validates if the number entered is not a word
    break
   else :
     
     # If a number contains words
     
     print("Invalid Score, renter without any words")
     continue
   # Repeat the program until a valid value has been entered

  teamdict = {"Team Name":teamtup1,"Members":teamtup2, "Events":teamtup3, "Score":teamtup4}
  with open("team.txt","a") as td:
   td.write(str(teamdict) +"\n")
    
   # Saves the data on a new line
   # Stores the data to team.txt

def AddIndividual():
 global individualdict
 while True:
   individualtup1 = input("Enter name of individual:")
   if individualtup1 and individualtup1.isalpha():
    break
   else :
     print("Enter name without numbers")
   continue

 print("You can only choose from Mastermind or Maths")
 while True:
   individualtup2 =input("Enter names of events:")
   if individualtup2 and individualtup2.isalpha():
    break
   else :
     print("Enter a number again")
   continue

 while True:
   individualtup3 =input("Enter total score:")
   if individualtup3 and individualtup3.isdigit():
    break
   else :
     print("Enter a number again")
   continue

 individualdict = {"Name":individualtup1,"Events":individualtup2, "Score":individualtup3}
 with open("individual.txt","a") as ind:
   
   # Stores data to individual.txt
  ind.write(str(individualdict)+ "\n")
   
  # Converts the data into a string and saves it on text file

def showevents():
 eventschoice =""
 
 while eventschoice !="0":
  print("""
        1) Show Team Data
        2) Show Individual Data
        0) Exit
        """)

  eventschoiceok = False
  while not eventschoiceok:
   eventsChoice=input("Enter number of your choice: ")
   if eventsChoice=="1":
     
     # User can see the teams
     teamdata()
     eventschoiceok = True
   elif eventsChoice=="2":
     
     # User can see individuals
     
     individualdata()
     eventschoiceok = True
   elif eventsChoice=="0": 
     
     # User can go to the Main Menu
     
     Menu()
     eventschoiceok = True
   else: 
     
     # Invalid choice chosen
     
     print("Please input only 1, 2 or 0: ")

def teamdata():
  tmd=open("team.txt","r")
  for x in tmd:
   print(x)
    
   # Stores all the data that is in the individual.txt file

def individualdata():
  ind=open("individual.txt","r")
  for x in ind:
   print(x)
    
   # Stores all the data that is in the team.txt file

def Exit():
  print("""The program has ended.""")
 
globalVars()
Menu()

# End of computer program