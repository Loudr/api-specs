To meet the expanding needs of clients, we are developing a RESTful, RAML documented
version of our API.

The fundamental structures are similar to the [v1 API](requests.md).

**Submitting Requests is still only possible via v1.** [See here.](requests.md#making-a-request)

**Clients may pull sound recordings, using one of the following two strategies**:

* [Query for multiple recordings](version2.md#query-sound-recordings)
* [Pull an individual recording](version2.md#individual-sound-recording)

### Request Authentication via Secret

The argument `secret` should contain your client token.
It may be provided in the query string, or in the JSON request data.

**Migrating from v1?** - `_secret` has become `secret`.

## Querying Sound Recordings

**Endpoint:**
`https://loudr.fm/api/client/sound_recordings`


### Pagination

Every query returns a `rel` object containing a link to the `next_page`.
Use this to paginate through the requests.

```json
"rel": {
    "next_page": "/api/client/sound_recordings?count=1&cursor=cXVlcnlUaGVuRmV0Y2g7OTsxMjUzMjY4ODo2OXNzZWJROVQ1dXR4T09hcTA2Y0lROzExOTc2MTg5OjZEVldldzEwUXF1Y2ZZVlRCSTIwdGc7MTIzOTc4NjA6ZU1jcWMtaFNTR2F2eXpCLUF0cDRKdzsxMTU5OTM0Mjo5WXRxUUhDSFN2eWY1bWpLdlVJbmhBOzEyMzA0NzI3OlJGT0xrQmpaUU5tWTdZRHltWjJlY2c7MTIxOTI5NTU6ckZ3OFUtcWFUOHV3TnpHcEpoRWltZzsxMTk5MjM2ODpFSTlHYUtVWFJIdU14TEdOZ2RmWUN3OzExNTk5MzQxOjlZdHFRSENIU3Z5ZjVtakt2VUluaEE7MTE5MDQ2NDg6Y241QVQwQnhUeFdMOU4wRVVyQzd3ZzswOw%3D%3D&secret=xxx"
  }
}
```

### Results

The query will return an array, `results`, containing each "sound recording resource."

```json
{
  "results": [
    { ... }
  ]
}
```

## Individual Sound Recording

**Endpoint:**
`https://loudr.fm/api/client/sound_recording/<client-id>/<vendor-id>`

The API path for a recording is comprised for the client ID, and vendor ID.
https://loudr.fm/api/client/sound_recording/api/client/sound_recording/xxx/abc123 is the home of request "abc123" provided by client "xxx".

This path is provided from the queries in `rel["canonical"] == "/api/client/sound_recording/xxx/abc123"`




# Resources

## Sound Recording `resource:sound-recording`

One or more license requests are embodied in a sound recording.
Multiple requests for one sound recording via the request structure.

See [Making a Request](requests.md#making-a-request).

**For a full example of a returned sound recording resource, [see the example at the end of this document](version2.md#example-sound-recording).**

### uri:
`string-uri`. URI for the recording.

### licensor:
`string`. Licensor of the request. 'licensor' of the content - in the context of
a streaming platform, this would be the distributor that initially
licensed and provided the sound recording underlying this request.

### license_config:
`resource:license-config` License configuration.

### license_fulfilled_at:
`integer-timestamp`. Time when this request was fulfilled.

A license request is considered fulfilled when its been
successfully licensed and is ready to be distributed. Importantly,
see the related `earliest_clearance_at` property, which indicates
WHEN a request may be distributed at the earliest.

### earliest_clearance_at:
`integer-timestamp`. Earliest timestamp when this request may be distributed.

A license request may be cleared for distribution at a
date that trails the `license_fulfilled_at` timestamp. If this is the
case, `earliest_clearance_at` returns a timestamp indicating when the
release may go live. A null value indicates that there is no
additional release restriction being implied.

### requests:
`list of resource:requests`. List of provided request metadata.

### recording:
`resource:recording`. Sound recording metadata.

### fulfillment_status:
`resource:fulfillment-status`. Fulfillment status metadata.

### fulfillment:
`resource:fulfillment`. Details from the fulfillment record.

### royalty_rates:
`resource:royalty-rates`. Royalty rates for this request.

### is_public_domain:
`bool`. Has this request been identified as a public domain usage?

### matched_compositions:
`list of resource:composition`. Compositions matched to this request.

### client:
`string-uri`. Client which owns this request.

### license_kind:
`string`. Kind of license request. Should always be `client request`.

### license_status:
`int`. One of the [license_status enum values](enums.md#license-statuses).

### license_status_str:
`string`. Status of request in english.

### is_rejection:
`bool`. Has this request been rejected?

### is_hard_rejection:
`bool`. Is this a HARD rejection? Requests which have been 'hard rejected' may not be resubmitted.

### rejections:
`list of resource:rejection`. List of applicable rejections.

### rel:
`object`. Contains links relative to this resource.


## Recording `resource:recording`

Provided metadata about a specific recording.

```json
"requests": [
  {
    "provided_research": {
      "album": [],
      "artist": [],
      "author": [
        "Laurent Lescarret"
      ],
      "composer": [
        "Laurent Lescarret"
      ],
      "composition_index": 0,
      "iswc": "T7027742505",
      "link": [],
      "notes": null,
      "source": [],
      "suggested_composition": "",
      "title": [
        "LE PARDON DU CHEVREUIL"
      ]
    }
  }
]
```

### title:
`string`. Recording title.

### artist:
`list of string`. Recording artist(s).

### album:
`string`. Recording album the song is released on, if any.

### isrc:
`string`. Recording ISRC.

### upc:
`string`. UPC for recording's release.

### label:
`string`. Label for this release.

### licensor:
`string`. Licensor for this release.

### vendor_id:
`string`. Vendor's ID.

### vendor_album_id:
`string`. Vendor's album ID.


## Request `resource:request`

An individual song request provided for with a sound recording.
More than one may exist per request, if the request is understood to be a medley.
If Loudr determines that a recording is a medley, additional requests will be added
to accomodate this discovery.

```json
[
  {
    "provided_research": {
      "album": [
        "Joyful, Vol. 6"
      ],
      "artist": [
        "Tom Dwyer"
      ],
      "iswc": null,
      "author": [],
      "composition_index": 0,
      "source": [],
      "link": [],
      "composer": [
        "Thomas Dwyer"
      ],
      "title": [
        "Time"
      ],
      "suggested_composition": "",
      "notes": null
    }
  }
]
```

### provided_research:
`resource:provided-research`. Object containing provided research for this request.


## Provided Research `provided-research`

Provided research, used to help identify works. (See [resource:request example](version2.md#request-resourcerequest))

### composition_index:
`int`. Index of this request. Helps match requests with matched compositions.

For example, if the a `matched_compositions` resource has `composition_index: 2`,
it corresponds to the `requests` resource with `composition_index: 2` as well.

### title:
`list of string`. Provided composition titles.

### artist:
`list of string`. Original performing artist(s).

### composer:
`list of string`. Original composer(s).

### author:
`list of string`. Original author(s) of the song.

Authors and composers may overlap, if so, they
only need to be mentioned once.

### album:
`list of string`. Original album the song was released on, if any.

### source:
`list of string`. Original source material, such as a movie or
    video game title.

### link:
`list of string`. URL to the source material.

### iswc:
`string`. International Standard Musical Work Code.

### notes:
`string`. Any additional notes to aid composition search.

### suggested_composition:
`string-uri`. Composition suggested by client.


## License Config `resource:license-config`

Describes the quantity and configuration of the license request.
Serialized as an object containing `{license_type: units}`.
A units value of -1 represents continuous administration, not fixed quantity.

```json
"license_config": {
    "dpd": -1,
    "stream": -1
}
```

Requests infinite streaming & digital downloads.


## Royalty Rates `resource:royalty-rates`

Describes the royalty rate for each configuration specified by `license_config`.
Serialized as an object containing `{license_type: royalty_per_unit}`.

The royalty per unit is expressed as a decimal value in USD.

```json
"royalty_rates": {
    "dpd": "0.091",
    "stream": "0.01"
}
```


## Fulfillment Status `resource:fulfillment-status`

Represents the fulfillment status for a request.

```json
{
  "allowed_expense": {
    "name": "NONE",
    "value": 0
  },
  "license_fulfilled": true,
  "license_fulfilled_at": "2017-01-31T01:33:04.571750+00:00",
  "maximum_expense": 0
}
```

### license_fulfilled:
`bool`. Has this request been fulfilled?

### license_fulfilled_at:
`timestamp-int`. When was this request fulfilled?

### allowed_expense:
`object`. Maximum expense authorized by client.
This is used by clients which approve their fulfillment expenses.

### maximum_expense:
`int`. Maximum expense imposed by this request.


## Fulfillment Detail `resource:fulfillment`

Describes the status of fulfillment for a recording.

```json
{
  "completed": true,
  "fulfilling_publishers": [
    "Sony/ATV Music Publishing LLC"
  ],
  "fulfillment_license_ids": [
    1234567890000000
  ],
  "fulfillment_methods": [
    "blanket"
  ],
  "territories": [
    "US"
  ],
  "uri": "sound_recording/creator/xxx--abc123/license_usage/active"
}
```

### completed:
`bool`. Has this fulfillment been completed.

### fulfillment_license_ids:
`list of int`. License fulfillment IDs. Used to verify fulfillment to publishing entities.

### fulfillment_methods:
`list of string`. Methods used to fulfill this request. Values include:
* `blanket`
* `digital-noi`
* `physical-noi`
* `copyright-noi`
* `direct`

### territories:
`list of string`. List of territories this license is being fulfilled in.
This will always be `["US"]` for now.

## Composition `resource:composition`

Represents a composition in Loudr's database which matched to this request.
Compositions are returned in `matched_compositions` of a license request.

```json
{
  "alias": [],
  "author_names": [
    "Laurent Lescarret"
  ],
  "author_publisher_pairs": [
    {
      "author": "Laurent Lescarret",
      "publisher": "Sony/ATV Music Publishing LLC"
    }
  ],
  "authors": [
    {
      "ipi": null,
      "name": "Laurent Lescarret",
      "role": {
        "code": "CA",
        "id": 1,
        "name": "Composer & Author"
      }
    }
  ],
  "composition_index": 0,
  "display_name": "LE PARDON DU CHEVREUIL",
  "kind": "composition",
  "publishers": [
    "Sony/ATV Music Publishing LLC"
  ],
  "rel": {
    "canonical": "/api/composition/dabt2KGm"
  },
  "title": "LE PARDON DU CHEVREUIL",
  "uri": "composition/dabt2KGm"
}
```

### title:
`string`. Title of the composition.

### alias:
`list of string`. Alternate titles for the composition.

### composition_index:
`int`. Used when the composition relates to a request index in a given way.
For example, if the a `matched_compositions` resource has `composition_index: 2`,
it corresponds to the `requests` resource with `composition_index: 2` as well.

### authors:
`list of objects`. A list of authors with Loudr metadata. Objects will contain
name, author role, and IPI. Of these, only name has a guaranteed response.

### author_publisher_pairs:
`list of objects`. A list of `{"author": author, "publisher": publisher}` objects.
The pairs of authors and publishers are not indicative of a relationship
between these two entities. Rather, `author_publisher_pairs` is provided as a
convenience tool for integrations that require such formatting.
The value "Unknown" is used in the absence of any information.


# Example Sound Recording

```json
{
  "client": "creator/xxx",
  "earliest_clearance_at": null,
  "fulfillment": {
    "completed": true,
    "fulfilling_publishers": [
      "Sony/ATV Music Publishing LLC"
    ],
    "fulfillment_license_ids": [
      1234567890000000
    ],
    "fulfillment_methods": [
      "blanket"
    ],
    "territories": [
      "US"
    ],
    "uri": "sound_recording/creator/xxx--abc123/license_usage/active"
  },
  "fulfillment_status": {
    "allowed_expense": {
      "name": "NONE",
      "value": 0
    },
    "license_fulfilled": true,
    "license_fulfilled_at": "2017-01-31T01:33:04.571750+00:00",
    "maximum_expense": 0
  },
  "is_hard_rejection": false,
  "is_public_domain": false,
  "is_rejection": false,
  "license_config": {
    "stream": -1
  },
  "license_fulfilled_at": "2017-01-31T01:33:04.571750+00:00",
  "license_kind": "client request",
  "license_status": 3,
  "license_status_str": "Completed",
  "licensor": null,
  "matched_compositions": [
    {
      "alias": [],
      "author_names": [
        "Laurent Lescarret"
      ],
      "author_publisher_pairs": [
        {
          "author": "Laurent Lescarret",
          "publisher": "Sony/ATV Music Publishing LLC"
        }
      ],
      "authors": [
        {
          "ipi": null,
          "name": "Laurent Lescarret",
          "role": {
            "code": "CA",
            "id": 1,
            "name": "Composer & Author"
          }
        }
      ],
      "composition_index": 0,
      "display_name": "LE PARDON DU CHEVREUIL",
      "kind": "composition",
      "publishers": [
        "Sony/ATV Music Publishing LLC"
      ],
      "rel": {
        "canonical": "/api/composition/dabt2KGm"
      },
      "title": "LE PARDON DU CHEVREUIL",
      "uri": "composition/dabt2KGm"
    }
  ],
  "payment_complete": false,
  "payment_initiated": null,
  "recording": {
    "album": "Lieu-dit (Bonus Track Version)",
    "artist": [
      "Doriand"
    ],
    "isrc": "FR13Z1100005",
    "label": "Johnny Flyer",
    "licensor": null,
    "title": "Le pardon du chevreuil",
    "upc": "3700551739820",
    "vendor_album_id": null,
    "vendor_id": "abc123"
  },
  "rejections": [],
  "rel": {
    "canonical": "/api/client/sound_recording/xxx/abc123"
  },
  "renewal_complete": null,
  "renewal_failed": null,
  "renewal_of": null,
  "requests": [
    {
      "provided_research": {
        "album": [],
        "artist": [],
        "author": [
          "Laurent Lescarret"
        ],
        "composer": [
          "Laurent Lescarret"
        ],
        "composition_index": 0,
        "iswc": "T7027742505",
        "link": [],
        "notes": null,
        "source": [],
        "suggested_composition": "",
        "title": [
          "LE PARDON DU CHEVREUIL"
        ]
      }
    }
  ],
  "royalty_rates": {
    "stream": "0.01"
  },
  "uri": "sound_recording/creator/xxx--abc123"
}
```

