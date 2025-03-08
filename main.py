import sys
import pygame
import settings
from game import Game
from timer import Timer

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.window_width = 1280
        self.window_height = 720
        self.display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.game_timer = Timer(100, repeat=True, autostart=True, func=self.game.update)
        self.pause_game = True

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause_game = not self.pause_game
                elif event.key == pygame.K_c:
                    self.game.clear()

    def draw(self) -> None:
        self.display_surface.fill(settings.BACKGROUND_COLOR)
        self.game.draw(self.display_surface)
        pygame.display.update()

    def update(self) -> None:
        self.clock.tick(settings.FPS)
        self.game.handle_draw_input()
        if not self.pause_game:
            self.game_timer.update()

    def run(self) -> None:
        while True:
            self.handle_event()
            self.draw()
            self.update()

if __name__ == "__main__":
    main = Main()
    main.run()
