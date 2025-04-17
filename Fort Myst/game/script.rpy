default inventory = ["Black Potion", "Sword Hilt", "Pointed Mold", "Mysterious Object", "Poem", "Book"]
## default inventory = []
default interact_room_items = []





default entrance_items = []
default passage_items = []
default courtyard_items = []
default smithy_items = []
default stables_items = []
default cellar_items = ["Pointed Mold","Spherical Mold","Cube Mold"]
default gatehouse_items = []
default kitchen_items = []
default armory_items = ["Sword Hilt"]
default tower_items = ["Poem"]
default great_hall_items = ["Gate key"]
default library_items = ["Book","Red Potion","Blue Potion","Yellow Potion"]
default throne_room_items = ["Mysterious Object"]




default pot = []
default forge = []

default room_state = {
    "entrance": 0,
    "passage": 0,
    "courtyard": 0,
    "smithy": 0,
    "stables": 0,
    "cellar": 0,
    "gatehouse": 0,
    "kitchen": 0,
    "armory": 0,
    "tower": 0,
    "great_hall": 0,
    "throne_room": 0,
    "library": 0
}

default room_investigate = {
    "entrance": 0,
    "passage": 0,
    "courtyard": 0,
    "smithy": 0,
    "stables": 0,
    "cellar": 0,
    "gatehouse": 0,
    "kitchen": 0,
    "armory": 0,
    "tower": 0,
    "great_hall": 0,
    "throne_room": 0,
    "library": 0
}

default current_room = "entrance"

default investigate_jump = "room_hub"
default current_investigate = "You investigating room 1."

## have a variable for state change
default entrance_state = "entrance"


init python:
    def potionColor(someList):
        if (("Red Potion" in someList and "Blue Potion" in someList and "Yellow Potion" in someList) or("Red Potion" in someList and "Green Potion" in someList) or("Blue Potion" in someList and "Orange Potion" in someList) or("Yellow Potion" in someList and "Purple Potion" in someList) or("Green Potion" in someList and "Purple Potion" in someList) or("Green Potion" in someList and "Red Potion" in someList) or("Orange Potion" in someList and "Blue Potion" in someList)or("Purple Potion" in someList and "Yellow Potion" in someList) or"Black Potion" in someList):
            return "Black"
        elif ("Red Potion" in someList and "Blue Potion" in someList ) or "Purple Potion" in someList:
            return "Purple"
        elif ("Red Potion" in someList and "Yellow Potion" in someList) or "Orange Potion" in someList:
            return "Orange"
        elif ("Blue Potion" in someList and "Yellow Potion" in someList) or "Green Potion" in someList:
            return "Green"
        elif "Red Potion" in someList:
            return "Red"
        elif "Blue Potion" in someList:
            return "Blue"
        elif "Yellow Potion" in someList:
            return "Yellow"
        else:
            return ""
    
    def anvil(forge):
        if "Pointed Mold" in forge and "Mysterious Object" in forge:
            return "Blade"
        elif "Spherical Mold" in forge and "Mysterious Object" in forge:
            return "Jewel"
        elif "Cube Mold" in forge and "Mysterious Object" in forge:
            return "Brick"
        elif "Blade" in forge and "Red Potion" in forge:
            return "Red Blade"
        elif "Blade" in forge and "Blue Potion" in forge:
            return "Blue Blade"
        elif "Blade" in forge and "Yellow Potion" in forge:
            return "Yellow Blade"
        elif "Blade" in forge and "Green Potion" in forge:
            return "Green Blade"
        elif "Blade" in forge and "Orange Potion" in forge:
            return "Orange Blade"
        elif "Blade" in forge and "Purple Potion" in forge:
            return "Purple Blade"
        elif "Blade" in forge and "Black Potion" in forge:
            return "Black Blade"
        elif "Jewel" in forge and "Red Potion" in forge:
            return "Red Jewel"
        elif "Jewel" in forge and "Blue Potion" in forge:
            return "Blue Jewel"
        elif "Jewel" in forge and "Yellow Potion" in forge:
            return "Yellow Jewel"
        elif "Jewel" in forge and "Green Potion" in forge:
            return "Green Jewel"
        elif "Jewel" in forge and "Orange Potion" in forge:
            return "Orange Jewel"
        elif "Jewel" in forge and "Purple Potion" in forge:
            return "Purple Jewel"
        elif "Jewel" in forge and "Black Potion" in forge:
            return "Black Jewel"
        elif "Brick" in forge and "Red Potion" in forge:
            return "Red Brick"
        elif "Brick" in forge and "Blue Potion" in forge:
            return "Blue Brick"
        elif "Brick" in forge and "Yellow Potion" in forge:
            return "Yellow Brick"
        elif "Brick" in forge and "Green Potion" in forge:
            return "Green Brick"
        elif "Brick" in forge and "Orange Potion" in forge:
            return "Orange Brick"
        elif "Brick" in forge and "Purple Potion" in forge:
            return "Purple Brick"
        elif "Brick" in forge and "Black Potion" in forge:
            return "Black Brick"
        elif "Sword Hilt" in forge and "Red Blade" in forge:
            return "Red Sword"
        elif "Sword Hilt" in forge and "Blue Blade" in forge:
            return "Blue Sword"
        elif "Sword Hilt" in forge and "Yellow Blade" in forge:
            return "Yellow Sword"
        elif "Sword Hilt" in forge and "Green Blade" in forge:
            return "Green Sword"
        elif "Sword Hilt" in forge and "Orange Blade" in forge:
            return "Orange Sword"
        elif "Sword Hilt" in forge and "Purple Blade" in forge:
            return "Purple Sword"
        elif "Sword Hilt" in forge and "Black Blade" in forge:
            return "Black Sword"
        else: 
            return ""

        


## probably going to want a set of functions that define the state of rooms


## going to reference https://youtu.be/c_MHMxcIpHI when attempting turn-based fight ending
## going to try a rock, paper, scissors system with attack, block, grab but the enemy telegraphs their actions

label start:
    scene black
    $ current_room = "entrance"
    "Welcome to Castle Myst"
    jump room_hub

label inventory_menu:
    if inventory:
        "You have the following items:"
        $ item_text = "\n".join(inventory)
        "[item_text]"
    else:
        "Your inventory is empty."
    jump room_hub

label investigate:
    "You investigate [current_room]"
    $ room_investigate[current_room] = 1
    jump room_hub

## re
label interact:
    if room_investigate[current_room] == 1:
        if current_room == "gate_house":
            jump interact_kitchen 
        elif current_room == "kitchen":
            jump interact_kitchen
        elif current_room == "armory":
            jump interact_armory 
        elif current_room == "tower":
            jump interact_tower
        elif current_room == "library":
            jump interact_kitchen
        elif current_room == "smithy":
            jump interact_smithy 
        elif current_room == "stables":
            jump interact_tower
        elif current_room == "cellar":
            jump interact_kitchen
        elif current_room == "great_hall":
            jump interact_great_hall
        elif current_room == "throne_room":
            jump interact_tower
        else: 
            "There is nothing to interact with"
            jump room_hub
    else: 
        "There is nothing to interact with"
        jump room_hub


label interact_kitchen:

    if potionColor(pot) != "":
        "The pot has [potionColor(pot)]"
    else:
        "The pot is empty"
    if "Book" in inventory:
        menu:
            "Add Red Potion" if "Red Potion" in inventory:
                $ pot.append("Red Potion")
                $ inventory.remove("Red Potion")
                jump interact_kitchen
            "Add Blue Potion" if "Blue Potion" in inventory:
                $ pot.append("Blue Potion")
                $ inventory.remove("Blue Potion")
                jump interact_kitchen
            "Add Yellow Potion" if "Yellow Potion" in inventory:
                $ pot.append("Yellow Potion")
                $ inventory.remove("Yellow Potion")
                jump interact_kitchen
            "Add Green Potion" if "Green Potion" in inventory:
                $ pot.append("Green Potion")
                $ inventory.remove("Green Potion")
                jump interact_kitchen
            "Add Purple Potion" if "Purple Potion" in inventory:
                $ pot.append("Purple Potion")
                $ inventory.remove("Purple Potion")
                jump interact_kitchen
            "Add Orange Potion" if "Orange Potion" in inventory:
                $ pot.append("Orange Potion")
                $ inventory.remove("Orange Potion")
                jump interact_kitchen
            "Add Black Potion" if "Black Potion" in inventory:
                $ pot.append("Black Potion")
                $ inventory.remove("Black Potion")
                jump interact_kitchen
            "Scoop":
                if potionColor(pot) != "":
                    "You scooped [potionColor(pot)] liquid"
                    $ inventory.append(potionColor(pot)+" Potion")
                    $ pot = []
                jump interact_kitchen
            "Leave":
                jump room_hub
    else: 
        menu:
            "Leave":
                jump room_hub
        
## behold the folley of man
## and ("Pointed Mold" in inventory or "Spherical Mold" in inventory or "Cube Mold" in inventory "Red Potion" in inventory or "Blue Potion" in inventory or "Yellow Potion" in inventory or "Green Potion" in inventory or "Orange Potion" in inventory or "Purple Potion" in inventory or "Black Potion" in inventory or "Mysterious Object" in inventory)
label interact_smithy:

    if len(forge)>0:
        "The forge has items"
    else:
        "The forge is empty"
    
    if "Poem" in inventory:
        menu:
            "Add Pointed Mold" if "Pointed Mold" in inventory and "Mysterious Object" in inventory:
                $ forge.append("Pointed Mold")
                $ inventory.remove("Pointed Mold")
                jump interact_smithy
            "Add Spherical Mold" if "Spherical Mold" in inventory and "Mysterious Object" in inventory:
                $ forge.append("Spherical Mold")
                $ inventory.remove("Spherical Mold")
                jump interact_smithy
            "Add Cube Mold" if "Cube Mold" in inventory and "Mysterious Object" in inventory:
                $ forge.append("Cube Mold")
                $ inventory.remove("Cube Mold")
                jump interact_smithy
            "Add Blade" if "Blade" in inventory:
                $ forge.append("Blade")
                $ inventory.remove("Blade")
                jump interact_smithy
            "Add Jewel" if "Jewel" in inventory:
                $ forge.append("Jewel")
                $ inventory.remove("Jewel")
                jump interact_smithy
            "Add Brick" if "Brick" in inventory:
                $ forge.append("Brick")
                $ inventory.remove("Brick")
                jump interact_smithy
            "Add Mysterious Object" if "Mysterious Object" in inventory:
                $ forge.append("Mysterious Object")
                $ inventory.remove("Mysterious Object")
                jump interact_smithy
            "Add Red Potion" if "Red Potion" in inventory:
                $ forge.append("Red Potion")
                $ inventory.remove("Red Potion")
                jump interact_smithy
            "Add Blue Potion" if "Blue Potion" in inventory:
                $ forge.append("Blue Potion")
                $ inventory.remove("Blue Potion")
                jump interact_smithy
            "Add Yellow Potion" if "Yellow Potion" in inventory:
                $ forge.append("Yellow Potion")
                $ inventory.remove("Yellow Potion")
                jump interact_smithy
            "Add Green Potion" if "Green Potion" in inventory:
                $ forge.append("Green Potion")
                $ inventory.remove("Green Potion")
                jump interact_smithy
            "Add Purple Potion" if "Purple Potion" in inventory:
                $ forge.append("Purple Potion")
                $ inventory.remove("Purple Potion")
                jump interact_smithy
            "Add Orange Potion" if "Orange Potion" in inventory:
                $ forge.append("Orange Potion")
                $ inventory.remove("Orange Potion")
                jump interact_smithy
            "Add Black Potion" if "Black Potion" in inventory:
                $ forge.append("Black Potion")
                $ inventory.remove("Black Potion")
                jump interact_smithy
            "Add Red Blade" if "Red Blade" in inventory:
                $ forge.append("Red Blade")
                $ inventory.remove("Red Blade")
                jump interact_smithy
            "Add Blue Blade" if "Blue Blade" in inventory:
                $ forge.append("Blue Blade")
                $ inventory.remove("Blue Blade")
                jump interact_smithy
            "Add Yellow Blade" if "Yellow Blade" in inventory:
                $ forge.append("Yellow Blade")
                $ inventory.remove("Yellow Blade")
                jump interact_smithy
            "Add Green Blade" if "Green Blade" in inventory:
                $ forge.append("Green Blade")
                $ inventory.remove("Green Blade")
                jump interact_smithy
            "Add Purple Blade" if "Purple Blade" in inventory:
                $ forge.append("Purple Blade")
                $ inventory.remove("Purple Blade")
                jump interact_smithy
            "Add Orange Blade" if "Orange Blade" in inventory:
                $ forge.append("Orange Blade")
                $ inventory.remove("Orange Blade")
                jump interact_smithy
            "Add Black Blade" if "Black Blade" in inventory:
                $ forge.append("Black Blade")
                $ inventory.remove("Black Blade")
                jump interact_smithy
            "Create":
                if anvil(forge) != "":
                    "You created placeholder"
                    $ inventory.append(anvil(forge))
                    $ forge = []
                jump interact_smithy
            "Leave":
                jump room_hub
    else: 
        menu:
            "Leave":
                jump room_hub


label interact_gate_house:
    "You try Cooking with your environment."
    jump room_hub


label room_hub:
    scene expression "bg " + current_room
    "You are in [current_room.capitalize()]."
    menu:
        "Navigate":
            jump expression current_room 
        "Inventory":
            jump inventory_menu
        "Investigate":
            jump investigate
        "Interact":
            jump interact


label entrance:
    $ current_investigate = "You investigating."
    menu:
        "Go to Passage":
            $ current_room = "passage"
            jump room_hub
        "Stay Here":
            jump room_hub


label passage:
    if room_state["entrance"] == 0:
        "Suddenly the Entrance Slams Shut!"
        $ room_state["entrance"] = 1
    menu:
        "Go to courtyard":
            $ current_room = "courtyard"
            jump room_hub
        "Go to entrance":
            if room_state["entrance"] == 1:
                "The entrance is barred!"
                jump room_hub
            else:
                $ current_room = entrace
                jump room_hub
        "Stay Here":
            jump room_hub

label courtyard:
    menu:
        "Go to Passage":
            $ current_room = "passage"
            jump room_hub
        "Go to Great Hall":
            $ current_room = "great_hall"
            jump room_hub
        "Go to GateHouse":
            $ current_room = "gatehouse"
            jump room_hub
        "Go to Smithy":
            $ current_room = "smithy"
            jump room_hub
        "Go to Stables":
            $ current_room = "stables"
            jump room_hub
        "Stay Here":
            jump room_hub

label smithy:
    menu:
        "Go to courtyard":
            $ current_room = "courtyard"
            jump room_hub
        "Stay Here":
            jump room_hub

label stables:
    menu:
        "Go to courtyard":
            $ current_room = "courtyard"
            jump room_hub
        "Go to cellar":
            $ current_room = "cellar"
            jump room_hub
        "Stay Here":
            jump room_hub

label cellar:
    menu:
        "Go to stables":
            $ current_room = "stables"
            jump room_hub
        "Stay Here":
            jump room_hub


label gatehouse:
    $ current_investigate = "You investigating."
    menu:
        "Go to couryard":
            $ current_room = "courtyard"
            jump room_hub
        "Go to kitchen":
            $ current_room = "kitchen"
            jump room_hub
        "Go to armory":
            $ current_room = "armory"
            jump room_hub
        "Go to tower":
            $ current_room = "tower"
            jump room_hub
        "Stay Here":
            jump room_hub

label kitchen:
    $ current_investigate = "You investigating."
    menu:
        "Go to gatehouse":
            $ current_room = "gatehouse"
            jump room_hub
        "Stay Here":
            jump room_hub

label armory:
    $ current_investigate = "You investigating."
    menu:
        "Go to gatehouse":
            $ current_room = "gatehouse"
            jump room_hub
        "Stay Here":
            jump room_hub

label tower:
    $ current_investigate = "You investigating."
    menu:
        "Go to gatehouse":
            $ current_room = "gatehouse"
            jump room_hub
        "Stay Here":
            jump room_hub

label great_hall:
    menu:
        "Go to Throne Room":
            $ current_room = "throne_room"
            jump room_hub
        "Go to Library":
            $ current_room = "library"
            jump room_hub
        "Go to Courtyard":
            $ current_room = "courtyard"
            jump room_hub
        "Stay Here":
            jump room_hub

label throne_room:
    menu:
        "Go to Great Hall":
            $ current_room = "great_hall"
            jump room_hub
        "Stay Here":
            jump room_hub
        

label end:
    scene black
    "Thanks for playing!"
    return




## potential way to do dynamic menus
## should probably redo inventory and interact scenes to use this
## kitchen would use this but only accept if its a potion
## smithy would use this but only accept if its a mold

# label start:

#     $ inventory = ["apple", "key", "map"]

#     "You look in your bag and see:"

#     python:
#         for item in inventory:
#             renpy.say(None, "• " + item)

#     "Which item do you want to use?"

#     python:
#         menu_items = []
#         for item in inventory:
#             menu_items.append((f"Use {item}", f"use_{item}"))

#         menu_items.append(("Never mind", "cancel"))

#         menu(menu_items)

#     return

# label use_apple:
#     "You eat the apple. Crunchy!"
#     return

# label use_key:
#     "You try the key on a nearby door."
#     return

# label use_map:
#     "You check the map. You're not lost anymore!"
#     return

# label cancel:
#     "You decide not to use anything right now."
#     return
