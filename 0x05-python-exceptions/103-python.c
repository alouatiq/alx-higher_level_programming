#include <Python.h>
#include <stdio.h>

/* Print info about a bytes object */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i, limit;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);

    limit = size >= 10 ? 10 : size + 1;
    printf("  first %zd bytes:", limit);
    for (i = 0; i < limit; i++)
        printf(" %02x", (unsigned char)string[i]);
    printf("\n");
}

/* Print info about a float object */
void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("  value: %.15g\n", value);  // Use %.15g for precision
}

/* Print info about a list object */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}
