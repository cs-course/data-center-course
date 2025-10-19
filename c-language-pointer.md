---
marp: true
theme: gaia
title: 软件技术基础
# size: 4:3
math: katex
paginate: true
---

<!-- _class: lead -->

# 软件技术基础

## 指针

**施展**
武汉光电国家研究中心 & 计算机学院
华中科技大学

---

<!-- _class: lead -->

# 8.1 指针的概念

---

## 变量与地址

- 变量占有一定数目（根据类型）的连续存储单元
- 变量的连续存储单元首地址称为变量的地址

```c
short x;
char a[5];
&x, a <= => &a[0]
```

---

## 思考

用什么类型的变量来保存地址数据？

| 地址 | 变量名 |
|------|--------|
| x    | a[0]   |
| a[0] | a[1]   |
| a[1] | a[2]   |
| a[2] | a[3]   |
| a[3] | a[4]   |

---

## 指针定义

- **指针**: 变量的地址
  - `&x`: 指针常量
  - `p`: 指针变量

- **指针变量**: 存放地址数据的变量
  - 指针变量也是一种变量，也要占用一定的内存单元
  - 特殊之处在于它存放的是另一个变量所占存储单元的起始地址

---

## 指针变量的声明

```c
数据类型 *标识符;  // 所指变量的数据类型
```

```c
short x = 1, y = 2, a[10], *p;
p = &x;     // √
p = a;      // √
p = a[0];   // ×
```

---

## 为什么使用指针？

**直接访问**: 通过变量名存取变量
```c
x = 0x1234;
printf("%x", x);
```

**间接访问**: 通过变量的地址存取变量
```c
p = &x;
printf("%x", *p);
```

---

## 指针运算符 *

```c
short x = 1, y = 2, *p;
p = &x;        // 指针p指向x
y = *p;        // *p<==>x
*p += 10;
printf("x=%hd,y=%hd", x, y);  // 输出：x=11,y=1
```

---

## 思考：为什么指针有类型？

```c
int x, *p;     // p是一个整型指针变量，其值不确定
x = 25;
*p = x;        // 使用悬挂指针，错！
scanf("%d", p); // 使用悬挂指针，错！
```

**悬挂指针（野指针）**: 指针的声明只是创建了指针变量，但并没有指向具体的变量，此时指针的值是不确定的随机值。

---

## 指针的移动操作 (+, -, ++, --, +=, -=)

指针的移动：指针在原有位置的基础上，通过加一个整数实现指针的前移（地址增大的方向）或者通过减一个整数实现指针的后移。

`p ± k` - 指针p前移/后移k个元素

---

## 指针移动示例

```c
int x[5] = {1, 3, 5, 7, 9}, *px = &x[1];
```

| 表达式 | 值 |
|--------|----|
| `++*px` | 4 |
| `*++px` | 5 |
| `*(--px)` | 1 |
| `*(px--)` | 3 |
| `*px++` | 3 |
| `px += 2, *px` | 7 |

---

## 指针的移动和类型有关

```c
int x = 0x1234ABCD, a, b, *p1;
char *p2;
p1 = &x; p2 = (char *)&x;
a = *p1; b = *p2;
printf("%x,%x", a, b);  // 1234ABCD,CD
b = *(p2 + 1);
printf("%x", b);        // AB
```

---

## 指针的赋值运算

```c
// (1) 同类型的指针可以直接赋值
int a[3] = {1, 2, 3}, x, *p, *q;
p = a; q = &x;

// (2) 不同类型的指针必须使用类型强制转换
long x;
char *p;
p = (char *)&x;
```

---

## 指针的应用

例：一个长整型数占4个字节，从低字节开始依次取出每个字节的高4位和低4位并以十六进制字符形式显示。

```c
#include <stdio.h>
int main(void) {
    long x = 0x1234ABCD, k;
    char *p = (char *)&x;
    char up_half, low_half;
    
    for(k = 0; k < 4; k++) {
        low_half = (*p) & 0x0f;        // 取低4位
        if(low_half < 10) low_half += '0';
        else low_half = (low_half - 10) + 'A';
        
        up_half = (*p >> 4) & 0x0f;    // 取高4位
        if(up_half < 10) up_half |= '0';
        else up_half = (up_half - 10) + 'A';
        
        printf("%c %c\n", up_half, low_half);
        p++;  // 指向下一个字节
    }
    return 0;
}
```

---

## 指针练习一

1. **检测机器的大小端模式**
   ```c
   int checkEndion(void);  // 返回1小端，0大端
   ```

2. **定义宏提取16位数据的高八位和低八位**
   ```c
   #define BYTE0(hdata) ________
   #define BYTE1(hdata) ________
   ```

3. **将int数的最高字节和最低字节交换**

4. **将32位整数IP转为点分十进制输出**

5. **32位本机字节序与网络字节序之间的转换**
   ```c
   unsigned long hton(unsigned long h);  // hton(0x1234)值为0x34120000
   ```

---

<!-- _class: lead -->

# 8.2 指针参数

---

## 传值调用

形参的修改无法影响实参变量的值。

```c
#include <stdio.h>
void swap(int x, int y) {
    int t;
    t = x; x = y; y = t;
}
int main(void) {
    int a = 3, b = 5;
    swap(a, b);
    printf("a=%d,b=%d\n", a, b);  // a=3,b=5
    return 0;
}
```

---

## 传址调用

以指针作为函数的参数实现变量值的交换。

```c
#include <stdio.h>
void swap(int *px, int *py) {
    int t;
    t = *px; *px = *py; *py = t;
}
int main(void) {
    int a = 10, b = 20, c = 30;
    swap(&a, &b);
    swap(&b, &c);
    printf("a=%d,b=%d,c=%d\n", a, b, c);  // a=10,b=30,c=20
    return 0;
}
```

---

## 指针作函数参数

- 改变主调函数中变量的值
- 使函数送回多个值

```c
// implicit returned values:
void sum(int x, int y, int *p) {
    *p = x + y;
}

// the caller
int sum;
sum(3, 4, &sum);
```

---

<!-- _class: lead -->

# 8.3 指针和一维数组

---

## 数组元素的表示

数组元素既可以用下标表示，也可以用指针表示。

```c
int a[10], *p = a;
```

| 表示方法 | 元素值 | 地址 |
|----------|--------|------|
| 下标法 | `a[i]` | `&a[i]` |
| 指针法（数组名） | `*(a+i)` | `a+i` |
| 指针法（指针变量） | `*(p+i)` | `p+i` |

---

## 数组元素的输入

```c
#define N 10
int a[N], *p, i;
p = a;
```

**方法1:**
```c
for(i = 0; i < N; i++)
    scanf("%d", &a[i]);  // 或 a+i, p+i
```

**方法2:**
```c
for(; p < a + N; p++)
    scanf("%d", p);      // 或 p++
```

---

## 数组元素的输出

```c
int a[10], *p, i;
p = a;
```

**方法1:**
```c
for(i = 0; i < 10; i++)
    printf("%d", a[i]);  // 或 *(a+i), *(p+i), *p++
```

**方法2:**
```c
for(; p < a + 10; p++)
    printf("%d", *p);
```

---

## 数组元素的输入和输出

```c
int a[10], *p, i;
for(p = a, i = 0; i < 10; i++)
    scanf("%d", p++);
while(p < a + 10)        // 错误！p已指向数组末尾
    printf("%d", *p++);
```

**正确做法：**
```c
// 逆序输出数组a的全部元素
int a[10], *p = a;
while(p < a + 10)
    scanf("%d", p++);
while(p > a)
    printf("%d", *--p);
```

---

## 指针的关系运算

`<`, `<=`, `>`, `>=`, `==`, `!=`

- 只限于同类型指针
- 不同类型指针之间的关系运算被视为非法操作

```c
int strlen(char s[]) {  // 等价于 int strlen(char *s)
    char *q = s;
    while(*s) s++;
    return (s - q);
}
```

---

## 常量指针

指向常量的指针

```c
int a = 5, b = 6;
const int *p;      // p是常量指针，可以不初始化
p = &a;            // 合法，可以修改指针本身的值
*p = 10;           // 非法，不能通过p修改所指变量a的值
a = 8;             // 合法，因为a不是常量
```

---

## 指针常量

类型是指针的常量

```c
int a = 5, b = 6;
int *const p = &a;  // p是指针常量，必须初始化
*p = 10;            // 合法，可以使用p修改所指对象的值
p = &b;             // 非法，它不能再指向别的变量

int x[10];          // x是指针常量
```

---

## 指向常量的指针常量

```c
int a = 5, b = 6;
const int *const p = &a;  // p是指向常量的指针常量，必须初始化
*p = 10;                  // 非法，不能通过p修改所指变量a的值
p = &b;                   // 非法，指针本身的值也不能修改
```

---

## 一维数组参数的指针表示

```c
// 形参：不指定长度的数组 指针
// 实参：数组名（指针常量） 指向数组元素的指针变量

void sort(int a[], int n) { ... }  // 等价于 void sort(int *a, int n)
```

---

## 冒泡排序示例

```c
#include<stdio.h>
#define N 10

void BubbleSort(int *a, int n) {  // 形参为指针
    int i, j, t;
    for(i = 1; i < n; i++)        // 共进行n-1轮"冒泡"
        for(j = 0; j < n - i; j++) // 对两两相邻的元素进行比较
            if(a[j] > a[j + 1]) {
                t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
            }
}

int main() {
    int x[N], i;
    printf("please input %d numbers:\n", N);
    for(i = 0; i < N; i++) scanf("%d", &x[i]);
    BubbleSort(x, N);  // 实参为数组名
    printf("the sorted numbers:\n");
    for(i = 0; i < N; i++) printf("%d ", x[i]);
    return 0;
}
```

---

<!-- _class: lead -->

# 高精度计算 - 超大整数的加法

---

## 高精度运算概念

高精度运算：是指参与运算的数范围大大超出了标准数据类型能表示的范围的运算。

例如：求两个100位的数的和，计算100!。

---

## 高精度计算解决的问题

1. **大数据存储**
2. **运算过程**
3. **大数据的输入和输出**

**存储**：用数组存储，每个数组元素存储1位
- 个位在`x[0]`，十位在`x[1]`，...
- 优点：每一位都是数的形式，可以直接加减

---

## 函数getBigNum

```c
// 函数功能：输入一个大整数，放于数组中
// 函数参数：存放大整数的数组x，能输入的最多位数lim
// 函数返回值：void
void getBigNum(int *x, int lim);
```

- 输入用字符一位一位输入，先输入高位再输入低位
- 实际存储：低位在低地址（也可以低位在高地址）
- 反转数组元素：个位在`x[1]`，十位在`x[2]`，...，`x[0]`放总位数

---

## 函数putBigNum

从高位按运算结果的实际位数输出每一位（数组元素）

---

## 运算过程

模拟列竖式计算两数相加（如45+96）

1. **运算顺序**：从低位向高位运算；先低位后高位
2. **运算规则**：相同位的两个数相加再加上进位，成为该位的和；这个和去掉向高位的进位就成为该位的值
3. **最后一位的进位**：如果完成两个数的相加后，进位位值不为0，则应添加一位
4. **位数不同**：按位数多的一个进行计算

---

## 函数addBigNum

```c
// 函数功能：两个大整数相加
// 函数参数：输入 x--被加数，y--加数；输出 z--和数
// 函数返回值：void
void addBigNum(int *z, int *x, int *y);
```

---

## 分治法

高精度计算是基于分治法。

**分治法**："分而治之"就是把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并。

**分治策略**：将"一个大数分为多个1位整数（0~9）"

---

## 优化策略

**缺点**：
1. 浪费空间：一个整型数组的每个元素只存放一位
2. 浪费时间：一次加法只处理一位

**优化**：
1. 分治策略：将"一个大数分为多个4位整数（0~9999）"
2. 一个数组元素存放四位数；将标准数组改为紧缩数组
3. 运算时：逢万进位；将"十进制运算"改为"万进制运算"
4. 输出时：最高位直接输出，其余各位要判断是否足够4位，不足部分要补0

---

## 思考练习

编程计算n!（n可达100）

---

<!-- _class: lead -->

# 8.4 指针和字符串

---

## 字符串的指针表示

字符串是一维字符数组，要访问和操纵字符串，可以用字符数组，也可用字符指针。

```c
// (1) 声明字符指针变量和字符数组
char s[80] = "This is a string.";
char *p = s;
puts(p);        // 输出：This is a string.
putchar(*p);    // 输出：T

s = "This is a book.";  // 错，数组名s是指针常量
strcpy(s, "This is a string.");  // √
```

---

## 字符串的指针表示(续)

```c
// (2) 声明和初始化字符指针变量
char *p = "This is a string.";
/* 分配内存给字符指针p；
   分配内存（静态区）给字符串常量（只读）；
   将字符串首地址赋值给字符指针； */
puts(p);        // 输出 This is a string.
putchar(p[1]);  // 输出 h

p = "This is a book.";  // √, p是指针变量, 不提倡
*p = 't';               // 运行错
```

---

## 字符串作函数参数

```c
void mystrcpy(char *t, const char *s) {
    while((*t++ = *s++) != '\0');
}

char t[30], s[] = "world";
char *p;
mystrcpy(t, "hello");  // √
mystrcpy(t, s);        // √
mystrcpy(p, s);        // ×
p = t;
mystrcpy(p, s);        // √
```

---

<!-- _class: lead -->

# 8.5 指针数组

---

## 指针数组定义

```c
int *p[3];  // p是一个有3个元素的整型指针数组
            // 即每个元素是指向整型变量的指针

char *ps[2] = {"red", "green"};  // ps是一个有2个元素的字符指针数组
                                 // ps[0]指向字符串"red"
                                 // ps[1]指向字符串"green"
```

---

## 字符指针数组 - 错误示例

```c
#define N 3
#include<stdio.h>
int main() {
    int i;
    char *s[N];
    for(i = 0; i < N; i++)
        fgets(s[i], 80, stdin);  // 错误，使用了悬挂指针
    return 0;
}
```

---

## 动态分配存储字符串的空间

```c
#define N 3
#include<stdio.h>
#include<stdlib.h>
int main() {
    int i;
    char *s[N];
    for(i = 0; i < N; i++) {
        char t[80];
        fgets(t, 80, stdin);
        s[i] = (char *)malloc(strlen(t) + 1);
        strcpy(s[i], t);
    }
    // ...
}
```

`malloc(size)`：分配size字节的存储区，返回所分配单元的起始地址。如不成功，返回NULL。

---

## 二级指针的应用

```c
char *s[4];  // s类型是char**（指向字符指针的指针）
```

- `(s+i)` 指向 `s[i]`
- `*(s+i)` 等价于 `s[i]`
- `*(s+i)+j` 指向 `s[i][j]`
- `*(*(s+i)+j)` 等价于 `s[i][j]`

**二级指针作函数的形参**：`char **s`

---

## 字符串排序函数 - strsort

```c
void strsort(char *s[], int n) {
    char *temp;
    int i, j;
    for(i = 0; i < n - 1; i++)
        for(j = 0; j < n - i - 1; j++)
            if(strcmp(s[j], s[j + 1]) > 0) {
                temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
}
/* 移动指针变量 */
```

---

## 例：输入N本书名，排序后输出

```c
#define N 3
#include<stdio.h>
#include<stdlib.h>
int main() {
    int i;
    char *s[N], t[80];
    for(i = 0; i < N; i++) {
        fgets(t, 80, stdin);
        s[i] = (char *)malloc(strlen(t) + 1);
        strcpy(s[i], t);
    }
    strsort(s, N);
    for(i = 0; i < N; i++) puts(s[i]);
}
```

---

<!-- _class: lead -->

# 8.6 带参数的main函数

---

## 命令行参数

求1+2+...+n，n值由用户指定

**方式1**：运行后输入
**方式2**：命令行中输入

```c
// 方式2的main函数
int main(int argc, char *argv[]) {
    // ...
}
```

命令行：`C:\> sum 11`

`argc`：命令行中参数的个数（包括文件名）
`argv`：长度为argc的字符指针数组

---

## 命令行参数的传递

```c
char *argv[] = {"sum", "11", NULL};
```

```c
#include<stdio.h>
#include<stdlib.h>
int main(int argc, char **argv) {
    int n, sum, i;
    if(argc != 2) {
        printf("Command line error!\n");
        return 1;
    }
    n = atoi(*++argv);
    // ...
}
```

`argv`的类型实质为 `char **`

---

<!-- _class: lead -->

# 8.7 指针函数

---

## 指针函数定义

在C语言中，函数返回的只能是值。这个值可以是一般的数值，也可以是某种类型的指针值。如果函数的返回值是指针类型的值，该函数称为指针函数。

```c
类型 *函数名(形参表);
```

如：`char *strcpy(char *t, const char *s);`

---

## 指针函数的定义

```c
char *strcpy(char *t, const char *s) {
    char *p = t;
    while(*t++ = *s++);
    return(p);  // 返回第1个串的首地址
}

int main() {
    char st1[40] = "abcd", st2[] = "hijklmn";
    printf("%s", strcpy(st1, st2));
    return 0;
}
```

---

<!-- _class: lead -->

# 8.8 函数的指针

---

## 函数指针的声明

每个函数都占用一段内存单元，有一个起始地址。

```c
int (*p)(int, int);  // p是指向有两个int参数的int函数的指针
```

**函数指针的声明**：
```c
类型 (*标识符)(形参表);
```

---

## 函数指针的使用

```c
void f1(int x) {
    printf("x=%d\n", x);
}

void f2(int x, int y) {
    printf("x=%d\n", x);
    printf("y=%d\n", y);
}

int main(void) {
    void (*pf1)(int x);
    void (*pf2)(int x, int y);
    pf1 = f1;
    pf2 = f2;
    pf1(5);         // 等价于(*pf1)(5);
    pf2(10, 20);    // 等价于(*pf2)(10, 20);
    return 0;
}
```

---

## 通用的整数排序函数

既能实现升序排序，也能实现降序排序

```c
// 对指针v指向的n个整数按comp规则排序
void sort(int *v, int n, int (*comp)(int, int)) {
    int i, j;
    for(i = 1; i < n; i++)        // 冒泡法
        for(j = 0; j < n - i; j++)
            // 对v[j]和v[j+1]按照comp的规则进行比较
            if(comp(v[j], v[j + 1]))
                swap(v + j, v + j + 1);  // 交换
}
```

---

## 回调函数

```c
// 规则：按升序排序
int asc(int x, int y) {    // 回调函数
    if(x > y) return 1;
    else return 0;
}

// caller
int a[6] = {4, 6, 3, 9, 7, 2};
sort(a, 6, asc);

// 思考：如果要降序，如何定义回调函数？
```

---

## 进阶：定义更通用的排序函数

能够对int、char、double、字符串、struct类型的数据排序。

```c
// stdlib.h中的标准库函数qsort----万能数组排序函数
void qsort(void *base, int nelem, int width, 
           int (*fcmp)(const void *, const void *));
```

**函数参数**：
- `void *v`：待排序数组首地址
- `int n`：数组中待排序元素数量
- `int size`：各元素的占用空间大小（字节）
- `int (*fcmp)(const void *, const void *)`：指向函数的指针，用于确定排序的规则

**思考**：如何调用qsort对字符串数组排序。

---

<!-- _class: lead -->

# 8.9 指针与二维数组

---

## 用指针表示二维数组元素

```c
#define M 3
#define N 2
int a[M][N] = {{1, 3}, {4, 6}, {7, 9}};
int *p;
```

**思考**：如何用指针p逐行输出数组a的所有元素？

---

## 用指向数组元素的指针表示二维数组

```c
// 方法1
for(p = a[0]; p < a[0] + M * N; p++) {
    if(!((p - a[0]) % N)) printf("\n");
    printf("%5d", *p);
}

// 方法2
p = a[0];  // 等价于 p = &a[0][0]
for(i = 0; i < M; i++) {
    printf("\n");
    for(j = 0; j < N; j++)
        printf("%5d", *(p + i * N + j));  // a[i][j]
}
```

---

## 行地址与元素地址

二维数组被看成以1维数组（行）为元素的数组。

```c
int u[2][3] = {{1, 3, 5}, {2, 4, 6}};
```

- 第0行地址：`u[0] == &u[0][0]`
- 第1行地址：`u[1] == &u[1][0]`
- i行j列元素的地址：`&u[i][j]`、`u[i] + j`、`*(u + i) + j`
- i行j列元素的表示：`u[i][j]`、`*(u[i] + j)`、`*(*(u + i) + j)`
- `*u`：第0行首元素地址

---

## 指向数组的指针

```c
类型名 (*标识符)[常量];
```

```c
int a[3][2] = {{1, 3}, {4, 6}, {7, 9}};
int (*p)[2];  // p是指向数组的指针，该数组有2个int型元素
p = a;        // p[i][j]: a[i][j]
```

| 表达式 | 等价表示 |
|--------|----------|
| `*(*p)` | `(*p)[0]` |
| `*(*p + 1)` | `(*p)[1]` |
| `*(*(p + 1))` | `(*(p + 1))[0]` |
| `*(*(p + 1) + 1)` | `(*(p + 1))[1]` |

---

## 二维数组元素的输入/输出

```c
#include <stdio.h>
#define I 2
#define J 3
int main(void) {
    int u[I][J], (*p)[J] = u;
    int j;
    
    for(j = 0; j < J; j++)      // 用指向数组元素的指针完成第0行元素的输入
        scanf("%d", (u[0] + j));
    
    for(p++, j = 0; j < J; j++) // 用指向数组的指针完成第1行元素的输入
        scanf("%d", (*p + j));
    
    for(j = 0; j < J; j++)      // 用指向数组的指针完成第0行元素的输出
        printf("%6d", *(*u + j));
    printf("\n");
    
    for(j = 0; j < J; j++)      // 用指向数组元素的指针完成第1行元素的输出
        printf("%6d", *(u[1] + j));
    return 0;
}
```

---

## 二维数组作函数参数

```c
// 形参说明为数组
void fun(int x[][4], int row) { ... }

// 形参说明为指针（指向下一级数组的指针）
void fun(int (*x)[4], int row) { ... }

// 指向数组元素的指针
void fun(int *x, int row, int col) { ... }

// 变长数组（C99）
void fun(int row, int col, int (*x)[col]) { ... }
```

---

## 三维数组的指针表示

三维数组被看成以2维数组（页）为元素的一维数组。

```c
int x[2][3][4];
int (*p)[3][4] = x;  // p是指向3行4列的二维整型数组的指针
```

| 表达式 | 等价表示 |
|--------|----------|
| `*(*(*(p + i) + j) + k)` | `x[i][j][k]` |
| `*(*(p[i] + j) + k)` | `x[i][j][k]` |
| `*(p[i][j] + k)` | `x[i][j][k]` |
| `p[i][j][k]` | `x[i][j][k]` |

---

<!-- _class: lead -->

# 8.10 用typedef定义类型

---

## typedef用法

typedef是关键字，为一个已有类型定义一个别名。

```c
// (1) 基本类型别名
typedef unsigned int size_t;
size_t x, y;  // unsigned int x, y;

// (2) 指针类型别名
typedef char *string;
string p, s[10];  // char *p, *s[10];

// (3) 函数指针类型别名
typedef int (*p_to_fun)(int, int);
p_to_fun pf;  // int (*pf)(int, int)
```

---

## typedef与#define的区别

```c
#define string char *  // string是宏名，简单的串替换
string p, s[10];      // char *p, s[10];
                       // p是字符指针
                       // s是含有10个元素的字符数组
```

---

<!-- _class: lead -->

# 8.11 复杂声明

---

## 函数指针数组

```c
int (*p[2])(int);  // p是含有2个指针元素的数组
                   // 每个指针指向有一个整型参数，返回值为整型的函数
```

---

## 函数指针数组的使用

```c
int fun1(int x) { return 2 * x; }
int fun2(int y) { return 3 * y; }

int main(void) {
    int i, (*fp[2])(int);  // fp是有2个元素的函数指针数组
                           // 每个元素指向的函数有一个整型形参，返回整型值
    fp[0] = fun1;          // 0号元素指向fun1函数
    fp[1] = fun2;          // 1号元素指向fun2函数
    
    for(i = 0; i < 2; i++)
        printf("%d\n", fp[i]((i + 1) * 5));  // 依次调用fp[0]、fp[1]所指函数
    return 0;
}
```

---

## 函数指针的应用 - 多分支函数处理

函数指针数组可用于设计所谓的派遣（dispatch）表，以实现多分支函数处理问题，从而省去了大量的if或switch语句。

```c
// 设有10个函数f0(x),f1(x),...,f9(x)以及一个变量index
// 当index=i时，就调用fi(x)

double f0(int), f1(int), ..., f9(int);  // 函数原型
static double (*dispatch[])(int) = {f0, f1, ..., f9};  // 函数指针数组

// 调用变量index所指定的函数
dispatch[index](x);  // (*dispatch[index])(x);
```

---

## 用函数指针数组控制菜单的驱动

```c
void (*cmd[4])(void) = {f1, f2, f3, f4};
// cmd是有4个元素的函数指针数组，函数无返回值，无参数

int main(void) {
    // ...
    do {
        printf("menu1\n");
        printf("menu2\n");
        printf("menu3\n");
        printf("menu4\n");
        printf("exit(0)\n");
        printf("Enter your choice:\n");
        scanf("%d", &choice);
        if(choice >= 1 && choice <= 4)
            cmd[choice - 1]();
    } while(choice);
}

void f1() { ... }
void f2() { ... }
void f3() { ... }
void f4() { ... }
```

---

## 指向函数的指针函数

```c
int (*f(char *, char *))(int, int);
```

f是一个指针函数，f函数有2个char *类型的形参，其返回值是指向有2个int参数且返回值为int的函数的指针。

---

## 指针函数的指针

```c
char * (*(*v)(void))[10];
```

1. `(*v)`：v是指针变量
2. `(*v)(void)`：v是指向函数的指针，所指函数无参数
3. `(*(*v)(void))`：v所指函数的返回值是指针
4. `(*(*v)(void))[10]`：返回的指针指向有10个元素的数组
5. `char * (*(*v)(void))[10]`：数组元素的类型是char *

**v是指向函数的指针，所指函数没有参数，返回值是指向有10个元素的字符指针数组的指针。**

---

## 总结

- 指针基础概念
- 指针参数
- 一维数组
- 高精度计算
- 字符串
- 指针数组
- 指针函数
- 二维数组
