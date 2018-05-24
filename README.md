# Basic Text Adventure Engine

Uses a set of easy-to-make text file templates to create a text adventure game.  
Created in Python 3.

## Releases

[v1.0 - The First Working Release](https://github.com/gardnerjack/TextAdventureEngine-Python/releases/tag/1.0)

## Usage

Download the zip from the above release and unzip it wherever you want to create the game.  
Create the required text files with the game information (see [Templates](#Templates)) in a directory with the unzipped contents.

Run the creation script with your new template directory to initialise the engine. For example:

```
sh create.sh sample
```

Then, just run the play Python program:

```
python play.py
```

## The Engine

### Templates

Two text files are used the craft the base game: *items.txt*, *locations.txt*.
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

Items with the same attributes can interact. For example, giving both a pickaxe and a rock the attribute 'mining' means that the pickaxe can be used on the rock with the command "use pickaxe on rock". Furthermore, if the rock is given a yield such as coal, the player will have coal added to their inventory after using the pickaxe on the rock, and the player will no longer be able to mine the rock.

## TODO:

- Combat
  - Weapon items
  - NPCs
- XP and levelling up
- Crafting?
