from panix.helpers.cleaners import clean_dict, lod_to_d


class ZonesetHelper:

    def __init__(self, zoneset_nxapi, vsan='1'):
        """
        Helps you navigate the NXAPI parsed output from 'show zoneset' and 'show zoneset active'
        :param zoneset_nxapi:
        :param vsan:
        """
        self.vsan = str(vsan)

        zonesets = {}

        zs_raw = clean_dict(zoneset_nxapi, 'zoneset')
        for zoneset in zs_raw:
            if zoneset['zoneset_vsan_id'] != self.vsan:
                continue

            zs_key = zoneset['zoneset_name']
            zonesets[zs_key] = {}

            try:
                z_raw = clean_dict(zoneset, 'zone')
            except KeyError:
                # empty zoneset
                continue

            for zone in z_raw:
                z_key = zone['zone_name']
                zonesets[zs_key][z_key] = {}

                m_raw = clean_dict(zone, 'zone_member')
                zonesets[zs_key][z_key]['members'] = [member for member in m_raw]

        self.zonesets = zonesets

    def __getitem__(self, item):
        return self.zonesets.__getitem__(item)

    def __setitem__(self, key, value):
        return KeyError('Read Only')

