# from https://www.youtube.com/watch?v=n1nTcagXioY&t=1343&list=PLkFqzDs4R3qwP5NNpsrCFMnAewAMlJqtR&index=6
# https://files.catbox.moe/uo8e7s.png for list of question

character_1 = {
    "player_name": "MysticWarden",
    "level": 8,
    "health": 120,
    "skills": ["elemental magic", "healing", "summoning", "enchanting", "illusion"],
    "allies": ["Falconer Kael", "Sorceress Elara"],
    "quest_log": {
        "Seal the Shadow Rift": "In Progress",
        "Gather the Sacred Herbs": "Completed",
        "Escort the Diplomat to Safety": "Not Started",
        "Break the Curse of the Old King": "In Progress",
        "Recover the Lost Staff of Ages": "Not Started"
    }
}
character_2 = {
    "player_name": "ShadowRogue",
    "level": 7,
    "health": 90,
    "skills": ["stealth", "lockpicking", "backstab", "poison crafting"],
    "quest_log": {
        "Steal the Cursed Gem": "In Progress",
        "Spy on the Enemy Camp": "Completed",
        "Infiltrate the Dark Fortress": "Not Started",
        "Assassinate the Corrupt Magistrate": "In Progress",
        "Retrieve the Ancient Manuscript": "Completed",
        "Uncover the Traitor": "Not Started",
        "Lead the Siege of the Enemy City": "Completed",
    }
}
character_3 = {
    "player_name": "WarriorKing",
    "level": 10,
    "health": 150,
    "skills": ["swordsmanship", "fortification", "blacksmithing"],
    "allies": ["Knight Roland", "Archer Diana"],
    "quest_log": {
        "Conquer the Rebel Forces": "In Progress",
        "Defend the Royal Castle": "Completed",
        "Forge the Sword of Legends": "Completed"
    }
}

char_dict_list = [character_1,character_2,character_3]

## Q.1 Check if one of the player is missing their allies print out which one
print('\t\tQ.1')
# for char in char_dict_list:
#     if 'allies' not in char:
#         print(f'{char["player_name"]} do not have ' + 'allies')

# # Q.2 How many skills does each character have?
print('\t\tQ.2')
# for char in char_dict_list:
#     print(f"{char['player_name']} has {len(char['skills'])} skills")

# # Q.3 What is the type of the values of each item?
print('\t\tQ.3')
# for char in char_dict_list:
#     print(f"value types for the player \t {char['player_name']}")
#     for key,val in char.items():
#         print(f'\t type for {key} is {type(val)}')

# # Q.4 Which character has the highest level and highest HP?” ind
print('\t\tQ.4')
# highest_hp = 0
# highest_lvl = 0
# for char in char_dict_list:
#     if char['level'] > highest_lvl:
#         highest_lvl = char['level']
#         highest_lvl_plyr = char['player_name']
#     if char['health'] > highest_hp:
#         highest_hp = char['health']
#         highest_hp_plyr = char['player_name']
#
# print(f" {highest_hp_plyr} has the highest HP : {highest_hp}")
# print(f" {highest_lvl_plyr} has the highest level : {highest_lvl}")

# # Q.5 What % of quests has each character ‘Completed’?
print('\t\tQ.5')
# for char in char_dict_list:
#     completed_quest = 0
#     total_quest_num = len(char['quest_log'])
#     # count completed quests
#     for status in char['quest_log'].values():
#         if status == "Completed":
#             completed_quest += 1
#
#     completion_rate = (completed_quest/total_quest_num) * 100
#     player = char['player_name']
#     print(f"{player} has done {completed_quest} out of {total_quest_num} with the complete rate of {completion_rate:.1f}%")

# Q.6 Print out the characters in a orderly manner.
for char in char_dict_list:
    print('\nPlayer:',char['player_name'])
    print(f"\tlevel: {char['level']}")
    print(f"\thealth: {char['health']}")
    print("Skill: ")
    for skills in char['skills']:
        print(f"\t- {skills}")
    print("Quest Log: ")
    for k,v in char['quest_log'].items():
        print(f"\t- {k} : {v}")
    print('-'*50)
