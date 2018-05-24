# Basic Text Adventure Engine

Uses a set of easy-to-make text file templates to create a text adventure game.  
Created in Python 3.

### Templates

Three text files are used the craft the game: *items.txt*, *locations.txt*, and *NPCs.txt*  
They all follow a similar format of listing fields with specific items separated by "--".

**Example Location (locations.txt):**  
name: mine  
description: A boring mine, with some rocks and stuff. The mine continues to the west.  
items: rock, big rock, stuff  
destinations: "deeper into the mine"[west]

**Example Tool (items.txt):**  
name: pickaxe  
type: tool  
description: a worn down pickaxe with a rusted iron head and wooden handle.  
attributes: mining

**Example Object (items.txt):**  
name: rock  
type: object  
description: A large boulder with mineral veins running through it.  
attributes: mining  
yield: coal

### Item Attributes and Yields

Items with the same attributes can interact. For example giving both a pickaxe and a rock the attribute 'mining' means that the pickaxe can be used on the rock with the command "use pickaxe on rock". Furthermore, if the rock is given a yield such as coal, the player will have coal added to their inventory after using the pickaxe on the rock, and the player will no longer be able to mine the rock.

## TODO:

- Comments, more comments, and even more comments
- Combat
  - Weapon items
  - NPCs
- XP and levelling up
- Crafting?
