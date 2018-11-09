""" Basic/standard functions 
"""

import utils
from rattlib import output


#------------------------------------------------------------------------------
def load_script( script_name ):
    """ Dynamically loads the specifies script and returns the 'module object'
        for the script.
    """
    m,e = utils.importFile( script_name )
    if ( m == None ):
        output.writeline( "Error loading script: (). [{}]".format( e ) )
        return None

    return m


