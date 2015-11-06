def main_screen(screen, color):
	with open('txt/init.txt') as inputfile:
		for i, line in enumerate(inputfile):
			machine=line.strip().split(',')
			screen.addstr(i,0,machine[0], color)

def game_screen(screen, color):
	with open('txt/machine.txt') as inputfile:
		for i, line in enumerate(inputfile):
			machine=line.strip().split(',')
			screen.addstr(i,0,machine[0], color)