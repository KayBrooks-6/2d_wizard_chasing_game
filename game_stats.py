class GameStats:
    """Track the statistics for the game."""

    def __init__(self, ai_game):
        """Initialize the statistics. """
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.wizard_lives_left = self.settings.wizard_lives