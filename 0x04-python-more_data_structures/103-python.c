#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: Pointer to a Python object (expected to be a bytes object).
 */
void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *bytes = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", bytes);

    Py_ssize_t limit = size > 10 ? 10 : size;
    printf("  first %zd bytes:", limit + 1);
    for (Py_ssize_t i = 0; i <= limit; i++) {
        printf(" %02x", (unsigned char)bytes[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: Pointer to a Python object (expected to be a list).
 */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}
