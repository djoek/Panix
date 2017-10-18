def clean_dict(d: dict, key: str):
    d_raw = d['TABLE_%s' % key]['ROW_%s' % key]
    if not isinstance(d_raw, list):
        d_raw = [d_raw]

    return d_raw


def lod_to_d(lod: list, id_key: str):
    return {
        d.pop(id_key): d for d in lod
    }


def rename_keys(d: dict, transform: callable):
    return {transform(k): v for k, v in d.items()}


def remove_key_prefix(d: dict, prefix: str):
    return rename_keys(d, lambda k: k.partition(prefix)[2] if k.startswith(prefix) else k)


def remove_key_suffix(d: dict, suffix: str):
    return rename_keys(d, lambda k: k.partition(suffix)[0] if k.endswith(suffix) else k)

