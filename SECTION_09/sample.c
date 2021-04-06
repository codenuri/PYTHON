// gcc -shared -fPIC -o libsample.so sample.c
// cl sample.c /LD

#ifdef _MSC_VER
#define EXPORT __declspec(dllexport)
#else
#define EXPORT 
#endif

#include <stdio.h>

EXPORT int add(int a, int b)
{
    printf("called add\n");
    return a + b;
}

// 인자로 out parameter 를 사용합니다
EXPORT void sub(double a, double b, double* ret)
{
    printf("called sub\n");
	*ret = a - b;
}

// 인자로 배열을 사용합니다.
EXPORT int sum(int* arr, int sz)
{
    printf("called sum\n");
	int s = 0;
	for (int i = 0; i < sz; i++)
		s += i;
	return s;
}

typedef struct _Rect
{
	int x;
	int y;
	int w;
	int h;
} Rect;

// 인자로 구조체를 사용합니다.
EXPORT int getarea(Rect* r)
{
    printf("called getarea\n");
	return (r->w * r->h);
}
