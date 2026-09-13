import loader
import random

version = "v1.2.0"

def get_version():
     return version

def num(num, input_txt=None):
    if num > 23:
        num = 23
    numbers = [
    """
                ############                            
                ############                            
                ####    ####                            
                ####    ####                                    
                ####    ####                                            
                ####    ####                                            
                ####    ####                                            
                ####    ####                                            
                ############                                            
                ############                                            
    """,
    """
                    ####        
                    ####        
                    ####        
                    ####        
                    ####        
                    ####        
                    ####        
                    ####        
                    ####        
                    ####        
    """,
    """
                ############    
                ############    
                        ####    
                        ####    
                ############    
                ############    
                ####            
                ####            
                ############    
                ############    
    """,
    """
                ############    
                ############    
                        ####    
                        ####    
                ############    
                ############    
                        ####    
                        ####    
                ############    
                ############    
    """,
    """
                ####    ####    
                ####    ####    
                ####    ####    
                ####    ####    
                ############    
                ############    
                        ####    
                        ####    
                        ####    
                        ####    
    """,
    """
                ############    
                ############    
                ####            
                ####            
                ############    
                ############    
                        ####    
                        ####    
                ############    
                ############    
    """,
    """
                ############    
                ############    
                ####            
                ####            
                ############    
                ############    
                ####    ####    
                ####    ####    
                ############    
                ############    
    """,
    """
                ############    
                ############    
                        ####    
                        ####    
                        ####    
                        ####    
                        ####    
                        ####    
                        ####    
                        ####    
    """,
    """
                ############    
                ############    
                ####    ####    
                ####    ####    
                ############    
                ############    
                ####    ####    
                ####    ####    
                ############    
                ############    
    """,
    """
                ############    
                ############    
                ####    ####    
                ####    ####    
                ############    
                ############    
                        ####    
                        ####    
                ############    
                ############    
    """,
    """
            ####        ############    
            ####        ############    
            ####        ####    ####    
            ####        ####    ####    
            ####        ####    ####    
            ####        ####    ####    
            ####        ####    ####    
            ####        ####    ####    
            ####        ############    
            ####        ############    
    """,
    """
            ####            ####        
            ####            ####        
            ####            ####        
            ####            ####        
            ####            ####        
            ####            ####        
            ####            ####        
            ####            ####        
            ####            ####        
            ####            ####        
    """,
    """
            ####        ############    
            ####        ############    
            ####                ####    
            ####                ####    
            ####        ############    
            ####        ############    
            ####        ####            
            ####        ####            
            ####        ############    
            ####        ############    
    """,
    """
            ####        ############    
            ####        ############    
            ####                ####    
            ####                ####    
            ####        ############    
            ####        ############    
            ####                ####    
            ####                ####    
            ####        ############    
            ####        ############    
    """,        
    """ 
            ####        ####    ####    
            ####        ####    ####    
            ####        ####    ####    
            ####        ####    ####    
            ####        ############    
            ####        ############    
            ####                ####    
            ####                ####    
            ####                ####    
            ####                ####    
    """,
    """
            ####        ############    
            ####        ############    
            ####        ####            
            ####        ####            
            ####        ############            
            ####        ############    
            ####                ####    
            ####                ####    
            ####        ############    
            ####        ############    
    """,
    """
            ####        ############    
            ####        ############    
            ####        ####            
            ####        ####            
            ####        ############    
            ####        ############    
            ####        ####    ####    
            ####        ####    ####    
            ####        ############    
            ####        ############    
    """,
    """
            ####        ############    
            ####        ############    
            ####                ####    
            ####                ####    
            ####                ####    
            ####                ####    
            ####                ####    
            ####                ####    
            ####                ####    
            ####                ####    
    """,
    """
            ####        ############    
            ####        ############    
            ####        ####    ####    
            ####        ####    ####    
            ####        ############    
            ####        ############    
            ####        ####    ####    
            ####        ####    ####    
            ####        ############    
            ####        ############    
    """,
    """
            ####        ############    
            ####        ############    
            ####        ####    ####    
            ####        ####    ####    
            ####        ############    
            ####        ############    
            ####                ####    
            ####                ####    
            ####        ############    
            ####        ############    
    """,
    """
        ############    ############    
        ############    ############    
                ####    ####    ####    
                ####    ####    ####    
        ############    ####    ####    
        ############    ####    ####    
        ####            ####    ####    
        ####            ####    ####    
        ############    ############    
        ############    ############    
    """,
    """
                        ####            
                       ####             
                      ####              
                     ####               
                    ####                
                   ####                 
                  ####                  
                 ####                   
                ####                    
               ####                     
    """,
    """
                   ##########           
                 ##############         
                ####        ####                
                ##         ####                 
                         ####                   
                      ####                      
                     ####                       

                    ####                
                    ####                
    """,
    """
                    ####                
                    ####                
                    ####                
                    ####                
                    ####                
                    ####                
                    ####                

                    ####                
                    ####                
    """
    ]

    try:
        return numbers[num]
    except Exception as e:
        print (e,"\n\nThe asset coud't be found")
        return None


def squid(step, input_txt=None):
    if step > 3:
        step = 3
    steps = [
    f"""
             #######              ############################################
          ###       ###          ##  Mr. Squid:
        ##             ##       ###  {input_txt}
       ##    ##    ##   ##     ###############################################
      ##   --       --   ##   ##
        ##    -----    ##    #
          ##         ##
     ##    ##  ##  ##    ##
   ##      ##  ##  ##      ##
     ##  ##    ##    ##  ##
       ##     #  #     ##
    """,
    f"""
             #######              ############################################
          ###       ###          ##  Mr. Squid:
        ##             ##       ###  {input_txt}
       ##    ##    ##   ##     ###############################################
      ##   --       --   ##   ##
        ##    00000    ##    #
          ##         ##
     ##    ##  ##  ##    ##
   ##      ##  ##  ##      ##
     ##  ##    ##    ##  ##
       ##     #  #     ##
    """,
    f"""
             #######              ############################################
          ###       ###          ##  Mr. Squid:
        ##             ##       ###  {input_txt}
       ##    ##    --   ##     ###############################################
      ##   --       --   ##   ##
        ##    -----    ##    #
          ##         ##
     ##    ##  ##  ##    ##
   ##      ##  ##  ##      ##
     ##  ##    ##    ##  ##
       ##     #  #     ##
    """,
    f"""
             #######              ############################################
          ###       ###          ##  Mr. Squid:
        ##             ##       ###  {input_txt}
       ##    --    --   ##     ###############################################
      ##   --       --   ##   ##
        ##    -----    ##    #
          ##         ##
     ##    ##  ##  ##    ##
   ##      ##  ##  ##      ##
     ##  ##    ##    ##  ##
       ##     #  #     ##
    """
    ]
    try:
        return steps[step]
    except Exception as e:
        print (e,"\n\nYour DM coud't be found")
        return None


def ass(ass, input_txt=None):
    if ass > 2:
        ass = 2
    asset = [
    """
                ######
                 ####
               ########
              ##########
             ############   
            ##############
           #### _Health ####
           #### Potion_ ####
            ##############
              ##########
    """,
    """
                ######
                 ####
               ########
              ##########
             ############
            ##############
           #### _Lucky_ ####
           #### Potion_ ####
            ##############
              ##########
    """,
    """
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
    """
    ]
    try:
        return asset[ass]
    except Exception as e:
         print (e,"\n\nThe asset coud't be found")
         return None

def map(ass):
    gamedata = loader.load_gamefile()
    asset = []
    asset_counter = None
    try:
        for map in gamedata["map"]:
                if asset_counter == None:
                        asset_counter = 0
                else:
                        asset_counter = asset_counter + 1   
                asset.append(gamedata["map"][map])
        if ass > asset_counter:
                ass = asset_counter
        return asset[ass]
    except Exception as e:
         print (e,"\n\nThe asset coud't be found")
         return None

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