# API Enumerations

## License Statuses

```js

license_statuses =
{
    0: "Unpaid",
    1: "Payment Pending",
    2: "In Progress",
    3: "Completed",
    4: "Rejected",
    5: "Pending Expense",
};

```

## License Configurations

Valid values for license configuration type:

```js

license_configuration_types = {
    'stream':           "INTERACTIVE_STREAM",
    'download':         "DPD",
    'dpd':              "DPD",
    'cd':               "PHYSICAL",
    'record':           "PHYSICAL",
    'physical':         "PHYSICAL",
    'ringtone':         "RINGTONE",
};

```

## Rejection Reasons

```js
rejection_reasons = {
    0: "Not rejected",
    1: "Other (See attached notes)",
    2: "Provided composition information is insufficient to identify the underlying musical work(s). Please re-submit with additional identifying information.",
    3: "Provided composition information is improperly formatted (for example, multiple pieces of information in the same field). Please reformat the provided information and re-submit.",
    4: "This musical work has been pre-emptively blocked by a publisher, and cannot be released. Please do NOT re-submit this work.",
    5: "This musical work has not yet been officially released as a phonorecord in the United States. Please re-submit when the work has been officially released.",
};

REJECTION_OTHER = 1;
REJECTION_RESEARCH_INSUFFICIENT = 2;
REJECTION_RESEARCH_FORMATTING = 3;
REJECTION_PUBLISHER_REJECTION = 4;
REJECTION_NOT_YET_RELEASED_IN_US = 5;
```
