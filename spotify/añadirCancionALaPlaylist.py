import requests

headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'uris': [
        'string',
    ],
    'position': 0,
}

response = requests.post('https://api.spotify.com/v1/playlists/playlist_id/tracks', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n  "uris": [\n    "string"\n  ],\n  "position": 0\n}'
#response = requests.post('https://api.spotify.com/v1/playlists/playlist_id/tracks', headers=headers, data=data)