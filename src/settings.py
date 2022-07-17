"""
This module is responsible for mapping configuration variable
settings and making them available to other modules.
"""

import configparser
import os


class Settings:
    """Reads a .INI file for settings and assigns them to a
    variable."""

    def __init__(self, environment):
        self.environment = environment
        self.configuration = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation()
        )
        self.configuration.read(
            os.path.join(os.path.dirname(__file__),
                "environments", self.environment.lower() + ".ini"
            )
        )

    def get_grid_url(self):
        """Get Grid property value."""
        grid_url = self.configuration.get("server.grid", "url")
        return grid_url

    def get_aut_url(self):
        """Get AUT property value."""
        aut_url = self.configuration.get("server.aut", "url")
        return aut_url
