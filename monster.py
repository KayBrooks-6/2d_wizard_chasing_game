import pygame 
from pygame.sprite import Sprite

class Monster(Sprite):
    """A class to represent a single monster."""

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the the a monster as a simple square and set its rect attribute
        self.rect = pygame.Rect(
            0, 0,
            self.settings.enemy_size,
            self.settings.enemy_size
        )

        # Starting position in the top left.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the monster's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Draw the monster as a red square."""
        pygame.draw.rect(self.screen, self.settings.enemy_color, self.rect)
