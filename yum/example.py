from yum import YummyDict


class AmazonSESNotification(YummyDict):
    """docstring for AmazonSESNotification"""
    _schema = {
        'description': 'A published notification message',
        'type': 'object',
        'properties': {
            'Message': {'type': 'string', 'minLength': 1, 'maxLength': 4096},
            'MessageId': {'type': 'string', 'identity': True},
            'Signature': {'type': 'string'},
            'SignatureVersion': {'type': 'string', 'enum': ['1']},
            'Timestamp': {'type': 'string'},
            'TopicArn': {'type': 'string', 'maxLength': 1224},

            'Type': {'type': 'string', 'enum': ['Notification']},

            'Subject': {'type': 'string', 'optional': True},
            'UnsubscribeURL': {'type': 'string'},
            },
        }



#  SubscriptionConfirmation + UnsubscribeConfirmation
{
'description': 'Confirmation message',
'type': 'object',
'properties': {
    'Message': {'type': 'string', 'minLength': 1, 'maxLength': 4096},
    'MessageId': {'type': 'string', 'identity': True},
    'Signature': {'type': 'string'},
    'SignatureVersion': {'type': 'string', 'enum': ['1']},
    'Timestamp': {'type': 'string'},
    'TopicArn': {'type': 'string', 'maxLength': 1224},

    'Type': {'type': 'string', 'enum': [ 'SubscriptionConfirmation', 'UnsubscribeConfirmation' ]},

    'SubscribeURL': {'type': 'string'},
    'Token': {'type': 'string'},
  }
}





{
'description': 'A published notification message',
'type': 'object',
'properties': {
    'Message': {'type': 'string', 'minLength': 1, 'maxLength': 4096},
    'MessageId': {'type': 'string', 'identity': True},
    'Signature': {'type': 'string'},
    'SignatureVersion': {'type': 'string', 'enum': ['1']},
    'Timestamp': {'type': 'string'},
    'TopicArn': {'type': 'string', 'maxLength': 1224},
    'Type': {'type': 'string', 'enum': ['Notification', 'SubscriptionConfirmation', 'UnsubscribeConfirmation']},
    'Subject': {'type': 'string', 'optional': True},
    'UnsubscribeURL': {'type': 'string'},
    'SubscribeURL': {'type': 'string'},
    'Token': {'type': 'string'},
    },
'additionalProperties': False,
'dependencies': {
    'UnsubscribeURL': {
        'type': 'object',
        'properties': {
            'Type': {'type': 'string', 'enum': ['Notification']},
            'Subject': {'type': 'string', 'optional': True},
            'UnsubscribeURL': {'type': 'string'},
            },
        'required': ['Message', 'MessageId', 'Signature', 'SignatureVersion', 'Timestamp', 'TopicArn', 'Type', 'UnsubscribeURL'],
        },
    'SubscribeURL': {},
    },

}
