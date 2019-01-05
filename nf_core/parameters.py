class Parameters:
    """Contains a static factory method
    for :class:`Parameter` object creation.
    """
    @staticmethod
    def create_from_json(parameters_json):
        """Creates a list of Parameter objects from
        a description in JSON.

        Args:
            parameters_json (str): Parameter(s) description in JSON.

        Returns:
            list: Parameter objects.
        """
        return None


class Parameter(object):
    """Holds information about a workflow parameter.
    """
    def __init__(self):
        pass