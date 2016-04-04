"""Window manager."""

import heapq

import curses

WINDOW_MAIN_OFFSET_X = 4
WINDOW_MAIN_OFFSET_Y = 6
WINDOW_MAIN_X = 2
WINDOW_MAIN_Y = 3
WINDOW_SELECT_HEIGHT = 6
WINDOW_SELECT_WIDTH = 20
WINDOW_STATUS_WIDTH = 17


class WindowManager(object):
    """Manages refreshing windows, bottom to top."""

    def __init__(self, stdscr, container_window, main_window, status_window):
        self.stdscr = stdscr
        self.container_window = container_window
        self.main_window = main_window
        self.status_window = status_window
        self.windows = [stdscr, container_window, main_window, status_window]

        self.is_recompose_main = False
        self._redraw_queue = []

    def queue_redraw(self, window):
        """Add a window to redraw queue."""
        heapq.heappush(self._redraw_queue, (self.windows.index(window), window))

    def redraw_all(self):
        """Redraw all windows, bottom to top."""
        for window in self.windows:
            window.noutrefresh()
        curses.doupdate()

    def redraw_queued(self):
        """Redraw previously queued windows, bottom to top."""
        while self._redraw_queue:
            _, window = heapq.heappop(self._redraw_queue)
            window.noutrefresh()
        self._redraw_queue = []
        curses.doupdate()
