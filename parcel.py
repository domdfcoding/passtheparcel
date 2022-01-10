# stdlib
import os
import random
import sys
import time

# 3rd party
import gi  # type: ignore

gi.require_version("Gst", "1.0")
# 3rd party
from gi.repository import Gst  # type: ignore

Gst.init(None)

playbin = Gst.ElementFactory.make("playbin", None)
track_finished = False


def on_track_finished(player):
	global track_finished
	track_finished = True


playbin.connect("about-to-finish", on_track_finished)

for song in sys.argv[1:]:
	track_finished = False

	playbin.set_state(Gst.State.READY)
	playbin.set_property("uri", f"file://{os.path.abspath(song)}")
	input("Ready?")
	playbin.set_state(Gst.State.PLAYING)
	status = playbin.get_state(Gst.CLOCK_TIME_NONE)
	if status[0] == Gst.StateChangeReturn.FAILURE:
		raise OSError(f"Failed to play {song!r}")

	while not track_finished:
		delay = random.randint(8, 15)
		time.sleep(delay)
		playbin.set_state(Gst.State.PAUSED)
		input("Ready?")
		playbin.set_state(Gst.State.PLAYING)
