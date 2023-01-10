# Folder Audio Playlist
Simple script to play all audio files in folder alphabetically using the `cvlc` command line program. Can play next file by simply hitting the enter key, plus a couple other features to change playback options.

I created this script as a way of running Sound for a theater, and a lot of the language used within, as well as its functionality, was intended to be used this way. This is my ideal program of running sound cues during a production of any musical or play a theater may put on.

## Installation
This script was designed to run on Linux. **I highly recommend NOT running this script under Windows!!! I will not provide Windows instructions because of this.** After some testing in a VM, you need to edit multiple lines of code and it will still not work 100%. For example, Keyboard Interrupts do not work the same way in Windows as they do in Linux. That was the only way I implemented to stop playback, so the only way to stop in the middle of an audio file playing is to kill VLC from Task Manager. This also makes functions such as looping playback basically broken.

Regardless of the platform you are installing on, you will need to make sure VLC Media Player is installed on your system, ensuring the `cvlc` command line program is also installed. This script calls on `cvlc` to play the actual files, so the program is required for any functionality. Head on over to [VLC's Download Page](https://www.videolan.org/vlc/) to download VLC if you are a different Operating System. If you are on Linux, it is recommended to download VLC from your distro's repositories:

Debian/Ubuntu: `sudo apt install vlc`

Fedora/DNF Distros: `sudo dnf install vlc`

Arch: `sudo pacman -S vlc`

Now you need to make sure Python 3 is installed on your system. If you run almost any Linux Distro, it should already be there. If you are on Ubuntu systems, the package and program is `python3`, while if you are on almost any other distro it will most likely be `python`. to download Python 3. Make sure you hit the tick box in the Installer to add Python to your PATH, this will make running this script much easier.

If you run MacOS, unfortunately I don't hold the information about installing and running Python. Consult Google on this matter, I have never owned a Mac and thus don't know the procedure.

From here, you are good to download the script and run it!

## Running the Script

### Arranging the Music to be Played
You may want to rename the music files to an order of your liking - the script uses Python's `sorted()` function to arrange all the files into alphabetical order when it loads the files in to be played. If the amount of files is less than 10, I would use a naming scheme similar to `1 First File.mp3`, `2 Second File.mp3`, `3 Third File.mp3`, and so on. If the number of files is greater or equal to 10, I would recommend using letters: `A First File.mp3`, `B Second File.mp3`. If you get to Z, I would use `ZA Twenty-Sixth File.mp3`, `ZB Twenty-Seventh File.mp3`, and so on. This is because of unfortunate limitations with Python's `sorted()` function, where if you have an 11 or a 12 in a name, it will sort it as "1, 10, 11, 12, 2, 3..." instead of "...9, 10, 11, 12...".

**It should also be noted that the script will only load in files with the extension of .mp3, .wav, and .ogg.**

### Running at the Command Prompt or Terminal
Place the script in the folder of music you wish to play, then open up a  Terminal (MacOS, Linux) and `cd` to the correct directory. If you don't know how to do this, consult Mr. Google. From here, if you are on basically any system except Ubuntu, type `python playAudioList.py`. If you are on an Ubuntu based system, use `python3 playAudioList.py`. It should load everything in and you should see every file loaded in, and their playback order. Wait a second, and then hit enter to play when you see `Press Enter to Play (with options?)...`.

## Playback Options
All of the following should be documented every time you start up the program, but here they are in this readme as well!
 - Use `p` to play the previous file. Note that it will not start playing until you hit enter at the prompt!
 - Use `s` to skip the loaded file.
 - Use `l` to enable loop playback on this file. You can also combine with `p` or `s`, so either `pl` or `ls` to loop previous or next file.
 - Use `goto <cue>` to go to the index of a file you wish to play. For example, if I have `First File.mp3`, `Second File.mp3`, and `Third File.mp3` loaded in that order and I'm at `First File.mp3` and want to be at `Third File.mp3`, I would type `goto 3`. Consult the order listed when you start the script to know which number correlates to which file. **This option does NOT immediatly start playing after you hit enter!** Rather, it takes you to the file you request and gives you another prompt to play it with any options you specify.

# License (GPLv3)
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
