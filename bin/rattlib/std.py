""" Basic/standard functions 
"""

import config
import utils
from rattlib import output


#------------------------------------------------------------------------------
def load( script_name ):
    """ Dynamically loads the specifies script and returns the 'module object'
        for the script.
    """
    m,e = utils.importFile( script_name, config.g_script_paths )
    if ( m == None ):
        output.writeline( "Error loading script: (). [{}]".format( e ) )
        return None

    return m


#
def shell( cmd ):
    """ Executes the specified command.  The method returns a tuple with the 
        exit code and output from the command.
    """    
    exitcode, result = utils.run_shell( cmd )
    output.writeline_verbose( result )
    return exitcode, result