import pytest

from television import Television


@pytest.fixture
def tv() -> Television:
    """Provide a fresh television for each test."""
    return Television()


def test_init(tv: Television) -> None:
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_power_on(tv: Television) -> None:
    tv.power()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'


def test_power_off(tv: Television) -> None:
    tv.power()
    tv.power()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_mute_when_on_and_muted(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'


def test_mute_when_on_and_unmuted(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_mute_when_off_and_muted(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.power()
    tv.mute()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_mute_when_off_and_unmuted(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.power()
    tv.mute()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 1'


def test_channel_up_when_off(tv: Television) -> None:
    tv.channel_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_channel_up_when_on(tv: Television) -> None:
    tv.power()
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'


def test_channel_up_past_maximum(tv: Television) -> None:
    tv.power()
    for _ in range(Television.MAX_CHANNEL):
        tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'


def test_channel_down_when_off(tv: Television) -> None:
    tv.channel_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_channel_down_when_on(tv: Television) -> None:
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'


def test_channel_down_past_minimum(tv: Television) -> None:
    tv.power()
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'


def test_volume_up_when_off(tv: Television) -> None:
    tv.volume_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_volume_up_when_on(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_up_when_muted(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'


def test_volume_up_past_maximum(tv: Television) -> None:
    tv.power()
    for _ in range(Television.MAX_VOLUME + 1):
        tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'


def test_volume_down_when_off(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.power()
    tv.volume_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 2'


def test_volume_down_when_on(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_down_when_muted(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_down_past_minimum(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'
