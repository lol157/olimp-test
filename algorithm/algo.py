import requests
from json import loads


def algo(data, windows_for_room):
    last_index = 0
    room = 1
    lit_rooms = []

    for floors, windows in data.items():
        for i in windows_for_room:
            if any(windows[last_index:last_index + i]):
                lit_rooms.append(room)
            last_index += i
            room += 1
        last_index = 0

    return lit_rooms
