#include <python.h>

/**
  *print_python_list_info - this function prints basic info about
  *python lists
  *@p: A pyObject list
  */

void print_python_list_info(PyObject *p)
{
	int size, alloc;
	PyObject *obj;
	int j;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);

		obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj)->tp-name);
	}
}
