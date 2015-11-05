import curses 
import threading

_init = 11
_max_element = 5
_init_coffee = 8
_init_water = 19
_init_temp = 30
_recipt_coffee = 1
_recipt_water = 2
_recipt_temp = 3
_last_y = 13
_last_x = 40
_total_x = 38
_total_y = 71

coffee = 0
water = 0
temp = 0
total = 0
screen = curses.initscr() 

curses.noecho() 
curses.curs_set(0) 
curses.resizeterm(45,90)
curses.setsyx(45,90)
screen.keypad(1)
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_CYAN)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)

def init():
   global active, water, coffee, temp, total
   coffee = 0
   water = 0
   temp = 0
   total = 0
   active = False
   screen.clear()
   curses.flash()
   with open('init.txt') as inputfile:
      for i, line in enumerate(inputfile):
         machine=line.strip().split(',')
         screen.addstr(i,0,machine[0], curses.color_pair(6))

def clean_row():
   st_empty = "                            "
   screen.addstr(_last_x,_last_y,st_empty) 

def process(element,quantity):
   global water, coffee, temp
   for i in range(quantity):
      if element == 'coffee':
         coffee = coffee - 1
         screen.addch((_init-coffee),_init_coffee," ")
      elif element == 'water':
         water = water - 1
         screen.addch((_init-water),_init_water," ")
      elif element == 'temperature':
         temp = temp - 1
         screen.addch((_init-temp),_init_temp," ")

def make_coffe():
   global coffee, water, temp, total
   if coffee >= _recipt_coffee and water >= _recipt_water and temp >= _recipt_temp:
      screen.addstr(_last_x,_last_y,"PREPARED COFFEE!", curses.color_pair(5))
      process('coffee',_recipt_coffee)
      process('water',_recipt_water)
      process('temperature',_recipt_temp)
      total = total + 1
      screen.addstr(_total_x,_total_y,str(total))
      curses.flash()
   else:
      if coffee < _recipt_coffee:
         clean_row()
         screen.addstr(_last_x,_last_y,"PLEASE ADD COFFEE!", curses.color_pair(4)) 
      elif water < _recipt_water:
         clean_row()
         screen.addstr(_last_x,_last_y,"PLEASE ADD WATER!", curses.color_pair(4)) 
      elif temp < _recipt_temp:
         clean_row()
         screen.addstr(_last_x,_last_y,"PLEASE ADD TEMPERATURE!", curses.color_pair(4)) 


init()

while True:
   global active 
   event = screen.getch() 
   if active :
      clean_row()
      if event == ord("q"): 
         init()
      elif event == ord("c"):
         if coffee != _max_element:
            screen.addstr(_last_x,_last_y,"ADD COFFEE", curses.color_pair(1))
            screen.addch((_init-coffee),_init_coffee," ", curses.color_pair(1))
            coffee = coffee + 1
         else:
            screen.addstr(_last_x,_last_y,"COFFEE FULL!", curses.color_pair(4))
      elif event == ord("w"): 
         if water != _max_element:
            screen.addstr(_last_x,_last_y,"ADD WATER", curses.color_pair(2)) 
            screen.addch((_init-water),_init_water," ", curses.color_pair(2))
            water = water + 1
         else:
            screen.addstr(_last_x,_last_y,"WATER FULL!", curses.color_pair(4))
      elif event == ord("t"): 
         if temp != _max_element: 
            screen.addstr(_last_x,_last_y,"ADD TEMPERATURE", curses.color_pair(3)) 
            screen.addch((_init-temp),_init_temp," ", curses.color_pair(3))
            temp = temp + 1
         else:
            screen.addstr(_last_x,_last_y,"TEMPERATURE MAX!", curses.color_pair(4))
      elif event == ord(" "): 
         make_coffe()
      else: 
         screen.addstr(_last_x,_last_y,"ACTION NOT VALID!", curses.color_pair(4))
   else:
      if event == ord("q"): break
      if event == ord(" "):
         active = True
         screen.clear()
         with open('machine.txt') as inputfile:
            for i, line in enumerate(inputfile):
               machine=line.strip().split(',')
               screen.addstr(i,0,machine[0])

curses.endwin()