#include <Python.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: The list object
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *obj;

	if (p == NULL)
		PyErr_Print();
	size = PyList_Size(p);
	allocated = ((PyListObject *)(p))->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
