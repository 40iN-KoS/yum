# -*- coding: utf-8 -*-

from main import Processor


bad_api_response = {
    'UserId': '42',  # string instead int
    'UserIsActive': 1,  # 1/0 instead True/False
    'UserFirstname': 'Marcus',  # annoying naming conventions
    'UserLastname': 'Aurelius',  # useless prefixes everywhere
}


class User(Processor):
    schema = {
        '$schema': 'http://json-schema.org/schema#',
        'type': 'object',
        'required': ['UserId', 'UserIsActive', 'UserFirstname', 'UserLastname'],
    }
    process = {
        'UserId': int,
        'UserIsActive': bool,
    }
    rename = {
        'UserId': 'id',
        'UserIsActive': 'is_active',
        'UserFirstname': 'firstname',
        'UserLastname': 'lastname',
    }



user = User(bad_api_response)
print user
print user._object
print dir(user)
print user.firstname
print type(user.id)
print hasattr(user, 'lastname')
