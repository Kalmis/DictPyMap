from typing import Any, List, Optional
from .exceptions import InvalidConfigOrData


def return_value_from_path_or_none(data: dict[Any, Any], path: List[str]) -> Optional[Any]:
    element_value = data
    try:
        for element_name in path:
            element_value = element_value[element_name]
        return element_value
    except KeyError:
        return None
    except TypeError:
        raise InvalidConfigOrData(
            f"While traversing path {path} at step {element_name} a element value of "
            f"{type(element_value)} was encountered and dict was expected"
        )
