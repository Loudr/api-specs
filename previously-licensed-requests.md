# Sending us Requests which you have "Previously Licensed" ?

Send previously licensed requests in the same format as above, with the following additional information in the `previous_license` object:

```json
"previous_license": {
  "license_id": "123456789", /* previous license ID from other partner - REQUIRED */
  "partner": "Licensing Agent", /* Name of previous partner coordinated with - REQUIRED (Please inquire with us what code to use for your previous partner) */
  "publisher_ids": ["P1234"], /* List of Previous partners worked with - OPTIONAL */
}
```

## Example
In full, this would make a single request look like this:

```json
{
  "isrc": "USE7D1300175",
  "title": "Pa Que Sigan Hable Y Hable",
  "artist": "Otro Nivel",
  "length": 213,
  "album": "Prendiendo El Motor",
  "label": "Del Records",
  "upc": "40232035791",
  "licenses": {
    "stream": "continuous"
  },
  "previous_license": {
    "license_id": "123456789",
    "partner": "Licensing Agent",
    "publisher_ids": ["P1234"]
  }
}
```