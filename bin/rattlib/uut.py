""" Functions to Access the UUT
"""

from rattlib import output
import time
import config

#------------------------------------------------------------------------------
#
def cli( cli_command ):
    """ Sends the specified cli_command/content to the UUT.  This call does not 
        block/wait for a response.
    """
    config.g_uut.sendline( cli_command )
    config.g_uut.flush()


#
def clear_buffer():
    """ This method clears and returnsthe pexpect buffer.  The less content
        in the pexpect buffer, the faster the 'wait_for' performance.  
    """
  
    # delay slightly so that any previous action has had chance to effect the UUT
    time.sleep( 0.35 )

    # Flush the UUT buffer
    max_retries = 1024
    flushed_stuff = ''
    while( max_retries ):
        d = config.g_uut.read_nonblocking(size=512)
        max_retries -= 1
        if ( d != None and d != ''):
            flushed_stuff += d
        else:
            output.writeline_verbose( flushed_stuff )
            return flushed_stuff

    # Make sure we return the 'flushed stuff' if the pexpect buffer is
    # constantly being filled up
    output.writeline_verbose( flushed_stuff )
    return flushed_stuff


#
def wait_for( timeout, needle, regex_match=False, output_buffer=True  ):
    """ Waits for the UUT to respond with 'needle'.  When 'regex' is true, then
        'needle' is assumed to be regular expression match; else a simple string
        match is used. The 'timeout' is the maximum time in seconds to wait for the
        matching response from the UUT.  If 'needle' was found, then the contents
        of the pexpect buffer (up to and including 'needle') is returned; else
        if 'needle' is not found then None is returned
    """
    
    # Housekeeping
    idx    = -1
    result = ""

    # String match
    if ( regex_match == False ):
        output.writeline( "Waiting up to {} seconds for the string: [{}]".format( timeout, needle ) )
        idx = config.g_uut.expect_str( [needle, pexpect.EOF, pexpect.TIMEOUT], timeout )

    # Regex Match
    elif ( tokens[1] == 'REGEX' ):
        output.writeline( "Waiting up to {} seconds for the regex: [{}]".format( timeout, needle ) )
        idx = config.g_uut.expect( [needle, pexpect.EOF, pexpect.TIMEOUT], timeout )

    result = str(config.g_uut.get_before())+str(config.g_uut.get_after()) 
    output.writeline_verbose( result )
    return result if idx == 0 else None
