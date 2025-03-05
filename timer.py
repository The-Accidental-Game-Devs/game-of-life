
import pygame

class Timer:
    def __init__(self, duration: float, repeat: bool=False, autostart = False, func = None) -> None:
        """
        duration: The timer duration in milliseconds.
        repeat: If True, the timer restarts automatically after finishing. Defaults to False.
        autostart: If True, the timer starts immediately upon initialization. Defaults to False.
        func: A function to be executed when the timer completes. Defaults to None.
        """
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.repeat = repeat
        self.func = func

        if autostart:
            self.activate()

    def activate(self) -> None:
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self) -> None:
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def update(self) -> None:
        if self.active:
            if pygame.time.get_ticks() - self.start_time >= self.duration:
                if self.func and self.start_time:
                    self.func()
                self.deactivate()
