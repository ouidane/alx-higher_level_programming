#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about Python lists.
 * @p: Python object pointer (should be a list).
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;
    printf("[*] Python list info\n[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, item->ob_type->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

/**
 * print_python_bytes - Prints basic information about Python bytes.
 * @p: Python object pointer (should be a bytes object).
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, print_size, i;
    char *string;

    if (!PyBytes_Check(p))
    {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);
    printf("[.] bytes object info\n  size: %zd\n  trying string: %s\n", size, string);

    print_size = size + 1 > 10 ? 10 : size + 1;
    printf("  first %zd bytes:", print_size);
    for (i = 0; i < print_size; i++)
        printf(" %02x", (unsigned char)string[i]);
    printf("\n");
}

/**
 * print_python_float - Prints basic information about Python floats.
 * @p: Python object pointer (should be a float).
 */
void print_python_float(PyObject *p)
{
    double value;

    if (!PyFloat_Check(p))
    {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %g\n", value);
}
