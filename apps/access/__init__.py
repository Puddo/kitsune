from authority import get_check


def has_perm_or_owns(user, perm, obj, perm_obj,
                     field_name='creator'):
    """
    Given a user, a permission, an object (obj) and another object to check
    permissions against (perm_obj), returns True if the user has perm on
    obj.
    """
    if user == getattr(obj, field_name):
        return True

    check = get_check(user, perm)
    if not check:
        return user.has_perm(perm)
    return check(perm_obj) or user.has_perm(perm)


def has_perm(user, perm, obj):
    """
    Given a user, a permission, an object (obj), returns True if the user
    has perm on obj.
    """
    check = get_check(user, perm)
    if not check:
        return user.has_perm(perm)
    return check(obj) or user.has_perm(perm)
