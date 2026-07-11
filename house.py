import time
import sys
import os

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

class Game:
    def __init__(self):
        self.room = "hallway"
        self.prog = {k: 0 for k in items}
        self.fast = os.environ.get("FAST") == "1"

    def say(self, text):
        if self.fast:
            print(text + "\n")
            return
            
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.02)
        print("\n")

    def done(self):
        return all(v == len(items[k]) - 1 for k, v in self.prog.items())

    def play(self):
        self.say("Welcome to the Memory House.")
        self.say("Type 'look', 'look [object]', 'go [room]', or 'quit'.")
        
        self.say(rooms[self.room]["name"].upper())
        self.say(rooms[self.room]["description"])
        
        try:
            while True:
                cmd = input("\n> ").lower().strip().split(" ", 1)
                act = cmd[0]
                
                if act == "quit":
                    self.say("Some memories are meant to be left for another day. Goodbye.")
                    break
                    
                elif act == "go":
                    if len(cmd) < 2:
                        print("Go where?")
                        continue
                        
                    dest = cmd[1]
                    if dest in rooms[self.room]["exits"]:
                        self.room = dest
                        self.say(rooms[self.room]["name"].upper())
                        self.say(rooms[self.room]["description"])
                    else:
                        print(f"Can't go to '{dest}'.")
                        
                elif act == "look":
                    if len(cmd) < 2:
                        self.say(rooms[self.room]["description"])
                        continue
                        
                    obj = cmd[1]
                    if obj in rooms[self.room]["items"]:
                        p = self.prog[obj]
                        self.say(items[obj][p])
                        
                        if p < len(items[obj]) - 1:
                            self.prog[obj] += 1
                            
                        if self.done():
                            print("-" * 50)
                            self.say("The house is quiet, but it doesn't feel heavy anymore. You are ready to move on.")
                            break
                    else:
                        print(f"No '{obj}' here.")
                        
                else:
                    print("Unknown command. Try 'go [room]', 'look [object]', or 'quit'.")
                    
        except KeyboardInterrupt:
            print("\n")
            self.say("Goodbye.")

if __name__ == "__main__":
    Game().play()
