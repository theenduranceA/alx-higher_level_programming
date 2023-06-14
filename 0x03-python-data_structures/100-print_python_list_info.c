#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Function that prints python list
<<<<<<< HEAD
 * @p: A pointer to pyobject list
 *
=======
 * @p: Pointer to a pyobject
>>>>>>> refs/remotes/origin/master
 */

void print_python_list_info(PyObject *p)
{
<<<<<<< HEAD
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

=======
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
>>>>>>> refs/remotes/origin/master
	}
}
