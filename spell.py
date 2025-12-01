import pygame
from pygame.sprite import Sprite

class Spell(Sprite):
    """A class to manage a simple fireball spell from the wizard."""

    def __init__(self, ai_game):
        """Create a spell object at the wizard's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        wizard = ai_game.wizard

        # Rectangle for the spell, where to create a spell at (0,0) and correct
        # for wizard position.
        self.rect = pygame.Rect(
            0, 0,
            self.settings.spell_width,
            self.settings.spell_height
        )
        self.rect.center = wizard.rect.center

        # Store the spell position as floats
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Get direction from wizard
        self.dir_x = wizard.dir_x
        self.dir_y = wizard.dir_y

        self.color = self.settings.spell_color
        self.speed = self.settings.spell_speed

    def update(self):
        """Move the spell in the direction the wizard is pointing."""
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)