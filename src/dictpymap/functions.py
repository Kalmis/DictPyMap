from typing import Any, Dict, List, Optional

from .exceptions import InvalidConfigOrDataError


def return_value_from_path_or_none(data: Dict[Any, Any], path: List[str]) -> Optional[Any]:
    element_value = data
    element_name = None
    try:
        for element_name in path:
            element_value = element_value[element_name]
        return element_value
    except KeyError:
        return None
    except TypeError:
        raise InvalidConfigOrDataError(
            f"While traversing path {path} at step {element_name} a element value of "
            f"{type(element_value)} was encountered and dict was expected"
        )
