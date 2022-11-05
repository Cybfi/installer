import os


def envBYN(key: str, val=None):
    if val is None:
        val = os.getenv(key)
    elif type(val) is not str:
        val = str(val)
    # envBYN (Binary Yes No) is a helper function to convert a string to a boolean
    yesvals = ['true', 'yes', 'y', '1']
    novals = ['false', 'no', 'n', '0']
    if val.lower() in yesvals:
        return True
    elif val.lower() in novals:
        return False
    else:
        return None