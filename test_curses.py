import curses
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    while True:
        stdscr.erase()
        height, width = stdscr.getmaxyx()
        y, x = height // 2, width // 2
        stdscr.addstr(y, x, 'x', curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.1)
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
