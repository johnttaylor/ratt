from rattlib import *
import config

def run():
    output.write_entry(__name__)

    passcode = config.g_passed

    # Send a newline to the UUT and wait for a response form UUT, i.e. is the UUT alive?
    r = uut.cli( "", "$>", 2)
    if ( r != None ):
        # Load and execute the test action
        passcode = std.load("action_uut.py").run(timeout=2)
    else:
        output.writeline("ERROR: The UUT is not responding")
        passcode = config.g_failed

    output.write_exit(__name__)
    return passcode