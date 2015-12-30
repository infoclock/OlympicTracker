# encoding: utf-8
import mimetypes
import re
from django.core.urlresolvers import reverse


def order_name(name, problem_name):
    """order_name -- Limit a text to 20 chars length, if necessary strips the
    middle of the text and substitute it for an ellipsis.

    name -- text to be limited.

    """
    name = re.sub(r'^.*/', '', name)
    if len(name) <= 20:
        return name
    return name[:10] + "..." + name[-7:]

def serialize(instance, file_attr='file'):
    """serialize -- Serialize a submission instance into a dict.

    instance -- Submission instance
    file_attr -- attribute name that contains the FileField

    """
    obj = getattr(instance, file_attr)
    problem_obj = getattr(instance, 'problem')
    return {
        'url': obj.url,
        'name': order_name(obj.name, problem_obj.name),
        'type': mimetypes.guess_type(obj.path)[0] or 'other',
        'size': obj.size,
        'problem_name': problem_obj.name,
    }


