#include <Python.h>
#include <floatobject.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject pointer to a Python list
 *
 * Description: This function prints information about a Python list,
 * including its size, allocated space, and the type of each element.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;
	const char *type_name;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		type_name = item->ob_type->tp_name;
		printf("Element %zd: %s\n", i, type_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject pointer to a Python byte object
 *
 * Description: This function prints information about a Python byte object,
 * including its size, string representation, and first 10 bytes.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %d bytes: ", size < 10 ? (int)size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", string[i]);
		if (i < 9 && i < size - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject pointer to a Python float object
 *
 * Description: This function prints the value of a Python float object.
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	printf("[.] float object info\n");
	printf("  value: %.16g\n", value);
}
