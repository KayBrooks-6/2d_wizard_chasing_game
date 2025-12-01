import pygame 
from pygame.sprite import Sprite
import random

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

        # Random monster position along the sides and top of the screen.
        screen_h = self.settings.screen_height
        screen_w = self.settings.screen_width

        edge = random.choice(["top", "left", "right"])

        if edge == "top":
            self.rect.x = random.randint(0, screen_w - self.rect.width)
            self.rect.y = 0
        elif edge == "left":
            self.rect.x = 0
            self.rect.y = random.randint(0, screen_h - self.rect.height)
        else: 
            self.rect.x = screen_w - self.rect.width
            self.rect.y = random.randint(0, screen_h - self.rect.height)

        # Store the monster's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = self.settings.enemy_color
        self.speed = self.settings.enemy_speed

    def draw(self):
        """Draw the monster as a red square."""
        pygame.draw.rect(self.screen, self.color, self.rect)
