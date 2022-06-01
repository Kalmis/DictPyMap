class DictPyMapError(Exception):
    pass


class InvalidConfigError(DictPyMapError):
    pass


class InvalidConfigOrDataError(DictPyMapError):
    pass
