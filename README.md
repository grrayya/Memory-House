# Memory-House

A short text-based adventure written in Python. 

*Memory House* is less about solving puzzles and more about exploring the emotional weight of a space left behind. 
As you interact with objects in the environment, the narrative progresses through stages of grief, moving slowly toward acceptance.


In this interactive fiction experience, you navigate a quiet house consisting of a Hallway, Kitchen, and Living Room. By repeatedly examining the everyday objects left behind (a coat, a mug, a chair), the protagonist's perspective shifts, reflecting the passage of time and emotional healing. this porject was make to repressent how ive been feeling recently, 


## How to Play
### Prerequisites
All you need is Python 3 installed on your computer. The game uses only built-in standard libraries (`time`, `sys`), so no external dependencies or virtual environments are required.

##Commands
Once the game starts, you can use the following commands to interact with the house:
go [room] - Move to a different area (e.g., go kitchen).
look - Read the description of your current room again.
look [object] - Inspect an item. Do this multiple times to see how things change (e.g., look mug).
quit - Exit the game.

##Fast mmode (skip animations)
If you want to replay the game without the slow-typing text effect, you can run it in fast mode by setting an environment variable:
Mac/Linux: FAST=1 python game.py
Windows (PowerShell): $env:FAST="1"; python game.py

Running the Game
1. Save the code into a file named `memory_house.py`.
2. Open your terminal or command prompt.
3. Navigate to the folder where you saved the file.
4. Run the script using the following command:
   ```bash
   python memory_house.py
