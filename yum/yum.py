# -*- coding: utf-8 -*-
import copy

import jsonschema



class YummyDict(object):
    _schema = {}
    __schema = {}
    _processing_mapping = {}
    __base_validator = jsonschema.Draft4Validator(__schema)
    _validator = jsonschema.Draft4Validator(_schema)
    # _defaults_map = {}

    def __init__(self, obj):
        self._validate(obj)
        self._object = self._processing(obj)
        self._raw_object = obj

    def __getattr__(self, name):
        return copy.deepcopy(self._object[name])

    # def __setattr__(self, name, value):
        # raise NotImplementedError

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
        cls.__base_validator.validate(obj)
        cls._validator.validate(obj)

    @classmethod
    def _processing(cls, obj):
        result = {}
        for k, v in obj.iteritems():
            result.update({k: cls._processing_mapping.get(k, lambda v: v)(v)})
        return result


if __name__ == '__main__':
    d = YummyDict({'a': 2})
    print d.a
    print d
    print len(d)
