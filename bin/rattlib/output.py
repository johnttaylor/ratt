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

def set_output_fd(out_fd, log_fd):
    global g_fdout
    global g_logout
    g_fdout  = out_fd
    g_logout = log_fd


#------------------------------------------------------------------------------
def get_available_serial_ports(platform="Windows"):
    """ Generates list of available/unused Serial ports.
        Current only support enumerating the COM ports under Windoze
    """

    result = []

    # Find all available COM Ports on a Windoze box
    if (platform == "Windows"):
        ports = ['COM%s' % (i + 1) for i in range(256)]
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
    else:
        result.append("Feature not supported on platform: {}".format(platform))

    return result

#
def string_to_parity_enum(s):
    if (s[:1] == 'e' or s[:1] == 'E'):
        return serial.PARITY_EVEN
    if (s[:1] == 'o' or s[:1] == 'O'):
        return serial.PARITY_ODD

    return serial.PARITY_NONE

#
def int_to_stopbits_enum(numbits):
    if (numbits == 1):
        return serial.STOPBITS_TWO
    
    return serial.STOPBITS_ONE

#
def int_to_databits_enum(numbits):
    if (numbits == 7):
        return serial.SEVENBITS
    if (numbits == 6):
        return serial.SIXBITS

    return serial.EIGHTBITS

#
def open_serial_port(serialPort, baudrate=115200, parity="none", stopbits=1, bytesize=8, timeout=None, platform="Windows"):
    # Open a Windows COM Port
    if (platform == "Windows"):
        try:
            serialConnection = serial.Serial(port=serialPort, baudrate=baudrate, parity=string_to_parity_enum(parity), stopbits=int_to_stopbits_enum(stopbits), bytesize=int_to_databits_enum(bytesize), timeout=timeout)
        except Exception as e:
            sys.exit("Failed to open serial port ({}). Error={}".format(serialPort, str(e)))

        return serialConnection

    else:
        return None


#------------------------------------------------------------------------------
def importCode(code, name):
    """ code can be any object containing code -- string, file object, or
        compiled code object. Returns a new module object initialized
        by dynamically importing the given code.  If the module has already
        been imported - then it is returned and not imported a second time.
    """
    global g_utils_import_dictionary
   
    # Check if 'code' has already been loaded
    if (name in g_utils_import_dictionary):
        return g_utils_import_dictionary[name]

    # Load the 'code' into the memory
    try:
        module = imp.new_module(name)
        g_utils_import_dictionary[name] = module
        exec code in module.__dict__
        return module

    except Exception as e:
        print "Error={}".format(str(e))
        return None

#
def importFile(filename, search_paths=None):
    """ Wrapper function to dynamically load/import the specified python
        script file.  The file name - sans the .py file extension - is used
        for the module name.

        'filename' should be without a absolute path.  The contents of 'search_paths'
        is prepended to 'filename' when trying to find/open the specified file.
        The search order is the order of the 'search_paths', i.e. index 0 is
        searched first, etc.  If 'search_parts' is None, then only the CWD
        is searched.

        Returns a tuple: [module|None, fullpath|errorMsg]
    """

    # Housekeeping
    fd = None
    fullpath = filename
    modname = os.path.splitext(os.path.split(filename)[1])[0]

    # Check for already loaded
    if (modname in g_utils_import_dictionary):
        return g_utils_import_dictionary[modname],fullpath

    # No search paths...
    if (search_paths == None):
        try:
            fd = open(fullpath, "rt")
        except Exception as e:
            return None, "ERROR. Unable to open the file {}.  Error={}".format(fullpath,str(e))

    # Search the search paths
    else:
        num_paths = len(search_paths)
        for p in search_paths:
            num_paths -= 1
            fullpath = os.path.join(p,filename)
            try:
                fd = open(fullpath, "rt")
                break
            except Exception as e:
                if (num_paths == 0):
                    return None, "ERROR. Unable to open the file {}.  Error={}".format(fname,str(e))

    # Load the script/module
    m = importCode(fd, modname)
    fd.close()
    return m,fullpath


