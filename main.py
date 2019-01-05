#!/usr/bin/env python
import nf_core.workflow as wf

import json
import jsonschema
import os
import sys

FILE_PATH = os.path.dirname(__file__)

EXAMPLE_JSON = os.path.join(FILE_PATH, "example.json")
EXAMPLE_SCHEMA = os.path.join(FILE_PATH, "example.schema.json")


def run():
    # Convert schema JSON
    with open(EXAMPLE_SCHEMA) as fp:
        schema = json.load(fp)

    # Read parameter JSON
    with open(EXAMPLE_JSON) as fp:
        params = fp.read()

    # Validate parameter JSON against schema
    jsonschema.validate(json.loads(params), schema)

    workflow = wf.Workflow("example", params)
    print(workflow.as_params_json(indent=4))
    # Modify a value
    workflow.parameters[1].value = 100
    print("Parameter after modification:")
    print(workflow.as_params_json(indent=4))


if __name__ == "__main__":
    run()
