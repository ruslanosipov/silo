"User interface helper functions."

import curses

import windowmanager

COLOR_WHITE = 0
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_BLUE = 3
COLOR_BLACK_ON_WHITE = 4


def init_colors():
    """Initialize curses color pairs, see constants up top."""
    if curses.has_colors():
        curses.start_color()

    curses.init_pair(COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(COLOR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(COLOR_BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(COLOR_BLACK_ON_WHITE, curses.COLOR_BLACK,
                     curses.COLOR_WHITE)


def create_windows(stdscr, title):
    """Create all necessary windows to start the application.

    Args:
        stdscr -- curses.stdscr.
        title -- window title.

    Returns:
        windowmanager.WindowManager instance.
    """
    stdscr.addstr(title, curses.A_REVERSE)
    stdscr.chgat(-1, curses.A_REVERSE)

    status_window = curses.newwin(
            1, windowmanager.WINDOW_STATUS_WIDTH, curses.LINES - 1, 0)

    container_window = curses.newwin(curses.LINES - 2, curses.COLS, 1, 0)
    container_window.box()
    main_window = container_window.subwin(
            curses.LINES - windowmanager.WINDOW_MAIN_OFFSET_Y,
            curses.COLS - windowmanager.WINDOW_MAIN_OFFSET_X,
            windowmanager.WINDOW_MAIN_Y,
            windowmanager.WINDOW_MAIN_X)

    return windowmanager.WindowManager(
        stdscr, container_window, main_window, status_window)
