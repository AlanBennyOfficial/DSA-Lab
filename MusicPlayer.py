from collections import deque
import time

class MediaPlayer:
    def __init__(self):
        self.q = deque()  # Playlist queue
        self.now = None

    def add(self, song):
        self.q.append(song)
        print(f"Added '{song}'")

    def play(self):
        if not self.q:
            print("Empty!")
            return
        self.now = self.q.popleft()
        print(f"Playing: {self.now}")
        time.sleep(1)  # Simulate play
        print(f"Done: {self.now}")
        self.now = None

    def skip(self):
        if self.now or self.q:
            self.now = self.q.popleft() if self.q else None
            print(f"Skipped: {self.now or 'None'}")
            if self.now:
                time.sleep(1)
                print(f"Done: {self.now}")
                self.now = None
        else:
            print("Empty!")

    def show(self):
        print("Playlist:", list(self.q) or "Empty!")

def main():
    p = MediaPlayer()
    while True:
        print("\n1.Add 2.Play 3.Skip 4.Show 5.Exit")
        c = input("> ")
        if c == '1':
            p.add(input("Song: "))
        elif c == '2':
            p.play()
        elif c == '3':
            p.skip()
        elif c == '4':
            p.show()
        elif c == '5':
            print("Bye!")
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()