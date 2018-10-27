# -*- encoding:utf-8 -*-


def existeuser(uid, pending):
    if str(uid) in pending.keys():
        return True
    return False
