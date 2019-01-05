import copy
import json

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

        Raises:
            IOError, if the JSON is of unknown schema to this parser.
        """
        properties = json.load(parameters_json)
        parameters = []
        try:
            for param in properties.get("parameters"):
                parameter = Parameter.builder().name(param.get("name"))
                                .label(param.get("label"))
                                .usage(param.get("usage"))
                                .type(param.get("type"))
                                .choices(param.get("choices"))
                                .default(param.get("default"))
                                .pattern(param.get("pattern"))
                                .arity(param.get("arity"))
                                .build()
                parameters.append(parameter)
            except Exception as e: 
                raise IOError(e)
        return parameters


class Parameter(object):
    """Holds information about a workflow parameter.
    """
    def __init__(self, param_builder):
        # Make some checks
        
        # Put content
        self.p_name = param_builder.p_name
        self.p_label = param_builder.p_label
        self.p_usage = param_builder.p_usage
        self.p_type = param_builder.p_type
        self.p_choices = copy.deepcopy(param_builder.p_choices)
        self.p_default_value = param_builder.p_default_value
        self.p_pattern = param_builder.p_pattern
        self.p_arity = param_builder.p_arity
    
    @staticmethod
    def builder():
        return ParameterBuilder()

class ParameterBuilder:
    """Parameter builder.
    """
    def __init__(self):
        self.p_name = ""
        self.p_label = ""
        self.p_usage = ""
        self.p_type = ""
        self.p_choices = []
        self.p_default_value = ""
        self.p_pattern = ""
        self.p_arity = ""
    
    def name(self, name):
        self.p_name = name
        return self
    
    def label(self, label):
        self.p_label = label
        return self
    
    def usage(self, usage):
        self.p_usage = usage
        return self
    
    def param_type(self, param_type):
        self.p_type = param_type
        return self
    
    def default(self, default):
        self.p_default_value = default
        return self
    
    def patter(self, pattern):
        self.p_pattern = pattern
        return self
    
    def build(self):
        return Parameter(self)

