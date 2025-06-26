import abc


class OutputDevice(abc.ABC):
    @abc.abstractmethod
    def play_sound(self, sound):
        pass

class Headphones(OutputDevice):
    def play_sound(self, sound):
        print(f" Playing through headphones: {sound}")

class Speaker(OutputDevice):
    def play_sound(self, sound):
        print(f" Playing through speaker: {sound}")


class MusicPlayer(abc.ABC):
    def __init__(self, device: OutputDevice):
        self.device = device

    @abc.abstractmethod
    def play(self, song):
        pass

class SpotifyPlayer(MusicPlayer):
    def play(self, song):
        print("Streaming on Spotify")
        self.device.play_sound(song)

class LocalPlayer(MusicPlayer):
    def play(self, song):
        print(" Playing local mp3")
        self.device.play_sound(song)



print()

local_on_headphones = LocalPlayer(Headphones())
local_on_headphones.play("radio 43.2")

print()

spotify_on_speaker = SpotifyPlayer(Speaker())
spotify_on_speaker.play("Fashion killa by A$AP Rocky")
