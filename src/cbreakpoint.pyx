
cdef extern from *:
    """
    long long last_breakpoint_id = -1;

    void cbreakpoint(long long breakpoint_id){
         last_breakpoint_id = breakpoint_id;
    }
    """
    void c_cbreakpoint "cbreakpoint"(long long breakpoint_id)


def cbreakpoint(breakpoint_id = 0):
    c_cbreakpoint(breakpoint_id)

__version__=(0,1,0)


