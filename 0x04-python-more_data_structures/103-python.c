#include <Python.h>

/**
 * print_python_list - Prints basic information about a Python list object.
 * @p: A PyObject pointer representing a Python list.
 *
 * Return: nothing
 */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = ((PyListObject *)p)->ob_item[i];
        const char *type = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);

        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: A PyObject pointer representing a Python bytes object.
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    char *str = ((PyBytesObject *)p)->ob_sval;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02x ", (unsigned char)str[i]);
    }
    if (size < 10) {
        printf("00");
    }
    printf("\n");
}
