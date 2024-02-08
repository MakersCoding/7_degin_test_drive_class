from lib.music_tracker import *

"""
add a track
return list of track/s added
"""
def test_add_track():
    track = MusicTracker()
    track.add_track("BAD")
    assert track.track_list() == ["BAD"]

"""
add multiple tracks
return list of track/s added
"""

def test_add_multiple_track():
    track = MusicTracker()
    track.add_track("BAD")
    track.add_track("Two become one")
    track.add_track("One")
    track.add_track("Falling")
    track.add_track("505")
    assert track.track_list() == ["BAD", "Two become one", "One", "Falling", "505"]