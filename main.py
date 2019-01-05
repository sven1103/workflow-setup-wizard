#!/usr/bin/env python
import nf_core.workflow as wf

import sys


def run(json_file):
    with open(json_file, "r") as fh:
        content = fh.read()
    workflow = wf.Workflow("example", content)
    print(workflow.as_params_json())


if __name__ == "__main__":
    assert len(sys.argv) == 2
    run(sys.argv[1])
