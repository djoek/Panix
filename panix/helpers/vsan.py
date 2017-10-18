from panix.helpers.cleaners import clean_dict, lod_to_d, remove_key_prefix


def vsan_helper(vsan_nxapi):
    """
    Helper to work with the NXAPI parsed output from 'show version'
    :param vsan_nxapi:
    """

    return {
        k: remove_key_prefix(v, 'vsan_')
        for k, v in lod_to_d(
            clean_dict(vsan_nxapi, 'vsan'),
            'vsan_id'
        ).items()
    }

