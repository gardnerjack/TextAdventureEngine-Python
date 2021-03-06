# Basic Text Adventure Engine

Uses a set of easy-to-make text file templates to create a text adventure game.  
Created in Python 3.

## Usage

Download the repository (or clone).  
Edit the text files with the game information (see [Templates](#templates)) in the gamne_info directory.

Run the `play.py` Python program.

## The Engine

### Templates

Two text files are used the craft the base game: *objects.txt*, *locations.txt*.
They all follow a similar format of listing fields with specific items separated by "--".

**Example Location (locations.txt):**  
name: mine  
description: A boring mine, with some rocks and stuff. The mine continues to the west.  
objects: rock, big rock, stuff  
destinations: "deeper into the mine"[west]

**Example Tool (objects.txt):**  
name: pickaxe  
type: tool  
description: a worn down pickaxe with a rusted iron head and wooden handle.  
attributes: mining

**Example Item (objects.txt):**  
name: rock  
type: item  
description: A large boulder with mineral veins running through it.  
attributes: mining  
yield: coal

### Object Attributes and Yields

Objects with the same attributes can interact. For example, giving both a pickaxe and a rock the attribute 'mining' means that the pickaxe can be used on the rock with the command "use pickaxe on rock". Furthermore, if the rock is given a yield such as coal, the player will have coal added to their inventory after using the pickaxe on the rock, and the player will no longer be able to mine the rock.

## TODO:

- Combat
  - Weapon items
  - NPCs
- XP and levelling up
- Crafting?
