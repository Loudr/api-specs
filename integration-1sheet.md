# Integration & On-boarding with Loudr

Integration with Loudr occurs multiple phases:

1. Content Match Test
2. Integration Test
3. Production Onboarding


## 1. Content Match Test

The content match test is designed to provide Loudr fulfillment options
for a given sample set of requests.

Loudr expects a data file containing requests in one of the following formats.
Learn more about the expected values in [requests](requests.md).

* **JSON Format**.
    Our preferred format for all data is JSON. See an example delivery at [requests-bulk.json](examples/requests-bulk.json).
    Please review the [request specification](requests.md) for clarity on fields. See this [single request](examples/request-single.json) for a more detailed example.

* **CSV Format**.
    You may submit a single `CSV` containing requests in the format demonstrated by [requests-bulk.csv](examples/requests-bulk.csv).
    Please review the [request specification](requests.md) for clarity on fields.


## 2. Integration Testing

Integration testing occurs in two parts:

a. Content Delivery Integration
b. Usage Report Integration Test


### a. Content Delivery Integration

If you have completed a "Content Match Test," you are technically ready to deliver
requests to Loudr.

We will want to verify:

* `vendor_id`/`partner_recording_id` uniquely identifies all requests.
* `length` is provided in the correct format (seconds).
* `metadata:publisher` is provided if available.
* provided research via `work author`/`compositions`


**Integrating via API**

You have the option of integrating with our API to deliver requests on the fly.
This is the expected option for partners which supply end-user licensing via Loudr's backend.

To test the API, we will expect you to deliver 9 requests with a sandbox API secret provided by Loudr.
Upon successful delivery, we will provide responses which simulate the following results:

* Public Domain (`public-domain`)
* Soft Rejection (`rejected`)
* Rejection with Notes (`rejected-more-info`)
* Hard Rejection (`rejected-hard`)
* Archived (`archived`)
* Fulfilled via Physical NOI (`physical`)
* Fulfilled via Digital NOI (`digital`)
* Fulfilled via Direct License (`direct`)
* Fulfilled via Blanket (`blanket`)
* Medley fulfillment (`medley`)

For most partners, there will be no difference between the method of fulfillment, as provided by
`physical`, `digital`, `direct`, and `blanket`. These are here for the record.

Clients will be expected to deliver requests via the v1 API specs detailed in [requests.md](requests.md).
Clients may query requests according to the [version-2 specificaitons](version2.md).

### b. Usage Report Integration Test

We expect all clients to be able to deliver their usage reports according to our [usage report specification](usage-reports.md).
We will want to receive an example delivery before we can commit to paying publishers for your content.


## 3. Production On-boarding

Once all integration tests are complete, we will be ready to move to a production environment,
where your requests will actively be matched and fulfilled.

Upon production integration, we deliver the API secret token for access.

