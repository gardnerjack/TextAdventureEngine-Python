MOVE    = 'move'
GET     = 'get'
DROP    = 'drop'
USE     = 'use'
INSPECT = 'inspect'

class Handler(object):

    directions = ('n', 'w', 's', 'e', 'north', 'west', 'south', 'east')

    def handle(self, command, player):

        if command in ('h', 'help'):
            self.help()

        elif command == 'show':
            player.location.output()

        elif command in self.directions:
            return MOVE

        elif command in ('p', 'player'):
            print(str(player))

        elif command.startswith('get '):
            return GET

        elif command.startswith('drop '):
            return DROP

        elif command.startswith('use '):
            return USE

        elif command.startswith('inspect '):
            return INSPECT

        else:
            print("Please enter a valid command")


    def help(self):
        print("Available commands:")
        print(" h, help - list commands")
        print(" q, quit - quit the game")
        print(" north, east, south, west - directions to move in")
        print(" n, e, s, w - abbreviated versions of movement commands")
        print(" show - show description of current location")
        print(" p, player - display player information")
        print(" actions:\n    get <object>\n    drop <object>\n    use <tool> on <item>\n    inspect <object>")


if __name__ == "__main__":
    print("Command handler class for game.py")
