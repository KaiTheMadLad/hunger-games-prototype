# Imports

import random as rand

# Variables

name_list = ['John','Charlie','Greg','Justin','Mark','Matthew','Peter','Philip','Jamie','Rodger','Uncle','Sarah','Emily','Megan','Melissa','Avery','Alex','Alexa']
character_list = []
locations = ['plains','forest','starting area','beach','pond','river']
item_list = ['spear','bow','knife','food','water','hatchet']
turn = 0
percent_list = []
damage_list = []

# Functions

def create_character():
    name = rand.choice(name_list)
    name_list.remove(name)
    print(name)
    atk = rand.randrange(1,11)
    defen = rand.randrange(1,11)
    luk = rand.randrange(1,11)
    intel = rand.randrange(1,11)
    health = 20
    location = 'starting area'
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

def update_character_stat(char,stat,new_stat):
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r')
    lines = opened_file.readlines()
    line = find_stat_line(char,stat)
    lines[line] = stat+": "+str(new_stat)+'\n'
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'w')
    opened_file.writelines(lines)
    opened_file.close()

def find_stat_line(char,stat):
    num = -1
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            num += 1
            if stat in attribute:
                return int(num)

def find_stat_value(char,stat):
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if stat in attribute:
                num = attribute.split(stat+': ')
                result = num.pop()
                return int(result)
    
def compare_stat(char1,char2,stat):
    if find_stat_value(char1,stat) > find_stat_value(char2,stat):
        return str(char1)
    else:
        return str(char2)

def get_location(char):
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if 'loc' in attribute:
                loc = attribute.split('loc: ')
                loc2 = loc.pop()
                result = loc2[:-1]
                return str(result)

def check_item(char,item):
    with open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r') as opened_file:
        lines = opened_file.readlines()
        for attribute in lines:
            if item in attribute:
                return True
            else:
                return False

def add_item(char,item):
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'r')
    lines = opened_file.readlines()
    line = find_stat_line(char,'inven')
    if lines[line] == 'inven: ':
        lines[line] = 'inven: '+item+'\n'
    else:
        opened_line1 = lines[line]
        opened_line2 = opened_line1[:-1]
        opened_line2 += ', '+item+'\n'
        lines[line] = opened_line2
    opened_file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+char+".txt",'w')
    opened_file.writelines(lines)
    opened_file.close()

def random_char():
    return rand.choice(character_list)

def calc_percent_luck(basep,char,boolorint):
    perc = basep+(find_stat_value(char,'luk')*2)
    calc = rand.randint(0,100) <= perc
    if calc:
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

def calc_damage(attacker,victim,damage):
    defense = find_stat_value(victim,'defen')
    ED = 0
    if check_item(attacker,'spear') and ED == 0:
        ED += 3.2
    if check_item(attacker,'hatchet') and ED == 0:
        ED += 2
    if check_item(attacker,'knife') and ED == 0:
        ED += 1.5
    if calc_percent_luck(0,attacker,bool):
        damage_reduced = damage+ED*2 * ((4 * defense)/100)
        print('Critical Hit!')
        damage_list.append(damage_reduced)
        return damage_reduced
    if not calc_percent_luck(0,attacker,bool):
        damage_reduced = damage+ED * ((4 * defense)/100)
        damage_list.append(damage_reduced)
        return damage_reduced
    else:
        print("Error: Calculating damage failed!")

def beginning():
    for person in character_list:
        if rand.randint(0,100) <= 50:
            if calc_percent_luck(45,person,bool):
                add_item(person,rand.choice(item_list))
            if not calc_percent_luck(45,person,bool):
                


# Main Code

ask_number = input("How many people would you like to have? ")

for i in range(0,int(ask_number)):
    create_character()

print(character_list)
print(find_stat_value(random_char(),'atk'))
print(find_stat_line(random_char(),'atk'))
update_character_stat(random_char(),'loc','plains')
print(get_location(random_char()))
add_item(random_char(),'spear')
add_item(random_char(),'hatchet')
do_damage(random_char(),random_char())
print(damage_list)



