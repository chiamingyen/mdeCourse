//@+leo-ver=5-thin
//@+node:kmolII_lite.20130614201704.2973: * @file c1/w10/pyfun/pyfun.c
#include "Python.h"
#include <stdio.h>

static PyObject *
pyfun(PyObject *self,PyObject *args)
{
	const char *to_who;
	if(!PyArg_ParseTuple(args,"s",&to_who))
		return NULL;
	 // pyfun 函式會將輸入字串變數傳回
	return PyUnicode_FromString(to_who);
}

// pyd 內有一個函式名稱為  pyfun
static PyMethodDef methods[] = {
	{"pyfun",(PyCFunction)pyfun,METH_VARARGS|METH_KEYWORDS},
	{NULL, NULL}
};

PyDoc_STRVAR(module_doc, "Example Python3 extending.\n");

static struct PyModuleDef moduledef = {
	PyModuleDef_HEAD_INIT,
	"hello",
	module_doc,
	-1,
	methods,
	NULL,
	NULL,
	NULL,
	NULL
};

// 此 pyd 必須命名為 pyfun.pyd, 因為必須與 PyInit_後的名稱相同
PyInit_pyfun(void)
{
	PyObject *m;
	m = PyModule_Create(&moduledef);
	return m;
}
//@-leo
