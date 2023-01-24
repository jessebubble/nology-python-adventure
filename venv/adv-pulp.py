from terminal_colored_print import colored_print

name = "PULP"

print("")
colored_print("...Welcome to the West End, " + name + "!", fg_color=200, format="Bold;Underline")
print("")
colored_print("        _____", fg_color=227, format="Bold")          
colored_print("      .'     `.  ", fg_color=227, format="Bold")      
colored_print("      |       |  ", fg_color=227, format="Bold")      
colored_print("      |.-----.|  ", fg_color=227, format="Bold")    
colored_print("      .'`.-.'`.  ", fg_color=227, format="Bold")  
colored_print("      `..' `..'  ", fg_color=227, format="Bold")      
colored_print("      (  (_)  )  ", fg_color=227, format="Bold")      
colored_print("         ___     ", fg_color=227, format="Bold")      
colored_print("          -      ", fg_color=227, format="Bold")      
colored_print("  _.==='-._.-`===._ ", fg_color=227, format="Bold")    
colored_print(".===================. ", fg_color=227, format="Bold") 
colored_print("===================== ", fg_color=227, format="Bold")
colored_print(":====================:", fg_color=227, format="Bold")
print("")

def start():
    print("")
    colored_print("She came from Greece, she had a thirst for knowledge.", fg_color=101, format="Bold;Italic")
    colored_print("She studied sculpture at Saint Martin's College.", fg_color=102, format="Bold;Italic")
    colored_print("That's where I...caught her eye.", fg_color=103, format="Bold;Italic")
    colored_print("She told me that her dad was loaded.", fg_color=104, format="Bold;Italic")
    colored_print("Well in that case, I'll have a rum and coca-cola.", fg_color=105, format="Bold;Italic")
    colored_print("She said (fine / no)", fg_color=105, format="Bold;Italic;Underline;Reversed")

    choice = input("> ")
    if choice == "fine":
        fine()
    elif choice == "no":
        no()
    else:
        print("")
        end("If you called your dad he could stop it all.")

def fine():
    print("")
    colored_print("She said, 'I wanna live like common people.", fg_color=204, format="Bold;Italic")
    colored_print("I wanna do whatever common people do.", fg_color=205, format="Bold;Italic")
    colored_print("I wanna sleep with common people.", fg_color=206, format="Bold;Italic")
    colored_print("I wanna sleep with common people like you.' ", fg_color=207, format="Bold;Italic")
    colored_print("Well, what else could I do? (i'll see what i can do / no) ", fg_color=204, format="Bold;Italic;Reversed")
    choice = input("> ")
    if choice == "i'll see what i can do":
        print("")
        colored_print("I said, 'pretend you've got no money.'", fg_color=46, format="Bold;Italic")
        colored_print("Rent a flat above a shop.", fg_color=47, format="Bold;Italic")
        colored_print("Cut your hair and get a job.", fg_color=48, format="Bold;Italic")
        colored_print("Pretend you never went to school.", fg_color=49, format="Bold;Italic")
        colored_print("continue (yes / no)", fg_color=49, format="Bold;Italic;Reversed")
        choice = input("> ")
        if choice == "yes":
            print("")
            colored_print("But still you'll never get it right.", fg_color=65, format="Bold;Italic")
            colored_print("Because when you lay in bed at night.", fg_color=65, format="Bold;Italic")
            colored_print("Watching roaches climb the wall.", fg_color=66, format="Bold;Italic")
            colored_print("If you called your dad he could stop it all.", fg_color=67, format="Bold;Italic")
            colored_print("You'll never live like common people.", fg_color=68, format="Bold;Italic")
            colored_print("You'll never do whatever common people do.", fg_color=69, format="Bold;Italic")
            colored_print("You'll never fail like common people.", fg_color=70, format="Bold;Italic")
            colored_print("You'll never watch your life slide out of view.", fg_color=71, format="Bold;Italic")
            colored_print("...And you dance and drink and screw.", fg_color=72, format="Bold;Italic")
            colored_print("Because there's nothing else to do.", fg_color=73, format="Bold;Italic")

        if choice == "no":
            print("")
            colored_print("Sing along with the common people.", bg_color=244, format="Bold;Italic")
            colored_print("Sing along and it might just get you through.", bg_color=244, format="Bold;Italic")
            colored_print("Laugh along with the common people.", bg_color=244, format="Bold;Italic")
            colored_print("Because you think that poor is cool.", bg_color=244, format="Bold;Italic")

    elif choice == "no":
        print("")
        colored_print("You wanna live like common people.", bg_color=244, format="Bold;Italic")
        colored_print("You wanna see whatever common people see.", bg_color=244, format="Bold;Italic")
        colored_print("wanna sleep with common people.", bg_color=244, format="Bold;Italic")
        colored_print("You wanna sleep with common people like me.", bg_color=244, format="Bold;Italic")
        colored_print("But she didn't understand.", bg_color=244, format="Bold;Italic")
        colored_print("She just smiled and held my hand.", bg_color=244, format="Bold;Italic")

    else:
        start()

def no():
    print("")
    colored_print("You'll never live like common people.", bg_color=244, format="Bold;Italic")
    colored_print("You'll never do what common people do.", bg_color=244, format="Bold;Italic")
    colored_print("You'll never fail like common people.", bg_color=244, format="Bold;Italic")
    colored_print("You'll never watch your life slide out of view.", bg_color=244, format="Bold;Italic")
    colored_print("...And then you dance and drink and screw.", bg_color=244, format="Bold;Italic")
    colored_print("Because there's nothing else to do.", bg_color=244, format="Bold;Italic")

def end(why):  
    colored_print(why, "", bg_color=244, format="Bold;Italic") 
    colored_print("You will never understand.", bg_color=244, format="Bold;Italic")
    colored_print("How it feels to live your life.", bg_color=244, format="Bold;Italic")
    colored_print("With no meaning or control.", bg_color=244, format="Bold;Italic")
    colored_print("And with nowhere left to go.", bg_color=244, format="Bold;Italic")
    exit(0)

start()