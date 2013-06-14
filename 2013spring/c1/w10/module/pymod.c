//@+leo-ver=5-thin
//@+node:kmolII_lite.20130614201704.2963: * @file c1/w10/module/pymod.c
//@@language c
//@+<< include >>
//@+node:kmolII_lite.20130614201704.2964: ** << include >>
#include <Python.h>
//@-<< include >>
//@+others
//@+node:kmolII_lite.20130614201704.2965: ** functions
// 宣告內部運算的 C 函式格式
int sum2(int a, int b);

// 定義內部運算的函式內容
int sum2(int a, int b)
{
    return a+b;
}

// sum 函式的 interface
static PyObject* mod_sum(PyObject *self, PyObject *args)
{
    int a;
    int b;
    int s;
    // ii 表示兩個輸入變數都是整數
    if (!PyArg_ParseTuple(args,"ii",&a,&b))
       return NULL;
    // 這裡的 sum2 則是內部的函式定義, 與外部呼叫模組或函式名稱沒有直接關係
    s = sum2(a,b);
    // i 表示 s 為整數
    return Py_BuildValue("i",s);
}

// 這裡的 sum 是外部模組的呼叫名稱, 而 mod_sum 則是內部的呼叫名稱 (即 interface function)
// Mod_Methods 為函式 (方法) 結構定義
static struct PyMethodDef Mod_Methods[] = {
    {"sum", mod_sum, METH_VARARGS, "Description.."},
    {NULL,NULL,0,NULL}
};

// 配合 Python 3 新增的模組結構定義
static struct PyModuleDef ModMethods = {
   PyModuleDef_HEAD_INIT,
   "SumModule",   /* 模組名稱 */
   "SumModule_doc", /* 模組文件, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   Mod_Methods  // 函式結構名稱
};

// 模組啟始, PyInit_ 後必須使用"名稱".pyd 中的模組名稱, 以便啟動
// 換言之, 若編譯連結後的動態模組名稱為 sum.pyd, 則此地的起始函式名稱必須為 PyInit_sum
PyMODINIT_FUNC 
PyInit_sum(void)
{
    // 建立模組的起始, 輸入為模組結構名稱之 address
    (void) PyModule_Create(&ModMethods);
}
//@-others
//@-leo
