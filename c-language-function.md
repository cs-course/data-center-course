---
marp: true
theme: gaia
title: C语言程序设计 - 第5章 函数
paginate: true
---

<!-- _class: lead -->

# 第5章 函数

**C语言程序设计**

---

## 主要内容
- 结构化编程和C程序的一般结构
- 函数的机制：函数定义、函数声明、函数调用
- 变量的存储类型
- 递归

---

## 5.1 模块化程序设计

- 把一个问题逐步细化分解为若干子问题，用函数实现子问题
- 使程序编制方便，易于管理、修改和调试
- 增强了程序的可读性、可维护性和可扩充性
- 函数可以公用，避免在程序中使用重复的代码
- 提高软件的可重用性

---

## 蒙特卡罗模拟：猜数游戏

**模拟算法**：编程实现现实世界中的随机事件

**随机数特点**：
- 不确定性和偶然性
- 应用领域：软件测试、加密系统、网络验证码

**随机数发生器**：
```c
int rand(void);  // 在stdlib.h中
```

---

## 猜数游戏主程序结构

```c
do {
    计算机产生一个1到1000的随机数；
    游戏者猜数，直至猜对；
    printf("Play again? (Y/N) ");
    scanf("%1s", &cmd);   
} while (cmd == 'y' || cmd == 'Y');
```

---

## 函数定义示例

```c
#define MAX_NUMBER 1000

int GetNum(void) {
    int x;
    printf("A magic number between 1 and %d has been chosen.\n", MAX_NUMBER);  
    x = rand();                    // 调用标准库函数rand产生随机数
    x = x % MAX_NUMBER + 1;        // 限制在1～MAX_NUMBER之间
    return x;  
}
```

---

## 完整猜数游戏代码

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX_NUMBER 1000

int GetNum(void);          // 函数原型
void GuessNum(int x);      // 函数原型

int main(void) {
    char command;
    int magic;
    
    srand(time(NULL));     // 初始化随机数种子
    
    do {
        magic = GetNum();      // 调用GetNum产生随机数
        GuessNum(magic);       // 调用GuessNum猜数
        printf("Play again? (Y/N) ");
        scanf("%1s", &command);    
    } while (command == 'y' || command == 'Y');
    
    return 0;
}
```

---

## 5.2 自定义函数

使用自定义函数需要做三件事：
1. 按语法规则编写函数（定义函数）
2. 在调用函数之前进行函数声明
3. 在需要时调用函数

---

## 函数的定义

**一般形式**：
```c
类型名 函数名(参数列表) {
    声明部分
    语句部分
}
```

**return语句形式**：
```c
return;              // void函数：无返回值函数
return 表达式;       // 非void函数：有返回值函数
```

---

## 函数原型与调用

```c
// 函数原型声明
int GetNum(void);
void GuessNum(int x);

int main(void) {
    int magic;
    magic = GetNum();        // 函数调用
    GuessNum(magic);         // 函数调用
    return 0;
}

// 函数定义
int GetNum(void) {
    // 函数体
}

void GuessNum(int x) {
    // 函数体
}
```

---

## 参数传递：值传递示例

```c
#include<stdio.h>
long power(int, int);  // 函数原型

int main(void) {
    int x, n;
    for(x = 1; x <= 10; x++) {
        for(n = 2; n <= 5; n++)
            printf("%10ld", power(x, n));
        printf("\n");
    }
    return 0;
}

long power(int x, int n) {  // 计算x的n次方
    long p;
    for (p = 1; n > 0; n--) p *= x;
    return p;
}
```

---

## 5.3 变量的存储类型

**存储类型决定**：
- 作用域
- 存储分配方式  
- 生命周期
- 初始化方式

**关键字**：`auto`、`extern`、`static`、`register`

---

## 作用域与变量分类

**作用域**：标识符的有效范围

**变量分类**：
- **局部变量**：在函数内部定义，作用域是定义该变量的程序块
- **全局变量**：在函数外部定义，作用域从其定义处开始到文件末尾

---

## 自动变量(auto)

```c
auto int a;  // 等价于 int a; 或 auto a;
```

**特性**：
- 作用域：局部于定义它的块
- 存储分配方式：动态分配
- 生命周期：短暂的，只存在于该块的执行期间
- 初始化：定义时没有显示初始化，初值不确定

---

## 外部变量(extern)

```c
int p = 1, q = 5;  // p、q为全局变量

float f1(int a) {   // 形参a为局部变量
    int b, c;       // b、c为局部变量
    // ...
}
```

**特性**：
- 作用域：从定义之后直到源文件结束
- 存储分配方式：静态分配
- 生命周期：永久的，存在于整个程序执行期间
- 初始化：定义时没有显示初始化，初值为0

---

## 静态变量(static)

**两种用法**：
1. 用于定义局部变量 → 静态局部变量
2. 用于定义外部变量 → 静态外部变量

**特性**：
- 存储分配方式：静态分配
- 生命周期：永久的
- 缺省初值：0，只执行一次初始化

---

## 静态局部变量示例

```c
// 计算1! + 2! + 3! + ... + n!
long factorial(int n) {
    static long cache[100] = {0};  // 静态局部变量，缓存已计算的值
    
    if (n == 0 || n == 1) return 1;
    if (cache[n] != 0) return cache[n];  // 如果已计算过，直接返回
    
    cache[n] = n * factorial(n - 1);     // 计算并缓存
    return cache[n];
}
```

---

## 寄存器变量(register)

```c
register int i;  // 等价于 register i;

for (i = 0; i <= N; i++) {
    // 频繁访问的变量
}
```

**目的**：提高程序执行速度
**限制**：不可多，不能使用&运算

---

## 5.4 递归

**递归函数**：在定义中含有递归调用的函数

```c
void prn_int(int n) {
    if (n > 0) {
        printf("%d ", n);
        prn_int(n - 1);  // 递归调用
    }
    printf("%d ", n);
}
```

输出：`4 3 2 1 0 1 2 3 4`

---

## 递归法求n!

```c
long fact(int n) {
    if (n == 0 || n == 1) {          // 递归结束条件
        return 1;
    } else {
        return (n * fact(n - 1));    // 递归调用
    }
}
```

**递归原则**："能进则进，不进则退"

---

## 迭代法求n!

```c
long factorial_iteration(int n) {
    int result = 1;
    while (n > 1) {
        result *= n;
        n--;
    }
    return result;
}
```

**比较**：递归结构清晰但效率低，迭代效率高

---

## 递归求Fibonacci数列

**基础版本**：
```c
long long fibo(long n) {
    if (n == 1 || n == 2) return 1;
    else return fibo(n - 1) + fibo(n - 2);
}
```

**问题**：存在大量重复计算，效率低

---

## 优化1：记忆化搜索

```c
long long fibo(long n) {
    static long long f[1000] = {0, 1, 1};  // 储存计算过的值
    
    if (f[n]) {           // 已计算过，直接返回
        return f[n];
    }
    return (f[n] = fibo(n - 1) + fibo(n - 2));
}
```

---

## 优化2：尾递归

```c
long long fibo_tail_rec(int n, long long first, long long second) {
    if (n <= 1) return first;
    else return fibo_tail_rec(n - 1, second, first + second);
}

long long fibo(long n) {
    return fibo_tail_rec(n, 1, 1);
}
```

**优点**：避免爆栈，当前运算结果通过参数传递

---

## 字符串的递归处理

**递归实现strlen**：
```c
int strlen(char s[]) {
    if (s[0] == '\0') {
        return 0;
    } else {
        return (1 + strlen(s + 1));  // 或 &s[1]
    }
}
```

---

## 汉诺塔问题

**递归算法**：
1. 把A上的n-1个盘子借助C移到B
2. 把A上剩下的盘子（最大的）移到C
3. 把B上的n-1个盘子借助A移到C

```c
void move(int n, int a, int b, int c) {
    if (n == 1) {
        printf(" %c --> %c\n", a, c);
    } else {
        move(n - 1, a, c, b);
        printf(" %c --> %c\n", a, c);
        move(n - 1, b, a, c);
    }
}
```

---

## 递归练习

**1. 数字逆序输出**：
```c
void reverse(long m) {
    if (m < 10) {
        printf("%ld", m);
    } else {
        printf("%ld", m % 10);
        reverse(m / 10);
    }
}
```

**2. 判断回文字符串**：
```c
int is_palindrome(char str[], int n) {
    if (n <= 1) return 1;
    if (str[0] != str[n - 1]) return 0;
    return is_palindrome(str + 1, n - 2);
}
```

---

## 整数的分划问题

```c
void split(int n, int cur) {
    static int a[100];  // 存储分划值
    
    if (!n) {  // 递归边界：已确定一种分划
        // 输出分划方案
        for (int i = 0; i < cur; i++) {
            printf("%d ", a[i]);
        }
        printf("\n");
        return;
    }
    
    for (int i = n; i >= 1; i--) {  // 枚举当前位置的分划值
        if (cur == 0 || i <= a[cur - 1]) {  // 避免重复，保持非递增
            a[cur] = i;
            split(n - i, cur + 1);  // 递归确定下一位置
        }
    }
}
```

---

## 枚举的递归实现

**八皇后问题**：
```c
int a[8];  // a[i]表示第i行皇后放在第a[i]列

void find(int a[], int i) {
    if (i == 8) {  // 递归边界：已枚举每一行
        // 输出解
        return;
    }
    
    for (int j = 0; j < 8; j++) {  // 将i行皇后放到j列
        if (is_valid(a, i, j)) {   // 判断是否互不攻击
            a[i] = j;
            find(a, i + 1);        // 枚举下一行
        }
    }
}
```

---

## 总结

- 能够设计模块化的程序结构
- 熟练运用各种存储类型的变量
- 理解并实现递归算法
- 能够对递归程序进行优化
- 解决经典递归问题（汉诺塔、八皇后等）
