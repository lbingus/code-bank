import time
import random as rd
from tabulate import tabulate as tb
import sys


# ===============
# CLASSES START
# ===============

# USER
class user:
    hp = None
    strength = None
    intel = None
    init = None
    stealth = None
    weapon = None
    armour = None
    char_class = None

    def __init__(user, hp, strength, intel, init, stealth, weapon, armour, char_class):
        user.hp = hp
        user.strength = strength
        user.intel = intel
        user.init = init
        user.stealth = stealth
        user.weapon = weapon
        user.armour = armour
        user.char_class = char_class


# ENEMIES
class enemy:
    _num: int
    _hp: int
    _strength: int
    _intel: int
    _init: int

    def __init__(enemy, num, hp, strength, intel, init):
        enemy._num = num
        enemy._hp = hp
        enemy._strength = strength
        enemy._intel = intel
        enemy._init = init


class orc(enemy):
    def __init__(orc, num, hp, strength, intel, init):
        super().__init__(num, hp, strength, intel, init)
    
    _num: int
    _hp: int
    _strength: int
    _intel: int
    _init: int


class guard(enemy):
    def __init__(guard, num, hp, strength, intel, init):
        super().__init__(num, hp, strength, intel, init)
    
    _num: int
    _hp: int
    _strength: int
    _intel: int
    _init: int


# ===============
# CLASSES END
# ===============

# ---------------
# FUNCTIONS START
# ---------------


def print_user_stats_table():
    user_stats_header = ['Attribute', 'Value']
    stats_table = tb([(k, v)
                      for k, v in user_stats.items()],
                     headers=user_stats_header)

    print('\nThese are your stats:')
    print('-' * 21)
    print(stats_table)
    print('-' * 21)


def class_mods(user_class):
    if user_class.isnumeric() is True:
        print(f'\n"{user_class}" is an invalid character class.')
        exit()
    else:
        if user_class.lower() == 'barbarian':
            user_stats['Strength'] = strength + 3
            user_stats['Intelligence'] = intel - 2
        elif user_class.lower() == 'bard':
            user_stats['Initiative'] = init + 3
            user_stats['Stealth'] = stealth - 2
        elif user_class.lower() == 'rogue':
            user_stats['Stealth'] = stealth + 3
            user_stats['Initiative'] = init - 2
        elif user_class.lower() == 'wizard':
            user_stats['Intelligence'] = intel + 3
            user_stats['Strength'] = strength - 2
        else:
            time.sleep(1)
            print(f'\n{user_class} does not exist. No adventures for you.')
            exit()


def print_class_mod_table():
    class_modifiers_header = ['Class', 'Gain', 'Loss']
    mod_table = tb([(k,) + v
                    for k, v in class_modifiers.items()],
                   headers=class_modifiers_header)

    print('\nChoose your character class. Each character class gains 3 bonus '
          '\npoints to one stat and loses 2 points from another stat: ')
    print('-' * 27)
    print(mod_table)
    print('-' * 27)
    return mod_table


def use_bag():
    time.sleep(1)
    for k, v in bag.items():    # prints bag contents
        print(k, v)
    resp = input('\nWhat do you want to do?\n'
                 '\nPotions/Equip\n')
    if resp.lower() == 'potions':
        use_potions()
    elif resp.lower() == 'equip':
        use_armour()
    else:
        print('\n Closing bag again.')
        return


def use_armour():
    time.sleep(1)
    for k, v in bag.items():    # prints bag contents
        print(k, v)
    resp = input('\nWhich item would you like to equip?\n')
    if resp.lower() == 'chestplate':
        resp2 = input(f'\nDo you want to equip the {resp.upper()}?' 
                      '\nY/N\n')
        try:
            if resp2.lower() == 'y':
                del bag['CHESTPLATE']
                armour = 20
                user.armour += armour
                time.sleep(1)
                print(f'\nYou equipped the {resp.upper()}.')
                time.sleep(2)
                print(f'\nYou gained {armour} armour. Your new armour is {user.armour}')
            return
        except:
            time.sleep(1)
            print(f'\n{resp} is not in your bag.')
            return
    elif resp.lower() == 'helmet':
        resp2 = input(f'\nDo you want to equip the {resp.upper()}?'
                      '\nY/N\n')
        try:
            if resp2.lower() == 'y':
                del bag['HELMET']
                armour = 15
                user.armour += armour
                time.sleep(1)
                print(f'\nYou equipped the {resp.upper()}.')
                time.sleep(2)
                print(f'\nYou gained {armour} armour. Your new armour is {user.armour}')
            return
        except:
            time.sleep(1)
            print(f'\n{resp} is not in your bag.')
            return
    elif resp.lower() == 'chainmail pants':
        resp2 = input(f'\nDo you want to equip the {resp.upper()}?' 
                      '\nY/N\n')
        try:
            if resp2.lower() == 'y':
                del bag['CHAINMAIL PANTS']
                armour = 15
                user.armour += armour
                time.sleep(1)
                print(f'\nYou equipped the {resp.upper()}.')
                time.sleep(2)
                print(f'\nYou gained {armour} armour. Your new armour is {user.armour}')
            return
        except:
            time.sleep(1)
            print(f'\n{resp} is not in your bag.')
            return
    elif resp.lower() == 'gloves':
        resp2 = input(f'\nDo you want to equip the {resp.upper()}?'
                      '\nY/N\n')
        try:
            if resp2.lower() == 'y':
                del bag['GLOVES']
                armour = 10
                user.armour += armour 
                time.sleep(1)
                print(f'\nYou equipped the {resp.upper()}.')
                time.sleep(2)
                print(f'\nYou gained {armour} armour. Your new armour is {user.armour}')
            return
        except:
            time.sleep(1)
            print(f'\n{resp} is not in your bag.')
            return
    
    # weapons
    elif resp.lower() == 'dwarven axe':
        resp2 = input(f'\nDo you want to equip the {resp.upper()}?'
                      '\nY/N\n')
        try:
            if resp2.lower() == 'y':
                del bag['DWARVEN AXE']
                strength_up = 10
                user.armour += strength_up
                time.sleep(1)
                print(f'\nYou equipped the {resp.upper()}.')
                time.sleep(2)
                print(f'\nYou gained {strength_up} STR. Your new STR is {user.armour}')
            return
        except:
            time.sleep(1)
            print(f'\n{resp} is not in your bag.')
            return
    elif resp.lower() == 'mystic dagger':
        resp2 = input(f'\nDo you want to equip the {resp.upper()}?'
                      '\nY/N\n')
        try:
            if resp2.lower() == 'y':
                del bag['MYSTIC DAGGER']
                strength_up = 10
                user.armour += strength_up
                time.sleep(1)
                print(f'\nYou equipped the {resp.upper()}.')
                time.sleep(2)
                print(f'\nYou gained {strength_up} STR. Your new STR is {user.armour}')
            return
        except:
            time.sleep(1)
            print(f'\n{resp} is not in your bag.')
            return
    elif resp.lower() == 'grand staff':
        resp2 = input(f'\nDo you want to equip the {resp.upper()}?'
                      '\nY/N\n')
        try:
            if resp2.lower() == 'y':
                del bag['GRAND STAFF']
                strength_up = 10
                user.armour += strength_up
                time.sleep(1)
                print(f'\nYou equipped the {resp.upper()}.')
                time.sleep(2)
                print(f'\nYou gained {strength_up} STR. Your new STR is {user.armour}')
            return
        except:
            time.sleep(1)
            print(f'\n{resp} is not in your bag.')
            return
    elif resp.lower() == 'golden lute':
        resp2 = input(f'\nDo you want to equip the {resp.upper()}?'
                      '\nY/N\n')
        try:
            if resp2.lower() == 'y':
                del bag['GOLDEN LUTE']
                strength_up = 10
                user.armour += strength_up
                time.sleep(1)
                print(f'\nYou equipped the {resp.upper()}.')
                time.sleep(2)
                print(f'\nYou gained {strength_up} STR. Your new STR is {user.armour}')
            return
        except:
            time.sleep(1)
            print(f'\n{resp} is not in your bag.')
            return
    else:
        time.sleep(1)
        print(f'\n{resp} is an invalid action.')
        return


def use_potions():
    running = True
    time.sleep(1)
    while running is True:
        for k, v in bag.items():    # prints bag contents
            print(k, v)
        resp = input('\nWhich potion do you want to use (NOTE: just type the name, e.g. "health" for a health potion etc.)?'
                     '\nType "return" to return to the game.\n')
        if resp.lower() == 'health':
            if bag['HLTH POTION'] != 0:
                user.hp += 30
                bag['HLTH POTION'] -= 1
                time.sleep(1)
                print(f'\nYou gained 30 HP. Your current HP is {user.hp}.')
                running = False     # ends running cycle
                return     # returns to fight
            elif bag['HLTH POTION'] == 0:
                del bag['HLTH POTION']
                return
    
        elif resp.lower() == 'strength':
            if bag['STR POTION'] >= 1:
                user.strength += 10
                bag['STR POTION'] -= 1
                time.sleep(1)
                print(f'\nYou gained 10 STR. Your current STR is {user.strength}.')
                running = False     # ends running cycle
                return     # returns to fight
            elif bag['STR POTION'] == 1:
                bag['STR POTION'] -= 1
                del bag['STR POTION']
                return
            
        elif resp.lower() == 'speed':
            if bag['INIT POTION'] != 0:
                user.init += 10
                bag['INIT POTION'] -= 1
                time.sleep(1)
                print(f'\nYou gained 10 INIT. Your current INIT is {user.init}.')
                running = False     # ends running cycle
                return     
            elif bag['INIT POTION'] == 0:
                del bag['INIT POTION']
                return
            
        elif resp.lower() == 'stealth':
            if bag['STL POTION'] != 0:
                user.stealth += 10
                bag['STL POTION'] -= 1
                time.sleep(1)
                print(f'\nYou gained 10 STL. Your current STL is {user.stealth}.')
                running = False     # ends running cycle
                return     # returns to fight
            elif bag['STL POTION'] == 0:
                del bag['STL POTION']
                return
            
        elif resp.lower() == 'intelligence':
            if bag['INTEL POTION'] != 0:
                user.intel += 10
                bag['INTEL POTION'] -= 1
                time.sleep(1)
                print(f'\nYou gained 10 INTEL. Your current INTEL is {user.intel}.')
                running = False     # ends running cycle
                return     # returns to fight
            elif bag['INTEL POTION'] == 0:
                del bag['INTEL POTION']
                return
            
        # returns to game
        elif resp.lower() == 'return':
            return
        
        else:
            print(f'{resp} is not a potion.')
            continue


def walls():
    time.sleep(1)
    resp = input('\nThere is a wall. Do you want to touch it?'
                 '\nY/N\n')
    if resp.lower() == 'y':
        time.sleep(1)
        print('\nThe wall is cold and rough.')
    else:
        return


def lick_wall():
    global achievement
    
    time.sleep(1)
    print('\nYou pause for a moment.')
    time.sleep(3)
    print('\nNobody would ever know, right?')
    time.sleep(3)
    print('\nYou approach the wall.')
    resp = input('\nDo you want to lick the wall like a goat?'
                 '\nY/N\n')
    if resp.lower() == 'y':
        time.sleep(1)
        print('\n*sluuuuuuuurp* "Eurgh," you exclaim as you brush dust and debris off your tongue.'
              '\nDid your mum not tell you not to lick the walls?')
        time.sleep(1)
        print('\nAchievement unlocked: Goat Simulator')
        achievement = True
        return
    else:
        return


def main_room_1():
    global main_room_1_counter
    global main_room_2_counter
    global main_room_3_counter
    main_corridor = True
    
    # tracks position within main corridor
    while main_corridor is True:
        time.sleep(1)
        resp = input('\nWhat do you want to do?'
                     '\nForward/Back/Right/Left/Bag\n')
        if resp.lower() == 'bag':
            use_bag()
        elif resp.lower() == 'forward':
            time.sleep(1)
            print('\nYou step forward. The sound of your step reverberates down the dark corridor.')
            main_room_1_counter += 1
            
            # first small loot room
            if main_room_1_counter == 2:
                time.sleep(1)
                resp2 = input('\nThere is a small room to your right.'
                              '\nWhat do you want to do?\n'
                              '\nForward/Back/Right/Left/Bag\n')
                if resp2.lower() == 'right':
                            time.sleep(1)
                            print('\nYou find 1 HLTH POTION and 1 STR POTION and go back to the main corridor.')
                            bag['HLTH POTION'] = 1
                            bag['STR POTION'] = 1
                            for k, v in bag.items():    # prints bag contents
                                print(k, v)
                else:
                    continue
            
            # entrance to side corridor 1
            elif main_room_1_counter == 4:
                time.sleep(1)
                resp2 = input('\nA corridor is to your left. You can hear someone talking. The voices mention armour.'
                              '\nWhat do you want to do?'
                              '\nForward/Back/Right/Left/Bag\n')
                if resp2.lower() == 'left':
                    side_corridor_1_walking()
                elif resp2.lower() == 'bag':
                    use_bag()
            
            # story element
            elif main_room_1_counter == 8:
                time.sleep(1)
                event1()
            
            # entrance to side corridor 2
            elif main_room_1_counter == 10:
                time.sleep(1)
                resp2 = input('\nA corridor is to your left. Loud grunts emanate from the darkness. You have the feeling that there will be great things in this corridor.'
                              '\nWhat do you want to do?'
                              '\nForward/Back/Right/Left/Bag\n')
                if resp2.lower() == 'left':
                    side_corridor_2_walking()
                elif resp2.lower() == 'bag':
                    use_bag()
                    continue
            elif main_room_1_counter == 8:
                time.sleep(1)
                event1()
            
            # entrance to main room 2
            elif main_room_1_counter == 13:
                time.sleep(1)
                resp2 = input('\nThe corridor leads to another room on the right. A cool breeze lets you know that this is the way out.'
                              '\nWhat do you want to do?'
                              '\nForward/Back/Right/Left/Bag\n')
                if resp2.lower() == 'right':
                    main_room_2()
                elif resp2.lower() == 'bag':
                    use_bag()
                    continue
        
        # back options                    
        elif resp.lower() == 'back':
            main_room_1_counter -=1
            if main_room_1_counter == 0:
                time.sleep(1)
                print('\nThere is nowhere to go back to. Walk into the darkness and face the monsters that await you.')
                main_room_1_counter = 0
            else:
                time.sleep(1)
                print('\nYou took a step back.')
        
        # right options
        elif resp.lower() == 'right':
            walls()
        
        # left options
        elif resp.lower() == 'left':
            walls()
        
        # invalid input
        else: 
            print(f'\n{resp} is not a valid action.')
            continue


def main_room_2():
    global main_room_1_counter
    global main_room_2_counter
    main_corridor = True
    
    main_room_1_counter = 0
    time.sleep(1)
    print('\nYou entered the second room. Suddenly, the wooden pillars that supported the ceiling'
          'break with a loud crack and the entrance collapses. There is no way back for you.')
    # tracks position within main corridor
    while main_corridor is True:
        time.sleep(1)
        resp = input('\nWhat do you want to do?'
                '\nForward/Back/Right/Left/Bag\n')
        
        # bag
        if resp.lower() == 'bag':
            use_bag()
        
        # 'back' options
        elif resp.lower() == 'back' and main_room_2_counter == 0:
            time.sleep(1)
            print('\nThe entrance is sealed off by a large pile of rocks. You cannot move them by yourself.')
            continue
        elif resp.lower() == 'back' and main_room_2_counter > 0:
            time.sleep(1)
            print('\nYou took a step back.')
            continue
        
        # 'right' options
        elif resp.lower() == 'right' and main_room_2_counter == 0:
            time.sleep(1)
            print('\nYou find 2 STL POTIONs, 2 INIT POTIONs, 2 HLTH POTIONs, 1 STR POTION, and GLOVES.')
            try:
                bag['STL POTION'] += 2
            except:
                bag['STL POTION'] = 2
            try:
                bag['INIT POTION'] += 2
            except:
                bag['INIT POTION'] = 2
            try:
                bag['HLTH POTION'] += 2
            except:
                bag['HLTH POTION'] = 2
            try:
                bag['STR POTION'] += 1
            except:
                bag['STR POTION'] = 1
            bag['GLOVES'] = 1
            for k, v in bag.items():    # prints bag contents
                print(k, v)
            resp2 = input('\nDo you want to equip the GLOVES?'
                          '\nY/N\n')
            if resp2.lower() == 'y':
                del bag['GLOVES']
                user.armour += 15
                time.sleep(1)
                print(f'\nYou equipped the GLOVES')
        elif resp.lower() == 'right' and main_room_2_counter > 0:
            walls()
        
        # 'left' optinos
        elif resp.lower() == 'left' and main_room_2_counter == 0:
            main_room_2_counter += 1
            time.sleep(1)
            print('\nWith cautious steps, you walk towards the far wall of the room.')
        elif resp.lower() == 'left' and main_room_2_counter == 7:
          time.sleep(1)
          print('\nStanding at the far wall of the room, you cannot help but wonder what brought you here. As far as you are aware,' 
                '\nyou do not have any enemies that would make you go through this ordeal. As you ponder the possibilities of this, you'
                '\nnotice that there is a small openin in the wall to your left. It is just big enough to let a person crawl through.'
                '\nA strong breeze of air blows through the cracks in the rocks. For asecond you hsitate. Weighing your chances of'
                '\nsurvival, you decide to crawl through the hole and leave the room behind.')
          main_room_3()
        elif resp.lower() == 'left' and main_room_2_counter > 0:
            walls()
        
        # 'forward' options
        elif resp.lower() == 'forward' and main_room_2_counter == 0:
            time.sleep(1)
            print('\nThere is just a wall. You look at it and consider licking the stone that surrounds you. Like a goat you crave that mineral.'
                  '\nBut after a short moment of consideration you snap back into the present and focus on something more pressing: Escaping this cave.')
        elif resp.lower() == 'forward' and main_room_2_counter == 2:
            main_room_2_counter += 1
            time.sleep(1)
            print('\nDisembodied voices float through the dark and you see a faint glow in the dark. You could swear you are alone here.')
        elif resp.lower() == 'forward' and main_room_2_counter == 4:
            main_room_2_counter += 1
            fight_guards()
        elif resp.lower() == 'forward' and main_room_2_counter == 5:
            main_room_2_counter += 1
            time.sleep(1)
            print('\nYou find 2 STL POTIONs, 2 INIT POTIONs, 2 HLTH POTIONs, 2 STR POTIONs, 2 INTEL POTIONs, and CHAINMAIL PANTS.')
            try:
                bag['STL POTION'] += 2
            except:
                bag['STL POTION'] = 2
            try:
                bag['INIT POTION'] += 2
            except:
                bag['INIT POTION'] = 2
            try:
                bag['HLTH POTION'] += 2
            except:
                bag['HLTH POTION'] = 2
            try:
                bag['STR POTION'] += 2
            except:
                bag['STR POTION'] = 2
            try:
                bag['INTEL POTION'] += 2
            except:
                bag['INTEL POTION'] = 2
            bag['CHAINMAIL PANTS'] = 1
            for k, v in bag.items():    # prints bag contents
                print(k, v)
            resp2 = input('\nDo you want to equip the CHAINMAIL PANTS?'
                          '\nY/N\n')
            if resp2.lower() == 'y':
                del bag['CHAINMAIL PANTS']
                user.armour += 15
                time.sleep(1)
                print(f'\nYou equipped the CHAINMAIL PANTS')
        elif resp.lower() == 'forward' and main_room_2_counter == 7:
            time.sleep(1)
            print('\nYou cannot go any further. The wall is right in front of you.')
            continue
        elif resp.lower() == 'forward':
            main_room_2_counter += 1
            time.sleep(1)
            print('\nYou step forward, ready to fight if necessary.')


def main_room_3():
    global main_room_1_counter
    global main_room_2_counter
    global main_room_3_counter
    main_corridor = True
      
    main_room_1_counter = 0
    main_room_2_counter = 0
    time.sleep(1)
    print('\nAs you squeeze yourself through the hole in the wall, you cannot help but notice'
          '\nthat debris is falling onto your head and just as you manage to struggle your way out of'
          '\nthe opning in the wall, the rock gives in and seals the opening shut. You cannot go back.')
      
    # tracks position within main corridor
    while main_corridor is True:
        time.sleep(1)
        resp = input('\nWhat do you want to do?'
                     '\nForward/Back/Right/Left/Bag\n')
          
        # bag
        if resp.lower() == 'bag':
            use_bag()
          
        # 'back' options
        elif resp.lower() == 'back' and main_room_3_counter == 0:
            time.sleep(1)
            print('\nThe opening in the wall collapsed. The debris and rocks are too heavy for you to move them.')
            continue
        elif resp.lower() == 'back' and main_room_3_counter > 0:
            main_room_3_counter -= 1
            time.sleep(1)
            print('\nYou took a step back.')
            continue
            
        # 'left' options
        elif resp.lower() == 'left':
            walls()
        
        # 'right' options
        elif resp.lower() == 'right' and main_room_3_counter == 0:
            main_room_3_counter += 1
            time.sleep(1)
            print('\nFreedom is close, you can practically taste it. Longing for fresh air, you'
                  '\nstep forward.')
        elif resp.lower() == 'right' and main_room_3_counter <= 4:
            walls()
        elif resp.lower() == 'right' and main_room_3_counter == 5:
            main_room_3_counter += 1
            time.sleep(1)
            print("\nYou follow the corridor's lead and go right.")
            fight_orcs()
            print("\nAfter a hard fight, you emerged victiriously with the orcs' heads as your trophies.")
            bag['ORC HEAD'] = 3
            for k, v in bag.items():    # prints bag contents
                    print(k, v)
                   
        elif resp.lower() == 'right' and main_room_3_counter >= 7:
            walls()
        
        # 'forward' options
        elif resp.lower() == 'forward' and main_room_3_counter == 0:
            time.sleep(1)
            print('\nYet again the urge to lick the jagged stone wall overwhelms you.')
            lick_wall()
        elif resp.lower() == 'forward' and main_room_3_counter == 1:
            main_room_3_counter += 1
            time.sleep(1)
            print('\nYour steps grow weaker as you progress through the room.')
            event2()
        elif resp.lower() == 'forward' and main_room_3_counter == 4:
            main_room_3_counter += 1
            time.sleep(1)
            print('\nFinally you can hear sounds from the outside world. The exit must be very close!'
                  '\nAnd as you dream of the outside world, a voice shouts at you: "Attack the intruder!"')
            fight_guards()
        elif resp.lower() == 'forward' and main_room_3_counter < 5 and main_room_3_counter >= 2:
            main_room_3_counter += 1
            time.sleep(1)
            print('\nVoices and grunts emanate through the darkness but you cannot make out where'
                  '\nthe enemy is or how many there are.')
        elif resp.lower() == 'forward' and main_room_3_counter == 5:
            time.sleep(1)
            print('\nThere is a wall in front of you. The corridor continues on the right.')
        elif resp.lower() == 'forward' and main_room_3_counter == 6:
            main_room_3_counter += 1
            time.sleep(1)
            print('\nPalms sweaty, knees weak, arms are heavy. But you cannot give up now. You are so'
                  'close to the exit.')
        elif resp.lower() == 'forward' and main_room_3_counter == 7:
            time.sleep(1)
            print('\nFinally, there it was: the exit. Sunshine caresses your cheeks and your troubles '
                  '\nare briefly forgotten. And then you wonder: If you had one shot or one opportunity '
                  '\nto seize everything you ever wanted in one moment... Would you capture it or just let'
                  '\nit slip? "I guess everyone has to decide for themselves," you think to yourself before'
                  '\nyour vision blurs and you collapse of exhaustion.')
            main_corridor = False
            main_room_1_counter = 0
            main_room_2_counter = 0
            main_room_3_counter = 0
            end()
        

def side_corridor_1_walking():
    global side_corridor_counter
    global bag
    side_corridor = True
    
    time.sleep(1)
    print('\nYou are in the side corridor. The voices are getting closer.')
    while side_corridor is True:
        time.sleep(1)
        resp = input('\nWhat do you want to do?'
                     '\nForward/Back/Right/Left/Bag\n')
        if resp.lower() == 'bag':
            use_bag()
        elif resp.lower() == 'forward' and side_corridor_counter == 1:
            side_corridor_counter += 1
            time.sleep(1)
            fight_guards()
        elif resp.lower() == 'forward' and side_corridor_counter == 3:
            side_corridor_counter += 1
            time.sleep(1)
            print('\nYou step forward. The corridor goes right here.')
        elif resp.lower() == 'forward' and side_corridor_counter == 5:
            side_corridor_counter += 1
            time.sleep(1)
            print('\nYou step forward. The corridor goes left here and leads to a door. Do you want to open it?')        
            resp2 = input('\nY/N\n')
            if resp2.lower() == 'y':
                print('\nYou opened the door and find 4 HLTH POTIONS, 3 STR POTIONS, and a CHESTPLATE (+20 armour).')
                try:
                    bag['HLTH POTION'] += 4
                except:
                    bag['HLTH POTION'] = 4
                try:
                    bag['STR POTION'] += 3
                except:
                    bag['STR POTION'] = 3
                try:
                    bag['CHESTPLATE'] += 1
                except:
                    bag['CHESTPLATE'] = 1
                for k, v in bag.items():    # prints bag contents
                    print(k, v)
                resp3 = input(f'\nDo you want to equip the CHESTPLATE?' 
                              '\nY/N\n')
                if resp3.lower() == 'y':
                    del bag['CHESTPLATE']
                    user.armour += 20
                    time.sleep(1)
                    print(f'\nYou equipped the CHESTPLATE and returned to the main corridor.')
                    side_corridor_counter = 0
                    side_corridor = False   # breaks while loop
                    main_room_1()
                else: 
                    print('\nYou did not equip the CHESTPLATE and returned to the main corridor.')
                    side_corridor_counter = 0
                    side_corridor = False   # breaks while loop
                    main_room_1()
            else:
                print('\nYou did not open the door and left the side corridor.')
                side_corridor_counter = 0
                side_corridor = False
                main_room_1()
        elif resp.lower() == 'forward':
            side_corridor_counter += 1
            print('\nYou step forward. The sound of your step reverberates down the dark corridor.')
        
        if resp.lower() == 'right' and side_corridor_counter == 4:
            side_corridor_counter += 1
            time.sleep(1)
            print("\nYou follow the corridor's lead.\n")
        
        elif resp.lower() == 'right':
            walls()
                
        elif resp.lower() == 'left':
            walls()
                
        elif resp.lower() == 'back':
            if side_corridor_counter <= 0:
                time.sleep(1)
                print('\nYou left the side corridor.')
                side_corridor_counter = 0
                side_corridor = False
                main_room_1()
            else:
                side_corridor_counter -= 1
                time.sleep(1)
                print('\nYou took a step back.')


def side_corridor_2_walking():
    global side_corridor_counter
    global bag 
    global fight 
    side_corridor = True
    time.sleep(1)
    print('\nYou step into the side corridor. The grunting is getting closer and louder.')
    time.sleep(1)
    print('\nYour foot lands in a puddle of viscous liquid and a wet thud echoes in the darkness.')
    side_corridor_counter = 1
    while side_corridor is True:
        
        # main part of side corridor 2       
        time.sleep(1)
        resp = input('\nWhat do you want to do?'
                '\nForward/Back/Right/Left/Bag\n')
        if resp.lower() == 'bag':
            use_bag()
    
        elif resp.lower() == 'forward' and side_corridor_counter == 2:
            side_corridor_counter += 1
            time.sleep(1)
            print('\nYou step forward. The corridor goes right here.')
        elif resp.lower() == 'forward' and side_corridor_counter == 4:
            side_corridor_counter += 1
            time.sleep(1)
            resp2 = input('\nYou step forward. In the darkness, you can barely make out the haggard silhouette of a human skeleton. It carries a bag and'
                          '\nthe armour it died in. Do you want to take the armour and look inside the bag?'
                          '\nY/N\n')
            if resp2.lower() == 'y':
                time.sleep(1)
                print('\nThe bag contained 2 HLTH POTIONS, 1 STL POTION, 2 INIT POTIONS, and 1 STR POTION. You took 1 HELMET (+15 armour) from the skeleton.')
                try:
                    bag['HLTH POTION'] += 2
                except:
                    bag['HLTH POTION'] = 2
                try:
                    bag['INIT POTION'] += 2
                except:
                    bag['INIT POTION'] = 2
                try:
                    bag['STL POTION'] += 1
                except:
                    bag['STL POTION'] = 1
                try:
                    bag['STR POTION'] += 1
                except:
                    bag['STR POTION'] = 1
                bag['HELMET'] = 1
                for k, v in bag.items():    # prints bag contents
                    print(k, v)
                resp3 = input(f'\nDo you want to equip the HELMET?' 
                              '\nY/N\n')
                if resp3.lower() == 'y':
                    del bag['HELMET']
                    user.armour += 15
                    time.sleep(1)
                    print(f'\nYou equipped the HELMET')
        elif resp.lower() == 'forward' and side_corridor_counter == 6:
            side_corridor_counter += 1
            time.sleep(1)
            print('\n\nYou step forward. Your foot lands in a puddle of viscous liquid and a wet thud echoes in the darkness. The grunts are getting louder and'
                  '\nyou worry that whatever lies at the end of the corridor has heard you. The corridor goes left here.')
        
        # starts orc fight
        elif resp.lower() == 'forward' and side_corridor_counter == 8:
            side_corridor_counter += 1
            fight_orcs()
        
        # only executed if orc is killed
        elif side_corridor_counter == 9 and fight is False:
            time.sleep(1)
            resp = input('\nAfter defeating the orc, you see a small chest laying behind him.'
                         '\nDo you want to open it?'
                         '\nY/N\n')
            if resp.lower() == 'y':
                if user_class.lower() == 'barbarian':
                    weapon = 'DWARVEN AXE'
                elif user_class.lower() == 'bard':
                    weapon = 'GOLDEN LUTE'
                elif user_class.lower() == 'rogue':
                    weapon = 'MYSTIC DAGGER'
                else:
                    weapon = 'GRAND STAFF'
                time.sleep(1)
                print(f'\nYou opened the chest. It held 2 HLTH POTIONS, 2 INTEL POTIONS, 1 STL POTION, and 1 {weapon}.')
                try:
                    bag['HLTH POTION'] += 2
                except:
                    bag['HLTH POTION'] = 2
                try:
                    bag['INTEL POTION'] += 2
                except:
                    bag['INTEL POTION'] = 2
                try:
                    bag['STL POTION'] += 1
                except:
                    bag['STL POTION'] = 1
                bag[weapon] = 1
                for k, v in bag.items():    # prints bag contents
                    print(k, v)
                resp3 = input(f'\nDo you want to equip the {weapon}?' 
                              '\nY/N\n')
                if resp3.lower() == 'y':
                    del bag[weapon]
                    user.armour += 15
                    time.sleep(1)
                    print(f'\nYou equipped the {weapon} and left the side corridor.')
                    side_corridor_counter = 0
                    main_room_1()
        
        # regular forward movement
        elif resp.lower() == 'forward':
            side_corridor_counter += 1
            print('\nThe grunting is getting closer and louder.')        
        
        # other options; OPTIONS ARE SORTED ACCORDING TO INPUT (i.e. all 'right' options are grouped)     
        elif resp.lower() == 'right' and side_corridor_counter == 3:
            side_corridor_counter += 1
            print('\nYou step forward. Your foot lands in a puddle of viscous liquid and a wet thud echoes in the darkness.')
        elif resp.lower() == 'right':
            walls()
                
        elif resp.lower() == 'left' and side_corridor_counter == 7:    # right before the orcs
            side_corridor_counter += 1
            print('\nYou step forward. Your foot lands in a puddle of viscous liquid and a wet thud echoes in the darkness.')
        elif resp.lower() == 'left':
            walls()
        elif resp.lower() == 'back':
            if side_corridor_counter == 0:
                time.sleep(1)
                print('\nYou left the side corridor.')
                side_corridor_counter = 0
                main_room_1()
            else:
                side_corridor_counter -= 1
                time.sleep(1)
                print('\nYou took a step back.')
                continue


def fight_guards():
    global side_corridor_counter
    global main_room_1_counter
    global main_room_2_counter
    global main_room_3_counter
    global fight
    fight = True
    
    #generates guards
    if main_room_1_counter > 0 and main_room_2_counter == 0 and main_room_3_counter == 0:
        guards = guard(rd.randint(1, 3), 25, 7, 10, 7)
    elif main_room_1_counter == 0 and main_room_2_counter > 0 and main_room_3_counter == 0:
        guards = guard(rd.randint(3, 6), 25, 7, 10, 7)
    else:
        guards = guard(8, 25, 7, 10, 7)
    
    time.sleep(1)
    print(f'\nYou encounter {guards._num} guard(s) in the corridor.')
    guard_hp_total = guards._hp * guards._num     # calculates total guard group hp
    guard_strength_total = guards._strength * guards._num     # calculates total guard group strength
    guard_intel_total = guards._intel * guards._num    # calculates total guard group intelligence
    guard_init_total = guards._init * guards._num    # calculates total guard group initiative
    
    first_attack = True
    while guard_hp_total > 0 and user.hp > 0:   #  loop only ends when guard hp is 0

        if first_attack is True:     # guards attack first if the following condition is met
            
            if (guard_strength_total + guard_init_total + guard_intel_total) > (user.intel + (user.stealth * 1.5) + (user.init * 1.5)):
                print('\nThe enemy heard your foot steps echoing down the hallway and is attacking you.')
                
                if user.armour > 0:  
                    damage_user = round((guard_strength_total * 1.3) / (((user.armour)/10) * 2))
                    damage_guards = round(user.strength * 1.5)  # user has 1.5 multiplier               
                else:
                    damage_user = round((guard_strength_total * 1.3) / 1.5)
                    damage_guards = round(user.strength * 1.5)  # user has 1.5 multiplier
                    guard_hp_total -= damage_guards
                    
                user.hp -= damage_user
                guard_hp_total -= damage_guards
                
                # losing condition if guards are too strong upon first attack
                if damage_user >= user.hp:
                    time.sleep(1)
                    print(f'\nYou suffered {damage_user} points damage.')
                    print('\nYour HP hit 0. You died. Thank you for playing.')
                    sys.exit('\nGAME OVER')                    
                else:
                    print(f'\nYou suffered {damage_user} damage. Your current HP is {user.hp}.')
                    first_attack = False
                    
            else:
                first_attack = False    # ensures first attack of guards is not repeated and regular fights begin

        # attacking cycle
        resp = input(f'\nYou see {guards._num} guard(s) before you.' 
                     '\nWhat do you want to do?\n'
                     '\nAttack/Potion/Retreat\n')
        if resp.lower() == 'attack':
            if user.armour > 0:  
                damage_user = round((guard_strength_total * 1.3) / (((user.armour)/10) * 2))
                user.hp -= damage_user
                damage_guards = round(user.strength * 1.5)  # user has 1.5 multiplier
                guard_hp_total -= damage_guards                
            else:
                damage_user = round((guard_strength_total * 1.3) / 1.5)
                user.hp -= damage_user
                damage_guards = round(user.strength * 1.5)  # user has 1.5 multiplier
                guard_hp_total -= damage_guards
            
            # win condition
            if damage_guards >= guard_hp_total:
                time.sleep(1)
                print('\nYou defeated the enemy. You can advance.')
                fight = False
                return
            
            # game over 
            elif damage_user >= user.hp:
                time.sleep(1)
                print(f'\nYou suffered {damage_user} points damage.')
                print('\nYour HP hit 0. You died. Thank you for playing.')
                sys.exit('\nGAME OVER')
            
            # loop repeats    
            elif damage_user < user.hp and damage_guards < guard_hp_total:
                print(f'\nYou suffered {damage_user} points damage. Your current HP is {user.hp}.')
                time.sleep(1)
                print(f'\nYou dealt {damage_guards} points damage. The current enemy HP is {guard_hp_total}.')
                continue          
            
        # player chose potions with first attack by guards
        elif resp.lower() == 'potion':
            use_potions()
            continue

        # player chose to retreat
        elif resp.lower() == 'retreat' and side_corridor_counter > 0:
            side_corridor_counter -= 1
            fight = False
            time.sleep(1)
            print('\nYou retreated from the fight.')
            return
        elif resp.lower() == 'retreat' and main_room_1_counter > 0:
            main_room_1_counter -= 1
            fight = False
            time.sleep(1)
            print('\nYou retreated from the fight.')
            return
        elif resp.lower() == 'retreat' and main_room_2_counter > 0:
            main_room_2_counter -= 1
            fight = False
            time.sleep(1)
            print('\nYou retreated from the fight.')
            return
        elif resp.lower() == 'retreat' and main_room_3_counter >0:
            main_room_3_counter -= 1
            fight = False
            time.sleep(1)
            print('\nYou retreated from the fight.')
            return
            
        # wrong input
        else:
            time.sleep(1)
            print(f'\nInvalid input. Try again.')
            continue
                          
  
def fight_orcs():
    global side_corridor_counter
    global main_room_1_counter
    global main_room_2_counter
    global main_room_3_counter
    global fight
    fight = True

    # generates orcs
    if main_room_1_counter == 0 and main_room_2_counter == 0:
        orcs = orc(3, 1, 13, 3, 5)
    else: 
        orcs = orc(1, 50, 13, 3, 5)

    time.sleep(1)
    print(f'\nYou encounter {orcs._num} orcs in the corridor.')
    orc_hp_total = orcs._hp * orcs._num     # calculates total orc group hp
    orc_strength_total = orcs._strength * orcs._num     # calculates total orc group strength
    orc_intel_total = orcs._intel * orcs._num    # calculates total orc group intelligence
    orc_init_total = orcs._init * orcs._num    # calculates total orc group initiative

    first_attack = True
    while orc_hp_total > 0 and user.hp > 0:   #  loop only ends when orc hp is 0

        if first_attack is True:     # orcs attack first if the following condition is met
            
            if (orc_strength_total + orc_init_total + orc_intel_total) > (user.intel + (user.stealth * 1.5) + (user.init * 1.5)):
                print('\nThe enemy heard your foot steps echoing down the hallway and is attacking you.')
                
                if user.armour > 0:  
                    damage_user = round((orc_strength_total * 1.3) / (((user.armour)/10) * 2))
                    damage_orcs = round(user.strength * 1.5)  # user has 1.5 multiplier               
                else:
                    damage_user = round((orc_strength_total * 1.3) / 1.5)
                    damage_orcs = round(user.strength * 1.5)  # user has 1.5 multiplier
                    orc_hp_total -= damage_orcs
                    
                user.hp -= damage_user
                orc_hp_total -= damage_orcs
                
                # losing condition if orcs are too strong upon first attack
                if damage_user >= user.hp:
                    time.sleep(1)
                    print(f'\nYou suffered {damage_user} points damage.')
                    print('\nYour HP hit 0. You died. Thank you for playing.')
                    sys.exit('\nGAME OVER')                    
                else:
                    print(f'\nYou suffered {damage_user} damage. Your current HP is {user.hp}.')
                    first_attack = False
                    
            else:
                first_attack = False    # ensures first attack of orcs is not repeated and regular fights begin

        # attacking cycle
        resp = input(f'\nYou see {orcs._num} orc(s) before you. '
                     '\nWhat do you want to do?\n'
                     '\nAttack/Potion/Retreat\n')
        if resp.lower() == 'attack':
            if user.armour > 0:  
                damage_user = round((orc_strength_total * 1.3) / (((user.armour)/10) * 2))
                user.hp -= damage_user
                damage_orcs = round(user.strength * 1.5)  # user has 1.5 multiplier
                orc_hp_total -= damage_orcs                
            else:
                damage_user = round((orc_strength_total * 1.3) / 1.5)
                user.hp -= damage_user
                damage_orcs = round(user.strength * 1.5)  # user has 1.5 multiplier
                orc_hp_total -= damage_orcs
            
            # win condition
            if damage_orcs >= orc_hp_total:
                time.sleep(1)
                print('\nYou defeated the enemy. You can advance.')
                fight = False
                return
            
            # game over 
            elif damage_user >= user.hp:
                time.sleep(1)
                print(f'\nYou suffered {damage_user} points damage.')
                print('\nYour HP hit 0. You died. Thank you for playing.')
                sys.exit('\nGAME OVER')
            
            # loop repeats    
            elif damage_user < user.hp and damage_orcs < orc_hp_total:
                print(f'\nYou suffered {damage_user} points damage. Your current HP is {user.hp}.')
                time.sleep(1)
                print(f'\nYou dealt {damage_orcs} points damage. The current enemy HP is {orc_hp_total}.')
                continue          
            
        # player chose potions with first attack by orcs
        elif resp.lower() == 'potion':
            use_potions()
            continue

        # player chose to retreat
        elif resp.lower() == 'retreat' and side_corridor_counter > 0:
            side_corridor_counter -= 1
            fight = False
            time.sleep(1)
            print('\nYou retreated from the fight.')
            return
        elif resp.lower() == 'retreat' and main_room_1_counter > 0:
            main_room_1_counter -= 1
            fight = False
            time.sleep(1)
            print('\nYou retreated from the fight.')
            return
        elif resp.lower() == 'retreat' and main_room_2_counter > 0:
            main_room_2_counter -= 1
            fight = False
            time.sleep(1)
            print('\nYou retreated from the fight.')
            return
        elif resp.lower() == 'retreat' and main_room_3_counter >0:
            main_room_3_counter -= 1
            fight = False
            time.sleep(1)
            print('\nYou retreated from the fight.')
            return
            
        # wrong input
        else:
            time.sleep(1)
            print(f'\nInvalid input. Try again.')
            continue
    

def event1():
    time.sleep(1)
    print("\nAs you walk down the cave's long main corridor, you get the feeling that someone is watching you."
          "\nPiercing glares are shooting at you from all directions and the foul stench of rotten flesh and"
          "\nmiasma invades your nostrils. Your eyes water as your sinuses start burning from the stench. And"
          "\nthere was it: The loud roar of your greatest nightmare: orcs." + '"Please, anything but orcs,"' + 
          "\nyou quietly said to yourself. You knew your prayers could not be heard from in here. So you"
          "\nmustered all your courage and pressed onward.")
    return
    

def event2():
    print("\n*squeek squeek squeek* You jumped as a mischief of rats scurried between your feet"
          "\nOne of your feet landed on one and you flattened her with a disgustingly wet splat."
          "\nThe remaining rats did not seem to notice that one of their siblings has been squashed"
          "\nunder your foot and they scurried into the darkness just as quickly as they had arrived."
          "\nAt least they had themselves. If you could choose between being yourself and one of these"
          "\nrats, you would definitely prefer being a rat. But day dreaming and wishing upon stars"
          "\nstill has not brought you out of this cave. You must find the exit. And you can feel that"
          "\nyou are very close")
    return


def end():
    global achievement
    global game_runs
    
    time.sleep(1)
    print('\nCreator: lbingus')
    time.sleep(1)
    print('\nThank you very much for playing this little game I made <3')
    
    if achievement is True:
        print('\nAchievement: Goat Simulator')
    else:
        pass
    
    game_runs = False   # exits the main while loop
    
    print('\nTHE END')
    
    time.sleep(8)
    
    sys.exit()  


# ---------------
# FUNCTIONS END
# ---------------


if __name__ == '__main__':
    game_runs = True
    
    while game_runs is True:
        print('=' * 92)
        print('VERY IMPORTANT!!'
              '\nThis game does not have a save function. If you die, you have to play the entire game again.'
              '\nYour stats are generated randomly. So is the number of enemies you face at every instance.')
        print('=' * 92)
        x = input('\nIf you have no problem with this, please press <Enter>.\n')
        if x == '':
            # generates stats randomly
            hp = 100
            strength = rd.randint(0, 20)
            intel = rd.randint(0, 20)
            init = rd.randint(0, 20)
            stealth = rd.randint(0, 20) 
            bag = dict()
            achievement = False    

            user_stats = {'HP': hp,
                          'Strength': strength,
                          'Intelligence': intel,
                          'Initiative': init,
                          'Stealth': stealth
                          }
            print_user_stats_table()
            time.sleep(1)

            # choose character class prompt
            class_modifiers = {'Barbarian': ('+3 STR', '-2 INT'),
                               'Bard': ('+3 INIT', '-2 STL'),
                               'Rogue': ('+3 STL', '-2 INIT'),
                               'Wizard': ('+3 INT', '-2 STR')
                               }
            print_class_mod_table()
            time.sleep(1)

            # adjusting stats based on class
            user_class = input('\nEnter your character class:\n')
            class_mods(user_class)
            time.sleep(1)
            print('\nGenerating new stats. Please wait...')
            time.sleep(1)
            print_user_stats_table()

            # creates user with stats attributes
            user = user(user_stats['HP'], 
                        user_stats['Strength'], 
                        user_stats['Intelligence'], 
                        user_stats['Initiative'], 
                        user_stats['Stealth'], 
                        None, 
                        0, 
                        user_class)

            # ===========
            # MAIN STORY
            # ===========

            print('\nAnd thus your adventure begins...')
            time.sleep(3)

            print('\nYou find yourself in a dimly lit cave. You cannot remember what brought you here but you can hear loud roaring from deep within'
                  '\nthe cave. It gives you a splitting headache as it is reflected off the stone walls. As the screaming ends, you try to collect'
                  '\nyourself. You pat yourself down and find that you still have your sword and a couple health potions to keep you afloat. But you'
                  '\nknow that this is not enough to get you out of this cave and face whatever made this horrible noise. You must venture deeper '
                  '\ninto the cave to get out of it. And with this realisation, you make your first step deeper into the darkness. ')

            main_room_1_counter = 0
            main_room_2_counter = 0
            main_room_3_counter = 0
            side_corridor_counter = 0
            fight = False
            main_room_1()
            break
        else:
            time.sleep(1)
            print('\nI said ' + '"please press <Enter>"' + ' you goldfish brain.\n\n')
            continue


"""
(C) lbingus 2022
Created as part of a project for a Python programming course.

I am very much aware that many things could have been better executed, however, this is everything
I have learned after only 4 weeks of daily Python classes. This game was cobbled together in only
2.5 days and I'm sure it shows. It is clunky and held together with duct tape and bedtime prayers.
However, it's something I made and I am very proud of it. I hope you enjoyed playing the game and 
if you're having a look at the source code, I salute you even more. Have a lil kiss on your noggin
and see you the next time I decide to spend too much effort on something like this <3

Love,

lbingus

GitHub: https://github.com/lbingus/code-bank
"""
