
from os import system
from random import randint

gametitle='Castle Dungeons'
system("mode 110,30")
system("title "+gametitle)

def cls():
    system('cls')

character_name=None
character_class=None
character_race=None
character_magic=None
character_dexterity=None
character_life=None
character_strength=None

cls()
print("Castle Dungeons")

def intro():
    print("")
    print("In this adventure, you are the hero!")
    print("Your choices,skills,and a bit of luck,will influence the outcome of the game.")
    print("")
    print("An evil sorcerer is holding your fellow adventurers prisoners.")
    print("Will you succeed in rescuing your friends from the castle dungeons, or peril trying?")
    print("")
    input("Press Enter to start...")

intro()

def create_character():
    cls()
    global character_name
    character_name=input("""
        Let's begin by creating your character.
        What is your character name?
        
        > """)
    global character_race
    while character_race is None:
        race_choice=input("""
            Choose your character race from the list below by entering the relevant number:
            1  Elf
            2  Dwarf
        
            > """)
    
        if race_choice=='1':
            character_race='Elf'
        elif race_choice=='2':
            character_race='Dwarf'
        else:
            print("invalid choice, try again")
    global character_class
    while character_class is None:
        class_choice=input("""
            Choose your character class from the list below by entering the relevant number:
            1  Warrior
            2  Wizzard
        
            > """)
        if class_choice=='1':
            character_class='Warrior'
        elif class_choice=='2':
                character_class='Wizard'
        else:
            print("invalid choice, try again")
            
create_character()

def create_character_skillsheet():
    cls()
    global character_name,character_class,character_race,character_life,character_dexterity,character_strength,character_magic
    print("""
    Now, let's determine your character's skills, which you will use throughout the game.
    In this game, your character has four skills:
    
    - Strength, which you will use in combat or any strength test
    - Dexterity, which you will use in any ability test
    - Magic, which you will use whenever you need to cast a spell or use/inspect a magical item or place
    - Life, which determines your life energy, points will be lost when hurt, 
      and whenever life reaches 0, your character dies.
      
      
      Depending on your race and class, you will have a certain point-base already calculated by the game.
      You will shortly be able to increase your skills by rolling a 6-face dice.
      
      Here is your base Character Skills Sheet:
      """)
    character_strength=5
    character_magic=0
    character_dexterity=3
    character_life=10
    
    if character_race=='Elf':
        character_strength=character_strength+3
        character_magic=character_magic+6
        character_dexterity=character_dexterity+4
        character_life=character_life+2
    elif character_race=='Dwarf':
        character_strength=character_strength+5
        character_life=character_life+4
    if character_class=='Wizard':
        character_magic=character_magic+4
    elif character_class=='Warrior':
        character_strength=character_strength+3
        character_life=character_life+3
    print("""
      Name: """ +character_name+
      """
      Race: """ +character_race+
      """
      Class: """ +character_class+
      """
    
      Strength: """ +str(character_strength)+
      """
      Dexterity: """ +str(character_dexterity)+
      """
      Magic: """ +str(character_magic)+
      """
      Life: """ +str(character_life)+"""
    
      """)
    input("Press Enter to apply skill modifiers")
        
create_character_skillsheet()

def modify_skills():
    cls()
    global character_dexterity,character_strength,character_life
    print("To modify yout skllls, roll a dice for each of your skills,and the game will add that number to your skills.")
    input('Press Enter to roll for Strength')
    roll=randint(1,6)
    print("You rolled > "+str(roll))
    character_strength=character_strength+roll
    input('Press Enter to roll for Dexterity')
    roll=randint(1,6)
    print("You rolled > "+str(roll))
    character_dexterity=character_dexterity+roll
    input('Press Enter to roll for Life')
    roll=randint(1,6)
    print("You rolled > "+str(roll))
    character_life=character_life+roll
    input('Press Enter to continue...')
    cls()
    print("""
    Congratulations! You have completed your character creation.
    Your final character sheet is:
    
      Name: """ +character_name+
      """
      Race: """ +character_race+
      """
      Class: """ +character_class+
      """
    
      Strength: """ +str(character_strength)+
      """
      Dexterity: """ +str(character_dexterity)+
      """
      Magic: """ +str(character_magic)+
      """
      Life: """ +str(character_life)+"""
    
      """)
    input('Press Enter to begin your adventure, if you dare..')

modify_skills()

def scene1():
    cls()
    choice=None
    while choice is None:
        user_input=input("""
        You have entered the Castle Dungeons..
        It is dark, however thankfully your torch is lit and you can see upto 2o feet away from you.
        The stone walls are damp, the smell of rats and orcs is strong.
        You walk down a narrow corridor, until you reach a thick strong wall.
        
        The corridor continues on the left, and on the right.
        
        What do you do?
        
        1. Turn left
        2. Turn right
        > """)
        if user_input=='1':
            choice='1'
            scene2()
        elif user_input=='2':
            choice=2
            scene3()
        else:
            print('Invalid! Type a number..')
        
def scene2():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    From the darkness behind you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input=="1":
            choice="1"
            combat()
        elif user_input=="2":
            choice="2"
            skill_check()
        else:
            print("""
            Invalid choice! type a number.."
            """)

def scene3():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    From the darkness ahead of you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input=="1":
            choice="1"
            combat()
        elif user_input=="2":
            choice="2"
            skill_check()
        else:
            print("""
            Not a valid choice, type a number..
            """)
    
def skill_check():
    cls()
    print('A giant rock falls from the ceiling, roll a die if you can dodge it...or you get smashed')
    roll=randint(1,6)
    print('You rolled > '+ str(roll))
    if roll+character_dexterity>10:
        print("""
            You dodged the rock and survived! Danger is not over yet..
            The strange noise in the darkness continues and it feels a lot closer now..""")
        input('Press Enter to continue...')
        combat()
    else:
        print('You got crushed by the rock..You die. The game is over')
        input('Press Enter to exit')
    
def combat():
    cls()
    global character_life
    print("A horrible orc attacks you...")
    input("""
    Press Enter to fight...
    """)
    orc_strength=10
    orc_life=14
    while orc_life>0 and character_life>0:
        char_roll=randint(1,6)
        print("You rolled > "+str(char_roll))
        monst_roll=randint(1,6)
        print("Monster rolled > " + str(monst_roll))
        if character_strength+char_roll>=monst_roll+orc_strength:
            print("You hit the monster!!")
            orc_life=orc_life-randint(1,6)
        else:
            print("Monster hit you")
            character_life=character_life-randint(1,6)
    if character_life>0:
        print("Congrats! You defeated the monster. You succeeded in rescuing your friends.")
        input("Press Enter to exit")
    else:
        print("The Monster defeated you.You are dead.You failed to rescue your friends.")
        input("Press Enter to exit")
    
scene1()
    


# In[ ]:




