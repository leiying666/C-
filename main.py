#include<stdio.h>
int main()
{
	int line = 0;
	printf("加入我们\n");
	while (line < 10)
	{
		printf("敲代码:%d\n", line+1);
		line++;
	}
	if (line >= 10)
		printf("成功\n");
			return 0;
}