# Pass The Parcel

Python/GStreamer [pass the parcel](https://en.wikipedia.org/wiki/Pass_the_parcel) music player.

## Installation

Install the following system packages:

```
gir1.2-gstreamer-1.0
gstreamer1.0-tools
gir1.2-gst-plugins-base-1.0
gstreamer1.0-plugins-good
gstreamer1.0-plugins-ugly
gstreamer1.0-alsa
```

Install `pygobject` from PyPI:

```console
pip install pygobject
```

## Usage

1. Run ``python3 parcel.py SONG1 [SONG2] [SONG3]``, where SONG1, SONG2 etc. are the filenames of the songs to use.
2. When prompted press the ``Enter ⏎`` key. The song will start playing.
3. After a random delay of 8 to 15 seconds, the music will pause.
4. Press the ``Enter ⏎`` key to resume the music.
