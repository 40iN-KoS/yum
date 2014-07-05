# -*- coding: utf-8 -*-

import copy

from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError as SchemaValidationError


class YumError(Exception):
    pass


class ValidationError(YumError):
    pass


class Dict(object):
    _schema = {}
    _process = {}
    _rename = {}

    __schema = {
        '$schema': 'http://json-schema.org/schema#',
        'type': 'object',
        'patternProperties': {'^[^_]': {}},
        'additionalProperties': False,
        }
    __base_validator = Draft4Validator(__schema)

    def __init__(self, obj):
        self._validate(obj)
        self._object = self._renaming(self._processing(obj))
        self._raw_object = obj

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError
        try:
            return copy.deepcopy(self._object[name])
        except KeyError:
            raise AttributeError

    def __setattr__(self, name, value):
        if name not in ['_object', '_raw_object']:
            raise AttributeError
        else:
            self.__dict__.update({name: value})

    def __len__(self):
        return self._object.__len__()

    def __str__(self):
        return self._object.__str__()

    def __repr__(self):
        return self._object.__repr__()

    def __iter__(self):
        return self._object.__iter__()

    @classmethod
    def _validate(cls, obj):
        try:
            cls.__base_validator.validate(obj)
        except (TypeError, SchemaValidationError):
            raise ValidationError
        validator = Draft4Validator(cls._schema)
        try:
            validator.validate(obj)
        except SchemaValidationError:
            raise ValidationError

    @classmethod
    def _processing(cls, obj):
        result = {}
        for k, v in obj.iteritems():
            result.update({k: cls._process.get(k, lambda v: v)(v)})
        return result

    @classmethod
    def _renaming(cls, obj):
        result = {}
        for k, v in obj.iteritems():
            result.update({cls._rename.get(k, k): v})
        return result
