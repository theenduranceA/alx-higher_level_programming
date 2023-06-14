#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Function that prints python list
 * @p: A pointer to pyobject list
 *
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, x;
	PyObject *object;

	int size = PyList_Size(p);

	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (x = 0; x < size; x++)
	{
		pyitem = PyList_Get_Item(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(object)->tp_name);

	}
}
