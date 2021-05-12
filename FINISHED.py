# Imports
import shutil
import random as rand
import time as t
import os
# Variables
log = False
name_list = ['John','Charlie','Greg','Justin','Mark','Matthew','Peter','Philip','Jamie','Rodger','Uncle','Sarah','Emily','Megan','Melissa','Avery','Alex','Alexa','Javani','caleb','Harvey','Ava','Elvis','Kat','Vitamin D']
character_list = []
locations = ['plains','forest','starting area','beach','pond','river','big hill','tall tree forest','huge clearing in forest','stream']
item_list = ['spear','bow','knife','food','water','hatchet','nuts','medical herbs']
weapon_list = ['spear','bow','knife','hatchet']
supply_list = ['food','water','nuts','medical herbs']
random_person = []
infected = []
chosen_name_list = []
disease_damage = 1.5
ask_death = 'N'
# Functions

def create_character():
    #if the chosen_name_list has a name in it
    if len(chosen_name_list) >= 1:
        # pick random name
        name = rand.choice(chosen_name_list)
        chosen_name_list.remove(name)
    else:
        name = rand.choice(name_list)
        name_list.remove(name)
    advanced_print(name)
    atk = rand.randrange(1,11)
    defen = rand.randrange(1,11)
    luk = rand.randrange(1,11)
    intel = rand.randrange(1,11)
    health = 20
    location = 'pedistal'
    file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+name+".txt",'w+')
    file.write("Name: "+name+"\n")
    file.write("loc: "+location+"\n")
    file.write("health: "+str(health)+"\n")
    file.write("atk: "+str(atk)+"\n")
    file.write("defen: "+str(defen)+"\n")
    file.write("luk: "+str(luk)+"\n")
    file.write("intel: "+str(intel)+"\n")
    file.write('inven: ')
    character_list.append(name)
    file.close()

def advanced_print(content):
    #if you want a log
    if log == True:
        #print and add the content to the log file
        print(content)
        file = open("C:/Users/Nooblet/Desktop/girl/stroage files/log.txt",'a')
        file.write(f"{content}\n")
        file.close
    else:
        #if you dont want a log, just print it
        print(content)

def update_character_stat(char,stat,new_stat):
    #open file in read mode
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r')
    lines = opened_file.readlines()
    #find the stat line
    line = find_stat_line(char,stat)
    #change stat
    lines[line] = stat+": "+str(new_stat)+'\n'
    #open file in write mode
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'w')
    #write the lines
    opened_file.writelines(lines)
    opened_file.close()

def find_stat_line(char,stat):
    num = -1
    #open file
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        #for all the stuff in lines
        for attribute in lines:
            #increase the line number
            num += 1
            #if stat is in the line
            if stat in attribute:
                #return the line number
                return int(num)

def find_stat_value(char,stat):
    #open file
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        #for all the stuff in lines
        for attribute in lines:
            #if the stat is in the line
            if stat in attribute:
                #split after the colon and return the stat
                num = attribute.split(stat+': ')
                result = num.pop()
                return float(result)
    
def get_location(char):
    #open file
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
         #for all the stuff in lnes
        for attribute in lines:
            #if location is in the line
            if 'loc' in attribute:
                loc = attribute.split('loc: ')
                loc2 = loc.pop()
                result = loc2[:-1]
                #return the location
                return str(result)

def check_item(char,item):
    #Open File
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        # For all the stuff in each line
        for attribute in lines:
            # if the item is in the line, return true or false
            if item in attribute:
                return True
            else:
                return False

''' OKAY LET ME BE COMPLETELY HONEST.
I WROTE THE INVENTORY CODE AT LIKE 1-5 AM
I DON'T GET IT AT ALL ANYMORE AND MY VARIABLE NAMES CONFUSE ME MORE
LIKE WHAT THE FUCK IS NEWPT2 ?? IS IT JUST NEW BUT THE NEWEST NEW ??
'''

def get_inventory(char):
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if 'inven' in attribute:
                inven_list1 = []
                inven_list2 = []
                inven_list = attribute.split('inven: ')
                inven_list = inven_list[1].split(', ')
                for i in inven_list:
                    inven_list1.append(i.split(',')[0])
                for i in inven_list1:
                    inven_list2.append(i.split('\n')[0])
                return inven_list2

def get_inventory_size(char):
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if 'inven' in attribute:
                inven_list1 = []
                inven_list2 = []
                inven_list = attribute.split('inven: ')
                inven_list = inven_list[1].split(', ')
                for i in inven_list:
                    inven_list1.append(i.split(',')[0])
                for i in inven_list1:
                    inven_list2.append(i.split('\n')[0])
                return len(inven_list2)
        

def add_item(char,item):
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r')
    lines = opened_file.readlines()
    line = find_stat_line(char,'inven')
    if lines[line] == 'inven: ':
        lines[line] = str('inven: '+item+'\n')
    else:
        opened_line1 = lines[line]
        if opened_line1[len(opened_line1)-1] == '\n':
            opened_line2 = opened_line1[:-1]
        else:
            opened_line2 = opened_line1
        opened_line2 += ', '+item+'\n'
        lines[line] = opened_line2
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'w')
    opened_file.writelines(lines)
    opened_file.close()

def remove_item(char,item):
    #WHAT THE FUCK IS THIS
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r')
    lines = opened_file.readlines()
    line = find_stat_line(char,'inven')
    for attribute in lines:
        if 'inven' in attribute:
            inven_list1 = []
            new = []
            inven_list = attribute.split('inven: ')
            inven_list = inven_list[1].split(', ')
            for i in inven_list:
                inven_list1.append(i.split(', ')[0])
            for i in inven_list1:
                new.append(i.split('\n')[0])
            new.remove(item)
            newpt2 = ""
            num = 0
            for i in new:
                num += 1
                if len(new) == num:
                    newpt2 += f"{i}"
                else:
                    newpt2 += f"{i}, "
            lines[line] = f"inven: {newpt2}"
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'w')
    opened_file.writelines(lines)
    opened_file.close()

''' OKAY LET ME BE COMPLETELY HONEST.
I WROTE THE INVENTORY CODE AT LIKE 1-5 AM
I DON'T GET IT AT ALL ANYMORE AND MY VARIABLE NAMES CONFUSE ME MORE
LIKE WHAT THE FUCK IS NEWPT2 ?? IS IT JUST NEW BUT THE NEWEST NEW ??
'''

def random_char():
    #just pick a random character
    return rand.choice(character_list)

def random_char_attack(victim):
    failed = 0
    get_character = True
    rand_char = random_char()
    while get_character:
        if not rand_char in random_person:
            victim_location = get_location(victim)
            rand_location = get_location(rand_char)
            if victim_location == rand_location:
                random_person.append(rand_char)
                get_character = False
            else:
                failed += 1
                if failed >= len(character_list):
                    get_character = False
                    random_person.append('none')
        else:
            if rand_char == victim:
                random_person.append(rand_char)
                get_character = False

def heal_char(char,num):
    current_health = find_stat_value(char,'health')
    healing_needed = 20-current_health
    if not healing_needed >= num:
        update_character_stat(char,'health',current_health+healing_needed)
        advanced_print(f"{char} has healed themselves for {healing_needed}!")
    else:
        update_character_stat(char,'health',current_health+num)
        advanced_print(f"{char} has healed themselves for {num}!")

def attack(attacker,victim):
    do_damage(attacker,victim)
    if calc_percent_luck(0,attacker,'bool','+'):
        advanced_print(f"{victim} didn't retaliate!")
    else:
        advanced_print(f"{victim} retaliated!")
        do_damage(victim,attacker)
    if attacker in infected:
        if victim not in infected:
            if not calc_percent_luck(0,victim,'bool','+'):
                infected.append(victim)
                advanced_print(f"{victim} has been infected! They will now take 1.5 damage everyday until it's healed!")
    if victim in infected:
        if attacker not in infected:
            if not calc_percent_luck(0,attacker,'bool','+'):
                infected.append(attacker)
                advanced_print(f"{attacker} has been infected! They will now take 1.5 damage everyday until it's healed!")
    

def search_location_char(char,boolorlist):
    same_location = []
    for person in character_list:
        if person != char:
            char_location = get_location(char)
            person_location = get_location(person)
            if char_location == person_location:
                same_location.append(person)
    if len(same_location) >= 1:
        if boolorlist == 'bool':
            return True
        if boolorlist == 'list':
            return same_location
        else:
            advanced_print('Error: Nothing specified in search_location_char')
    else:
        advanced_print('No one was found.')

def calc_percent_luck(basep,char,boolorint,plusorminus):
    #if i'm being completely honest, i have no idea what was going through my head while making this, i'm having trouble trying to remember what this all does
    if plusorminus == '+':
        perc = basep+(find_stat_value(char,'luk')*5)
        perc = 0 + perc
        randnumber = rand.randint(0,100)
    if plusorminus == '-':
        perc = basep+(find_stat_value(char,'luk')*5)
        randnumber = rand.randint(0,100)
        perc = 100 - perc
    if randnumber > perc:
        if boolorint == 'int':
            return perc
        if boolorint == 'bool':
            return True
    else:
        if boolorint == 'bool':
            return False

def do_damage(attacker,victim):
    damage_done = calc_damage(attacker,victim,find_stat_value(attacker,'atk'))
    update_character_stat(victim,'health',find_stat_value(victim,'health')-damage_done)
    advanced_print(attacker+' has attacked '+victim+' for '+str(damage_done)+'!')

def select_two_people():
    get_character = True
    rand_char = random_char()
    while get_character:
        if not rand_char in random_person:
            random_person.append(rand_char)
            get_character = False
    get_character = True
    rand_char = random_char()
    while get_character:
        if not rand_char in random_person:
            random_person.append(rand_char)
            get_character = False

def calc_damage(attacker,victim,damage):
    defense = find_stat_value(victim,'defen')
    ED = 0
    if check_item(attacker,'bow') and ED == 0:
        ED += 3.2
    if check_item(attacker,'spear') and ED == 0:
        ED += 3
    if check_item(attacker,'hatchet') and ED == 0:
        ED += 2
    if check_item(attacker,'knife') and ED == 0:
        ED += 1.5
    if calc_percent_luck(0,attacker,'bool','-'):
        damage_reduced = ((damage+ED)*2) * ((8 * defense)/100)
        advanced_print('Critical Hit!')
        damage_done = ((damage+ED)*2) - damage_reduced
        return damage_done
    else:
        damage_reduced = (damage+ED) * ((8 * defense)/100)
        damage_done = (damage+ED) - damage_reduced
        return damage_done

def disease():
    for person in infected:
        if person in character_list:
            advanced_print(f"{person} has taken {disease_damage} damage from their disease!")
            update_character_stat(person,'health',find_stat_value(person,'health')-disease_damage)
            check_death()
        else:
            infected.remove(person)

def beginning():
    for person in character_list:
        advanced_print("|-------------------------------------------------------|")
        if rand.randint(0,100) <= 50:
            advanced_print(''+person+' went to the middle!')
            update_character_stat(person,'loc','starting area')
            #t.sleep(0.2)
            if calc_percent_luck(45,person,'bool','-'):
                item = rand.choice(item_list)
                advanced_print(f"{person} got a new item! It's a {item}!")
                add_item(person,item)
            if not calc_percent_luck(45,person,'bool','-'):
                random_person.clear()
                random_person.append(person)
                random_char_attack(person)
                if random_person[1] != 'none':
                    if not random_person[1] == person:
                        attack(random_person[1],person)
                        random_person.clear()
                    else: 
                        advanced_print(f"{person} tried to attack themselves.")
                else:
                    advanced_print('No one was there to attack him!')
            if find_stat_value(person,'health') == 20:
                advanced_print('Nothing happened to '+person+'!')
        else:
            advanced_print(' '+person+' ran away from the middle!')
            complete = True
            if len(locations) > 1:
                while complete:
                    location = rand.choice(locations)
                    if location != 'starting area':
                        update_character_stat(person,'loc',location)
                        advanced_print(f"{person} ran to {location}!")
                        complete = False
                    else:
                        complete = True
        advanced_print("|-------------------------------------------------------|")
    for person in character_list:
        complete = True
        if get_location(person) == 'starting area':
            complete = True
            if len(locations) > 1:
                while complete:
                    location = rand.choice(locations)
                    if location != 'starting area':
                        update_character_stat(person,'loc',location)
                        advanced_print(f"{person} ran to {location}!")
                        complete = False
                    else:
                        complete = True
    advanced_print('Day one complete!')

def diceroll():
    return rand.randint(1,4)

def end_game():
    if len(character_list) == 1:
        advanced_print(f"{character_list[0]} has won the hunger games!")
        advanced_print("Here are their stats!")
        with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+character_list[0]+".txt",'r') as opened_file:
            lines = opened_file.readlines()
            for attribute in lines:
                if attribute == "\n":
                    pass
                else:
                    advanced_print(attribute)
        exit()
    else:
        pass

def check_death():
    for person in character_list:
        if find_stat_value(person,'health') <= 0:
            character_list.remove(person)
            advanced_print(f"{person} has died!")
            if ask_death == 'N':
                os.remove(f"C:/Users/Nooblet/Desktop/girl/stroage files/{person}.txt")
            else:
                os.rename(f"C:/Users/Nooblet/Desktop/girl/stroage files/{person}.txt", f"C:/Users/Nooblet/Desktop/girl/stroage files/dead people/(dead){person}.txt")
            end_game()

def events():
    result = diceroll()
    if result == 1:
        location = rand.choice(locations)
        advanced_print(f"{location} has been swarmed with really angry wasps!")
        for person in character_list:
            if get_location(person) == location:
                advanced_print(f"{person} has been attacked by wasps! They were stung for 4.5 health!")
                update_character_stat(person,'health',find_stat_value(person,'health')-4.5)
                check_death()
    if result == 2:
        person = rand.choice(character_list)
        if len(infected) >= 1:
            global disease_damage
            advanced_print("The disease has mutated! It's attack has grown by .1 damage!")
            disease_damage += 0.1
        if person not in infected:
            if not len(infected) >= 1:
                infected.append(person)
                advanced_print(f"{person} has been infected! They will now take 1.5 damage everyday until it's healed!")
    if result == 3:
        advanced_print("A flash storm has covered the whole area! Watch out!")
        for person in character_list:
            if not calc_percent_luck(45,person,'bool','-'):
                update_character_stat(person,'health',find_stat_value(person,'health')-10.5)
                advanced_print(f"{person} has been struck by lightning for 10.5 damage!")
    if result == 4:
        pass

def new_day():
    check_death()
    bomb = day % 3
    if bomb == 0:
        advanced_print(f"|-----------------------Day {str(day)}-----------------------------|")
        if rand.randint(1,100) < 50:
            if len(locations) > 1:
                advanced_print(f"bombing has commenced.")
                list_chosen = rand.choice(locations)
                locations.remove(list_chosen)
                advanced_print(f"{list_chosen} has been bombed! You can't go there anymore.")
                for person in character_list:
                    if get_location(person) == list_chosen:
                        advanced_print(f"{person} has been bombed for 5 health!")
                        update_character_stat(person,'health',find_stat_value(person,'health')-5)
                        complete = True
                        if len(locations) > 1:
                            while complete:
                                location = rand.choice(locations) 
                                if location != get_location(person):
                                    update_character_stat(person,'loc',location)
                                    advanced_print(f"{person} ran to {location}!")
                                    complete = False
                                else:
                                    complete = True
            else:
                advanced_print('No bombing today.')
        else:
            advanced_print('No bombing today.')
    else:
        advanced_print('No bombing today.')
    advanced_print('Type Y to start new day')
    advanced_print(f"|-----------------------Day {str(day)}-----------------------------|")
    advanced_print("Locations available: ")
    if log == True:
        file = open("C:/Users/Nooblet/Desktop/girl/stroage files/log.txt",'a')
        file.write(str(locations))
        file.write('\n')
        file.close()
    print(*locations, sep = ", ")

    advanced_print(f"|-----------------------Day {str(day)}-----------------------------|")
    #(this is just code for if you want to wait to start the next day)
    #start_day = input()
    #if start_day == 'Y' or 'y':
    event = day % 5
    if event == 0:
        if rand.randint(1,3) == 2:
            if len(infected) >= 1:
                infect = rand.choice(infected)
                infected.remove(infect)
                advanced_print(f"{infect} has been cured!")
        events()
    disease()
    for person in character_list:
        if get_location(person) not in locations:
            advanced_print(f"{person} has been bombed for 5 health!")
            update_character_stat(person,'health',find_stat_value(person,'health')-5)
            complete = True
            while complete:
                location = rand.choice(locations) 
                if location != get_location(person):
                    update_character_stat(person,'loc',location)
                    advanced_print(f"{person} ran to {location}!")
                    complete = False
                else:
                    complete = True
        rolled_num = diceroll()
        if rolled_num == 1:
            advanced_print(f"{person} has decided to scavenge for supplies.")
            if calc_percent_luck(30,person,'bool','-'):
                random_item = rand.choice(item_list)
                if get_inventory_size(person) > 5:
                    if random_item in weapon_list:
                        if random_item in get_inventory(person):
                            advanced_print(f"{person} found another {random_item}, but decided not to take it.")
                        else:
                            advanced_print(f"{person} found {random_item}!")
                            add_item(person,random_item)
                    else:
                        advanced_print(f"{person} found {random_item}!")
                        add_item(person,random_item)
                else:
                    advanced_print(f"{person}'s bag is full!")
            else:
                advanced_print(f"{person} didn't find anything!")
            if calc_percent_luck(45,person,'bool','+'):
                if search_location_char(person,'bool'):
                    advanced_print(f"{person} has found {len(search_location_char(person,'list'))} people in {get_location(person)}!")
                    if calc_percent_luck(48,person,'bool','+'):
                        advanced_print(f"{person} is going after one of the people!")
                        attack(person,rand.choice(search_location_char(person,'list')))
            advanced_print(f"{person} has finished scavenging.")
        if rolled_num == 2:
            advanced_print(f"{person} has decided to get food and water.")
            if calc_percent_luck(50,person,'bool','-'):
                random_item = rand.choice(supply_list)
                advanced_print(f"{person} found {random_item}!")
                add_item(person,random_item)
            else:
                advanced_print(f"{person} didn't find anything!")
            if calc_percent_luck(45,person,'bool','+'):
                if search_location_char(person,'bool'):
                    advanced_print(f"{person} has found {len(search_location_char(person,'list'))} people in {get_location(person)}!")
                    if calc_percent_luck(48,person,'bool','+'):
                        advanced_print(f"{person} is going after one of the people!")
                        attack(person,rand.choice(search_location_char(person,'list')))
        if rolled_num == 3:
            advanced_print(f"{person} has decided to scout the {get_location(person)}.")
            if calc_percent_luck(50,person,'bool','+'):
                if search_location_char(person,'bool'):
                    advanced_print(f"{person} has found {len(search_location_char(person,'list'))} people in {get_location(person)}!")
                    if calc_percent_luck(48,person,'bool','+'):
                        advanced_print(f"{person} is going after one of the people!")
                        attack(person,rand.choice(search_location_char(person,'list')))
                    advanced_print(f"{person} has finished scouting, they found {len(search_location_char(person,'list'))} people.")
            else:
                advanced_print(f"{person} has finished scouting, they found nothing.")
        if rolled_num == 4:
            advanced_print(f"{person} has decided to hunt for others.")
            if search_location_char(person,'bool'):
                random_choice = rand.choice(search_location_char(person,'list'))
                attack(person,random_choice)
        else:
            advanced_print(f"{person} has decided to relax.")
            for item in supply_list:
                if item in get_inventory(person):
                    if find_stat_value(person,'health') < 20:
                        advanced_print(f"{person} has decided to use {item}!")
                        if item == 'medical herbs':
                            heal_char(person,7)
                            remove_item(person,'medical herbs')
                        if item == 'food':
                            heal_char(person,3)
                            remove_item(person,'food')
                        if item == 'water':
                            heal_char(person,5)
                            remove_item(person,'water')
                        if item == 'nuts':
                            heal_char(person,1.5)
                            remove_item(person,'nuts')
        check_death()
        advanced_print(f"|-----------------------Day {str(day)}-----------------------------|")
    for person in character_list:
        if rand.randint(1,2) == 1:
            if len(locations) > 1:
                complete = True
                while complete:
                    location = rand.choice(locations) 
                    if location != get_location(person):
                        update_character_stat(person,'loc',location)
                        advanced_print(f"{person} ran to {location}!")
                        complete = False
                    else:
                        complete = True
        else:
            advanced_print(f"{person} is going to stay in {get_location(person)}")
    else:
        end_game()

# Main Code

ask_create_log = input("Do you want a log of this game? Y or N: ")
if ask_create_log == 'Y':
    log = True
    file = open("C:/Users/Nooblet/Desktop/girl/stroage files/log.txt",'x')
    file.close()
    advanced_print("Log file created!")
else:
    print("No log for you!")

ask_number = input(f"How many people would you like to have? (The max of people for randoms is {len(name_list)}) ")
ask_if_names = input("Would you like to have custom names or random names? Y for custom N for random: ")
if ask_if_names == 'Y':
    for i in range(0,int(ask_number)):
        ask_name = input("Please give name: ")
        chosen_name_list.append(str(ask_name))
else:
    advanced_print('Random names it is!')
ask_num_locations = input("How many locations do you want removed? (there are 10 locations) ")

if not int(ask_num_locations) == 0: 
    complete = True
    num = 0    
    while complete:
        location = rand.choice(locations) 
        if location != 'starting area':
            locations.remove(location)
            advanced_print(f"{location} has been removed!")
            num += 1 
            if num == int(ask_num_locations):
                complete = False
        else:
            complete = True

t.sleep(1.2)
ask_death = input("Do you want to keep characters files after they die?  ")
if ask_death != 'N':
    try:
        #try to remove the dead people folder, if you can't 
        shutil.rmtree("C:/Users/Nooblet/Desktop/girl/stroage files/dead people")
    except:
        pass
    os.mkdir("C:/Users/Nooblet/Desktop/girl/stroage files/dead people")

for i in range(0,int(ask_number)):
    create_character()

beginning()
day = 1
while len(character_list) >= 1:
    day += 1
    new_day()
