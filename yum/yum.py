# -*- coding: utf-8 -*-
import copy

from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError

from errors import ValidationError as YumValidationError


class YummyDict(object):
    _schema = {}  # TODO: schema validation
    __schema = {
        '$schema': 'http://json-schema.org/schema#',
        'type': 'object',
        'patternProperties': {'^[^_]': {}},
        'additionalProperties': False,
        }
    _processing_mapping = {}
    __base_validator = Draft4Validator(__schema)

    def __init__(self, obj):
        self._validate(obj)
        self._object = self._process(obj)
        self._raw_object = obj

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError
        return copy.deepcopy(self._object[name])

    def __setattr__(self, name, value):
        if name not in ['_object', '_raw_object']:
            raise AttributeError
        else:
            self.__dict__.update({name: value})

    def __len__(self):
        return len(self._object)

    def __str__(self):
        return str(self._object)

    def __repr__(self):
        return repr(self._object)

    def __iter__(self):
        raise NotImplementedError

    @classmethod
    def _validate(cls, obj):
        try:
            cls.__base_validator.validate(obj)
        except (TypeError, ValidationError):
            raise YumValidationError
        validator = Draft4Validator(cls._schema)
        validator.validate(obj)

    @classmethod
    def _process(cls, obj):
        result = {}
        for k, v in obj.iteritems():
            result.update({k: cls._processing_mapping.get(k, lambda v: v)(v)})
        return result
