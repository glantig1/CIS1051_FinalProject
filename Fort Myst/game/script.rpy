default player_health = 100
default enemy_health = 100
default inventory = []
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
default tower_items = []
default great_hall_items = ["Gate key"]
default library_items = ["Red Potion","Blue Potion","Yellow Potion"]
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
default entrance_state = "entrance"


init python:
    # I should have done this for more things
    def formalize_scene_name(current_room):
        formalized_names = {
            "entrance": "Entrance",
            "passage": "Passageway",
            "courtyard": "Courtyard",
            "smithy": "Smithy",
            "stables": "Stables",
            "cellar": "Cellar",
            "gatehouse": "Gatehouse",
            "kitchen": "Kitchen",
            "armory": "Armory",
            "tower": "Tower",
            "great_hall": "Great Hall",
            "throne_room": "Throne Room",
            "library": "Library",
            "end": "End"
        }
        return formalized_names[current_room]

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




label start:
    scene black
    $ current_room = "entrance"
    "In a world of magic and monsters, the job of a ranger takes on a bit of a different meaning."
    "You've been tasked with investigating the state of Fort Myst since they've gone silent for some months"
    "As a ranger, you're no stranger to monster ravaged outposts, but this is different"
    "The castle stands, but aged far past what it should be."
    "Rounding the perimeter, you find no other entrance than the front gate."
    jump room_hub

# https://www.renpy.org/doc/html/screens.html
# https://www.renpy.org/doc/html/gui.html
label inventory_menu:
    if inventory:
        call screen inventory_screen
        jump room_hub
    else:
        "Your inventory is empty."
        jump room_hub
    return


label investigate:
    if room_investigate[current_room] == 0:
        $ room_investigate[current_room] = 1
    if current_room == "gatehouse":
        if room_investigate[current_room] == 1:
            $ room_investigate[current_room] = 2
            "You see a mechanism with a slotted insert"
            if "Gate key" in inventory:
                "Do you insert the Gate Key?"
                menu:
                    "Yes":
                        $ room_state["entrance"] = 2
                        $ room_investigate[current_room] = 3
                        "The grinding of gears fills the room as a rumble from outside shakes the room."
                        jump room_hub
                    "No":
                        jump room_hub
        elif room_investigate[current_room] == 2:
            "The mechanism remains."
            if "Gate key" in inventory:
                "Do you insert the Gate Key?"
                menu:
                    "Yes":
                        $ room_state["entrance"] = 2
                        $ room_investigate[current_room] = 3 
                        "The grinding of gears fills the room as a rumble from outside shakes the room."
                        jump room_hub
                    "No":
                        jump room_hub
        else: 
            "The mechanism seems broken"
    elif current_room == "kitchen":
        if potionColor(pot) != "":
            "The pot has [potionColor(pot)]"
        else:
            "The pot is empty"
        if room_investigate["cellar"] == 2:
            menu:
                "Add Red Potion" if "Red Potion" in inventory:
                    $ pot.append("Red Potion")
                    $ inventory.remove("Red Potion")
                    jump investigate
                "Add Blue Potion" if "Blue Potion" in inventory:
                    $ pot.append("Blue Potion")
                    $ inventory.remove("Blue Potion")
                    jump investigate
                "Add Yellow Potion" if "Yellow Potion" in inventory:
                    $ pot.append("Yellow Potion")
                    $ inventory.remove("Yellow Potion")
                    jump investigate
                "Add Green Potion" if "Green Potion" in inventory:
                    $ pot.append("Green Potion")
                    $ inventory.remove("Green Potion")
                    jump investigate
                "Add Purple Potion" if "Purple Potion" in inventory:
                    $ pot.append("Purple Potion")
                    $ inventory.remove("Purple Potion")
                    jump investigate
                "Add Orange Potion" if "Orange Potion" in inventory:
                    $ pot.append("Orange Potion")
                    $ inventory.remove("Orange Potion")
                    jump investigate
                "Add Black Potion" if "Black Potion" in inventory:
                    $ pot.append("Black Potion")
                    $ inventory.remove("Black Potion")
                    jump investigate
                "Scoop":
                    if potionColor(pot) != "":
                        "You scooped [potionColor(pot)] liquid"
                        $ inventory.append(potionColor(pot)+" Potion")
                        $ pot = []
                    jump investigate
                "Leave":
                    jump room_hub
        else: 
            menu:
                "Leave":
                    jump room_hub
    elif current_room == "armory":
        if room_investigate[current_room] == 1:
            $ room_investigate[current_room] = 2
            "You find a piece of paper stuck under some planks of wood. Do you read it?"
            menu:
                "Yes":
                    $ room_investigate[current_room] = 3
                    $ inventory.append(armory_items[0])
                    "Sword Hilt Added to Inventory"
                "No": 
                    jump room_hub
        elif room_investigate[current_room] == 2:
            "The Sword Hilt remains. Do you take it?"
            menu:
                "Yes":
                    $ room_investigate[current_room] = 3
                    $ inventory.append("Sword Hilt")
                    "Sword Hilt Added to Inventory"
                "No": 
                    jump room_hub

        else:
            "The armory lays bare"
            jump room_hub
    elif current_room == "tower":
        if room_investigate[current_room] == 1:
            $ room_investigate[current_room] = 2
            "You find a piece of paper stuck under some planks of wood. Do you read it?"
            menu:
                "Yes":
                    jump poem
                "No": 
                    jump room_hub
        else:
            "The poem remains. Do you read it?"
            menu:
                "Yes":
                    jump poem
                "No": 
                    jump room_hub
    elif current_room == "library":
        if room_investigate[current_room] == 1:
            $ room_investigate[current_room] = 2
            "You find A Variety of Colored Potions"
            "Red Potion Added to Inventory"
            $ inventory.append(library_items[0])
            "Blue Potion Added to Inventory"
            $ inventory.append(library_items[1])
            "Yellow Potion Added to Inventory"
            $ inventory.append(library_items[2])
            "You also find an inscription on the wall. Do you read it?"
            menu:
                "Yes":
                    jump inscription
                "No": 
                    jump room_hub
        else:
            "The inscription remains. Do you read it?"
            menu:
                "Yes":
                    jump inscription
                "No": 
                    jump room_hub
    elif current_room == "smithy":
        "There is a forge, ready and primed at the center of this room"
        if len(forge)>0:
            "The forge has items"
        else:
            "The forge is empty"
        
        if room_investigate["cellar"] == 2:
            menu:
                "Add Pointed Mold" if "Pointed Mold" in inventory and ("Mysterious Object" in inventory or "Mysterious Object" in forge) and len(forge)<2:
                    $ forge.append("Pointed Mold")
                    $ inventory.remove("Pointed Mold")
                    jump investigate
                "Add Spherical Mold" if "Spherical Mold" in inventory and ("Mysterious Object" in inventory or "Mysterious Object" in forge) and len(forge)<2:
                    $ forge.append("Spherical Mold")
                    $ inventory.remove("Spherical Mold")
                    jump investigate
                "Add Cube Mold" if "Cube Mold" in inventory and ("Mysterious Object" in inventory or "Mysterious Object" in forge) and len(forge)<2:
                    $ forge.append("Cube Mold")
                    $ inventory.remove("Cube Mold")
                    jump investigate
                "Add Blade" if "Blade" in inventory and len(forge)<2:
                    $ forge.append("Blade")
                    $ inventory.remove("Blade")
                    jump investigate
                "Add Jewel" if "Jewel" in inventory and len(forge)<2:
                    $ forge.append("Jewel")
                    $ inventory.remove("Jewel")
                    jump investigate
                "Add Brick" if "Brick" in inventory and len(forge)<2:
                    $ forge.append("Brick")
                    $ inventory.remove("Brick")
                    jump investigate
                "Add Mysterious Object" if "Mysterious Object" in inventory and len(forge)<2:
                    $ forge.append("Mysterious Object")
                    $ inventory.remove("Mysterious Object")
                    jump investigate
                "Add Red Potion" if "Red Potion" in inventory and len(forge)<2:
                    $ forge.append("Red Potion")
                    $ inventory.remove("Red Potion")
                    jump investigate
                "Add Blue Potion" if "Blue Potion" in inventory and len(forge)<2:
                    $ forge.append("Blue Potion")
                    $ inventory.remove("Blue Potion")
                    jump investigate
                "Add Yellow Potion" if "Yellow Potion" in inventory and len(forge)<2:
                    $ forge.append("Yellow Potion")
                    $ inventory.remove("Yellow Potion")
                    jump investigate
                "Add Green Potion" if "Green Potion" in inventory and len(forge)<2:
                    $ forge.append("Green Potion")
                    $ inventory.remove("Green Potion")
                    jump investigate
                "Add Purple Potion" if "Purple Potion" in inventory and len(forge)<2:
                    $ forge.append("Purple Potion")
                    $ inventory.remove("Purple Potion")
                    jump investigate
                "Add Orange Potion" if "Orange Potion" in inventory and len(forge)<2:
                    $ forge.append("Orange Potion")
                    $ inventory.remove("Orange Potion")
                    jump investigate
                "Add Black Potion" if "Black Potion" in inventory and len(forge)<2:
                    $ forge.append("Black Potion")
                    $ inventory.remove("Black Potion")
                    jump investigate
                "Add Red Blade" if "Red Blade" in inventory and len(forge)<2:
                    $ forge.append("Red Blade")
                    $ inventory.remove("Red Blade")
                    jump investigate
                "Add Blue Blade" if "Blue Blade" in inventory and len(forge)<2:
                    $ forge.append("Blue Blade")
                    $ inventory.remove("Blue Blade")
                    jump investigate
                "Add Yellow Blade" if "Yellow Blade" in inventory and len(forge)<2:
                    $ forge.append("Yellow Blade")
                    $ inventory.remove("Yellow Blade")
                    jump investigate
                "Add Green Blade" if "Green Blade" in inventory and len(forge)<2:
                    $ forge.append("Green Blade")
                    $ inventory.remove("Green Blade")
                    jump investigate
                "Add Purple Blade" if "Purple Blade" in inventory and len(forge)<2:
                    $ forge.append("Purple Blade")
                    $ inventory.remove("Purple Blade")
                    jump investigate
                "Add Orange Blade" if "Orange Blade" in inventory and len(forge)<2:
                    $ forge.append("Orange Blade")
                    $ inventory.remove("Orange Blade")
                    jump investigate
                "Add Black Blade" if "Black Blade" in inventory and len(forge)<2:
                    $ forge.append("Black Blade")
                    $ inventory.remove("Black Blade")
                    jump investigate
                "Add Sword Hilt" if "Sword Hilt" in inventory and len(forge)<2:
                    $ forge.append("Sword Hilt")
                    $ inventory.remove("Sword Hilt")
                    jump investigate
                "Create" if len(forge) == 2:
                    if anvil(forge) != "":
                        "You created [anvil(forge)]"
                        $ inventory.append(anvil(forge))
                        $ forge = []
                    jump investigate
                "Take Back Items" if len(forge)>0:
                    $ inventory.extend(forge)
                    $ forge = []
                    jump investigate
                "Leave":
                    jump room_hub
        else: 
            menu:
                "Leave":
                    jump room_hub
    elif current_room == "stables":
        "You investigate [formalize_scene_name(current_room)]"
    elif current_room == "cellar":
        "You stand in a damp cellar"
        if room_investigate[current_room] == 1:
            $ room_investigate[current_room] = 2
            "You find A Variety of metal molds"
            "Pointed Mold Added to Inventory"
            $ inventory.append(cellar_items[0])
            "Spherical Mold Added to Inventory"
            $ inventory.append(cellar_items[1])
            "Cube Mold Added to Inventory"
            $ inventory.append(cellar_items[2])
            "You also find a book beside them. Do you read it?"
            menu:
                "Yes":
                    $ room_state["cellar"] = 1
                    jump book
                "No": 
                    jump room_hub
        else:
            "The book remains. Do you read it?"
            menu:
                "Yes":
                    jump book
                "No": 
                    jump room_hub
    elif current_room == "great_hall":
        if room_investigate[current_room] == 1:
            $ room_investigate[current_room] = 2
            "You walk great halls lined with crumbling arch-ways"
            "In the corner you see the glint of something (suprisingly) untarnished"
            "Its a key!"
            "Do you take it?"
            menu:
                "Yes":
                    $ room_investigate[current_room] = 3
                    $ inventory.append(great_hall_items[0])
                    "Gate Key Added to Inventory"
                "No": 
                    "The remains undisturbed"
            
        elif room_investigate[current_room] == 2:
            "The key remains. Do you take it?"
            menu:
                "Yes":
                    $ room_investigate[current_room] = 3
                    $ inventory.append(great_hall_items[0])
                    "Gate Key Added to Inventory"
                "No": 
                    "The remains undisturbed"
        else:
            "The rusted sets armour seem to whistle in chorus, but alas its just the wind"
    elif current_room == "throne_room":
        if room_investigate[current_room] == 1:
            $ room_investigate[current_room] = 2
            "You stand in a throne room. Banners hang on the walls, tattered and faded."
            "Set at the back of the room rests a throne. Though it should be empty, abandonded ass the rest of the castle, you spot something strange resting on it"
            "As you approach you behold writhing mass, glowing in shifting, pearlecent colors"
            "Do you take it?"
            menu:
                "Yes":
                    $ room_investigate[current_room] = 3
                    $ inventory.append(throne_room_items[0])
                    "Mysterious Object Added to Inventory"
                "No": 
                    "The Mysterious Object continues to writhe"
            
        elif room_investigate[current_room] == 2:
            "The Mysterious Object remains. Do you take it?"
            menu:
                "Yes":
                    $ room_investigate[current_room] = 3
                    $ inventory.append(throne_room_items[0])
                    "Mysterious Object Added to Inventory"
                "No": 
                    "The Mysterious Object continues to writhe"
        else:
            "The throne lays bare, the rooms hums in silence"
    else: 
        "There is nothing here of note."
    jump room_hub



label room_hub:
    scene expression current_room at center:
        zoom 2.0  
        xalign 0.5
        yalign 0.5
    "You are in the [formalize_scene_name(current_room)]."
    if room_state["entrance"] == 0 and current_room == "passage":
        "Suddenly the Entrance Slams Shut!"
        $ room_state["entrance"] = 1
    elif room_state["entrance"] == 2 and current_room == "passage":
        $ room_state["entrance"] = 3
        "The Entrance is open!"
    menu:
        "Navigate":
            jump expression current_room 
        "Inventory":
            call inventory_menu
        "Investigate":
            jump investigate
        # "Interact":
        #     jump interact


label entrance:
    menu:
        "Go to Passage":
            $ current_room = "passage"
            jump room_hub
        "Stay Here":
            jump room_hub


label passage:
    if room_state["entrance"] == 3:
        "Freedom is nigh"
    menu:
        "Go to courtyard":
            $ current_room = "courtyard"
            jump room_hub
        "Go to entrance":
            if room_state["entrance"] == 1:
                "The entrance is barred!"
                jump room_hub
            else:
                # $ current_room = "end"
                jump end
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
    menu:
        "Go to gatehouse":
            $ current_room = "gatehouse"
            jump room_hub
        "Stay Here":
            jump room_hub

label armory:
    menu:
        "Go to gatehouse":
            $ current_room = "gatehouse"
            jump room_hub
        "Stay Here":
            jump room_hub

label tower:
    menu:
        "Go to gatehouse":
            $ current_room = "gatehouse"
            jump room_hub
        "Stay Here":
            jump room_hub

label poem:
    "There once was a Fae\nIt hid amongst Hay\nHoarding round Jewels of Green with Envy"
    "Then there came along\na knight o so strong\nwith a wrought iron sword; very heavy"
    "From bones came a form\ncolors changing, warm\npressed to shapes against any enemy"
    "Castle's now cursed\nSon seen dead, perversed\nEven Fae seek vengeance quite readily"
    jump room_hub

label book:
    "Skimming through the book, most of it seems to be faded, barley visible text."
    "One page is intact, however."
    "It reads: " 
    "\"The Alchemist cleared my smithy for his personal research.\""
    "\"Apparently the substance needs a furnace's heat to be made into anything useful.\""
    "\"Don't know why its any different than mmetal, but then again i did hear him cackle about \'his potions changing everything\'.\""
    "\"I made the molds he asked for, but for now I am called away to fix some armor.\""
    "\"Ill stow them away in the cellar for now, I don't want get fired because a servant got handsy.\""
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

label library:
    menu:
        "Go to Great Hall":
            $ current_room = "great_hall"
            jump room_hub
        "Stay Here":
            jump room_hub

label inscription:
    "FOLLOW THESE INSTRUCTIONS MY ACOLYTES"
    "EACH ELEMENT HAS A COLOR AND MIXES TO MAKE MORE COMPLEX ELEMENTS"
    "EVEN A SCULLERY CAN ENACT MYSTIC POLIMERIZATION"
    "WITH GREAT HEAT THESE WILL IMBUE THE MOST RESONANT OF MATERIALS WITH ANY PROPERTY"
    jump room_hub

label throne_room:
    menu:
        "Go to Great Hall":
            $ current_room = "great_hall"
            jump room_hub
        "Stay Here":
            jump room_hub
        

label end:
    scene expression "end" at center:
        zoom 2.0  
        xalign 0.5
        yalign 0.5
    "You rush out, and are blinded by the difference in light."
    "Before your eyes adjust, you feel it before you see it"
    "A Fae Creature stands before you."
    "What do you do?"
    menu:
        "Fight":
            jump fight
        "Plea":
            jump plea


label fight:
    if player_health <= 0:
        "You fall to the ground, defeated."
        jump death
    elif enemy_health <= 0:
        "You did it!"
        jump fight_win

    "Your Health: [player_health] || The Creature's Health: [enemy_health]"

    $ import random
    $ enemy_move = renpy.random.choice(["attack", "parry", "grab"])

    if enemy_move == "attack":
        "The create tenses, ready to strike."
    elif enemy_move == "parry":
        "The creature watches you closely."
    elif enemy_move == "grab":
        "The creature lowers its stance as if ready to lunge at you."
    "What do you do?"
    menu:
        "Attack":
            $ player_move = "attack"
        "Parry":
            $ player_move = "parry"
        "Grab":
            $ player_move = "grab"

    if player_move == enemy_move:
        "You both clash, neither winning out."
    elif (player_move == "attack" and enemy_move == "grab") or (player_move == "parry" and enemy_move == "attack") or (player_move == "grab" and enemy_move == "parry"):
        if "Black Sword" in inventory:
            if player_move == "attack": 
                "You damage the creature severly"
                $ enemy_health -= 25
            elif player_move == "parry":
                "You deflect the creature's attack, damaging it with it own strength"
                $ enemy_health -= 25
            elif player_move == "grab":
                "You take advantage of the creature's hesitance, damaging it"
                $ enemy_health -= 25
        else:
            "Your attack barely seems to land and are damaged from the recoil"
            $ enemy_health -= 1
            $ player_health -= 10
        
    else:
        "Your move is countered!"
        $ player_health -= 25

    jump fight

label plea:
    menu:
        "Say: \"Can I leave?\"":
            jump death
        "Prostrate":
            if "Green Jewel" in inventory:
                jump plea_2
            else:
                jump death

label plea_2:
    "The creature inspects you"
    menu:
        "Say: \"May I pass?\"":
            jump death
        "Offer Green Jewel" if "Green Jewel" in inventory:
            jump plea_3

label plea_3:
    "The creature sobs"
    menu:
        "Say: \"Is this enough?\"":
            jump death
        "Say: \"This will never be enough\"":
            jump plea_4
        "Sprint Away":
            jump death

label plea_4:
    "The creature regards you"
    menu:
        "Say: \"You're just going to kill me anyway\"":
            jump death
        "Say: \"What was done to you was a travesty\"":
            jump plea_5
        "Say: \"What was done to your child was a travesty\"":
            jump plea_6
        "Sprint Away":
            jump death

label plea_5:
    "The creature becomes flush with rage"
    menu:
        "Say: \"This is what you hoard right?\"":
            jump death
        "Say: \"But I am not the one who did this\"":
            jump plea_6
        "Sprint Away":
            jump death

label plea_6:
    "The creature becomes composed"
    menu:
        "Say: \"Take this as something to remember him by.\"":
            "The creature bows its head"
            jump plea_7
        "Walk Away":
            jump death
label plea_7:
    "What do you do?"
    menu:
        "Bow in return":
            "The creature bows its head"
            jump plea_win
        "Reach out and touch it":
            "The creature is perplexed by your audacity, shoving you away"
            jump plea_win
        "Walk Away":
            jump plea_win
        "Attack it!":
            jump death
        


label fight_win:
    "You defeated the creature and successfully escaped"
    "Reading the poem taught you how to slay its kind, though maybe not what happned in the castle."
    "While showered with prestige once returning home, you can't shake a sense of unease."
    return

label plea_win:
    "You are granted leave, a boon for having more honor than those who once inhabited this castle"
    return

label death:
    "You do not make it, falling to a fate best undescribed."
    return

