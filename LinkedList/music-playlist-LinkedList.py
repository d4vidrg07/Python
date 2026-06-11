class Playlist(ContainerBase):

    def __init__(self):
        super().__init__()
        self._duration_played = 0

    def add_song(self, song):
        new_node = self.Node(song)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def get_song(self, position):
        current = self.first
        index = 0
        while current is not None:
            if index == position:
                return current.song
            index += 1
            current = current.next
        return None

    def play_song(self, position):
        if self.first is None:
            return None
        if position == 0:
            song = self.first.song
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._duration_played += song.duration
            return song
        current = self.first
        index = 0
        while current.next is not None:
            if index + 1 == position:
                song = current.next.song
                if current.next == self.last:
                    self.last = current
                current.next = current.next.next
                self._duration_played += song.duration
                return song
            index += 1
            current = current.next
        return None

    @property
    def duration_left(self):
        total = 0
        current = self.first
        while current is not None:
            total += current.song.duration
            current = current.next
        return total

    @property
    def duration_played(self):
        return self._duration_played
