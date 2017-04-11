It is highly recommended that all clients integrate with Loudr using the [Version 2 API, click here for details](https://github.com/Loudr/api-specs/blob/master/version2.md).

This document is provided as a guide for clients still using the version 1 integration for reading responses.

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
