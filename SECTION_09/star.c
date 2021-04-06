#include <stdio.h>
#include <python.h>

int add(int a, int b)
{
	printf("add : %d, %d\n", a, b);
	return a + b;
}

PyObject* py_add(PyObject* self, PyObject* args)
{
	PyTupleObject* tp = (PyTupleObject*)args;
	PyLongObject*  p1 = (PyLongObject*)(tp->ob_item[0]);

	int n = p1->ob_digit[0];
	printf("first argument : %d\n", n);

	int x, y;

	if (!PyArg_ParseTuple(args, "ii", &x, &y))
	{
		return NULL;
	}
	int result = add(x, y);

	// C int 로 부터 Python PyLongObject 객체 생성
	PyObject* ret = Py_BuildValue("i", result);
	return ret;
}




// 'star' 라는 모듈에 있는 함수의 정보를 담은 배열
PyMethodDef Methods[] = {
  {"add", py_add, METH_VARARGS, "Integer add"},
  { NULL, NULL, 0, NULL}
};
   
// start 모듈 자체의 정보
struct PyModuleDef star_module = {
  PyModuleDef_HEAD_INIT,
  "star",                   // 모듈 이름
  "star module doc string", // Doc string 
  -1,						// Size of per-interpreter state or -1 */
  Methods				    // 함수 정보를 담은 배열
};  
   
// 모듈 초기화 함수
PyMODINIT_FUNC PyInit_star(void) 
{
	return PyModule_Create(&star_module);
}
