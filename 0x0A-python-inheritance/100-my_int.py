#!/usr/bin/python3
"""T100"""

class MyInt(int):
    """MyInt class is a rebel
    it inverts == and != operators."""

    def __eq__(self, other):
        """Inverts the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        return super().__eq__(other)
