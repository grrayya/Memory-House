import time
import sys

# --- THE DATA ---
# This is where you will write your rooms and exits.
rooms = {
    "hallway": {
        "name": "The Hallway",
        "description": "The entryway is dim. The silence here feels heavy. You can go to the 'kitchen' or the 'living room'.",
        "items": ["coat"],
        "exits": ["kitchen", "living room"]
    },
    "kitchen": {
        "name": "The Kitchen",
        "description": "The afternoon sun hits the table just like it used to. You can go back to the 'hallway'.",
        "items": ["mug"],
        "exits": ["hallway"]
    },
    "living room": {
        "name": "The Living Room",
        "description": "The dust is starting to settle on the bookshelves. You can go back to the 'hallway'.",
        "items": ["chair"],
        "exits": ["hallway"]
    }
}

# This dictionary stores the memories. 
# As you look at an object repeatedly, the game reads the next sentence in the list.
items = {
    "coat": [
        "Their coat is still on the hook. You keep expecting them to walk in and grab it.",
        "The coat is gathering dust. It looks so empty now.",
        "You gently take the coat off the hook and fold it into a box. The hallway feels a little larger."
    ],
    "mug": [
        "Their favorite coffee mug is sitting on the counter, unwashed.",
        "You washed the mug, but you can't bring yourself to put it in the cupboard.",
        "The mug is in the cupboard with the others. It's just a mug again."
    ],
    "chair": [
        "The armchair still has the imprint of where they used to sit.",
        "You try sitting in the chair. It doesn't feel the same without them across the room.",
        "You move the chair slightly to face the window. It looks nice there."
    ]
}

# This tracks how many times you've looked at an item
item_progress = {item: 0 for item in items}
current_room = "hallway"

# --- THE GAME ENGINE ---
def type_text(text):
    """Prints text slowly for a dramatic, storytelling effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

def play():
    global current_room
    
    print("\n" + "="*50)
    type_text("Welcome to the Memory House.")
    type_text("Type 'look [object]' to inspect memories, 'go [room]' to move, or 'quit' to leave.")
    print("="*50 + "\n")
    
    # Show the first room description
    type_text(rooms[current_room]["name"].upper())
    type_text(rooms[current_room]["description"])
    
    # The main game loop
    while True:
        command = input("\n> ").lower().strip().split(" ", 1)
        action = command[0]
        
        if action == "quit":
            type_text("Some memories are meant to be left for another day. Goodbye.")
            break
            
        elif action == "go":
            if len(command) < 2:
                print("Go where? (e.g., 'go kitchen')")
                continue
                
            destination = command[1]
            if destination in rooms[current_room]["exits"]:
                current_room = destination
                print("\n" + "-"*30)
                type_text(rooms[current_room]["name"].upper())
                type_text(rooms[current_room]["description"])
            else:
                print(f"You can't go to the '{destination}' from here.")
                
        elif action == "look":
            if len(command) < 2:
                print("Look at what? (e.g., 'look mug')")
                continue
                
            target = command[1]
            if target in rooms[current_room]["items"]:
                # Get how many times we've looked at this item
                progress = item_progress[target]
                descriptions = items[target]
                
                # Print the current description
                type_text(descriptions[progress])
                
                # Advance the progress, but stop at the last description (acceptance)
                if progress < len(descriptions) - 1:
                    item_progress[target] += 1
            else:
                print(f"There is no '{target}' here.")
                
        else:
            print("I don't understand that command. Try 'go [room]', 'look [object]', or 'quit'.")

# Start the game
if __name__ == "__main__":
    play()
