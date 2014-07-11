# -*- coding: utf-8 -*-

from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError as SchemaValidationError

__version__ = '0.1'


class YumError(Exception):
    pass


class ValidationError(YumError):
    pass


class Processor(object):
    schema = {}
    process = {}
    rename = {}

    def __new__(self, obj):
        filtered_obj = self.filter(obj)
        return Dict(filtered_obj)

    @classmethod
    def filter(cls, obj):
        cls.validate(obj)
        return cls.renaming(cls.processing(obj))

    @classmethod
    def validate(cls, obj):
        validator = Draft4Validator(cls.schema)
        try:
            validator.validate(obj)
        except SchemaValidationError:
            raise ValidationError

    @classmethod
    def processing(cls, obj):
        result = {}
        for k, v in obj.iteritems():
            result.update({k: cls.process.get(k, lambda v: v)(v)})
        return result

    @classmethod
    def renaming(cls, obj):
        result = {}
        for k, v in obj.iteritems():
            result.update({cls.rename.get(k, k): v})
        return result


class Dict(object):
    __base_validator = Draft4Validator({
        '$schema': 'http://json-schema.org/schema#',
        'type': 'object',
        'patternProperties': {'^[^_]': {}},
        'additionalProperties': False,
        }
    )
    def __init__(self, obj):
        try:
            self.__base_validator.validate(obj)
        except (TypeError, SchemaValidationError):
            raise ValidationError
        self._object = obj

    def __getattr__(self, name):
        try:
            return self._object[name]
        except KeyError:
            raise AttributeError

    def __len__(self):
        return self._object.__len__()

    def __str__(self):
        return self._object.__str__()

    def __repr__(self):
        return self._object.__repr__()

    def __iter__(self):
        return self._object.__iter__()
