from robot import Robot


def test_moving():
    robot = Robot()

    assert robot.execute("0 0 NORTH A") == "0 1 NORTH"
    assert robot.execute("7 3 NORTH RAALAL") == "9 4 WEST"
    assert robot.execute("0 0 NORTH L") == "0 0 WEST"
    assert robot.execute("0 0 NORTH R") == "0 0 EAST"
    assert robot.execute("0 0 NORTH AAAALAAAALAAAALAAAAL") == "0 0 NORTH"


def test_input():
    robot = Robot()

    assert str(robot.execute("0 0 www AAAA")) == "Invalid direction"
    assert str(robot.execute("A 0 NORTH RAALAL")) == "Invalid coordinates"
    assert str(robot.execute("0 0 WEST RAAT")) == "Invalid command"
    assert str(robot.execute("")) == "Invalid amount of arguments"
