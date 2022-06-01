from typing import Any, Callable, Dict, List, Union

from .exceptions import InvalidConfigError
from .functions import return_value_from_path_or_none

SchemaDict = Dict[Any, Union[str, Dict]]


def transform_data_to_data_schema(
    schema_config: SchemaDict,
    data: Dict[Any, Any],
    default_function: Callable[[Dict, List], Any] = return_value_from_path_or_none,
):
    new_data: Dict[Any, Any] = {}
    for key, config in schema_config.items():
        if config is None or isinstance(config, str):
            # None or hardcoded strings are allowed
            new_data[key] = config
        elif isinstance(config, list):
            # The default option, value is a "__path" to the value of interest
            new_data[key] = default_function(data, config)
        elif isinstance(config, dict) and "__path" in config and "__function" in config:
            # Full config given.
            new_data[key] = config["__function"](data, config["__path"])
        elif isinstance(config, dict):
            # The dictionary is part of the new schema
            new_data[key] = transform_data_to_data_schema(config, data)
        else:
            raise InvalidConfigError(f"Key {key} in schema has invalid config")
    return new_data
