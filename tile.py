class Tile:
    def __init__(self,value=None):
        """
        :param value: value assigned to tile
        :variable merged: boolean to keep track of tile containing merged value

        """
        self.value = value
        self.merged = False

    def update_value(self,value):
        """
        :method updates value in tile

        """
        self.value = value
