#include <Python.h>
#include <float.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *trying_str = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    trying_str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", trying_str);

    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < size + 1 && i < 10; i++)
    {
        printf(" %02hhx", trying_str[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    char *buf = NULL;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    buf = PyOS_double_to_string(PyFloat_AS_DOUBLE(p), 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buf);
    PyMem_Free(buf);
}
