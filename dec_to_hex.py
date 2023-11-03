def decimal_to_hexadecimal(decimal):
    if decimal < 0:
        return "-" + hex(abs(decimal))[2:]
    else:
        return hex(decimal)[2:]
