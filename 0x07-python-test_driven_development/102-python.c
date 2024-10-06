#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

/**
 * print_python_string - Prints information about Python string objects
 * @p: The Python object to check
 */
void print_python_string(PyObject *p)
{
    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_SIZE(p);
    const char *type = (PyUnicode_IS_COMPACT_ASCII(p)) ? "compact ascii" : "compact unicode object";
    const char *value = PyUnicode_AsUTF8(p);

    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %s\n", value);
}
