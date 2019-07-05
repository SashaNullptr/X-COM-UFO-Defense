from configparser import ConfigParser
from x_com import DB_CONFIG


def config( filename=None, section='postgresql' ):

    filename = filename if filename is not None else DB_CONFIG

    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise FileNotFoundError('Section {0} not found in the {1} file'.format(section, filename))

    return db
