""" 
def binary_search(a_list, TrgVal):
    left, right = 0, len(a_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if a_list[mid] == TrgVal:
            print(TrgVal)
            return
        elif a_list[mid] < TrgVal:
            left = mid + 1
        else:
            right = mid - 1

    print(None)


list = input().split()
TrgValues = []


value = input()
while value != "#": 
    TrgValues.append(value)
    value = input()

for value in TrgValues:
    binary_search(list, value)

 """


class song:
    def __init__(self, track_id, song_id, artist, title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.title = title


    def lt(self, other):
        if self.artist < other.artist:
            return True
        else:
            return False



rader = []
with open("unique_tracks.txt", "r") as file:
    for rad in file:
        rad = rad.split("<SEP>")
        for item in rad:
            rader.append(song(*rad))
