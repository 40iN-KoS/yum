# -*- coding: utf-8 -*-

from yum import Processor


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
if user.is_active:
    print user.firstname, user.lastname

print user
print type(user)
print type(user.id)
