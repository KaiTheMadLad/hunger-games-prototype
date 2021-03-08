# Imports

import random as rand

# Variables

name_list = ['John','Charlie','Greg','Justin','Mark','Matthew','Peter','Philip','Jamie','Rodger','Uncle']
character_list = []
locations = ['plains','forest','starting area','beach','pond','river']

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
    file = open("C:/Users/Nooblet/Desktop/girl/stroage files/"+name+".txt",'w+')
    file.write("Name: "+name+"\n")
    file.write("health: "+str(health)+"\n")
    file.write("atk: "+str(atk)+"\n")
    file.write("defen: "+str(defen)+"\n")
    file.write("luk: "+str(luk)+"\n")
    file.write("intel: "+str(intel)+"\n")
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

# Main Code

ask_number = input("How many people would you like to have? ")

for i in range(0,int(ask_number)):
    create_character()

print(character_list)
print(find_stat_value(rand.choice(character_list),'atk'))
print(find_stat_line(rand.choice(character_list),'atk'))
update_character_stat(rand.choice(character_list),'atk',4)






