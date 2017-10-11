def clean_dict(d, key):
    d_raw = d['TABLE_%s' % key]['ROW_%s' % key]
    if not isinstance(d_raw, list):
        d_raw = [d_raw]

    return d_raw


def lod_to_d(lod, id_key):
    return {
        d.pop(id_key): d for d in lod
    }
