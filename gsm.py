"""Manages global state variables, to be inherited from."""

import sys

class GlobalStateManager(object):
    """Manages variables and methods which must be global.

    See all the state variables in `__init__`. Important part here is
    all the `exec_*` methods, which are called dynamically from
    `main` using `KEYS` dict. Each `exec_*` method corresponds to a
    keystroke and performs some operations on the global state
    variables inside the class.
    """

    def __init__(self, window_manager, scene):
        self.scene = scene
        self.window_manager = window_manager
        cursor_y, cursor_x = window_manager.main_window.getmaxyx()
        self.cursor_y, self.cursor_x = cursor_y / 2, cursor_x / 2

    def exec_quit(self):
        """Exit the application."""
        sys.exit(0)
