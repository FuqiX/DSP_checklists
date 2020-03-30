This is a collection of checklists used in the EBI Data submission portal. Updated on 28/02/2020

### Get checklists 

#### from DSP
```sh
# From DSP dev
curl "https://submission-test.ebi.ac.uk/api/checklists?ize=300" > DSP_schema.json

# From DSP production, not available until end of April, 2020
curl "https://submission.ebi.ac.uk/api/checklists?ize=300" > DSP_schema.json
```

#### Alternative solution

[A script](https://github.com/FuqiX/DSP_checklists/blob/master/get_DSP_checklists.py) for extracting the DSP checklists to dir `DSP_checklists`, and generating [a summary csv file](https://github.com/FuqiX/DSP_checklists/blob/master/20200228_checklists_summary.csv)

### Structure of DSP checklists
A complete DSP checklist (e.g. [ERC000040](https://github.com/FuqiX/DSP_checklists/blob/master/ERC000040.json) includes a `spreadsheetTemplate` and a `validationSchema`. The `validationSchema` can be used to validate your data.

*The validationSchema of some checklists are still under development*
