#CODE
import queue
class MusicPlayer:
    # A simple music player class that manages a playlist and controls playback
    def __init__(self):
    # Initialize the Musicplayer object with an empty playlist and no current song.
        self.playlist = queue.Queue()
        self.current_song= None
        self.is_playing=False

    def add_song(self, song: str) -> None:
    # add a song to the playlist
        self.playlist.put(song)


    def play(self) -> None:
    #Play the song in the playlist if available
        if self.playlist.empty():
            print("Playlist is Empty.")
            return
        
        self.current_song = self.playlist.get()
        self.is_playing = True
        print(f"Now playing: {self.current_song}")


    def pause(self) -> None:
        # Pause the current playback if playing
        if not self.is_playing:
            print("Playback is not currently playing")
            return
        self.is_playing = False
        print("Playback paused.")


    def skip(self) -> None:
        # Skip the current song and play the next one if available
        if self.playlist.empty():
            print("Playlist is empty.")
            return
        if self.current_song is None:
            self.play()
            return
        self.playlist.get()
        self.play()


    def stop(self) -> None:
        # stop the music player and clears the playlist.
        self.playlist = queue.Queue()
        self.current_song = None
        self.is_playing = False

# Testing the implementation of the code
player = MusicPlayer()
while True:
    s = input(f'Add a song (or type "stop" to stop adding songs): ')


    if s.lower() == "stop":
        break
    player.add_song(s)
    print("Song Added")

while True:
    try:
        x = int(input("What do you want to do:-\n1. Play\n2. Pause\n3. Skip\n4. Stop\n"))
    except ValueError:
        print("Invalid Input. Please enter a number")
        continue

    if x == 1:
        player.play()
    elif x == 2:
        player.pause()
    elif x == 3:
        player.skip()
    elif x == 4:
        player.stop()
        print("Music Player Stopped")
        break
    else:
        print("Invalid Option. Please enter a number between 1 and 4.")
