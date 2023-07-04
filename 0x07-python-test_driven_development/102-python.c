#include <stdio.h>
#include <string.h>
#include <Python.h>

void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %s\n", PyUnicode_AsUTF8(p));
}
