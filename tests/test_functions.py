import pytest
from dictpymap import return_value_from_path_or_none, InvalidConfigOrData


class TestFunctions:
    def test_return_value_or_none(self):
        expected = "value!"
        data = {"existing": {"path": expected}}
        actual = return_value_from_path_or_none(data, ["existing", "path"])
        assert expected == actual

    def test_return_value_or_none_non_existing_value(self):
        data = {}
        actual = return_value_from_path_or_none(data, ["non", "existent"])
        assert actual is None

        data = {"non": {}}
        actual = return_value_from_path_or_none(data, ["non", "existent"])
        assert actual is None

    def test_return_value_or_none_invalid_data(self):
        data = {"non": []}
        with pytest.raises(InvalidConfigOrData):
            return_value_from_path_or_none(data, ["non", "existent"])

        data = {"non": "text"}
        with pytest.raises(InvalidConfigOrData):
            return_value_from_path_or_none(data, ["non", "existent"])

        data = {"non": 1}
        with pytest.raises(InvalidConfigOrData):
            return_value_from_path_or_none(data, ["non", "existent"])

        data = {"non": InvalidConfigOrData}
        with pytest.raises(InvalidConfigOrData):
            return_value_from_path_or_none(data, ["non", "existent"])
