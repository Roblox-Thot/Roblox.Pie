import re
import secrets
import uuid

import requests


# region Cleaner code found on GitHub
def replace_referents(data):
    """Replaces the data in a RBXLX to make Roblox let the file be uploaded"""
    cache = {}

    def _replace_ref(match):
        ref = match.group(1)
        if ref not in cache:
            cache[ref] = ("RBX" + secrets.token_hex(16).upper()).encode()
        return cache[ref]

    data = re.sub(
        b"(RBX[A-Z0-9]{32})",
        _replace_ref,
        data
    )
    return data


def replace_script_guids(data):
    cache = {}

    def _replace_guid(match):
        guid = match.group(1)
        if guid not in cache:
            cache[guid] = ("{" + str(uuid.uuid4()).upper() + "}").encode()
        return cache[guid]

    data = re.sub(
        b"(\{[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}\})",
        _replace_guid,
        data
    )
    return data
# endregion
