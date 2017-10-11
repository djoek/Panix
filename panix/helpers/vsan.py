from panix.helpers.cleaners import clean_dict, lod_to_d


class VSANHelper:

    def __init__(self, vsan_nxapi):
        """
        Helper to work with the NXAPI parsed output from 'show version'
        :param vsan_nxapi:
        """

        self.vsans = lod_to_d(
            clean_dict(vsan_nxapi, 'vsan'),
            'vsan_id'
        )

    def __getitem__(self, item):
        return self.vsans.__getitem__(item)

    def __setitem__(self, key, value):
        return KeyError('Read Only')

