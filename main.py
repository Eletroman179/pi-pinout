#!/usr/bin/env python3
import curses

def main(stdscr):
    # Clear screen and disable cursor
    stdscr.clear()
    curses.curs_set(0)

    # Set up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Black text on white background
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # White text on black background
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green text on black background
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Cyan text on black background
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Yellow text on black background
    
    # Define the ASCII art as a string
    ASCII = """
    ┌────────────────────────────────────┐
 ┌──┴─┐                  ┌──────┐(1) (2) │
 │USBC│                  │ WIFI │(3) (4) │
 └──┬─┘                  │      │(5) (6) │
 ┌──┴─┐                  └──────┘(7) (8) │
 │HDMI│                          (9) (10)│
 └──┬─┘                         (11) (12)│
 ┌──┴─┐  ┌───────────┐          (13) (14)│
 │HDMI│  │    SoC    │ ┌──────┐ (15) (16)│
 └──┬─┘  │           │ │ RAM  │ (17) (18)│
    │    │           │ │      │ (19) (20)│
    │    │           │ │      │ (21) (22)│
    │    │           │ └──────┘ (23) (24)│
    │    └───────────┘          (25) (26)│
    │                           (27) (28)│
    │                           (29) (30)│
    │                           (31) (32)│
    │                   ┌─────┐ (33) (34)│
    │                   │ RP1 │ (35) (36)│
    │                   │     │ (37) (38)│
    │┌──────┐           └─────┘ (39) (40)│
    ││      │    ┌──────┐    ┌──────┐    │
    ││      │    │      │    │      │    │
    └┤      ├────┤      ├────┤      ├────┘
     │ NET  │    │ USB3 │    │ USB2 │
     └──────┘    └──────┘    └──────┘
 
"""

    info = """
    
       3V3  (1) (2)  5V    
     GPIO2  (3) (4)  5V    
     GPIO3  (5) (6)  GND   
     GPIO4  (7) (8)  GPIO14
       GND  (9) (10) GPIO15
    GPIO17 (11) (12) GPIO18
    GPIO27 (13) (14) GND   
    GPIO22 (15) (16) GPIO23
       3V3 (17) (18) GPIO24
    GPIO10 (19) (20) GND   
     GPIO9 (21) (22) GPIO25
    GPIO11 (23) (24) GPIO8 
       GND (25) (26) GPIO7 
     GPIO0 (27) (28) GPIO1 
     GPIO5 (29) (30) GND   
     GPIO6 (31) (32) GPIO12
    GPIO13 (33) (34) GND   
    GPIO19 (35) (36) GPIO16
    GPIO26 (37) (38) GPIO20
       GND (39) (40) GPIO21
    """
    
    # Get the screen size in y, x
    height, width = stdscr.getmaxyx()

    # Calculate the center position of the ASCII art
    art_height = ASCII.count('\n')
    art_width = max(len(line) for line in ASCII.splitlines())
    start_y_art = (height // 2) - (art_height // 2)
    start_x_art = (width // 2) - (art_width // 2) - 20

    # Calculate the center position of the info text, to the right of ASCII art
    info_height = info.count('\n')
    info_width = max(len(line) for line in info.splitlines())
    start_y_info = start_y_art  # Align vertically with ASCII art
    start_x_info = start_x_art + art_width + 2  # Position to the right of ASCII art with a small gap

    # Set color for the box (background black, text white)
    stdscr.attron(curses.color_pair(2))

    # Print ASCII art at the center
    for i, line in enumerate(ASCII.splitlines()):
        if start_y_art + i < height:  # Ensure we're not writing off the screen
            stdscr.addstr(start_y_art + i, start_x_art, line, curses.A_BOLD | curses.color_pair(3))  # Green for the ASCII art

    # Print the GPIO info to the right of the ASCII art
    for i, line in enumerate(info.splitlines()):
        if start_y_info + i < height:  # Ensure we're not writing off the screen
            # Ensure the line doesn't exceed the screen width
            line_to_print = line[:width - start_x_info]
            stdscr.addstr(start_y_info + i, start_x_info, line_to_print, curses.A_BOLD | curses.color_pair(4))  # Cyan for the info text
    
    stdscr.addstr(height-1,0,"press any key to contuine ...",curses.A_BOLD | curses.color_pair(5))
    
    stdscr.attroff(curses.color_pair(2))

    # Refresh the screen to display
    stdscr.refresh()

    # Wait for user input to exit
    stdscr.getch()

# Run the curses application
try:
   curses.wrapper(main)
except curses.error:
   print("term too small")
