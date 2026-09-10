main_version = "v2.0.0"
import random
from time import sleep
import loader
import os
import subprocess
import sys
import numbers as num

Name = "Edward"
difficulty = 5
dice_roll = 0
current_scene = 1
update_available = False
suported_updater = "v1.0.0"
Character_stats = {"HP": None,
            "EP": None,
            "Strength": None,
            "Constitution": None,
            "Dexterity": None,
            "Wisdom": None,
            "Intelligence": None,
            "Charisma": None,
            "Backstory": "You are the Story to be told"
}
Character_profiles = {}
story = {}
title = "no Game loaded"
game_version = "v0.0"
ui_wait_time = 1.5

repl_man = """
Updater Instructions
====================

1. Download the latest "updater.py" from GitHub:

   https://github.com/Emil-das-rosa-Einhorn/PaP-Text/blob/main/updater.py

2. Open the location of your current "updater.py".

3. Replace the old "updater.py" with the newly downloaded version.

4. If you are not sure where the file is located, check the path printed in the console.

5. Make sure the downloaded file is named exactly:

   updater.py

6. Restart the application after replacing the file.

Note:
The updater should not be replaced while it is currently running.
"""

def check_updater():
    global update_available
    outofdate = []
    check, update_info = loader.load_update_info()
    cur_l_version = loader.get_version()
    cur_m_version = main_version
    r = False
    try:
        if cur_l_version != update_info["loader"]["version"]:
            r = True
            outofdate.append("loader")
        else:
            pass

        if cur_m_version != update_info["main"]["version"]:
            r = True
            outofdate.append("main")
        else:
            pass

        if update_info["updater"]["version"] != suported_updater:
            r = True
            outofdate.append("updater")

        if r:
            update_available = True
            return True, outofdate
        else:
            update_available = False
            return False, outofdate
        
    except Exception as e:
        return False, outofdate


def lounch_updater (outofdate):
    loader_up = "False"
    main_up = "False"
    for skript in outofdate:
        if skript == "loader":
            loader_up = "True"
        elif skript == "main":
            main_up = "True"

    with open("updater.log", "w", encoding="utf-8") as log:
        subprocess.Popen(
            [
                sys.executable,
                "updater.py",
                loader_up,
                main_up
            ],
            stdout=log,
            stderr=log,
            stdin=subprocess.DEVNULL
        )
    sys.exit(0)

def download_game (filename):
    global story, Character_profiles, title, game_version
    loader.download_gamefile(filename)
    gamedata = loader.load_gamefile()
    story = gamedata["content"]
    Character_profiles = gamedata["Character_profiles"]
    title = gamedata["titel"]
    game_version = gamedata["version"] 

def load_game_local ():
    global story, Character_profiles, title, game_version
    gamedata = loader.load_gamefile()
    if gamedata == None:
        print("no Game is stored. Please select a file to Download")
        return False
    else:
        story = gamedata["content"]
        Character_profiles = gamedata["Character_profiles"]
        title = gamedata["titel"]
        game_version = gamedata["version"]

        return True


def squid_say(squid_say):
    os.system("cls" if os.name == "nt" else "clear")
    os.system('')
    print("\033[2J\033[?25l", end="")
    move_set = [[0,0,1,1,3,0,0,1,1,2,2,2,0,0,0],
                [0,1,1,0,0,0,0,3,3,1,1,0,3,0,0],
                [0,0,2,2,3,0,1,1,0,0,0,0,1,1,0],
                [0,0,1,1,3,0,1,1,0,2,1,1,0,0,1],
                [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0]]
    move = random.choice(move_set)
    for i in move:
        if i == 1:
            print(f"\033[H{num.num(25,squid_say)}")
        elif i == 2:
            print(f"\033[H{num.num(26,squid_say)}")
        elif i == 3:
            print(f"\033[H{num.num(27,squid_say)}")
        else:
            print(f"\033[H{num.num(24,squid_say)}")
        sleep (0.2)
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[?25h")

def dice_animation(sides,result):
    os.system("cls" if os.name == "nt" else "clear")
    os.system('')
    print("\033[2J\033[?25l", end="")
    time = 0.05
    multi = 1.15
    wait = 0.9
    last_num = 0
    for i in range(5):
        number = random.randint(1, sides)
        if number == last_num:
            number =+ 1
        else:
            pass
        if number > sides:
            number = 1
        print(f"\33[H{num.num(number)}")
        sleep (time)
        print("\033[2J\033[H", end="")
    numb_all = list(range(1, sides + 1))
    wight_result= 6
    for i in range(20):
        wights = [wight_result if z == result else 1 for z in numb_all]
        number = random.choices(numb_all, weights=wights, k=1)[0]
        if number == last_num:
            number =+ 1
        else:
            pass
        if number > sides:
            number = 1
        print(f"\33[H{num.num(number)}")
        sleep (time)
        print("\033[2J\033[H", end="")
        time = time * multi
        number = last_num
    print(f"\33[H{num.num(result)}")
    sleep (time)

    os.system("cls" if os.name == "nt" else "clear")
    print ("You rolled a...")
    sleep (wait)
    for _ in range(3):
        print(f"\33[H{num.num(result)}")
        sleep (wait)
        os.system("cls" if os.name == "nt" else "clear")
        sleep (wait)
    print("\033[?25h")



def roll_dice(sides=6):
    if sides > 20:
        sides = 20
    result = random.randint(1, sides)
    dice_animation(sides, result)
    return result

def say (type):
    if type == "thinking":
        say = ["Let me think about that...",
               "Hmm, that's a tough one...",
               "I need to consider my options...",
               "This is a difficult decision...",
               "I need to weigh the pros and cons..."]
    elif type == "success":
        say = ["Great choice!",
               "That was a smart move!",
               "You made the right decision!",
               "Well done!",
               "Excellent choice!"]
    elif type == "failure":
        say = ["Oh no, that didn't work out.",
               "That was a risky move.",
               "Unfortunately, that didn't go as planned.",
               "Better luck next time.",
               "That choice didn't pay off."]
    elif type == "name":
        say = ["Thats a great name!",
                "hmm, I like that name.",
                "Interesting choice for a name.",
                "I wouldn't choose that name if I were you... but it could work.",
                "OK, I guess that name will do."]
    elif type == "dice_low":
        say = ["Oh no, that dosen't look good.",
                "hmm, i hope that works out for you.",
                "This might be a tough situation.",
                "Wow, that is a low roll. Good luck!",
                "it dons't go way lower than that, but it could be worse."]
    elif type == "dice_high":
        say = ["WOW, that is a high roll!",
                "keep it up, you are doing great!",
                "...This is a fantastic roll!",
                "Now this is what I call a lucky roll!",
                "You are on a roll!"]
    elif type == "dice_mid":
        say = ["That's a decent roll.",
                "Not bad!",
                "Could be better, but not terrible.",
                "A solid performance.",
                "You're doing alright.",
                "it could be worse!"]
    elif type == "dice_krit_suc":
        say = ["WOW, that is a critical success!",
                "Wow what a lucky roll!",
                "As high as it gets! This is a fantastic roll!",
                "Oh great, I wish I could roll like that!",
                "Kritical success!",
                "It couldn't go much better!"]
    elif type == "dice_krit_fail":
        say = ["Oh not good, really not good.",
                "this is a fail!",
                "Oh no, that didn't work out.",
                "That was risky and it didn't pay off.",
                "This is a tough situation.",
                "Better luck next time."]
    elif type == "END_suc":
        say = ["Oh Wow, that was a great outcome!",
                "You made the right decisions!",
                "i hope you have the same luck next time!"]
    elif type == "END_fail":
        say = ["Oh no, what a terible outcome!",
                "You put your hopes on your not existing luck!",
                "That was a skill issue, i would say!"]
    elif type == "END_mid":
        say = ["That could have gone better. But also much worse.",
                "Well, that was a ride. For the future, may try thinking, befor moving.",
                "You made some good choices, but also some questionable ones. But you got yourself out of the situation, so that's something."]
    else:
        say = ["I'm not sure what to say."]
    msg = "DM: " + random.choice(say)
    return msg

def thinking_time(say_type=None):
    os.system("cls" if os.name == "nt" else "clear")
    print (" ")
    print (" ")
    print ("=" * 50)
    print (say (say_type))
    for i in range(3):
        dot = "." * (i + 1)
        print(dot)
        WT = random.randint(8, 15) / 10
        sleep(ui_wait_time/3)
    os.system("cls" if os.name == "nt" else "clear")

header = f"""
===============================================
=======  Pen and Paper Solo Adventures  =======
===============================================
===================  Menu  ====================
"""

footer ="""
===============================================
    """

def menu_F():
    check, outofdate = check_updater()
    if check:
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            for skript in outofdate:
                if skript == "updater":
                    path = os.path.join(os.path.dirname(__file__))
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print ("Your Update Skript is not up to date!")
                        print ("-"*50)
                        print (f"Please manualy Update your updater.py skript in the folowing folder: {path}")
                        print ("-"*50)
                        print ("A: Manual for the Update")
                        print ("B: Update now")
                        print ("C: Exit [not recommended]")
                        choice = input ("Please chose an Option: ").upper()
                        if choice == "A":
                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print(f"path of the file: {path}")
                                print (repl_man)
                                print ("-"*50)
                                print ("A: Update now")
                                print ("B: Exit")
                                print ("-"*50)
                                choice = input ("Please chose an Option: ").upper()
                                if choice == "A":
                                    os.system("cls" if os.name == "nt" else "clear")
                                    print ("Game will be closed...")
                                    sleep(ui_wait_time)
                                    sys.exit(0)
                                elif choice == "B":
                                    break
                                else:
                                    print("choose a valid option")
                                    sleep(ui_wait_time)
                        elif choice == "B":
                            os.system("cls" if os.name == "nt" else "clear")
                            print ("Game will be closed...")
                            sleep(ui_wait_time)
                            sys.exit(0)
                        elif choice == "C":
                            while True:
                                os.system("cls" if os.name == "nt" else "clear")
                                print ("By not updating the skript, you run the rist of corrupting your game and or gamefiles")
                                sleep(ui_wait_time)
                                choice = input ("Type 'Yes' to continue or 'No' to Update Manualy: ")
                                if choice == "Yes":
                                    return
                                elif choice == "No":
                                    break
                                else:
                                    print ("choose valid option")
                                    sleep (ui_wait_time)


            print ("There is a new Update")
            print (f"This files will be Updated: {outofdate}")
            print ("-"*50)
            print ("A: Update Game")
            print ("B: Exit")
            print ("-"*50)
            choice = input ("Please chose an Option: ").upper()
            if choice == "A":
                lounch_updater(outofdate)
                break
            elif choice == "B":
                break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print ("Please choose a valid option")
                sleep (ui_wait_time)
        os.system("cls" if os.name == "nt" else "clear")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print ("You are Up to date!")
        sleep(ui_wait_time)
        os.system("cls" if os.name == "nt" else "clear")

def menu ():
    while True:
        if update_available:
            uda = "[new Update]"
        else:
            uda = ""
        os.system("cls" if os.name == "nt" else "clear")
        print (header)
        print (f"Geladener Titel: {title} | Version: {game_version}")
        print ("-"*50)
        print ("A: Load game")
        print ("B: Download game")
        print ("C: Choose Character")
        print ("D: Choose difficulty level")
        print ("E: Play")
        print (f"F: Check Update {uda}")
        print ("G: Select Chapters")
        print ("To Quit the Game, please press strg + C")
        print (footer)
        choice = input ("Please chose an Option: ").upper()
        os.system("cls" if os.name == "nt" else "clear")
        if choice == "A":
            if load_game_local():
                print ("succsesfuly loaded")
                sleep(ui_wait_time)
            else:
                print ("unable to load")
                sleep(ui_wait_time)
        elif choice == "B":
            menu_B()
        elif choice == "C":
            if Character_profiles == {}:
                print ("Please load a Game first!")
                sleep (ui_wait_time)
                os.system("cls" if os.name == "nt" else "clear")
            else:
                menu_C()
        elif choice == "D":
            while True:
                global difficulty
                print (header)
                print (f"Please Input the Difficulty Level you want to Play at [currently: {difficulty}]")
                print ("1 - 3: Easy | 4 - 7: Mid | 8 - 10: Hard")
                inp = input ("Difficulty Level: ")
                try:
                    difficulty = int(inp)
                    if difficulty < 1 or difficulty > 10:
                        os.system("cls" if os.name == "nt" else "clear")
                        print ("Input a hole Number form 1 to 10")
                        sleep(ui_wait_time)
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print (f"Difficulty Level was set to: {difficulty}")
                        sleep(ui_wait_time)
                        break
                except ValueError:
                    os.system("cls" if os.name == "nt" else "clear")
                    print ("Input a hole Number form 1 to 10")
                    sleep(ui_wait_time)
                os.system("cls" if os.name == "nt" else "clear")

        elif choice == "E":
            if story == {}:
                print ("please select a Game first")
                sleep(ui_wait_time)
                os.system("cls" if os.name == "nt" else "clear")
            else:
                break

        elif choice == "F":
            menu_F()

        elif choice == "G":
            while True:
                global current_scene
                chap_counter = 0
                for key in story:
                    chap_counter += 1
                if chap_counter == 0:
                    os.system("cls" if os.name == "nt" else "clear")
                    print (f"Please select a Game first")
                    sleep(ui_wait_time)
                    break
                print (f"Please select the Szene you whant to start with [currently: {current_scene}/{chap_counter}]")
                inp = input (f"Szene (1 - {chap_counter}): ")
                try:
                    inp_int = int(inp)
                    if 0 < inp_int <= chap_counter:
                        current_scene = inp_int
                        os.system("cls" if os.name == "nt" else "clear")
                        print (f"The Adventure will start at: {current_scene}")
                        sleep(ui_wait_time)
                        break
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print (f"Select a Szene between 1 and {chap_counter}")
                        sleep(ui_wait_time)
                except ValueError:
                    os.system("cls" if os.name == "nt" else "clear")
                    print ("Input a hole Numbers:")
                    sleep(ui_wait_time)
                os.system("cls" if os.name == "nt" else "clear")
        
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print ("Please choose a valid option")
            sleep (ui_wait_time)
            os.system("cls" if os.name == "nt" else "clear")

def menu_B():
    while True:
        print (header)
        gamelist = loader.check_gamelist()
        game_infos, game_version = loader.load_info()
        game_counter = 0
        for game in gamelist:
            print (f"Title: {game} | {game_version[game_counter]}")
            print (f"Info: {game_infos[game_counter]}")
            print ("-"*50)
            game_counter = game_counter + 1
        print ("Press E to go back to the Menu")
        print (footer)
        filename = input ("Please type in the Game you want to Play: ")
        if filename == "E" or filename == "e":
            break
        elif filename in gamelist:
            download_game(filename)
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print ("Please select one of the Games or press E to go back to the Menu")
            sleep(ui_wait_time)


        os.system("cls" if os.name == "nt" else "clear")

def menu_C():
    global Character_profiles, Character_stats, Name
    while True:
        print (header)
        print ("Loaded Profile")
        print ("-"*50)
        print (f"Name: {Name}")
        print (f"HP: {Character_stats["HP"]}")
        print (f"EP: {Character_stats["EP"]}")
        print (f"Strength: {Character_stats["Strength"]}")
        print (f"Constitution: {Character_stats["Constitution"]}")
        print (f"Dexterity: {Character_stats["Dexterity"]}")
        print (f"Wisdom: {Character_stats["Wisdom"]}")
        print (f"Intelligence: {Character_stats["Intelligence"]}")
        print (f"Charisma: {Character_stats["Charisma"]}")
        print (f"Backstory: {Character_stats["Backstory"]}")
        print ("-"*50)
        print ("A: Character Name")
        print ("B: Character Profile")
        print ("C: Exit")
        print (footer)
        choice = input ("Please chose an Option: ").upper()
        os.system("cls" if os.name == "nt" else "clear")
        if choice == "A":
            Name = input ("Please Typ in your Charakter Name: ")
            print (say("name"))
            sleep (ui_wait_time)
            os.system("cls" if os.name == "nt" else "clear")
        elif choice == "B":
            while True:
                print (header)
                print ("charakters")
                print ("-"*50)
                char_numbers = []
                for key in Character_profiles:
                    char_numbers.append(key)
                    print (f"Charakter {key}")
                    print (f"HP: {Character_profiles[key]["HP"]}")
                    print (f"EP: {Character_profiles[key]["EP"]}")
                    print (f"Strength: {Character_profiles[key]["Strength"]}")
                    print (f"Constitution: {Character_profiles[key]["Constitution"]}")
                    print (f"Dexterity: {Character_profiles[key]["Dexterity"]}")
                    print (f"Wisdom: {Character_profiles[key]["Wisdom"]}")
                    print (f"Intelligence: {Character_profiles[key]["Intelligence"]}")
                    print (f"Charisma: {Character_profiles[key]["Charisma"]}")
                    print (f"Backstory: {Character_profiles[key]["Backstory"]}")
                    print ("-"*50)
                print ("A: Chose a Character")
                print ("B: Random")
                print ("C: Exit")
                choice = input("Please select a Option: ").upper()
                os.system("cls" if os.name == "nt" else "clear")
                if choice == "A":
                    charakter = input("Chose your Character by typing in the Character Number: ")
                    if charakter in char_numbers:
                        load_in_character (charakter)
                        break
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print ("Invalid Choice!")
                        print ("Chose your Character by typing in the Character Number")
                        sleep (ui_wait_time)
                elif choice == "B":
                    charakter = random.choice(char_numbers)
                    load_in_character (charakter)
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                elif choice == "C":
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print ("Invalid Choice!")
                    print ("Chose your Character by typing in the Character Number")
                    sleep (ui_wait_time)

        elif choice == "C":
            break
        else:
            print ("Please select a Option")
            sleep (ui_wait_time)
            os.system("cls" if os.name == "nt" else "clear")

def load_in_character (charakter):
     Character_stats["HP"] = Character_profiles[charakter]["HP"]
     Character_stats["EP"] = Character_profiles[charakter]["EP"]
     Character_stats["Strength"] = Character_profiles[charakter]["Strength"]
     Character_stats["Constitution"] = Character_profiles[charakter]["Constitution"]
     Character_stats["Dexterity"] = Character_profiles[charakter]["Dexterity"]
     Character_stats["Wisdom"] = Character_profiles[charakter]["Wisdom"]
     Character_stats["Intelligence"] = Character_profiles[charakter]["Intelligence"]
     Character_stats["Charisma"] = Character_profiles[charakter]["Charisma"]
     Character_stats["Backstory"] = Character_profiles[charakter]["Backstory"]
    
def main():
    global current_scene
    try:
        while True:
            menu_F()
            while True:
                print ("Main Menu:")
                menu()
                input ("Press Enter to start the adventure...")
                break
            while True:
                try:
                    print (story[str(current_scene)]["plot"])
                    if story[str(current_scene)]["choices"]["A"][0] == "END":
                        print (story[str(current_scene)]["choices"]["A"][2])
                        print (" ")
                        print ("-"*50)
                        input ("press any key to continue or str + C to quit")
                        current_scene = 1
                        break
                    else:
                        print (" ")
                        print (" ")
                        print ("=" * 50)
                        for choice in story[str(current_scene)]["choices"]:
                            print(f"{choice}: {story[str(current_scene)]['choices'][choice][0]}")
                        while True:
                            print (" ")
                            user_choice = input("What do you choose? ").upper()
                            if user_choice in story[str(current_scene)]["choices"]:
                                current_scene = story[str(current_scene)]["choices"][user_choice][1]
                                break
                            else:
                                print("Invalid choice. Please choose again.")
                        thinking_time(say_type="thinking")
                except Exception as e:
                    print ("404: here is a lose End!")
                    print ("Please Inform your DM and try againe")
                    sleep(ui_wait_time)
                    break
    except KeyboardInterrupt:
            print("\nAdventure ended by user.")

if __name__ == "__main__":
    main()