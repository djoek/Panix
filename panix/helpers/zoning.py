from panix.helpers.cleaners import clean_dict


def zone_helper(zoneset_nxapi, vsan='1'):
    """
    Helps you navigate the NXAPI parsed output from 'show zoneset' and 'show zoneset active'
    :param zoneset_nxapi: data structure returned from NXAPI
    :param vsan: which VSAN to return, default is 1
    """
    zonesets = dict()

    zs_raw = clean_dict(zoneset_nxapi, 'zoneset')
    for zoneset in zs_raw:
        if zoneset['zoneset_vsan_id'] != vsan:
            continue

        zs_key = zoneset['zoneset_name']
        zonesets[zs_key] = dict()

        try:
            z_raw = clean_dict(zoneset, 'zone')
        except KeyError:
            continue  # empty zoneset

        for zone in z_raw:
            z_key = zone['zone_name']
            zonesets[zs_key][z_key] = {}

            m_raw = clean_dict(zone, 'zone_member')
            zonesets[zs_key][z_key]['members'] = [member for member in m_raw]

    return zonesets


