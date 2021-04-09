# Imports

import random as rand
import time as t
import os
# Variables

name_list = ['John','Charlie','Greg','Justin','Mark','Matthew','Peter','Philip','Jamie','Rodger','Uncle','Sarah','Emily','Megan','Melissa','Avery','Alex','Alexa','Javani']
character_list = []
locations = ['plains','forest','starting area','beach','pond','river']
item_list = ['spear','bow','knife','food','water','hatchet']
turn = 0
percent_list = []
damage_list = []
random_person = []

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

def add_item(char,item):
    opened_file = open("M:/CSP/Python/github_stuff/storage files/"+char+".txt",'r')
    lines = opened_file.readlines()
    line = find_stat_line(char,'inven')
    if lines[line] == 'inven: ':
        lines[line] = str('inven: '+item+'\n')
    else:
        opened_line1 = lines[line]
        opened_line2 = opened_line1[:-1]
        opened_line2 += ', '+item+'\n'
        lines[line] = opened_line2
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


def attack_random_char(attacker):
    pass


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

def beginning():
    for person in character_list:
        if rand.randint(0,100) <= 50:
            print(''+person+' went to the middle!')
            update_character_stat(person,'loc','starting area')
            t.sleep(0.2)
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
                        do_damage(random_person[1],person)
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
            while complete:
                complete = True
                location = rand.choice(locations)
                if location != 'starting area':
                    update_character_stat(person,'loc',location)
                    print(f"{person} ran to {location}!")
                    complete = False
    for person in character_list:
        complete = True
        if get_location(person) == 'starting area':
            complete = True
            while complete:
                complete = True
                location = rand.choice(locations)
                if location != 'starting area':
                    update_character_stat(person,'loc',location)
                    print(f"{person} ran to {location}!")
                    complete = False
    print('Day one complete!')

def diceroll():
    return rand.randint(4,4)

def end_game():
    if len(character_list) == 1:
        print('game won')
        exit()
    else:
        pass

def new_day():
    for person in character_list:
        if find_stat_value(person,'health') <= 0:
            character_list.remove(person)
            print(f"{person} has died!")
    end_game()
    print('Type Y to start new day')
    start_day = input()
    if start_day == 'Y' or 'y':
        for person in character_list:
            rolled_num = diceroll()
            if rolled_num == 1:
                print(f"{person} has decided to scavenge for supplies.")
            if rolled_num == 2:
                print(f"{person} has decided to get food and water.")
            if rolled_num == 3:
                print(f"{person} has decided to scout the area.")
            if rolled_num == 4:
                print(f"{person} has decided to hunt for others.")
                if search_location_char(person,'bool'):
                    random_choice = rand.choice(search_location_char(person,'list'))
                    do_damage(person,random_choice)
            if rolled_num == 5:
                print(f"{person} has decided to try to make this area their home.")
            if rolled_num == 6 and get_home(person) != "None":
                print(f"{person} has decided to patrol their area ")
            else:
                print(f"{person} has decided to relax.")
        for person in character_list:
            if rand.randint(1,2) == 1:
                complete = True
                while complete:
                    location = rand.choice(locations)
                    if location != get_location(person):
                        update_character_stat(person,'loc',location)
                        print(f"{person} ran to {location}!")
                        complete = False
            else:
                print(f"{person} is going to stay in {get_location(person)}")
    else:
        end_game()

# Main Code

ask_number = input("How many people would you like to have? ")

for i in range(0,int(ask_number)):
    create_character()

print(character_list)
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
while len(character_list) >= 1:
    new_day()
