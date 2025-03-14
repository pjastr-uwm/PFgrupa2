class Song:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.artists = []

    def calculate_royalty(self):
        return 0.1 * self.duration

    def add_artist(self, param):
        if param == "":
            raise ValueError("Artist name cannot be empty")

        self.artists.append(param)
