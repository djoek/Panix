from datetime import datetime, timedelta


def version_helper(nxapi_parsed_show_version):
    result = dict()

    # Weird date format 1
    result['kernel_uptime'] = timedelta(
        days=nxapi_parsed_show_version.pop('kern_uptm_days'),
        hours=nxapi_parsed_show_version.pop('kern_uptm_hrs'),
        minutes=nxapi_parsed_show_version.pop('kern_uptm_mins'),
        seconds=nxapi_parsed_show_version.pop('kern_uptm_secs'),
    )

    # Weird date format 2
    result['bios_compile_datetime'] = datetime.strptime(
        nxapi_parsed_show_version.pop('bios_cmpl_time'),
        "%m/%d/%Y"
    )

    # Make naming consistent
    for key, value in nxapi_parsed_show_version.items():
        new_key = key

        # clean endings
        new_key = new_key.replace(
            '_str', '').replace(
            '_version', '_ver').replace(
            '_ver', '_version').replace(
            '_cmpl_time', '_compile_datetime').replace(
            '_tmstmp', '_datetime')

        # clean beginnings
        new_key = new_key.replace(
            'kick_', 'kickstart_').replace(
            'sys_', 'system_')

        # clean values
        try:
            value = value.strip()
        except AttributeError:
            # this is an int, not a str
            pass

        if new_key.endswith('_datetime'):
            try:
                value = datetime.strptime(value, "%m/%d/%Y %H:%M:%S")
            except ValueError:
                pass
            except TypeError:
                pass

        result[new_key] = value

    return result
