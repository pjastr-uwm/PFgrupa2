class Song:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def calculate_royalty(self):
        return 0.1 * self.duration
