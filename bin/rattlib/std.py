""" Basic/standard functions 
"""

import utils
import rattlib

g_verbose = False
g_debug   = False
g_fdout   = None

#------------------------------------------------------------------------------
def load_script( script_name ):
    """ Dynamically loads the specifies script and returns the 'module object'
        for the script.
    """
    m,e = utils.importFile( script_name )
    if ( m == None ):
        rattlib.output.writeline( "Error loading script: (). [{}]".format( e ) )
        return None

    return m


