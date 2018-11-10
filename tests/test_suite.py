from rattlib import *
import config

def main():
    output.write_entry( __name__ )
    passcode = config.g_passed

    # Test rattlib.uut
    if ( passcode == config.g_passed ):
         passcode = std.load("tc_uut.py").run()

    # Test rattlib.std
    #if ( passcode == config.g_passed ):
    #     passcode = std.load("tc_std.py").run()

    # Test ratt search paths
    if ( passcode == config.g_passed ):
         passcode = std.load("tc_paths.py").run()
    
    output.write_exit( __name__ )
    return passcode