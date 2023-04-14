# ----------------------------------------------------------- #
#                       Display module                        #
#                   ©2023 Mathurin Roulier                    #
# ----------------------------------------------------------- #

"""
This module some functions used to display or ask information information to the user in the terminal.

menu
----
Displays a menu and asks the user to make a choice among the proposed options.

"""
 
def menu(options:list, question:str="Faites votre choix :") -> tuple[int, str]:
    """Affiche un menu et demande à l'utilisateur de faire un choix parmi les options proposées."""
    print(str(question))                                                                        # Show the question
    for i in range(len(options)):                                                               # For each option
        print(str(i+1) + " : " + str(options[i]))                                               # Show the option number and the option
    choice=int(input(">>> "))                                                                   # Ask the user to make a choice
    if choice <= len(options) and choice >= 0:                                                  # If the choice is valid
        print("Your choice : " + str(options[choice-1]) + " (" + str(choice) + ")")             # Show the choice
    return choice, options[choice-1]                                                            # Return the choice and the option
