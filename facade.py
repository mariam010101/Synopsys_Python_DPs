class VideoFile:
    def __init__(self, filename):
        self.filename = filename

class Codec:
    def decode(self, file):
        print(f"Decoding {file.filename}")

    def encode(self, file):
        print(f"Encoding {file.filename}")

class VideoConverterFacade:
    def convert(self, filename):
        file = VideoFile(filename)
        codec = Codec()
        codec.decode(file)
        codec.encode(file)
        print("Conversion complete!")


converter = VideoConverterFacade()
converter.convert("movie.mp4")
