""" Provides an 'pexpect' object based on platform/connection type
"""
#------------------------------------------------------------------------------
class ExpectWindowsConsole(object):
    def __init__( self, exename, logfile =None ):
        self._exename    = exename
        self._logfile    = logfile
        self._child      = pexpect.popen_spawn.PopenSpawn(exename,logfile=logfile,maxread=1)

    def is_detached_uut(self):
        return False;

    def respawn( self ):
        self._child = pexpect.popen_spawn.PopenSpawn(self._exename,logfile=self._logfile,maxread=1)

    def sendline( self, s ):
        self._child.sendline(s)

    def flush( self ):
        self._child.flush()

    def read_nonblocking( self, size=1, timeout=None ):
        return self._child.read_nonblocking( size, timeout )


    def expect( self, regex_list, timeout=-1, searchwindowsize=-1 ):
        return self._child.expect( regex_list, timeout=timeout, searchwindowsize=searchwindowsize )

    def expect_str( self, string_list, timeout=-1, searchwindowsize=-1 ):
        return self._child.expect_exact( string_list, timeout=timeout, searchwindowsize=searchwindowsize )

    def get_before( self ):
        return self._child.before

    def get_after( self ):
        return self._child.after

    def close( self ):
        try:
            self._child.kill(signal.SIGTERM)     
        except:
            pass

#------------------------------------------------------------------------------
class ExpectLinuxConsole(object):
    def __init__( self, exename, logfile=None ):
       self._exename     = exename
       self._logfile     = logfile
       self._child = pexpect.spawn(exename,logfile=logfile,maxread=1)

    def respawn( self ):
        self._child = pexpect.popen_spawn.PopenSpawn(self._exename,logfile=self._logfile,maxread=1)

    def is_detached_uut(self):
        return False;

    def sendline( self, s ):
        self._child.sendline(s)

    def flush( self ):
        self._child.flush()

    def read_nonblocking( self, size=1, timeout=None ):
        return self._child.read_nonblocking( size, timeout )

    def expect( self, regex_list, timeout=-1, searchwindowsize=-1 ):
        return self._child.expect( regex_list, timeout=timeout, searchwindowsize=searchwindowsize )

    def expect_str( self, string_list, timeout=-1, searchwindowsize=-1 ):
        return self._child.expect_exact( string_list, timeout=timeout, searchwindowsize=searchwindowsize )

    def get_before( self ):
        return self._child.before

    def get_after( self ):
        return self._child.after

    def close( self ):
        try:
            self._child.kill(signal.SIGTERM)     
        except:
            pass

#------------------------------------------------------------------------------
class ExpectSerial(object):
    def __init__( self, serial, logfile=None ):
        self._logfile     = logfile
        self._serial      = serial
        self._child       = SerialSpawn(serial,logfile=logfile,maxread=1)

    def respawn( self ):
        self._child = SerialSpawn(self._serial,logfile=self._logfile,maxread=1)

    def is_detached_uut(self):
        return True;

    def sendline( self, s ):
        self._child.sendline(s)

    def flush( self ):
        self._child.flush()

    def read_nonblocking( self, size=1, timeout=None ):
        return self._child.read_nonblocking( size, timeout )

    def expect( self, regex_list, timeout=-1, searchwindowsize=-1 ):
        return self._child.expect( regex_list, timeout=timeout, searchwindowsize=searchwindowsize )

    def expect_str( self, string_list, timeout=-1, searchwindowsize=-1 ):
        return self._child.expect_exact( string_list, timeout=timeout, searchwindowsize=searchwindowsize )

    def get_before( self ):
        return self._child.before

    def get_after( self ):
        return self._child.after

    def close( self ):
        self._child.close()

#------------------------------------------------------------------------------
class ExpectNullConsole(object):
    def __init__( self, logfile=None ):
        self.logfile  = logfile

    def is_detached_uut(self):
        return False;

    def sendline( self, s ):
        pass

    def flush( self ):
        pass


    def read_nonblocking( self, size=1, timeout=None ):
        return pexpect.TIMEOUT

    # Return the last index -->assumption is that the last item in the list is EOF or TIMEOUT
    def expect( self, regex_list, timeout=-1, searchwindowsize=-1 ):
        return len(regex_list)  -1

    # Return the last index -->assumption is that the last item in the list is EOF or TIMEOUT
    def expect_str( self, string_list, timeout=-1, searchwindowsize=-1 ):
        return len(regex_list)  -1
        return self._child.expect_exact( string_list, timeout=timeout, searchwindowsize=searchwindowsize )

    def get_before( self ):
        return none 

    def get_after( self ):
        return none

    def close( self ):
        pass

