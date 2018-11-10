from rattlib import *
import config

def run():
    output.write_entry(__name__)
    passcode = config.g_failed

    output.writeline( "ERROR: {} in pathb/ executated".format( __name__ ))

    output.write_exit(__name__)
    return passcode
