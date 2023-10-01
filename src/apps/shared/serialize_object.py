def serialize_object(object):
    if not object:
        return []
    serialized = [dict(item) for item in object]
    return serialized
