name = "PULP"

print("")
print("Welcome to the West End, " + name + "!")
print("")
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
print("")

def start():
    print("She came from Greece, she had a thirst for knowledge.")
    print("She studied sculpture at Saint Martin's College.")
    print("That's where I...caught her eye.")
    print("She told me that her dad was loaded.")
    print("Well in that case, I'll have a rum and coca-cola.")
    print("She said (fine / no)")

    choice = input("> ")
    if choice == "fine":
        fine()
    elif choice == "no":
        no()
    else:
        end("If you called your dad he could stop it all.")

def fine():
    print("She said, 'I wanna live like common people.")
    print("I wanna do whatever common people do.")
    print("I wanna sleep with common people.")
    print("I wanna sleep with common people like you.' ")
    print("Well, what else could I do? (i'll see what i can do / no) ")
    choice = input("> ")
    if choice == "i'll see what i can do":
        print("I said, 'pretend you've got no money.'")
        print("She just laughed and said, `Ha, you're so funny.'")
        print("Rent a flat above a shop.")
        print("Cut your hair and get a job.")
        print("Pretend you never went to school.")
        print("continue (yes / no)")
        choice = input("> ")
        if choice == "yes":
            print("But still you'll never get it right.")
            print("'Cause when you're laid in bed at night.")
            print("Watching roaches climb the wall.")
            print("If you called your dad he could stop it all.")
            print("You'll never live like common people.")
            print("You'll never do whatever common people do.")
            print("You'll never fail like common people.")
            print("You'll never watch your life slide out of view.")
            print("And you dance and drink and screw.")
            print("Because there's nothing else to do.")

            if choice == "no":
                print("Sing along with the common people.")
                print("Sing along and it might just get you through.")
                print("Laugh along with the common people.")
                print("Because you think that poor is cool.")

    elif choice == "no":
        print("You wanna live like common people.")
        print("You wanna see whatever common people see.")
        print("wanna sleep with common people.")
        print("You wanna sleep with common people like me.")
        print("But she didn't understand.")
        print("She just smiled and held my hand.")

    else:
        start()

def no():
    print("Never live like common people.")
    print("Never do what common people do.")
    print("Never fail like common people.")
    print("You'll never watch your life slide out of view.")
    print("And then you dance and drink and screw.")
    print("Because there's nothing else to do.")

def end(why):  
    print(why, "") 
    print("You will never understand.")
    print("How it feels to live your life.")
    print("With no meaning or control.")
    print("And with nowhere left to go.")
    exit(0)

start()