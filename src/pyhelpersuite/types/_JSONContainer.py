import json

#class JSONContainer:
class JSON:
    """
    A container class for handling any data from a JSON format.

    This class provides methods to load data from a string or file, dump data to a string or file,
    and allows accessing and modifying the stored data. It also supports dynamic creation of the
    object from a JSON string or file.

    Attributes:
        _data: The stored data, which can be of any type.
    """

    def __init__(self, data=None):
        """
        Initialize the container with the provided data.

        Parameters:
            data: The initial data to be stored in the container. Can be of any type. Default is None.
        """
        self._data = data

    def __call__(self):
        """
        Return the stored data when the object is called.

        Returns:
            any: The stored data of any type.
        """
        return self._data

    @property
    def value(self):
        """
        Get the stored value.

        Returns:
            any: The stored data of any type.
        """
        return self._data

    @value.setter
    def value(self, new_value):
        """
        Set a new value to the container.

        Parameters:
            new_value: The new data to be stored. Can be of any type.
        """
        self._data = new_value

    def loads(self, json_string, **kwargs):
        """
        Load data from a JSON string and store it in the container.

        Parameters:
            json_string (str): A string containing JSON data.
            **kwargs: Additional arguments for json.loads. For example:
                - 'parse_float': Use a custom function to parse floats (e.g., parse_float=decimal.Decimal).
                - 'object_hook': Custom function to transform JSON objects (e.g., object_hook=my_custom_decoder).
        """
        self._data = json.loads(json_string, **kwargs)

    def load(self, file_path, **kwargs):
        """
        Load data from a JSON file and store it in the container.

        Parameters:
            file_path (str): Path to the JSON file.
            **kwargs: Additional arguments for json.load. For example:
                - 'object_hook': Custom function to transform JSON objects (e.g., object_hook=my_custom_decoder).
                - 'parse_int': Custom function to parse integers (e.g., parse_int=lambda x: int(x, 16)).
        """
        with open(file_path, 'r') as f:
            self._data = json.load(f, **kwargs)

    def dump(self, file_path, **kwargs):
        """
        Dump the stored data into a file.

        Parameters:
            file_path (str): Path to the file where data will be written.
            **kwargs: Additional arguments for json.dump. For example:
                - 'indent': Number of spaces for indentation (e.g., indent=4).
                - 'separators': Tuple to specify separators between items (e.g., separators=(',', ':')).
        """
        with open(file_path, 'w') as f:
            json.dump(self._data, f, **kwargs)

    def dumps(self, **kwargs):
        """
        Return the stored data as a JSON string.

        Parameters:
            **kwargs: Additional arguments for json.dumps. For example:
                - 'indent': Number of spaces for indentation (e.g., indent=4).
                - 'ensure_ascii': Ensure the output is ASCII-only (e.g., ensure_ascii=False).
        
        Returns:
            str: JSON string representation of the stored data.
        """
        return json.dumps(self._data, **kwargs)

    def dumpf(self, file_obj, **kwargs):
        """
        Dump the stored data to a file-like object.

        Parameters:
            file_obj: File object or file descriptor where data will be written.
            **kwargs: Additional arguments for json.dump. For example:
                - 'indent': Number of spaces for indentation (e.g., indent=4).
                - 'default': Function to handle objects that cannot be serialized (e.g., default=str).
        """
        json.dump(self._data, file_obj, **kwargs)

    def type(self):
        """
        Return the type of the stored data.

        Returns:
            type: The type of the stored data.
        """
        return type(self._data)

    @staticmethod
    def from_str(json_str, **kwargs):
        """
        Create a JSONContainer object from a JSON string.

        Parameters:
            json_string (str): A string containing JSON data.
            **kwargs: Additional arguments for json.loads. For example:
                - 'parse_float': Custom function to parse floats (e.g., parse_float=decimal.Decimal).
                - 'object_hook': Custom function to transform JSON objects (e.g., object_hook=my_custom_decoder).

        Returns:
            JSONContainer: A new JSONContainer object containing the data from the string.
        """
        data = json.loads(json_str, **kwargs)
        return JSONContainer(data)

    @staticmethod
    def from_file(file_path, **kwargs):
        """
        Create a JSONContainer object from a JSON file.

        Parameters:
            file_path (str): Path to the JSON file.
            **kwargs: Additional arguments for json.load. For example:
                - 'object_hook': Custom function to transform JSON objects (e.g., object_hook=my_custom_decoder).
                - 'parse_int': Custom function to parse integers (e.g., parse_int=lambda x: int(x, 16)).

        Returns:
            JSONContainer: A new JSONContainer object containing the data from the file.
        """
        with open(file_path, 'r') as f:
            data = json.load(f, **kwargs)
        return JSONContainer(data)

    def __repr__(self):
        """
        Return a string representation for debugging purposes.

        Returns:
            str: String representation of the class instance, including the type and data.
        """
        return f"JSONContainer(data={repr(self._data)})"

    def __str__(self):
        """
        Return a user-friendly string representation of the stored data in JSON format.

        Returns:
            str: Pretty-printed JSON string of the stored data with an indent of 4 spaces.
        """
        return json.dumps(self._data, indent=4)
