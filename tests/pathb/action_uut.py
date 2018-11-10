from rattlib import *
import config

def run( timeout ):
    output.write_entry(__name__)
    passcode = config.g_passed

    uut.cli( '.spam 2 200 "Spam message 2";', "$>", timeout )
    uut.cli( '.spam 1 1000 "Spam message 1";', "$>", timeout )
    r = uut.waitfor( timeout, "message 1")
    if ( r == None ):
        output.writeline( "uut.waitfor(): FAILED to find 'message 1'")
        passcode = config.g_failed
    elif ( "spam 1" in r ):
        output.writeline( "uut.waitfor(): MATCHED the WRONG 'message1', from: [{}] ".format( r ) )
        passcode = config.g_failed
    else:    
        output.writeline_verbose( "uut.waitfor(): MATCHED 'message1', from: [{}] ".format( r ) )

    output.write_exit(__name__)
    return passcode
