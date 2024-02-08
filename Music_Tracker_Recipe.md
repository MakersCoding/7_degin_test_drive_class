## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    def __init__(self):
        # Parameters:
        #   no parameters
        # Side effects:
        # 
        pass

    def add_track(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        # 
        pass # No code here yet

    def track_list(self):
        # Returns:
        #   A list of all the added tracks
        # Side-effects:
        # 
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
add a track
return list of track/s added
"""
track = MusicTracker()
track.add_track("BAD")
track.track_list() # => ["BAD"]

"""
add multiple tracks
return list of track/s added
"""
track = MusicTracker()
track.add_track("BAD")
track.add_track("Two become one")
track.add_track("One")
track.add_track("Falling")
track.add_track("505")
track.track_list() # => ["BAD", "Two become one", "One", "Falling", "505"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
