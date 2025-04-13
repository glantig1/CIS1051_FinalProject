default inventory = []
default current_room = "beginning_entrance"
default current_investigate = "You investigating room 1."


## probably going to want a set of functions that define the state of rooms

label start:
    scene black
    $ current_room = "beginning_entrance"
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
    "[current_investigate.capitalize()]."
    jump room_hub

label interact:
    "You try interacting with your environment."
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


label beginning_entrance:
    $ current_investigate = "You investigating."
    menu:
        "Go to Passage":
            $ current_room = "passage"
            jump room_hub
        "Stay Here":
            jump room_hub

label passage:
    menu:
        "Go to courtyard":
            $ current_room = "passage"
            jump room_hub
        "Go to beginning_entrance":
            $ current_room = "beginning_entrance"
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