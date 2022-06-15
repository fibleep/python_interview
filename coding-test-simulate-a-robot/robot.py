CARDINAL_DIRECTIONS: list = ("NORTH", "EAST", "SOUTH", "WEST")


class Robot:
    __robot_position: dict

    def execute(self, passed_data: str) -> str:
        """
        Moves the robot based on input
        :param passed_data: (str) Input that has been passed to the robot (X Y BEARING COMMAND)
        :return:(str): Final position of the robot (X Y BEARING)
        """
        data_list: list = passed_data.split(" ")

        try:
            if len(data_list) != 4: raise TypeError("Invalid amount of arguments")
            if data_list[2] not in CARDINAL_DIRECTIONS: raise ValueError("Invalid direction")

            try:
                self.__robot_position = {"X": int(data_list[0]), "Y": int(data_list[1]),
                                         "DIRECTION": data_list[2].upper()}
            except ValueError:
                raise TypeError("Invalid coordinates")
            command_list: list = [entry.upper() for entry in data_list[3]]

            for entry in command_list:
                self.__advance() if entry == 'A' else self.__turn(entry)

        except Exception as ex:
            return ex

        return ' '.join([str(value) for value in self.__robot_position.values()])

    def __advance(self) -> None:
        """
        Advances the robot in the direction it is currently facing
        """
        if self.__robot_position["DIRECTION"] == "NORTH":
            self.__robot_position["Y"] += 1
        elif self.__robot_position["DIRECTION"] == "SOUTH":
            self.__robot_position["Y"] -= 1
        elif self.__robot_position["DIRECTION"] == "EAST":
            self.__robot_position["X"] += 1
        elif self.__robot_position["DIRECTION"] == "WEST":
            self.__robot_position["X"] -= 1

    def __turn(self, direction: str) -> None:
        """
        Check the index of the direction the robot is facing and depending on whether the command is L or R:
            L - subtract 1 from current index, if below 0 (NORTH) - go to 3 (WEST)
            R - add 1 to current index, if above 3 (WEST) - go to 0 (NORTH)
        :param direction: either L (LEFT) or R (RIGHT)
        """

        current_direction_index: int = CARDINAL_DIRECTIONS.index(self.__robot_position["DIRECTION"])
        if direction == 'L':
            self.__robot_position["DIRECTION"] = CARDINAL_DIRECTIONS[
                current_direction_index - 1] if CARDINAL_DIRECTIONS.index(
                self.__robot_position["DIRECTION"]) - 1 >= 0 else CARDINAL_DIRECTIONS[3]

        elif direction == 'R':
            self.__robot_position["DIRECTION"] = CARDINAL_DIRECTIONS[
                current_direction_index + 1] if CARDINAL_DIRECTIONS.index(
                self.__robot_position["DIRECTION"]) + 1 < 4 else CARDINAL_DIRECTIONS[0]
        else:
            raise ValueError("Invalid command")
