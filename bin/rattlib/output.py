""" Utility functions for output messages/information that get sent to 
    stdout as well as the log file
"""

g_verbose = False
g_debug   = False
g_fdout   = None
g_logout  = None

#------------------------------------------------------------------------------
def write(string, log_only=False):
    """ Write/appends 'string' to the output stream
    """
    if ( g_fdout != None and log_only == False ):
        g_fdout.write(string)
    if ( g_logout != None ):
        g_logout.write(string)

#
def writeline(string, log_only=False):
    """ Write/appends 'string' to the output stream AND adds a trailine
        newline
    """
    if ( g_fdout != None and log_only == False):
        g_fdout.write(string + "\n")
    if ( g_logout != None ):
        g_logout.write(string + "\n")

def write_verbose(string, log_only=False):
    """ Same as write(), except the output is only 'enabled' when verbose
        output has been enabled.
    """
    if ( g_verbose ):
        write(string,log_only)

#
def writeline_verbose(string, log_only=False):
    """ Same as writeline(), except the output is only 'enabled' when verbose
        output has been enabled.
    """
    if ( g_verbose ):
        writeline(string,log_only)

#
def write_debug(string, log_only=False):
    """ Same as write(), except the output is only 'enabled' when debug
        output has been enabled.
    """
    if ( g_debug ):
        write(string,log_only)

#
def writeline_debug(string, log_only=False):
    """ Same as writeline(), except the output is only 'enabled' when debug
        output has been enabled.
    """
    if ( g_debug ):
        writeline(string,log_only)

#
def set_verbose_mode( enabled ):
    global g_verbose
    g_verbose = enabled

#
def set_debug_mode ( enabled):
    global g_debug
    g_debug = enabled

#
def set_output_fd(out_fd, log_fd):
    global g_fdout
    global g_logout
    g_fdout  = out_fd
    g_logout = log_fd


