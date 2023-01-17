# adventure game
name = "Pet Shop Boy"
print("Welcome to the West End, " + name + "!")
print("        _____")          
print("      .'     `.  ")      
print("      |       |  ")      
print("      |.-----.|  ")    
print("      .'`.-.'`.  ")  
print("      `..' `..'  ")      
print("      (  (_)  )  ")      
print("         ___     ")      
print("          -      ")      
print("  _.==='-._.-`===._ ")    
print(".===================. ") 
print("======================= ")
print(":=======================:")

def start():
    print("In a West End town.")
    print("A dead end world.")
    print("Are you an East End boy or a West End girl?")

    choice = input("> ")

    if choice == "East End":
        east_end()
    elif choice == "West End":
        west_end()
    else:
        dead("You think you're mad, too unstable.")

def east_end():
    print("Call the police?")
    print("There's a madman around.")
    print("Running down, underground.")
    print("To a dive bar in a West End town.")
    get_police = False

    while True:
        choice = input("> ")

        if choice == "no":
            dead("Sometimes you're better off dead.")
        elif choice == "yes" and not get_police:
            print("Too many shadows.")
            print("Whispering voices.")
            get_police = True
        else:
            print("Faces on posters, too many choices. (yes/no)")

def west_end():
    print("You got no future, we've got no past.")
    print("Here today and built to last.")
    print("In every city in every nation. From Lake Geneva to the Finland Station.")
    print("How much do you need? (nothing/something)")

    choice = input("> ")

    if choice == "nothing":
        print("Have you got it?")
        print("Do you get it?")
        print("If so, how often?")
    elif "something" in choice:
        start()
    else:
        west_end()

def dead(why):
    print(why, "Kicking in chairs and knocking down tables.")
    exit(0)

start()
