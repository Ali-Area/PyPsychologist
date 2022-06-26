
import ActionsMadule as action


class Person():

    # * --- properties --- #
    name = None
    family = None
    age = None
    counselingCost = 0

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def PrintUserInformation(self):
        print(f"\n--- User Personal Information ---\nHello {self.name} {self.family} - {self.age} Years old.\nWelcome to our Helpful Application.\n--- ---\n")

    def PrintCosts(self):
        print(f"\nThe cost of your psychological counseling is : {self.counselingCost}\n")

    def PrintEntireInvoice(self, counselingResult):
        print(f"""
                --------------------------------------------------------
             Name : {self.name} | Family : {self.family} | Age : {self.age}     
        |                                                                       |
            Dear,                                                               
        |   You explained your feelings and problems to usو and we recognized   |
            that you have {counselingResult} disorder.                          
        |                -----------------------------------                    |
            Amount of money That had to be paid : {self.counselingCost}$        
        |                                                                       |
            Always be healthy :)                                                
                --------------------------------------------------------
        """)


# * --- other methods --- * # 
def GetUserInformation(text):
    print(f"\n--- {text} ---\n")

    while(True):
        try:
            name = input(f"What is Your Name? ")
            family = input(f"Your Family?")
            age = int(input(f"enter the age :"))

            
            return [name, family, age]
        except:

            GetUserInformation("Entered Values are Incurrent. try again :)")
        
    
# --- take user information --- # 
user_information = GetUserInformation("Fill out the Personal Information")

# --- instantiation of the person class --- #
user = Person(name=user_information[0], family=user_information[1], age=user_information[2])

# --- print user information --- #
user.PrintUserInformation()

# --- take the user description of the feelings --- #
entered_keys = action.TakeUserDescription()

# --- find the last result of counseling --- #
counseling_result = action.FindCounselingResult(entered_keys)

# --- print the last result of counseling --- #
action.PrintCounselingResult(counseling_result)


# --- set the person cost --- # 
if(counseling_result == "Depression"):
    Person.counselingCost = 200
elif(counseling_result == "Mood"):
    Person.counselingCost = 150
elif(counseling_result == "Anxiety"):
    Person.counselingCost = 340
elif(counseling_result == "Social Anxiety"):
    Person.counselingCost = 510
elif(counseling_result == "Sleeping"):
    Person.counselingCost = 120

# --- print the counseling cost --- #
user.PrintCosts()

# --- print the entire invoice --- #
print("--- Your Invoice ---")
user.PrintEntireInvoice(counselingResult=counseling_result)