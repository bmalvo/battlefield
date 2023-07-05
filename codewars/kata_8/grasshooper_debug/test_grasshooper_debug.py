from grasshooper_debug import weather_info


def test_weather_info():
    assert weather_info(50) == '10.0 is above freezing temperature'


def test_2_weather_info():
    assert weather_info(23) == '-5.0 is freezing temperature'
