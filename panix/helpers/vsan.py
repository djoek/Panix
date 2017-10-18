from panix.helpers.cleaners import clean_dict, lod_to_d


def vsan_helper(vsan_nxapi):
    """
    Helper to work with the NXAPI parsed output from 'show version'
    :param vsan_nxapi:
    """

    return lod_to_d(
        clean_dict(vsan_nxapi, 'vsan'),
        'vsan_id'
    )

