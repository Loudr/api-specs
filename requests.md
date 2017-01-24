_this document will always live at (https://github.com/Loudr/api-specs/blob/master/requests.md)_

# Making a Request

Send a `POST` request to `/v1/sound_recording/request_license` with a JSON body described by [request-single.json](examples/request-single.json) in this repository.

You may also send bulk request files. [Click here to learn more](https://github.com/Loudr/api-specs/blob/master/requests.md#sending-bulk-requests).


## POST Data

### Sample Post Data
```json
{
  "title": "Track Title",           /* required */
  "artist": "Track Artist",         /* required */
  "length": 120,                    /* required */
  "album": "Album Title",           /* required */
  "isrc": "US-S1Z-99-00001",
  "upc": "840218195668",
  "label": "Label Name",
  "release_date": "2015-01-01",
  "licensor": "Licensor of Content",
  "compositions": [
    {
      /* title is required, as well as one or more of an author or composer */
      "title": "Original Song Title",
      "artist": "Original Artist",
      "composer": "Original Composer",
      "author": ["Original Song Writer 1", "Original Song Writer 2"],
      "album": "Optional Source Album",
      "source": "Optional Source Material (film or video game title, etc)",
      "link": "Optional URL to Original Song (YouTube, etc)",
      "iswc": "International Standard Musical Work Code",
      "notes": "Any Additional Research Notes (Optional)"
    }
  ],
  "metadata": {
      /* this is a custom object you may use */
      "publisher": "Optional known publisher if present"
  },
  "licenses": {
    "stream": "continuous",
  },
  "vendor_id": "Unique ID of this record in your system - if None provided, ISRC is used",
  "_secret": "YOUR LICENSEE SECRET"
}
```

### Request Fields

Any of the following fields which aren't explicitly required may be
required depending on your business agreement with Loudr.

    title:
        `str` Required.
        Title of track or sound recording being licensed.
    artist:
        `str` Required.
        Original performing artist(s).
    length:
        `int` Required.
        Length in seconds. Round up to the nearest whole second.
    album:
        `str` Required.
        Name of the album this request was or will be released on.
    isrc:
        `str`.
        ISRC of request.
    upc:
        `str`.
        UPC of the album.
    label:
        `str`.
        ISRC of request.
    release_date:
        `date`.
        ISO formatted date this content will be or was released. `YYYY-MM-DD`.
    licensor:
        `str`.
        Name of the original licensor of content.
    licenses:
        `object` Required.
        Describes the configurations of licenses requested, as well as units.
        See the "Licenses (Configurations)" section below.

### Vendor ID, and a note on IDs

The `vendor_id` property is used to directly associate our records with yours.
If you omit this field, which is valid, we will use the ISRC as the unique ID.

    vendor_id:
        `str`.
        An ID you may specify to retain your database ID for a given request.

### Licenses (Configurations)

The **`licenses`** property defines what kind of licenses you are requesting, and in what quantity.

To specify licensing for digital downloads with continuous reporting (instead of a fixed quantity):
```json
    "licenses": {
      "download": "continuous",
    }
```

To specify licensing for interactive streams with continuous reporting (instead of a fixed quantity):
```json
    "licenses": {
      "stream": "continuous",
    }
```

A full list of acceptable types exists in [enums.md](enums.md).

### Compositions (Songs being Covered - what we're licensing)

Depending on your business agreement with Loudr, you may leave compositions empty if you do not know exactly what has been covered. If you *do* know, it is always better to tell us - as providing this information greatly decreases the amount of time it takes to process and fulfill a license.

Properties for each **composition**:

_All fields may be a single string or list of strings (except for 'notes' and 'iswc')._

    title:
        `str` Required.
        Composition title. Provide multiple titles if the composition may have alternate names (or in alternate languages).
    artist:
        `str`
        Original performing artist(s).
    composer:
        `str`
        Original composer(s).
        (Either one composer or one author is required)
    author:
        `str`.
        Original author(s) of the song. Authors and composers may overlap,
        if so, they only need to be mentioned once.
        (Either one composer or one author is required)
    album:
        `str`.
        Original album the song was released on, if any.
    source:
        `str`.
        Original source material. Such as a movie or video game title.
    link:
        `str`.
        URL to the source material.
    iswc:
        `str`.
        International Standard Musical Work Code.
        (Only a single string)
    notes:
        `str`.
        Any additional notes to aid composition search.
        (Only a string).

***Note:** if publisher information is known, it should provided in the `metadata` object at the top level of the request.*

### Prior Licenses

When requesting licenses for content (sound recording) that has been previously released (and licensed),
we must know the dates and configurations that were captured in the past.

The **`prior_licenses`** field describes prior licenses obtained for a fixed quantity license.

It must include each configuration previously purchased, and the release date specified on the original license.

***prior_licenses* is only expected for fixed quantity licenses.**

Example::

```json
  "prior_licenses": {
    "dpd": "2015-01-01",
    "stream": "2015-01-01"
  }
```

### Requests which have been previously licensed

Send previously licensed requests in the same format as above, with the following additional information in the `previous_license` object:

```json
"previous_license": {
  "license_id": "123456789", /* previous license ID from other partner - REQUIRED */
  "partner": "Licensing Agent", /* Name of previous partner coordinated with - REQUIRED (Please inquire with us what code to use for your previous partner) */
  "publisher_ids": ["P1234"], /* List of Previous partners worked with - OPTIONAL */
}
```

See a full example: [request-single-previously-licensed.json](examples/request-single-previously-licensed.json).

### _secret

The `_secret` property is your secret token. It enables you to
make and view requests on behalf of your client account (`creator/some-id`).

This secret token works much like an OAuth2 access grant, so don't
share it or lose it.

## Response

The response is a JSON object that provides:

```json
{
  "_message": null,
  "_single": "sound_recording",
  "sound_recording": {
    "_fb": true,
    "_js_kind": "Sound_Recording",
    "_kind": "sound_recording",
    "_permissions": [
      "owner"
    ],
    "_uri": "sound_recording/creator/7cSdD--USE7D0900003",
    "album": "El Diablo De Culiacan",
    "artist": "Atomo",
    "created_ago": null,
    "created_at": null,
    "earliest_clearance_at": null,
    "is_hard_rejection": false,
    "isrc": "USE7D0900003",
    "label": "Del Records",
    "length": 192,
    "license_fulfilled": false,
    "license_fulfilled_at": null,
    "license_status": 2,
    "license_status_str": "In Progress",
    "p_id": "creator/7cSdD--USE7D0900003",
    "p_key": "agxkZXZ-cmRzY292ZXJyMQsSEFJkU291bmRSZWNvcmRpbmciG2NyZWF0b3IvN2NTZEQtLVVTRTdEMDkwMDAwMww",
    "partner": "creator/7cSdD",
    "partner_recording_id": "USE7D0900003",
    "release_date": null,
    "title": "5.7",
    "upc": "705105796444",
    "updated_at": "2015-06-15T22:37:00.156993",
    "vendor_album_id": ""
  }
}
```

(You may see a lot more detail then this, but you only need `response['sound_recording']['_uri']` for now.)

You will use the URI to retrieve status updates, match streamed API results to your content, and include in your **usage reports.**


# Retrieving Requests

## By URI

Send a `GET` request to `/v1/sound_recording/get` with the following parameter:

* `_secret`:
    * Your 'API Secret' which was provided to you.
* `key`:
    * The `_uri` from the request when it was originally made.

### Response

```json
{
  "_message": null,
  "_single": "sound_recording",
  "sound_recording": {
    "_fb": true,
    "_js_kind": "Sound_Recording",
    "_kind": "sound_recording",
    "_permissions": [
      "owner"
    ],
    "_uri": "sound_recording/creator/7cSdD--USE7D0900003",
    "album": "El Diablo De Culiacan",
    "artist": "Atomo",
    "created_ago": null,
    "created_at": null,
    "earliest_clearance_at": null,
    "is_hard_rejection": false,
    "isrc": "USE7D0900003",
    "label": "Del Records",
    "length": 192,
    "license_fulfilled": false,
    "license_fulfilled_at": null,
    "license_status": 2,
    "license_status_str": "In Progress",
    "p_id": "creator/7cSdD--USE7D0900003",
    "p_key": "agxkZXZ-cmRzY292ZXJyMQsSEFJkU291bmRSZWNvcmRpbmciG2NyZWF0b3IvN2NTZEQtLVVTRTdEMDkwMDAwMww",
    "partner": "creator/7cSdD",
    "partner_recording_id": "USE7D0900003",
    "release_date": null,
    "title": "5.7",
    "upc": "705105796444",
    "updated_at": "2015-06-15T22:37:00.156993",
    "vendor_album_id": ""
  },
  "status": "OK"
}
```

### Rejections

If a request has been rejected, it will return a property named `rejection_status_messages`, which is an
array of objects that describe various rejections.

Those look like this:

```json
{
  ...
  "rejection_status_messages": [
    {
      "reason": 5,
      "message": "This musical work has not yet been...",
      "notes": null,
      "is_hard_rejection": false
    }
  ],
  ...
}
```

In some cases, rejected requests may be resent when more information is gathered, or at a later date.
In other cases, the rejection is considered a *hard rejection*, because we are blocked from obtaining a license.
In the case of a hard rejection, requests are not eligible to be resubmitted.

The `notes` field may be propogated to end users for more details about
the rejection, however, _it may not always be populated_, in which cases it may
be ideal to show the `message` value as well.

Rejection reasons are detailed in [enums.md](enums.md).

## Query

Send a `GET` request to `/v1/sound_recordings` with the following parameters:

* `_secret`:
    * Your 'API Secret' which was provided to you.
* `since`:
    * A unix timestamp used to filter the list to only those recordings cleared since you 'last checked'. You may also use an ISO datetime. Use the `retrieved_at` value of a previous query request to create a smart system that only retrieves requests that have been updated since your last query.
* `cursor`:
    * Optional string used to paginate results. Provide the value of 'cursor' from a previous page of the same query to retrieve the next page.
* `status`:
    * Optional string used to filter results. Valid choices include `in_progress`, `completed`, and `rejected`. No
    * value will return all sound recordings.
* `count`:
    * Optional integer to dictate size of one page of results. Should not exceed 100.

### Response:

Json Object containing:
* `cursor`:
    *  String used to fetch next page.
* `count`:
    * Number of results in this pagination.
* `results`:
    * List of results. Each object will contain at the very least:
        * `_uri`: The Loudr URI for this request.
        * `earliest_clearance_at`: The earliest timestamp (UTC) this content may be distributed.
        * `license_fulfilled_at`: When Loudr obtained the license.

```json
{
  "_js_kind": "Results",
  "_kind": "results",
  "count": 1,
  "cursor": "CkcSQWoMZGV2fnJkc2NvdmVycjELEhBSZFNvdW5kUmVjb3JkaW5nIhtjcmVhdG9yLzdjU2RELS1VU0U3RDA5MDAwMDMMGAAgAA==",
  "estimated_total": 64,
  "results": [
    {
      "_fb": true,
      "_js_kind": "Sound_Recording",
      "_kind": "sound_recording",
      "_permissions": [],
      "_uri": "sound_recording/creator/7cSdD--USE7D0900003",
      "album": "El Diablo De Culiacan",
      "artist": "Atomo",
      "created_ago": null,
      "created_at": null,
      "earliest_clearance_at": null,
      "is_hard_rejection": false,
      "isrc": "USE7D0900003",
      "label": "Del Records",
      "length": 192,
      "license_fulfilled": false,
      "license_fulfilled_at": null,
      "license_status": 2,
      "license_status_str": "In Progress",
      "p_id": "creator/7cSdD--USE7D0900003",
      "p_key": "agxkZXZ-cmRzY292ZXJyMQsSEFJkU291bmRSZWNvcmRpbmciG2NyZWF0b3IvN2NTZEQtLVVTRTdEMDkwMDAwMww",
      "partner": "creator/7cSdD",
      "partner_recording_id": "USE7D0900003",
      "release_date": null,
      "title": "5.7",
      "upc": "705105796444",
      "updated_at": null,
      "vendor_album_id": ""
    }
  ],
  "retrieved_at": "2015-06-15T22:11:19.692033",
  "status": "OK"
}
```


# Sending Bulk Requests

For large deliveries of bulk requests, you may choose to send them over SFTP or Email.

### JSON [preferred method]

With a bulk upload, we expect a JSON file with **one line per recording**. See the example [requests-bulk.json](examples/requests-bulk.json).

### CSV

While we prefer the JSON format, you may also create a CSV to export your requests. See the example [requests-bulk.csv](examples/requests-bulk.csv).
Multiple artists and authors should be denoted with the SEMICOLON character, and all fields containing commas may be wrapped in quotes ("). (See request 2 in the above example.)
As a rule, UPCs are best formatted as strings (and presented in quotes), to prevent modern editors from reading scientific notation.

Example:

    "Here’s a ""quote"" in a field"

will appear as

    Here's a "quote" in a field

