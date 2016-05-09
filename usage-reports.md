_this document will always live at (https://github.com/Loudr/api-specs/blob/master/usage-reports.md)_

# Delivering Usage Reports

Loudr accepts Usage Reports to enable administration for content that we have
licensed on your behalf.


## Usage Report Format

The usage report is a multi-line JSON file containing information required to pay
administrators for your content.

### Aggregating Report Lines

We will require this information to be **aggregated by these identifying fields**:

- Vendor ID
- Type of Configuration
- Units
- Date of Fixation/Reproduction
- Per-Play License Fee
- Platform/Store of Reproduction (i.e. iTunes)
- Country of Fixation or Reproduction (i.e. US for now)

As such, in a report you may yield multiple lines for a single piece of content.

For example, if `my-vendor-id` plays ten times with two different
per-play fees, you would generate two lines, grouping the plays by the fields
mentioned above:

```json
{"vendor_id": "my-vendor-id", "license_fee": "0.0054", "units": 6, "date": "2015-05-01", "config": "stream", "country": "US", "store": "itunes"}
{"vendor_id": "my-vendor-id", "license_fee": "0.0064", "units": 4, "date": "2015-05-01", "config": "stream", "country": "US", "store": "itunes"}
```


### Report Segmentation

Due to the complexity of the reports, you may segment the your report into multiple
files as you please. If you have a lot of usage data, we reccommend a segmenting your data
into weekly or daily groupings. (or more, if desired)

_Each uploaded file will appear with attached royalties and service fee for your review
before finalizing and adding the cost to your monthly invoice._


### Report Compression

Due to the required granularity of the report, these usage reports may be very large.
To mitigate this, we **strongly encourage** you to `gzip` your reports before uploading to the dashboard.

The ideal filename for delivery will ultimately look similar to `usage-report-YYYY-MM-DD.json.gz`.


### Report Delivery

Initially, delivery of usage reports will be executed via your client dashboard,
which we will have available at a later date.

As the size of reports grow, we may support delivery over SFTP at a later date.


## Full `.json` Specification


Each line of the report should be a single JSON object with no trailing commas
or enclosing array brackets around all items.

The full specification of fields follows:

### License ID

**One, and only one** of the following identifiers is required to match your usage
to your licensed  content. We recommend the `vendor_id`.

    vendor_id:
        `str`. Vendor ID.


    loudr_uri:
        `str`. Loudr URI of request.


    isrc:
        `str`. ISRC of content. Only use this if you do not have the
        vendor_id or loudr_uri explicitly.


### Usage data

    license_fee:
        `str`. Applicable per-play Music License Fee, as determined by
        Client based on internal service information.

        A string intepretation of this decimal value in USD is expected.
        Please avoid using float values, as json parsing may lose accuracy
        of high-precision values.

        This value may be omitted depending on how your deal with Loudr is
        structured. We may be ultimately responsible for determining this value,
        in which case you may omit this property, or provide a `null` value.


    fee_currency:
        `str`. Not yet supported. License fee currency.
        "USD" is implied at this time, this field should be omitted.


    config:
        `str`. Type of configuration made pursuant to the license. We use this value
        to communicate how content was delivered to publishers, in addition to
        asserting that license configurations were are correctly fulfilled.

        Expected values include:
            "stream" - interactive stream
            "download" or "dpd" - digital permanent download

    units:
        `int`. Number of fixations or reproductions made pursuant to the license.
        This integer is multiplied by the license_fee to determine the payout
        due to publishers.


    country:
        `str`. Country of fixation or reproduction.
        This value should be a 2 character ISO-3166 country code.
        Right now, we only accept the value `US` - for United States.


    date:
        `str`. ISO formatted date "YYYY-MM-DD" of content delivery.


    store:
        `str`. The name of the distribution outlet which serviced this usage.
        Accepted values are listed below. If you have received royalty revenue from a
        store we do *not* have listed below, please contact your business representative.

#### Stores

Accepted values for the `store` property are below:

* `itunes`: Apple iTunes / Apple Music
* `spotify`: Spotify
* `googlemusic`: Google Music
* `amazon`: Amazon
* `deezer`: Deezer
* `rdio`: Rdio


#### Ideal line formatting:
```json
{"vendor_id": "my-vendor-id", "license_fee": "0.0054", "units": 6, "date": "2015-05-01", "config": "stream", "country": "US", "store": "itunes"}
{"vendor_id": "my-vendor-id", "license_fee": "0.0064", "units": 4, "date": "2015-05-01", "config": "stream", "country": "US", "store": "itunes"}
{"vendor_id": "my-vendor-id", "license_fee": "0.0064", "units": 9, "date": "2015-05-02", "config": "stream", "country": "US", "store": "itunes"}
```

#### OK line formatting:
```json
[{"vendor_id": "my-vendor-id", "license_fee": "0.0054", "units": 6, "date": "2015-05-01", "config": "stream", "country": "US", "store": "itunes"},
{"vendor_id": "my-vendor-id", "license_fee": "0.0064", "units": 4, "date": "2015-05-01", "config": "stream", "country": "US", "store": "itunes"},
{"vendor_id": "my-vendor-id", "license_fee": "0.0064", "units": 9, "date": "2015-05-02", "config": "stream", "country": "US", "store": "itunes"}]
```

#### Bad line formatting:
Do NOT send usage reports in multiple lines, or a single line:
```json
[
  {
    "vendor_id": "my-vendor-id",
    "license_fee": "0.0054",
    "units": 6,
    "date": "2015-05-01",
    "config": "stream",
    "country": "US",
    "store": "itunes"
  },
  {
    "vendor_id": "my-vendor-id",
    "license_fee": "0.0064",
    "units": 4,
    "date": "2015-05-01",
    "config": "stream",
    "country": "US",
    "store": "itunes"
  },
  {
    "vendor_id": "my-vendor-id",
    "license_fee": "0.0064",
    "units": 9,
    "date": "2015-05-02",
    "config": "stream",
    "country": "US",
    "store": "itunes"
  }
]
```

Also wrong:
```json
[{"vendor_id":"my-vendor-id","license_fee":"0.0054","units":6,"date":"2015-05-01","config":"stream","country":"US"},{"vendor_id":"my-vendor-id","license_fee":"0.0064","units":4,"date":"2015-05-01","config":"stream","country":"US"},{"vendor_id":"my-vendor-id","license_fee":"0.0064","units":9,"date":"2015-05-02","config":"stream","country":"US"}]
```


## Discrepencies between expected royalty costs, and actual royalty costs

You may note that some usage reports yield a larger royalty cost than the
sum of all provided `license_fee * units`. This is due to the fact that
some recordings might be identified as medleys, and require one or more
licenses to fulfill.

We will integrate a system that catches these cases and communicates them
back to you as we continue to develop our systems.
