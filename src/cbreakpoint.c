//
// if you change first 15 lines, make sure to change 
// cbreakpoint_condition_line
//

#define PY_SSIZE_T_CLEAN
#include <Python.h>

long long last_breakpoint_id = -1;

void cbreakpoint(long long breakpoint_id){
     last_breakpoint_id = breakpoint_id;   //<---------- this is cbreakpoint line
}

static PyObject *
cbreakpoint_cbreakpoint(PyObject *self, PyObject *args, PyObject *keywds)
{
    long long id=-1;
    static char *kwlist[] = {"breakpoint_id", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, keywds, "|L", kwlist,
                                     &id))
        return NULL;


    cbreakpoint(id);
    return PyLong_FromLongLong(last_breakpoint_id);
}

static PyObject *
cbreakpoint_condition_line(PyObject *self, PyObject *args)
{
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    return PyLong_FromLongLong(12);
}

static PyMethodDef CbreakpointMethods[] = {
    {"cbreakpoint", (PyCFunction)cbreakpoint_cbreakpoint, METH_VARARGS | METH_KEYWORDS,
     "sets a c-breakpoint with given id."},
    {"condition_line",  cbreakpoint_condition_line, METH_VARARGS,
     "return line number which can be used in gbd for conditional breakpoints, i.e. 'break src/cbreakpoint.c:<condition line> if breakpoint_id == 2'"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef cbreakpointmodule = {
    PyModuleDef_HEAD_INIT,
    "cbreakpoint",   /* name of module */
    NULL,            /* module documentation, may be NULL */
    -1,              /* size of per-interpreter state of the module,
                        or -1 if the module keeps state in global variables. */
    CbreakpointMethods
};

PyMODINIT_FUNC
PyInit_cbreakpoint(void)
{
    return PyModule_Create(&cbreakpointmodule);
}




