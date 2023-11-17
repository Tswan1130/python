import pytest
from television import Television

def test_init():
    tv = Television()
    assert not tv._Television__status  # Accessing the private attribute for testing
    assert not tv._Television__muted
    assert tv._Television__volume == Television.MIN_VOLUME
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status
    tv.power()
    assert not tv._Television__status

def test_mute():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.mute()
    assert tv._Television__muted
    tv.mute()
    assert not tv._Television__muted

def test_channel_up():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.channel_up()
    assert tv._Television__channel == 1
    tv.channel_up()
    assert tv._Television__channel == 2
    tv.channel_up()
    assert tv._Television__channel == 3
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL  # Should wrap around

def test_channel_down():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL  # Should wrap around
    tv.channel_down()
    assert tv._Television__channel == 2

def test_volume_up():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.volume_up()
    assert tv._Television__volume == 1
    tv.volume_up()
    assert tv._Television__volume == 2
    tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME  # Should stay at max

def test_volume_down():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME  # Should stay at min
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 1
