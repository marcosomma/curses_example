import __main__ as main

def set():
   while True:
      event = main.screen.getch() 
      if main.active :
         main.clean_row()
         if event == ord("q"): 
            main.init()
         elif event == ord("c"):
            if main.coffee != main._max_element:
               main.screen.addstr( main._last_x, main._last_y, "ADD COFFEE" , main.curses.color_pair(1))
               main.screen.addch(( main._init - main.coffee) , main._init_coffee, " " , main.curses.color_pair(1))
               main.coffee = main.coffee + 1
            else:
               main.screen.addstr( main._last_x, main._last_y, "COFFEE FULL!" , main.curses.color_pair(4))
         elif event == ord("w"): 
            if main.water != main._max_element:
               main.screen.addstr( main._last_x, main._last_y, "ADD WATER" , main.curses.color_pair(2)) 
               main.screen.addch(( main._init - main.water) , main._init_water, " " , main.curses.color_pair(2))
               main.water = main.water + 1
            else:
               main.screen.addstr( main._last_x, main._last_y, "WATER FULL!" , main.curses.color_pair(4))
         elif event == ord("t"): 
            if main.temp != main._max_element: 
               main.screen.addstr( main._last_x, main._last_y, "ADD TEMPERATURE" , main.curses.color_pair(3)) 
               main.screen.addch(( main._init - main.temp) , main._init_temp, " " , main.curses.color_pair(3))
               main.temp = main.temp + 1
            else:
               main.screen.addstr( main._last_x, main._last_y, "TEMPERATURE MAX!" , main.curses.color_pair(4))
         elif event == ord(" "): 
            main.make_coffe()
         else: 
            main.screen.addstr( main._last_x, main._last_y, "ACTION NOT VALID!" , main.curses.color_pair(4))
      else:
         if event == ord("q"): break
         if event == ord(" "):
            main.active = True
            main.screen.clear()
            main.draw.game_screen(main.screen, main.curses.A_REVERSE)