This is a collection of [meta]data standards used in the EBI Data submission portal. Updated on 14/05/2020

DSP have two endpoints for querying those standards, __checklists__ and __validationSchema__. A complete DSP checklist (e.g. [ERC000040](ERC000040.json) includes a `spreadsheetTemplate` and a `validationSchema`. The `validationSchema` can be used to validate your JSON data.

*The validationSchema of some checklists are still under development*

:bulb: It's recommended to use the [validationschema](https://submission.ebi.ac.uk/api/validationSchemas?size=100) endpoint, instead of the [checklists](https://submission.ebi.ac.uk/api/checklists?size=100) endpoint.


#### Get validation schemas
```sh
#validation schemas
curl "https://submission-test.ebi.ac.uk/api/validationSchemas?size=100 " > DSP_schema.json
```

#### Get A summary of all validationschemas

[A small script](get_DSP_checklists.py) to extract all DSP validation schemas into seperate JSON files, and generate [a summary tsv file](validationSchema_summary.tsv).


