from dictpymap import transform_data_to_data_schema, return_value_from_path_or_none

from typing import Any, List, Optional


def return_value_from_path_or_test_str(data: dict[Any, Any], path: List[str]) -> Optional[Any]:
    value = return_value_from_path_or_none(data, path)
    return value or "TEST_VALUE!"


class TestMain:
    def test_minimal(self):
        schema = {
            "hardcoded_str": "hardcoded",
            "hardcoded_none": None,
            "path_shortcut": ["existing", "path"],
            "full_config": {
                "path": ["Another", "Path"],
                "function": return_value_from_path_or_test_str,
            },
            "non_existing": ["Non", "existing", "path"],
            "full_config_non_existing": {
                "path": ["Another", "Non", "Existent", "Path"],
                "function": return_value_from_path_or_test_str,
            },
        }
        data = {"existing": {"path": "Hello"}, "Another": {"Path": "World!"}}
        expected = {
            "hardcoded_str": "hardcoded",
            "hardcoded_none": None,
            "path_shortcut": "Hello",
            "full_config": "World!",
            "non_existing": None,
            "full_config_non_existing": "TEST_VALUE!",
        }
        actual = transform_data_to_data_schema(schema, data)
        assert expected == actual
