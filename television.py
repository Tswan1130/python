class Television:
    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """Initialize the Television object with default settings."""
        # Instance variables (private)
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power status of the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status of the television."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel, wrapping around to MIN_CHANNEL if MAX_CHANNEL is reached."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the channel, wrapping around to MAX_CHANNEL if MIN_CHANNEL is reached."""
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """Increase the volume by 1, up to MAX_VOLUME."""
        if self.__status and not self.__muted:
            self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decrease the volume by 1, down to MIN_VOLUME."""
        if self.__status and not self.__muted:
            self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self) -> str:
        """Return a string representation of the Television object."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
