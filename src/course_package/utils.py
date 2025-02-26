class DottedDict:
    """
     Class to create DottedDict object which is takes an dictionary and
     sets attributes from keys.

     It also handles nested dictionaries

    Args:
        dictionary (dict): 

    Returns:
        (MakeDatasetObject): object with attributes for each key

    """
    def __init__(self, dictionary):

        # unravels nested dictionaries with recursion
        for key, value in dictionary.items():
            if isinstance(value, dict):
                value = DottedDict(value)
            self.__dict__[key] = value

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def __setattr__(self, name, value):
        self.__dict__[name] = value
