#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Function that prints python list
 * @p: Pointer to a pyobject
 */

void print_python_list_info(PyObject *p)
{
	int x;
	int size = Py_SIZE(p);
	PyListObject *obj = (PyListObject *) p;
	PyObject *object;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int) obj->allocated);
	for (x = 0; x < size; x++)
	{
		object = PyList_GET_ITEM(p, x);
		printf("Element %d: %s\n", x, Py_TYPE(object)->tp_name);
	}
}
