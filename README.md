This is a collection of checklists used in the EBI Data submission portal. Updated on 28/02/2020

### Get checklists 

#### from DSP
```sh
curl "https://submission.ebi.ac.uk/api/checklists?size=300" > DSP_schema.json
```

#### Alternative solution

[A script](get_DSP_checklists.py) for extracting the DSP checklists to dir `DSP_checklists`, and generating [a summary csv file](20200228_checklists_summary.csv)

### Structure of DSP checklists
A complete DSP checklist (e.g. [ERC000040](ERC000040.json) includes a `spreadsheetTemplate` and a `validationSchema`. The `validationSchema` can be used to validate your data.

*The validationSchema of some checklists are still under development*
