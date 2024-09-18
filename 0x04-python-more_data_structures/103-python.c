#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic information about Python bytes objects.
 * @p: PyObject pointer (should be a PyBytesObject).
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < (size < 10 ? size + 1 : 10); i++)
        printf(" %02x", (unsigned char)string[i]);
    printf("\n");
}

/**
 * print_python_list - Prints basic information about Python list objects.
 * @p: PyObject pointer (should be a PyListObject).
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    Py_ssize_t allocated;
    PyObject *item;
    PyListObject *list;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = list->ob_item[i];
        printf("Element %zd: %s\n", i, item->ob_type->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
