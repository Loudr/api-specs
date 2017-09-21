"""Demonstrates creating a request, and fetching that resource from the API."""

import requests
import json

LOUDR_BASE = "https://loudr.fm"
SECRET = "..."

# Create a new request with a PUT to /api/client/sound_recording.

# Build the document payload according to the API specifications.
payload = {
    "recording": {
        "album": "Hero of Time",
        "artist": "Eric Buchholz",
        "isrc": "QZ6K41600179",
        "length": 209,
        "release_date": "2017-03-09",
        "title": "The Legendary Blade",
        "label": "Materia Collective",
        "vendor_id": "QZ6K41600179-dpd"
    },
    "requests": [{
        "composer": "Koji Kando",
        "source": "The Legend of Zelda: Ocarina of Time",
        "title": "Temple of Time"
    }],
    "license_territories": ["US"],
    "license_config": {
        "dpd": -1
    }
}

# Use your client access token as the query-string argument, "secret".
response = requests.put(LOUDR_BASE+"/api/client/sound_recording?secret="+SECRET,
    json.dumps(payload),
    headers={"content_type":"application/json"})

# Assert the response status of 201 when creating a new sound recording.
assert response.status_code == 201, "Loudr returned status %d;\n%s" % (response.status_code, response.content)

# The sound_recording object can be retrieved by interpreting the JSON response.
sound_recording = response.json()

# Each sound_recording is identified by its URI.
sound_recording_uri = sound_recording['uri']
# The sound_recording may be refreshed by making a call to sound_recording['rel']['canonical'].
sound_recording_canonical = sound_recording['rel']['canonical']

# The same URI may be built: "/api/client/sound_recording/%s/%s?secret=%s" % (client_id, vendor_id, secret)
response = requests.get(LOUDR_BASE+sound_recording_canonical+"?secret="+SECRET)

# Assert the response status when retrieving an existing sound recording.
assert response.status_code == 200, "Loudr returned status %d;\n%s" % (response.status_code, response.content)

# The same object will be returned.
assert response.json()['uri'] == sound_recording_uri


#########################
### Querying Requests ###
#########################

# Query for recordings.
# You may fetch your recordings using /api/client/sound_recordings?secret=<secret>.
response = requests.get(LOUDR_BASE+"/api/client/sound_recordings?secret="+SECRET)

# A page of results will be returned, and may be scrolled using the following logic.
assert response.status_code == 200, "Loudr returned status %d;\n%s" % (response.status_code, response.content)

data = response.json()
total_results = data['total']
sound_recordings = data['results']
next_page = data['rel']['next_page']

# Scroll to the next page.
while next_page:
    # Query for the next page using data['rel']['next_page']
    response = requests.get(LOUDR_BASE+next_page)
    # The next page of results will be returned.
    assert response.status_code == 200, "Loudr returned status %d;\n%s" % (response.status_code, response.content)
    data = response.json()
    # Empty page will signify end of results.
    if not data['results']:
        break
    sound_recordings.extend(data['results'])
    next_page = data['rel']['next_page']

# Assert our original sound_recording appears in the search.
assert sound_recording_uri in [sr['uri'] for sr in sound_recordings], \
    "Could not find new sound_recording `%s` when querying for recordings." % sound_recording_uri


########################
### Updating Request ###
########################

# When a recording has been "soft rejected," you may update the request and recording metadata to
# trigger a re-attempt to secure licensing.
payload = {
    "recording": {
        "title": "The Legendary Blades",  # change title to The Legendary Blades
    },
    "requests": [{
        "composer": ["Koji Kando", "Nobuo Uematsu"],  # add composer Nobuo Uematsu
        "composition_index": sound_recording['requests'][0]['provided_research']['composition_index']
    }]
}

# Update a recording by sending a POST request to the recordings canonical link.
response = requests.post(LOUDR_BASE+sound_recording_canonical+"?secret="+SECRET,
    json.dumps(payload),
    headers={"content_type":"application/json"})

# A 400 Bad Request error occurs if the recording is not eligible to be updated.
# Only "SOFT REJECTED" requests may be updated at this time.
if response.status_code == 400:
    raise Exception("Sound Recording @ `%s` is not in a valid state to be updated:\n%s" %
        (sound_recording_canonical, response.content))

# Assert the response status of 200 when updating an existing sound recording.
assert response.status_code == 200, "Loudr returned status %d;\n%s" % (response.status_code, response.content)

# You can verify that your updated payload is now embodied in the provided_research object of the only request.
data = response.json()
# Please note how the underlying work metadata appears in the provided_research object of the request.
assert data['requests'][0]['provided_research']['composer'] == payload['requests'][0]['composer']
