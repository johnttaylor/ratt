from rattlib import *
import config

def run():
    output.write_entry(__name__)
    passcode = config.g_passed

    # Load Test action -->should be the test action script from patha/
    passcode = std.load("action_path_check.py").run()

    output.write_exit(__name__)
    return passcode