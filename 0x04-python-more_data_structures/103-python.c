#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about a Python list object.
 * @p: A PyObject pointer representing a Python list.
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: A PyObject pointer representing a Python bytes object.
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    char *str;
    Py_ssize_t i, max_bytes;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    max_bytes = size + 1 > 10 ? 10 : size + 1;
    printf("  first %zd bytes:", max_bytes);

    for (i = 0; i < max_bytes; i++)
        printf(" %02x", (unsigned char)str[i]);
    
    printf("\n");
}
