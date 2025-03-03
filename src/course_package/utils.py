from typing import Any


class DottedDict:
    """Use keys as attributes

    Class to create DottedDict object which is takes an dictionary and
    sets attributes from keys. It also handles nested dictionaries

    Attributes
    ----------
    keys from the dictionary that was put in as a argument

    Typical usage example
    ---------------------

        my_dotted_dict = DottedDict({"foo": "bar"})
        my_dotted_dict.spam = "alot"
    """

    def __init__(self, dictionary: dict):
        """Initializes object

        Args:
          dictionary: dictionary that we want to use dot notation for

        """

        # unravels nested dictionaries with recursion
        for key, value in dictionary.items():
            if isinstance(value, dict):
                value = DottedDict(value)
            self.__dict__[key] = value

    def __getattr__(self, name: str) -> Any:
        """Method to retrieve the value

        Parameters
        ----------
          name: name of the attribute

        Returns
        -------
          value of the attribute

        """
        if name in self.__dict__:
            return self.__dict__[name]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def __setattr__(self, name: str, value: Any):
        """Method to assign a value to an attribute

        Parameters
        ----------
          name: name of the attribute
          value: value of the attribute
        """
        self.__dict__[name] = value
