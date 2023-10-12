from regular_ball_super_ball import ball1, ball2


def test_ball_without_arg():
    assert ball1.ball_type == 'regular'

    
def test_ball_with_arg():
    assert ball2.ball_type == 'super'
