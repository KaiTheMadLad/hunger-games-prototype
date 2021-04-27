# Imports

import random as rand
import time as t
import os
# Variables

name_list = ['John','Charlie','Greg','Justin','Mark','Matthew','Peter','Philip','Jamie','Rodger','Uncle','Sarah','Emily','Megan','Melissa','Avery','Alex','Alexa','Javani','caleb']
character_list = []
locations = ['plains','forest','starting area','beach','pond','river']
item_list = ['spear','bow','knife','food','water','hatchet','nuts','medical herbs']
weapon_list = ['spear','bow','knife','hatchet']
supply_list = ['food','water','nuts','medical herbs']
percent_list = []
damage_list = []
random_person = []
infected = []

# Functions

def create_character():
    name = rand.choice(name_list)
    name_list.remove(name)
    print(name)
    atk = rand.randrange(1,11)
    defen = rand.randrange(1,11)
    luk = rand.randrange(1,11)
    intel = rand.randrange(1,11)
    home = None
    health = 20
    location = 'pedistal'
    file = open("M:/CSP/Python/github_stuff/storage files/"+name+".txt",'w+')
    file.write("Name: "+name+"\n")
    file.write("loc: "+location+"\n")
    file.write("health: "+str(health)+"\n")
    file.write("atk: "+str(atk)+"\n")
    file.write("defen: "+str(defen)+"\n")
    file.write("luk: "+str(luk)+"\n")
    file.write("intel: "+str(intel)+"\n")
    file.write("home: "+str(home)+"\n")
    file.write('inven: ')
    character_list.append(name)
    file.close()

def update_character_stat(char,stat,new_stat):
    opened_file = open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r')
    lines = opened_file.readlines()
    line = find_stat_line(char,stat)
    lines[line] = stat+": "+str(new_stat)+'\n'
    opened_file = open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'w')
    opened_file.writelines(lines)
    opened_file.close()

def find_stat_line(char,stat):
    num = -1
    with open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            num += 1
            if stat in attribute:
                return int(num)

def find_stat_value(char,stat):
    with open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if stat in attribute:
                num = attribute.split(stat+': ')
                result = num.pop()
                return float(result)
    
def compare_stat(char1,char2,stat):
    if find_stat_value(char1,stat) > find_stat_value(char2,stat):
        return str(char1)
    else:
        return str(char2)

def get_location(char):
    with open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if 'loc' in attribute:
                loc = attribute.split('loc: ')
                loc2 = loc.pop()
                result = loc2[:-1]
                return str(result)

def get_home(char):
    with open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if 'home' in attribute:
                home = attribute.split('home: ')
                home2 = home.pop()
                result = home2[:-1]
                return str(result)

def check_item(char,item):
    with open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if item in attribute:
                return True
            else:
                return False

def get_inventory(char):
    with open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r') as opened_file:
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
    with open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r') as opened_file:
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
    opened_file = open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r')
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
    opened_file = open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'w')
    opened_file.writelines(lines)
    opened_file.close()

def remove_item(char,item):
    opened_file = open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r')
    lines = opened_file.readlines()
    line = find_stat_line(char,'inven')
    for attribute in lines:
        if 'inven' in attribute:
            inven_list1 = []
            new = []
            inven_list = attribute.split('inven: ')
            inven_list = inven_list[1].split(', ')
            #print(f"inven_list:{inven_list}")
            for i in inven_list:
                #print(f"first i:{i}")
                inven_list1.append(i.split(', ')[0])
            #print(f"inven_list1:{inven_list1}")
            for i in inven_list1:
                #print(f"second i:{i}")
                new.append(i.split('\n')[0])
            #print(f"new:{new}")
            new.remove(item)
            newpt2 = ""
            num = 0
            for i in new:
                num += 1
                if len(new) == num:
                    newpt2 += f"{i}"
                else:
                    newpt2 += f"{i}, "
            #print(f"newpt2:{newpt2}")
            lines[line] = f"inven: {newpt2}"
    opened_file = open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'w')
    opened_file.writelines(lines)
    opened_file.close()

def random_char():
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
        print(f"{char} has healed themselves for {healing_needed}!")
    else:
        update_character_stat(char,'health',current_health+num)
        print(f"{char} has healed themselves for {num}!")

def attack(attacker,victim):
    do_damage(attacker,victim)
    if calc_percent_luck(0,attacker,'bool','+'):
        print(f"{victim} didn't retaliate!")
    else:
        print(f"{victim} retaliated!")
        do_damage(victim,attacker)
    

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
            print('Error: Nothing specified in search_location_char')
    else:
        print('No one was found.')

def calc_percent_luck(basep,char,boolorint,plusorminus):
    if plusorminus == '+':
        perc = basep+(find_stat_value(char,'luk')*5)
        perc = 0 + perc
        randnumber = rand.randint(0,100)
    if plusorminus == '-':
        perc = basep+(find_stat_value(char,'luk')*5)
        randnumber = rand.randint(0,100)
        perc = 100 - perc
    if randnumber > perc:
        damage_list.append(int(perc))
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
    print(attacker+' has attacked '+victim+' for '+str(damage_done)+'!')

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
    if check_item(attacker,'spear') and ED == 0:
        ED += 3.2
    if check_item(attacker,'spear') and ED == 0:
        ED += 2.2
    if check_item(attacker,'hatchet') and ED == 0:
        ED += 2
    if check_item(attacker,'knife') and ED == 0:
        ED += 1.5
    if calc_percent_luck(0,attacker,'bool','-'):
        damage_reduced = ((damage+ED)*2) * ((8 * defense)/100)
        print('Critical Hit!')
        damage_done = ((damage+ED)*2) - damage_reduced
        damage_list.append(damage_reduced)
        return damage_done
    else:
        damage_reduced = (damage+ED) * ((8 * defense)/100)
        damage_done = (damage+ED) - damage_reduced
        damage_list.append(damage_reduced)
        return damage_done

def disease():
    for person in infected:
        if person in character_list:
            print(f"{person} has taken 1.5 damage from their disease!")
            update_character_stat(person,'health',find_stat_value(person,'health')-1.5)
            check_death()
        else:
            infected.remove(person)

def beginning():
    for person in character_list:
        print("|-------------------------------------------------------|")
        if rand.randint(0,100) <= 50:
            print(''+person+' went to the middle!')
            update_character_stat(person,'loc','starting area')
            #t.sleep(0.2)
            if calc_percent_luck(45,person,'bool','-'):
                item = rand.choice(item_list)
                print(f"{person} got a new item! It's a {item}!")
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
                        print(f"{person} tried to attack themselves.")
                else:
                    print('No one was there to attack him!')
            if find_stat_value(person,'health') == 20:
                print('Nothing happened to '+person+'!')
        else:
            print(' '+person+' ran away from the middle!')
            complete = True
            if len(locations) > 1:
                while complete:
                    location = rand.choice(locations)
                    if location != 'starting area':
                        update_character_stat(person,'loc',location)
                        print(f"{person} ran to {location}!")
                        complete = False
                    else:
                        complete = True
        print("|-------------------------------------------------------|")
    for person in character_list:
        complete = True
        if get_location(person) == 'starting area':
            complete = True
            if len(locations) > 1:
                while complete:
                    location = rand.choice(locations)
                    if location != 'starting area':
                        update_character_stat(person,'loc',location)
                        print(f"{person} ran to {location}!")
                        complete = False
                    else:
                        complete = True
    print('Day one complete!')

def diceroll():
    return rand.randint(1,4)

def end_game():
    if len(character_list) == 1:
        print('game won')
        exit()
    else:
        pass

def check_death():
    for person in character_list:
        if find_stat_value(person,'health') <= 0:
            character_list.remove(person)
            print(f"{person} has died!")
            os.remove(f"M:/CSP/Python/github_stuff/storage files/{person}.txt")
            end_game()

def events():
    result = diceroll()
    if result == 1:
        location = rand.choice(locations)
        print(f"{location} has been swarmed with really angry wasps!")
        for person in character_list:
            if get_location(person) == location:
                print(f"{person} has been attacked by wasps! They were stung for 4.5 health!")
                update_character_stat(person,'health',find_stat_value(person,'health')-4.5)
                check_death()
    if result == 2:
        person = rand.choice(character_list)
        if person not in infected:
            infected.append(person)
            print(f"{person} has been infected! They will now take 1.5 damage everyday until it's healed!")
    if result == 3:
        print("A flash storm has covered the whole area! Watch out!")
        for person in character_list:
            if not calc_percent_luck(45,person,'bool','-'):
                update_character_stat(person,'health',find_stat_value(person,'health')-10.5)
                print(f"{person} has been struck by lightning for 10.5 damage!")
    if result == 4:
        pass

def new_day():
    check_death()
    bomb = day % 3
    if bomb == 0:
        print(f"|-----------------------Day {str(day)}-----------------------------|")
        if rand.randint(1,100) < 50:
            if len(locations) > 1:
                print(f"bombing has commenced.")
                list_chosen = rand.choice(locations)
                locations.remove(list_chosen)
                print(f"{list_chosen} has been bombed! You can't go there anymore.")
                for person in character_list:
                    if get_location(person) == list_chosen:
                        print(f"{person} has been bombed for 5 health!")
                        update_character_stat(person,'health',find_stat_value(person,'health')-5)
                        complete = True
                        if len(locations) > 1:
                            while complete:
                                location = rand.choice(locations) 
                                if location != get_location(person):
                                    update_character_stat(person,'loc',location)
                                    print(f"{person} ran to {location}!")
                                    complete = False
                                else:
                                    complete = True
            else:
                print('No bombing today.')
        else:
            print('No bombing today.')
    else:
        print('No bombing today.')
    print('Type Y to start new day')
    print(f"|-----------------------Day {str(day)}-----------------------------|")
    print(str(locations))
    #start_day = input()
    #if start_day == 'Y' or 'y':
    event = day % 5
    if event == 0:
        if rand.randint(1,3) == 2:
            if len(infected) >= 1:
                infect = rand.choice(infected)
                infected.remove(infect)
                print(f"{infect} has been cured!")
        events()
    disease()
    for person in character_list:
        if get_location(person) not in locations:
            print(f"{person} has been bombed for 5 health!")
            update_character_stat(person,'health',find_stat_value(person,'health')-5)
            complete = True
            while complete:
                location = rand.choice(locations) 
                if location != get_location(person):
                    update_character_stat(person,'loc',location)
                    print(f"{person} ran to {location}!")
                    complete = False
                else:
                    complete = True
        rolled_num = diceroll()
        if rolled_num == 1:
            print(f"{person} has decided to scavenge for supplies.")
            if calc_percent_luck(30,person,'bool','-'):
                random_item = rand.choice(item_list)
                if get_inventory_size(person) > 5:
                    if random_item in weapon_list:
                        if random_item in get_inventory(person):
                            print(f"{person} found another {random_item}, but decided not to take it.")
                        else:
                            print(f"{person} found {random_item}!")
                            add_item(person,random_item)
                    else:
                        print(f"{person} found {random_item}!")
                        add_item(person,random_item)
                else:
                    print(f"{person}'s bag is full!")
            else:
                print(f"{person} didn't find anything!")
            if calc_percent_luck(45,person,'bool','+'):
                if search_location_char(person,'bool'):
                    print(f"{person} has found {len(search_location_char(person,'list'))} people in {get_location(person)}!")
                    if calc_percent_luck(48,person,'bool','+'):
                        print(f"{person} is going after one of the people!")
                        attack(person,rand.choice(search_location_char(person,'list')))
            print(f"{person} has finished scavenging.")
        if rolled_num == 2:
            print(f"{person} has decided to get food and water.")
            if calc_percent_luck(50,person,'bool','-'):
                random_item = rand.choice(supply_list)
                print(f"{person} found {random_item}!")
                add_item(person,random_item)
            else:
                print(f"{person} didn't find anything!")
            if calc_percent_luck(45,person,'bool','+'):
                if search_location_char(person,'bool'):
                    print(f"{person} has found {len(search_location_char(person,'list'))} people in {get_location(person)}!")
                    if calc_percent_luck(48,person,'bool','+'):
                        print(f"{person} is going after one of the people!")
                        attack(person,rand.choice(search_location_char(person,'list')))
        if rolled_num == 3:
            print(f"{person} has decided to scout the {get_location(person)}.")
            if calc_percent_luck(50,person,'bool','+'):
                if search_location_char(person,'bool'):
                    print(f"{person} has found {len(search_location_char(person,'list'))} people in {get_location(person)}!")
                    if calc_percent_luck(48,person,'bool','+'):
                        print(f"{person} is going after one of the people!")
                        attack(person,rand.choice(search_location_char(person,'list')))
                    print(f"{person} has finished scouting, they found {len(search_location_char(person,'list'))} people.")
            else:
                print(f"{person} has finished scouting, they found nothing.")
        if rolled_num == 4:
            print(f"{person} has decided to hunt for others.")
            if search_location_char(person,'bool'):
                random_choice = rand.choice(search_location_char(person,'list'))
                attack(person,random_choice)
        if rolled_num == 5:
            print(f"{person} has decided to try to make this area their home.")
        if rolled_num == 6 and get_home(person) != "None":
            print(f"{person} has decided to patrol their area ")
        else:
            print(f"{person} has decided to relax.")
            for item in supply_list:
                if item in get_inventory(person):
                    #print(item)
                    if find_stat_value(person,'health') < 20:
                        print(f"{person} has decided to use {item}!")
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
        print(f"|-----------------------Day {str(day)}-----------------------------|")
    for person in character_list:
        if rand.randint(1,2) == 1:
            if len(locations) > 1:
                complete = True
                while complete:
                    location = rand.choice(locations) 
                    if location != get_location(person):
                        update_character_stat(person,'loc',location)
                        print(f"{person} ran to {location}!")
                        complete = False
                    else:
                        complete = True
        else:
            print(f"{person} is going to stay in {get_location(person)}")
    else:
        end_game()

# Main Code

ask_number = input("How many people would you like to have? ")

for i in range(0,int(ask_number)):
    create_character()
 
#print(character_list)
'''
    print(find_stat_value(random_char(),'atk'))
    print(find_stat_line(random_char(),'atk'))
    update_character_stat(random_char(),'loc','plains')
    print(get_location(random_char()))
    add_item(random_char(),'spear')
    add_item(random_char(),'hatchet')
    do_damage(random_char(),random_char())
    print(damage_list) '''

beginning()
day = 1
while len(character_list) >= 1:
    day += 1
    new_day()
