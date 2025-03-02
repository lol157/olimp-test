from flask import Flask
import requests
from json import loads

app = Flask(__name__)

@app.get("/")
def root():
  day_to_indices = { }


  for i in range(1, 8):
    data = loads(requests.get(f"http://26.241.32.104:5001/?day=2{i}&month=02&year=25").content)["message"]
    windows_for_room = data["windows_for_room"]["data"]
    print(windows_for_room)

    last_index = 0
    room = 1
    lit_rooms = []

    for floors, windows in data["windows"]["data"].items():
      print(floors, windows)
      for i in windows_for_room:
        if any(windows[last_index:last_index+i]):
          lit_rooms += [room]
        last_index += i
        room += 1
      last_index = 0
    
    day_to_indices[f"2{i}-02-25"] = lit_rooms
  
  return f"{day_to_indices}"

  # results = []

  # for key, value in day_to_indices.items():
  #   post_request = {
  #     "data": {
  #       "count": len(value),
  #       "rooms": value
  #     },
  #     "date": key
  #   }
  #   results += [requests.post("http://26.241.32.104:5001", json=post_request).status_code]

  # return f"<p>{results}</p>"