import random

# Global variables
yes = ['A', 'a']
no = ['B', 'b']
quit = ['quit', 'Quit', 'Q', 'q']
alternate_response = ["I'm sorry, could you try again?", 
                      "One more time, please?", "I couldn't quite get that."]
exit = ["Bye!", "See ya!", "Sayonara!", "So long!", "That was fun!"]


def star_wars():
    """Function for instructions on beginning this task.
	
	Parameters
	---------
	Prints out what's going to occur in code.

	Returns
	---------
	begin_character : True
	"""
    
    print("Welcome to the Star Wars character customization!")
    print("By completing this task, you will successfully create your own"
          + " Star Wars entity.")
    print("To select an option from the menu, you will type in the letter"
          + " option provided.")
    print("If at any point you would like to leave, just type quit\n")
    begin_character()
    
    
def begin_character():
    """Function to begin a character

	Parameters
	---------
	answer : input
	response : []
		when prompted to type, the user types an answer
	
	Returns
	-------
	response : answer
		response becomes the answer
	begin_character : True
		starting the character is true
	character_side : True
		starting the side is true
	"""
    
    print("Do you want to create a Star Wars character?")
    
    # Calls upon the "yes" or "no" menu for user
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If the user selects "yes", the character customization begins
        if answer in yes:
            print("Awesome! Lets start...\n")
            user = True
            character_side()
        
        # If the user selects "no", the character customization ends
        elif answer in no:
            print("Bummer. See you later!")
            user = False
            break
            
        # Code stops running if user types "quit"
        elif answer in quit:
                print(random.choice(exit))
                break
                
        # Alternate response for an option not provided in the question menu
        else:
            print(random.choice(alternate_response))
            begin_character()
            

def character_side():
    """Function to determine if user is on the "light" or the "dark" side

	Parameters
	---------
	answer : input
		when prompted to type, the user types an answer
	
	Returns
	-------
	value : answer
		value becomes the first answer
	value1 : answer
		value1 becomes the second answer
	name_selection : True
		starting name selection is true
	"""
    
    print("Do you want to be on the light side or the dark side?")
    
    # Calls upon the side menu for user to select
    side_menu()
    
    answer = input()
    
    # Local variables
    light_side = ['A', 'a']
    dark_side = ['B', 'b']
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user selects to be on the light side
        if answer in light_side:
            print("Welcome to the light side.\nNow it's time to make your"
                  + " jedi name.\n")
            value = "light side"
            value1 = "Jedi Master"
            
            # Calls name selection function with stored variables
            name_selection(value, value1)
            
        # If user selects to be on the dark side
        elif answer in dark_side:
            print("Welcome to the dark side.\nNow it's time to make your"
                  + " sith name.\n")
            value = "dark side"
            value1 = "Darth"
            
            # Calls name selection function with stored variables
            name_selection(value, value1)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
        
        # Alternate response for an option not provided in the side menu
        else:
            print(random.choice(alternate_response))
            character_side()
            
            
def name_selection(value, value1):
    """Function to select a name for the user
	
	Parameters
	---------
	name : input
		When prompted to type, the user types a name
	
	Returns
	-------
	starwars_name : name
		Name becomes the starwars character name
	lightsaber_color : True
		Calling the function is true.
	"""
    
    print("As a member of the " + value + ", you need a name heard"
          + " throughout the galaxy.")
    print("Please enter your name: ")
    name = input()
    response = []
    response.append(name)
    
    for name in response:
        
        # Code stops running if user types "quit"
        if name in quit:
            print(random.choice(exit))
            break
        
        # User's name is stored in a variable
        else:
            print("Welcome, " + value1 + " " + name + ".")
            starwars_name = (value1 + " " + name)
            print("Now you need to craft a weapon.\n")
            
            # Calls upon the lightsaber function with the stored variables
            lightsaber_color(value1, name)
            

def lightsaber_color(value1, name):
    """Function to select a lightsaber color
	
	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	red_saber :True
	blue_saber : True
	green_saber : True
	purple_saber : True
	yellow_saber : True
	orange_saber : True
	cyan_saber : True
	magenta_saber : True
		Starting all color functions is true.
	"""
    
    print("A lightsaber is a powerful and elegant weapon from a more"
          + " civilized age.")
    print("This weapon will be your life, so choose wisely.")
    print("Please select a color for your lightsaber: ")
    
    # Displays the options for lightsaber colors
    color_menu()
    
    answer = input()
    
    # Local variables
    a = ['A', 'a']
    b = ['B', 'b']
    c = ['C', 'c']
    d = ['D', 'd']
    e = ['E', 'e']
    f = ['F', 'f']
    g = ['G', 'g']
    h = ['H', 'h']
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks red
        if answer in a:
            red_saber(value1, name)
        
        # If user picks blue
        elif answer in b:
            blue_saber(value1, name)
            
        # If user picks green
        elif answer in c:
            green_saber(value1, name)
        
        # If user picks purple
        elif answer in d:
            purple_saber(value1, name)
            
        # If user picks yellow
        elif answer in e:
            yellow_saber(value1, name)
            
        # If user picks orange
        elif answer in f:
            orange_saber(value1, name)
            
        # If user picks cyan
        elif answer in g:
            cyan_saber(value1, name)
            
        # If user picks magenta
        elif answer in h:
            magenta_saber(value1, name)
        
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the color menu
        else:
            print(random.choice(alternate_response))
            lightsaber_color(value1, name)
            

def red_saber(value1, name):
    """Function for a red lightsaber

	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	saber_value : answer
		Answer is stored in variable
	emitter : True
		Function called is true.
	"""
    
    print("Are you sure you want a red lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks "yes", stores red as lightsaber color
        if answer in yes:
            saber_value = "red"
            print(saber_value + "'s a good choice!")
            print("Let's move into customizing your blade.\n")
            emitter(value1, name, saber_value)
            
        # If user selects "no", goes back to color selection function
        elif answer in no:
            print("Okay, going back to the color selection screen...\n")
            lightsaber_color(value1, name)
            
        # Code stops running if user types "quit"
        elif answer in quit:
                print(random.choice(exit))
                break
                
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            red_saber(value1, name)
            
        
def blue_saber(value1, name):
    """Function for a blue lightsaber
	
	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	saber_value : answer
		Answer is stored in a variable
	emitter : True
		Function called is true.
	"""
    
    print("Are you sure you want a blue lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks "yes", stores red as lightsaber color
        if answer in yes:
            saber_value = "blue"
            print(saber_value + "'s a good choice!")
            print("\nLet's move into customizing your blade.")
            emitter(value1, name, saber_value)
            
        # If user selects "no", goes back to color selection function
        elif answer in no:
            print("Okay, going back to the color selection screen...\n")
            lightsaber_color(value1, name)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu
        else:
            print(random.choice(alternate_response))
            blue_saber(value1, name)

            
def green_saber(value1, name):
    """Function for a green lightsaber

	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	saber_value : answer
		Answer is stored in a variable
	emitter : True
		Function called is true.
	"""
    
    print("Are you sure you want a green lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks "yes", stores green as lightsaber color
        if answer in yes:
            saber_value = "green"
            print(saber_value + "'s a good choice!")
            print("\nLet's move into customizing your blade.")
            emitter(value1, name, saber_value)
            
        # If user selects "no", goes back to color selection function
        elif answer in no:
            print("Okay, going back to the color selection screen...\n")
            lightsaber_color(value1, name)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            green_saber(value1, name)
        
        
def purple_saber(value1, name):
    """Function for a purple lightsaber

	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	saber_value : answer
		Answer is stored in a variable
	emitter : True
		Function called is true.
	"""
    
    print("Are you sure you want a purple lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks "yes", stores purple as lightsaber color
        if answer in yes:
            saber_value = "purple"
            print(saber_value + "'s a good choice!")
            print("\nLet's move into customizing your blade.")
            emitter(value1, name, saber_value)
            
        # If user selects "no", goes back to color selection function
        elif answer in no:
            print("Okay, going back to the color selection screen...\n")
            lightsaber_color(value1, name)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            purple_saber(value1, name)
            

def yellow_saber(value1, name):
    """Function for a yellow lightsaber

	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	saber_value : answer
		Answer is stored in a variable
	emitter : True
		Function called is true.
	"""
    
    print("Are you sure you want a yellow lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks "yes", stores yellow as lightsaber color
        if answer in yes:
            saber_value = "yellow"
            print(saber_value + "'s a good choice!")
            print("\nLet's move into customizing your blade.")
            emitter(value1, name, saber_value)
        
        # If user selects "no", goes back to color selection function
        elif answer in no:
            print("Okay, going back to the color selection screen...\n")
            lightsaber_color(value1, name)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            yellow_saber(value1, name)
            

def orange_saber(value1, name):
    """Function for a orange lightsaber

	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	saber_value : answer
		Answer is stored in a variable
	emitter : True
		Function called is true.
	"""
    
    print("Are you sure you want an orange lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks "yes", stores orange as lightsaber color
        if answer in yes:
            saber_value = "orange"
            print(saber_value + "'s a good choice!")
            print("\nLet's move into customizing your blade.")
            emitter(value1, name, saber_value)
            
        # If user selects "no", goes back to color selection function
        elif answer in no:
            print("Okay, going back to the color selection screen...\n")
            lightsaber_color(value1, name)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            orange_saber(value1, name)
            
        
def cyan_saber(value1, name):
    """Function for a cyan lightsaber

	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	saber_value : answer
		Answer is stored in a variable
	emitter : True
		Function called is true.
	"""
    
    print("Are you sure you want a cyan lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks "yes", stores cyan as lightsaber color
        if answer in yes:
            saber_value = "cyan"
            print(saber_value + "'s a good choice!")
            print("\nLet's move into customizing your blade.")
            emitter(value1, name, saber_value)
            
        # If user selects "no", goes back to color selection function
        elif answer in no:
            print("Okay, going back to the color selection screen...\n")
            lightsaber_color(value1, name)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            cyan_saber(value1, name)
        
        
def magenta_saber(value1, name):
    """Function for a magenta lightsaber
	
	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	saber_value : answer
		Answer is stored in a variable
	emitter : True
		Function called is true.
	"""
    
    print("Are you sure you want a magenta lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user picks "yes", stores magenta as lightsaber color
        if answer in yes:
            saber_value = "magenta"
            print(saber_value + "'s a good choice!")
            print("\nLet's move into customizing your blade.")
            emitter(value1, name, saber_value)
            
        # If user selects "no", goes back to color selection function
        elif answer in no:
            print("Okay, going back to the color selection screen...\n")
            lightsaber_color(value1, name)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            magenta_saber(value1, name)
            

def emitter(value1, name, saber_value):
    """Function to create an emitter for a lightsaber

	Parameters
	---------
	answer : input
		When prompted to type, the user types an answer
	
	Returns
	-------
	duty_resolve_emitter : True
	magus_emitter : True
	peace_justice_emitter : True
	valor_wisdom_emitter : True
	power_control_emitter : True
	elemental_nature_emitter : True
		All emitter functions are True when called.
	"""
    
    print("An emitter converts a lightsaber's beam energy into a blade of"
          + " plasma.")
    print("It's integral for your saber.")
    print("Please select the emitter for you saber: ")
    
    # Displays a menu of emitters for selection 
    emitter_menu()
    
    answer = input()
    
    # Local variables
    a = ["A", "a"]
    b = ["B", "b"]
    c = ["C", "c"]
    d = ["D", "d"]
    e = ["E", "e"]
    f = ["F", "f"]
    
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If answer picks the duty and resolve emitter, calls that function
        if answer in a:
            duty_resolve_emitter(value1, name, saber_value)
            
        # If answer picks the magus emitter, calls that function
        elif answer in b:
            magus_emitter(value1, name, saber_value)
            
        # If answer picks the peace and justice emitter, calls that function
        elif answer in c:
            peace_justice_emitter(value1, name, saber_value)
            
        # If answer picks the valor and wisdom emitter, calls that function
        elif answer in d:
            valor_wisdom_emitter(value1, name, saber_value)
            
        # If answer picks the power and control emitter, calls that function
        elif answer in e:
            power_control_emitter(value1, name, saber_value)
            
        # If answer picks the elemental nature emitter, calls that function
        elif answer in f:
            elemental_nature_emitter(value1, name, saber_value)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the emitter menu 
        else:
            print(random.choice(alternate_response))
            emitter(value1, name, saber_value)
        
        
def duty_resolve_emitter(value1, name, saber_value):
    """Function for duty and resolve emitter

	Parameters
	---------
	calls function

	Returns
	-------
	emitter : answer
		Value of answer is stored in emitter
	saber_blade : True
		Function called is true.
	"""
    
    # Stores duty and resolve emitter as emitter value
    emitter = "duty and resolve"
    print("Equiped the " + emitter + " emitter!\n")
    saber_blade(value1, name, saber_value, emitter)
    
    
def magus_emitter(value1, name, saber_value):
    """Function for magus emitter

	Parameters
	---------
	calls function

	Returns
	-------
	emitter : answer
		Value of answer is stored in emitter
	saber_blade : True
		Function called is true.
	"""
    
    # Stores magus emitter as emitter value
    emitter = "magus"
    print("Equiped the " + emitter + " emitter!\n")
    saber_blade(value1, name, saber_value, emitter)
    
    
def peace_justice_emitter(value1, name, saber_value):
    """Function for peace and justice emitter

	Parameters
	---------
	calls function

	Returns
	-------
	emitter : answer
		Value of answer is stored in emitter
	saber_blade : True
		Function called is true.
	"""
    
    # Stores peace and justice emitter as emitter value
    emitter = "peace and justice"
    print("Equiped the " + emitter + " emitter!\n")
    saber_blade(value1, name, saber_value, emitter)
    
    
def valor_wisdom_emitter(value1, name, saber_value):
    """Function for valor and wisdom emitter

	Parameters
	---------
	calls function

	Returns
	-------
	emitter : answer
		Value of answer is stored in emitter
	saber_blade : True
		Function called is true.
	"""
    
    # Stores valor and wisdom emitter as emitter value
    emitter = "valor and wisdom"
    print("Equiped the " + emitter + " emitter!\n")
    saber_blade(value1, name, saber_value, emitter)
    
    
def power_control_emitter(value1, name, saber_value):
    """Function for power and control emitter

	Parameters
	---------
	calls function

	Returns
	-------
	emitter : answer
		Value of answer is stored in emitter
	saber_blade : True
		Function called is true.
	"""
    
    # Stores power and control emitter as emitter value
    emitter = "power and control"
    print("Equiped the " + emitter + " emitter!\n")
    saber_blade(value1, name, saber_value, emitter)
    
    
def elemental_nature_emitter(value1, name, saber_value):
    """Function for elemental nature emitter

	Parameters
	---------
	calls function

	Returns
	-------
	emitter : answer
		Value of answer is stored in emitter
	saber_blade : True
		Function called is true.
	"""
    
    # Stores elemental nature emitter as emitter value
    emitter = "elemental nature"
    print("Equiped the " + emitter + " emitter!\n")
    saber_blade(value1, name, saber_value, emitter)
    
    
def saber_blade(value1, name, saber_value, emitter):
    """Function for the type of saber blade

	Parameters
	---------
	answer : input
		Input entered is stored as answer
	local variables : True
		If variables are true, continue with code

	Returns
	-------
	single_blade : True
	double_blade : True
	two_blades : True
	curved_blade : True
		Functions called are all true.
	"""
    
    print("What lightsaber option would you like to weild?")
    
    # Displays menu for saber options
    saber_menu()
    
    answer = input()
    
    # Local variables
    single = ['A', 'a']
    double = ['B', 'b']
    two = ['C', 'c']
    curved = ['D', 'd']
    
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user selects "single", calls single blade function
        if answer in single:
            single_blade(value1, name, saber_value, emitter)
            
        # If user selects "double", calls double-blade function
        elif answer in double:
            double_blade(value1, name, saber_value, emitter)
            
        # If user selects "two", calls the two blades function
        elif answer in two:
            two_blades(value1, name, saber_value, emitter)
        
        # If user selects "curved", calls curved handle function
        elif answer in curved:
            curved_handle(value1, name, saber_value, emitter)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the saber menu
        else:
            print(random.choice(alternate_response))
            saber_blade(value1, name, saber_value, emitter)
            
            
def single_blade(value1, name, saber_value, emitter):
    """Function for a single blade saber

	Parameters
	---------
	answer : input
		Input entered is stored as answer
	global variables : True
		If global variables entered, code continues
	
	Returns
	-------
	blade : answer
		Answer stored in variable
	droid : True
		Function called in true.
	"""
    
    print("Do you want to weild a single lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user selects "yes", stores saber value as being a single saber
        if answer in yes:
            print("A noble choice.")
            blade = "single saber"
            droid(value1, name, saber_value, emitter, blade)
        
        # If user selects "no", goes back to initial saber function
        elif answer in no:
            print("Alright, sounds good.")
            saber_blade(value1, name, saber_value, emitter)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
        
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            single_blade(value1, name, saber_value, emitter)
            
            
def double_blade(value1, name, saber_value, emitter):
    """Function for a double-bladed saber

	Parameters
	---------
	answer : input
		Input entered is stored as answer
	global variables : True
		If global variables entered, code continues
	
	Returns
	-------
	blade : answer
		Answer stored in variable
	droid : True
		Function called in true.
	"""
    
    print("Do you want to weild a double-bladed lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user selects "yes", stores saber value as being a double-bladed saber
        if answer in yes:
            print("Modeling your blade after Darth Maul, I see.")
            blade = "double-bladed"
            droid(value1, name, saber_value, emitter, blade)
            
         # If user selects "no", goes back to initial saber function
        elif answer in no:
            print("Alright, sounds good.")
            saber_blade(value1, name, saber_value, emitter)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            double_bladed(value1, name, saber_value, emitter)
            

def two_blades(value1, name, saber_value, emitter):
    """Function for two sabers
	
	Parameters
	---------
	answer : input
		Input entered is stored as answer
	global variables : True
		If global variables entered, code continues
	
	Returns
	-------
	blade : answer
		Answer stored in variable
	droid : True
		Function called in true.
	"""
    
    print("Do you want to weild two lightsabers?")
    
    # Displays "yes" or "no" menu
    question_menu()

    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user selects "yes", stores saber value as being two sabers
        if answer in yes:
            print("Modeling your blade after Ahsoka Tano, I see.")
            blade = "two saber"
            droid(value1, name, saber_value, emitter, blade)
            
         # If user selects "no", goes back to initial saber function
        elif answer in no:
            print("Alright, sounds good.")
            saber_blade(value1, name, saber_value, emitter)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            two_blades(value1, name, saber_value, emitter)
            
            
def curved_handle(value1, name, saber_value, emitter):
    """Function for a curved-blade saber

	Parameters
	---------
	answer : input
		Input entered is stored as answer
	global variables : True
		If global variables entered, code continues
	
	Returns
	-------
	blade : answer
		Answer stored in variable
	droid : True
		Function called in true.
	"""
    
    print("Do you want to weild a curved-handle lightsaber? ")
    
    # Displays "yes" or "no" menu
    question_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    for answer in response:
        
        # If user selects "yes", stores saber value as being a curved-handled saber
        if answer in yes:
            print("Modeling after Count Dooku, I see.")
            blade = "curved-handle"
            droid(value1, name, saber_value, emitter, blade)
            
         # If user selects "no", goes back to initial saber function
        elif answer in no:
            print("Alright, sounds good.\n")
            saber_blade(value1, name, saber_value, emitter)
            
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
            
        # Alternate response for an option not provided in the question menu 
        else:
            print(random.choice(alternate_response))
            curved_handle(value1, name, saber_value, emitter)
            
            
def droid(value1, name, saber_value, emitter, blade):
    """Function to create a droid companion

	Parameters
	---------
	answer : input
		Input entered is stored as answer
	local variables : True
		If local variables entered, code continues
	
	Returns
	-------
	droid : answer
		Answer stored in variable
	finish : True
		Function called in true."""
    
    print("It's time to pick your droid companion.")
    print("\nPlease select your droid: ")
    
    # Displays droid menu
    droid_menu()
    
    answer = input()
    response = []
    response.append(answer)
    
    # Local variables
    rtwo = ['A', 'a']
    rfour = ['B', 'b']
    bb = ['C', 'c']
    probe = ['D', 'd']
    protocol = ['E', 'e']
    
    for answer in response:
        
        # If user selects R2, stores value of R2 into droid variable
        if answer in rtwo:
            droid = "R2 unit"
            print("You've added an " + droid + " to the family!")
            finish(value1, name, blade, saber_value, emitter, droid)
                
        # If user selects R4, stores value of R4 into droid variable
        elif answer in rfour:
            droid = "R4 unit"
            print("You've added an " + droid + " to the family!")
            finish(value1, name, blade, saber_value, emitter, droid)
                
        # If user selects BB, stores value of BB into droid variable
        elif answer in bb:
            droid = "BB unit"
            print("You've added a " + droid + " to the family!")
            finish(value1, name, blade, saber_value, emitter, droid)
                
        # If user selects Probe droid, stores value of probe droid into droid variable
        elif answer in probe:
            droid = "probe droid"
            print("You've added a " + droid + " to the family!")
            finish(value1, name, blade, saber_value, emitter, droid)
            
        # If user selects Human protocol droid, stores value of human protocol droid into droid variable
        elif answer in protocol:
            droid = "human protocol droid"
            print("You've added a " + droid + " to the family!")
            finish(value1, name, blade, saber_value, emitter, droid)
                
        # Code stops running if user types "quit"
        elif answer in quit:
            print(random.choice(exit))
            break
        
        # Alternate response for an option not provided in the droid menu 
        else:
            print(random.choice(alternate_response))
            droid(value1, name, saber_value, emitter, blade)
            
            
def finish(value1, name, blade, saber_value, emitter, droid):
    """Function to combine all the stored variables together into one final output

	Parameters
	---------
	stored variables need to be successful
	
	Returns
	-------
	prints final statement
	
    
    print("\n\nYou have successfully customized a Star Wars character!")
    print("Generated character: " + value1 + " " + name + " who weilds a " 
         + blade + " " + saber_value + " lightsaber with a "
         + emitter + " emitter, and a " + droid + " companion.")
    
    
def question_menu():
    """Function that displays a 'yes' or 'no' menu"""
    
    print("a) Yes\nb) No")

    
def side_menu():
    """Function that displays a menu for the 'light side' or the 'dark side' option"""
    
    print("a) Light Side\nb) Dark Side")
    
    
def color_menu():
    """Function that displays a menu for color options for lightsabers"""
    
    print("a) Red\nb) Blue\nc) Green\nd) Purple\ne) Yellow\nf) Orange\ng)" 
          + " Cyan\nh) Magenta")

    
def emitter_menu():
    """Function that displays a menu for emitter options for lightsabers"""
    
    print("a) Duty and Resolve\nb) Magus\nc) Peace and Justice\nd) Valor"
          + " and Wisdom\ne) Power and Control\nf) Elemental Nature")
    
    
def droid_menu():
    """Function that displays a menu for droid-companion options"""
    
    print("a) R2 Unit\nb) R4 Unit\nc) BB Unit\nd) Probe Droid\ne) Human"
          + " Protocol Droid")
    
    
def saber_menu():
    """Function that displays a menu for lightsaber type options"""
    
    print("a) Single blade saber\nb) Double-bladed saber\nc) Two blades"
          + " saber\nd) Curved-handle saber")



star_wars()

