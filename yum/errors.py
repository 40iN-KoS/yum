# -*- coding: utf-8 -*-

class YumError(Exception):
    pass


class YumValidationError(YumError):
    pass


class YumProcessingError(YumError):
    pass
