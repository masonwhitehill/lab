class Television:
    """
    Class to represent the TV objects
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to represent the TV's default state
        """
        self.__tv_channel: int = Television.MIN_CHANNEL
        self.__tv_vol: int = Television.MIN_VOLUME
        self.__tv_power: bool = False

    def power(self) -> None:
        """
        Method that determines if the TV is on or off
        """
        if self.__tv_power == False:
            self.__tv_power = True
        elif self.__tv_power == True:
            self.__tv_power = False

    def channel_up(self) -> None:
        """
        Method that turns the TV channel up
        """
        if self.__tv_power == True:
            self.__tv_channel += 1
            if self.__tv_channel > Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method that turns the TV channel down
        """
        if self.__tv_power == True:
            self.__tv_channel -= 1
            if self.__tv_channel < Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method that turns the TV volume up
        """
        if self.__tv_power == True:
            self.__tv_vol += 1
            if self.__tv_vol > Television.MAX_VOLUME:
                self.__tv_vol = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method that turns the TV volume down
        """
        if self.__tv_power == True:
            self.__tv_vol -= 1
            if self.__tv_vol < Television.MIN_VOLUME:
                self.__tv_vol = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method that creates a string stating the current TV status
        """
        return f'TV status: Is on = {self.__tv_power}, Channel = {self.__tv_channel}, Volume = {self.__tv_vol}'
