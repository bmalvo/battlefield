from playing_with_cubes_2 import Cube


def test_Cube_arg_10():
    cube = Cube(10)
    assert cube.get_side() == 10


def test_Cube_noargs():
    cube = Cube()
    assert cube.get_side() == 0


def test_Cube_negative_arg():
    cube = Cube(-7)
    assert cube.get_side() == 7
