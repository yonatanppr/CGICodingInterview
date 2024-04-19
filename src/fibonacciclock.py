from datetime import datetime
from typing import List


class FibonacciClock:
    def __init__(self):
        # initialize fibonacci values
        self.fibonacci_values = [1, 1, 2, 3, 5]
        # initialize color blocks
        self.colors = ['white', 'white', 'white', 'white', 'white']
        # initialize R, G and B values with 0
        self.R, self.G, self.B = 0, 0, 0

    def update_colors(self, current_time: datetime):
        """
        Updates the colors of the squares based on the current time.

        Args:
        current_time (datetime): The current system time
        """
        # initialize all colors with white
        self.colors = ['white', 'white', 'white', 'white', 'white']

        hours = current_time.hour % 12  # hour mod 12 to convert from 24 to 12-hour format.
        # 0 % 12 will not work. This needs to be hardcoded.
        if hours == 0:
            hours = 12
        # round minutes to nearest 5
        minutes = current_time.minute - (current_time.minute % 5)

        # initialize sums for R, G, B
        self.R, self.G, self.B = 0, 0, 0

        # iterate over reversed fibonacci values (to first check largest values) and calculate blocks needed to
        # represent minutes and hours
        used_for_hours = self._calculate_required_blocks(hours)
        used_for_minutes = self._calculate_required_blocks(minutes, minutes=True)

        # assign colors based on usage of blocks
        for i in range(len(self.fibonacci_values)):
            # if block is used for both minutes and hours -> set color to blue
            if used_for_hours[i] and used_for_minutes[i]:
                self.colors[i] = 'blue'
                self.B += self.fibonacci_values[i]
            # if block is used for both minutes and hours -> set color to red
            elif used_for_hours[i]:
                self.colors[i] = 'red'
                self.R += self.fibonacci_values[i]
            # if block is used for both minutes and hours -> set color to green
            elif used_for_minutes[i]:
                self.colors[i] = 'green'
                self.G += self.fibonacci_values[i]

    def _calculate_required_blocks(self, time_value: int, minutes: bool = False):
        """
        Reverses the fibonacci sequence and calculates required color blocks for representing time value

        Args:
        time_value (int): time_value from current time (either minutes or hours)
        minutes (bool): boolean necessary to check if time needs to be multiplied by 5
        """
        if minutes:
            multiplier = 5
        else:
            multiplier = 1
        # initialize values to keep track of accumulated values for minutes
        time_value_sum = 0
        # initialize lists to keep track of whether a fibonacci sequence block is used for representing minutes
        used_blocks = [False] * 5
        # Calculate minute sums
        for i in reversed(range(len(self.fibonacci_values))):
            value = self.fibonacci_values[i] * multiplier
            if time_value_sum + value <= time_value:
                time_value_sum += value
                used_blocks[i] = True
        return used_blocks

    def get_time_representation(self) -> str:
        """
        Returns the current color configuration of the squares in the format R:xx G:xx B:xx.

        Returns:
        str: A string representing the state of each Fibonacci square for hours (R), minutes (G), and both (B).
        """
        return f"R:{self.R} G:{self.G} B:{self.B}"

    def get_colors(self) -> List[str]:
        """
        Getter function for the color list

        Returns:
        list: a list with all the color values for red, green and blue
        """
        return self.colors
