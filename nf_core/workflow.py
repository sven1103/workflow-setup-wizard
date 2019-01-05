from parameters import Parameters
from parameters import Parameter

class Workflow(object):
    """nf-core workflow object that holds run parameter information.

    Args:
        name (str): Workflow name.
        parameters_json (str): Workflow parameter data in JSON. 
    """
    def __init__(self, name, parameters_json):
        self.name = name
        self.parameters = Parameters.create_from_json(parameters_json)
