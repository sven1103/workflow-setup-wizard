# workflow-setup-wizard
Consumes a Nextflow workflow parameter metadata JSON and provides a model to query these.

Some parameter properties could look like these:

* name: (*) the parameter name, it should a valid identifier (no blanks, etc)
* label: human readable name
* usage: param description showed in the help text
* type: (*) string, integer, decimal, boolean, mem unit
* render: file (local path), url, upload, range, check-box, radio-button, list-box, drop-down
* choices: possible values for check-box, radio-button, list-box, drop-down
* defvalue: (*) default value
* pattern: regex validation rule
* arity: 1 or many