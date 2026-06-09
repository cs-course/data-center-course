---
marp: true
theme: gaia
title: C语言程序设计 - 第2章 基本元素
paginate: true
math: katex
---

<!-- _class: lead -->

# 第2章 基本元素

**C语言程序设计**

---

## 本章内容

- 字符集和标识符
- 数据类型
- 常量与变量
- 运算符和表达式
- 位运算
- 类型转换

---

## 字符集

<style scoped>
  li {
    font-size: 24px;
  }
</style>

C 语言的字符集包括：

- **字母**：`a`~`z`、`A`~`Z`
- **数字**：`0`~`9`
- **特殊符号**：`+ - * / = < > ! & | ^ ~ # ' " ; : , . ? \ ( ) [ ] { }`
- **空白符**：空格、制表符 `\t`、换行符 `\n`、回车 `\r`、换页 `\f`
- **转义字符**：以 `\` 开头的特殊字符序列

| 转义字符 | 含义 | ASCII |
|:---:|:---|:---:|
| `\n` | 换行 | 10 |
| `\t` | 水平制表 | 9 |
| `\\` | 反斜杠 | 92 |
| `\'` | 单引号 | 39 |
| `\"` | 双引号 | 34 |
| `\0` | 空字符 | 0 |

---

## 标识符

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**标识符**：用来命名变量、函数、类型等的符号

**命名规则**：
- 只能由**字母**、**数字**和**下划线**组成
- 第一个字符必须是**字母**或**下划线**
- 不能使用**关键字**作为标识符
- 区分大小写（`count` ≠ `Count`）

**合法示例**：`score`、`student_name`、`_count`、`MAX_SIZE`

**非法示例**：`2nd`（数字开头）、`my-var`（含减号）、`int`（关键字）

**命名风格建议**：
- 变量/函数：小写+下划线 `student_count`
- 常量/宏：全大写 `MAX_SIZE`
- 避免以 `_` 或 `__` 开头（系统保留）

---

## C语言关键字（C89 共32个）

<style scoped>
  table {
    font-size: 18px;
  }
</style>

| 类别 | 关键字 |
|:---|:---|
| 数据类型 | `int` `char` `float` `double` `void` `short` `long` `unsigned` `signed` |
| 构造类型 | `struct` `union` `enum` `typedef` |
| 存储类别 | `auto` `static` `extern` `register` |
| 控制语句 | `if` `else` `switch` `case` `default` `for` `while` `do` `break` `continue` `goto` `return` |
| 其他 | `const` `volatile` `sizeof` |

> C99 新增：`inline` `restrict` `_Bool` `_Complex` `_Imaginary`
> C11 新增：`_Alignas` `_Alignof` `_Atomic` `_Generic` `_Noreturn` `_Static_assert` `_Thread_local`

---

## 数据类型概览

<style scoped>
  p {
    text-align: center;
  }
</style>

```
                        C语言数据类型
                           │
          ┌────────────────┼────────────────┐
          │                │                │
      基本类型        构造类型         指针类型
    ┌───┴───┐      ┌──┴──┐             │
   整型  浮点型    数组 结构体          变量地址
   │     │      联合体 枚举           函数地址
 char  float
  int  double
short long
unsigned signed
          │
       空类型(void)
```

---

## 整数类型

<style scoped>
  table {
    font-size: 20px;
  }
  p {
    font-size: 20px;
  }
</style>

| 类型 | 典型字节数 | 值域（32位系统） |
|:---|:---:|:---|
| `char` | 1 | $-128$ ~ $127$ 或 $0$ ~ $255$ |
| `short` / `short int` | 2 | $-32768$ ~ $32767$ |
| `int` | 4 | $-2^{31}$ ~ $2^{31}-1$ |
| `long` / `long int` | 4/8 | 平台相关 |
| `long long` (C99) | 8 | $-2^{63}$ ~ $2^{63}-1$ |

加 `unsigned`：零和正数范围翻倍

| 类型 | 值域 |
|:---|:---|
| `unsigned char` | $0$ ~ $255$ |
| `unsigned short` | $0$ ~ $65535$ |
| `unsigned int` | $0$ ~ $2^{32}-1$ |
| `unsigned long long` | $0$ ~ $2^{64}-1$ |

> 字节数可用 `sizeof` 运算符在目标平台上验证

---

### 用 `sizeof` 验证类型大小

```c
#include <stdio.h>

int main(void) {
    printf("char:   %zu bytes\n", sizeof(char));     // 1
    printf("short:  %zu bytes\n", sizeof(short));    // 2
    printf("int:    %zu bytes\n", sizeof(int));      // 4
    printf("long:   %zu bytes\n", sizeof(long));     // 4 或 8
    printf("long long: %zu bytes\n", sizeof(long long)); // 8
    printf("float:  %zu bytes\n", sizeof(float));    // 4
    printf("double: %zu bytes\n", sizeof(double));   // 8
    return 0;
}
```

- `sizeof` 是**编译时运算符**，不是函数
- 返回 `size_t` 类型，用 `%zu` 打印（C99）
- `char` 永远是 1 字节，其他类型平台相关

---

## 浮点类型

<style scoped>
  table {
    font-size: 20px;
  }
</style>

| 类型 | 字节数 | 有效数字 | 值域（绝对值） |
|:---|:---:|:---:|:---|
| `float` | 4 | 6~7 位 | $1.2 \times 10^{-38}$ ~ $3.4 \times 10^{38}$ |
| `double` | 8 | 15~16 位 | $2.2 \times 10^{-308}$ ~ $1.8 \times 10^{308}$ |
| `long double` | 8/12/16 | 18+ 位 | 平台相关 |

**浮点数的精度陷阱**：

```c
float f = 0.1f;
printf("%.20f\n", f);   // 输出: 0.10000000149011611938
```

- 0.1 无法精确表示为二进制浮点数
- **经验法则**：比较浮点数用 `fabs(a - b) < EPS`，不要用 `a == b`

---

## 字符类型

<style scoped>
  li {
    font-size: 24px;
  }
</style>

- `char` 在内存中存储的是字符的 **ASCII 码值**（0~127）
- 字符常量用**单引号**括起：`'A'`、`'0'`、`'\n'`

```c
char ch = 'A';     // 等价于 char ch = 65;
printf("%c %d\n", ch, ch);  // 输出: A 65
```

- `'0'` 的 ASCII 码是 48，**不等于**整数 `0`
- `'A'`~`'Z'` 连续编码 65~90
- `'a'`~`'z'` 连续编码 97~122
- 大小写转换：`ch - 'A' + 'a'` 或 `ch + 32`

```c
char upper = 'G';
char lower = upper - 'A' + 'a';   // 'g'
```

---

## 布尔类型（C99）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

C99 引入 `_Bool` 类型和 `<stdbool.h>` 头文件：

```c
#include <stdbool.h>

bool flag = true;    // 等价于 _Bool flag = 1;
if (flag) {
    printf("flag is true\n");
}
flag = false;        // 等价于 flag = 0;
```

- C 语言中，**0 为假，非 0 为真**
- `true` = 1，`false` = 0（定义在 `<stdbool.h>` 中）
- 逻辑表达式（`<` `>` `==` `&&` `||` `!`）的结果为 `0` 或 `1`

---

## 常量

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**字面常量**：直接写在代码里的值

| 类型 | 示例 | 说明 |
|:---|:---|:---|
| 整型 | `42` | 十进制 |
| 整型 | `052` | 八进制（前缀 `0`） |
| 整型 | `0x2A` | 十六进制（前缀 `0x`） |
| 长整型 | `42L` | 后缀 `L` |
| 无符号 | `42U` | 后缀 `U` |
| 浮点 | `3.14` | 默认 `double` |
| 浮点 | `3.14f` | 后缀 `f` 为 `float` |
| 浮点 | `1.0e-3` | 科学计数法 |
| 字符 | `'A'` | 单引号 |
| 字符串 | `"hello"` | 双引号，末尾自动加 `'\0'` |

---

### 符号常量

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**方式一：`#define` 宏定义**（预处理替换，无类型检查）

```c
#define PI 3.14159
#define MAX_SIZE 100
```

**方式二：`const` 修饰**（有类型检查，推荐）

```c
const double PI = 3.14159;
const int MAX_SIZE = 100;
```

**区别**：

| 特性 | `#define` | `const` |
|:---|:---|:---|
| 处理时机 | 预处理阶段 | 编译阶段 |
| 类型检查 | 无 | 有 |
| 调试可见性 | 不可见（已替换） | 可见 |
| 作用域 | 全局（从定义到文件末尾） | 遵循作用域规则 |

---

## 变量

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**变量**：程序运行过程中值可以改变的量

**声明与定义**：

```c
int age;                 // 定义：分配内存
int age = 20;            // 定义并初始化
extern int count;        // 声明（不分配内存）：告诉编译器 count 在别处定义
```

**要点**：
- 变量**必须先定义后使用**
- C89 要求变量定义在代码块**开头**；C99 允许在任意位置定义
- 未初始化的**局部变量值不确定**（未定义行为），**全局变量默认初始化为 0**

```c
int main(void) {
    int a;              // 局部变量，值不确定！
    int b = 0;          // 显式初始化
    // C99 写法：
    for (int i = 0; i < 10; i++) { ... }
}
```

---

### 变量的作用域

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```c
#include <stdio.h>

int g = 100;                // 全局变量：文件作用域

void func(void) {
    int a = 1;              // 局部变量：块作用域
    printf("a=%d, g=%d\n", a, g);
}

int main(void) {
    int a = 2;              // 另一个局部变量，与 func 中的 a 无关
    {
        int b = 3;          // 内层块作用域
        printf("b=%d\n", b);
    }
    // printf("%d\n", b);  // 错误！b 不在此作用域
    printf("a=%d, g=%d\n", a, g);
    return 0;
}
```

- **全局变量**：函数外定义，整个文件可见
- **局部变量**：函数或代码块内定义，仅在该块内可见
- 同名变量：内层作用域**遮蔽**外层

---

## 运算符和表达式

### 算术运算符

<style scoped>
  table {
    font-size: 22px;
  }
</style>

| 运算符 | 含义 | 示例 | 结果 |
|:---:|:---|:---|:---|
| `+` | 加 | `3 + 2` | `5` |
| `-` | 减 | `3 - 2` | `1` |
| `*` | 乘 | `3 * 2` | `6` |
| `/` | 除 | `7 / 2` | `3`（整数除法） |
| `%` | 取模 | `7 % 2` | `1` |
| `++` | 自增 | `i++` / `++i` | i 的值加 1 |
| `--` | 自减 | `i--` / `--i` | i 的值减 1 |

**注意**：
- 整数除法**截断小数**：`7 / 2` → `3`，不是 `3.5`
- `%` 只能用于整数
- `++i`（前缀）：先加 1 再使用；`i++`（后缀）：先使用再加 1

---

### 自增/自减运算符详解

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```c
int i = 5;
int a = ++i;   // i 先变为 6，a = 6
int b = i++;   // b = 6（使用当前值），然后 i 变为 7
```

**经典陷阱**：不要在同一个表达式中对同一变量多次使用 `++`/`--`

```c
int i = 3;
int a = i++ + ++i;   // 未定义行为！不同编译器结果不同
```

> **规则**：两个序列点之间，同一变量的值最多被修改一次。

---

### 关系运算符

<style scoped>
  table {
    font-size: 22px;
  }
</style>

| 运算符 | 含义 | 示例 | 结果 |
|:---:|:---|:---|:---|
| `>` | 大于 | `5 > 3` | `1` |
| `<` | 小于 | `5 < 3` | `0` |
| `>=` | 大于等于 | `5 >= 5` | `1` |
| `<=` | 小于等于 | `5 <= 3` | `0` |
| `==` | 等于 | `5 == 3` | `0` |
| `!=` | 不等于 | `5 != 3` | `1` |

- 关系表达式的结果是 `0`（假）或 `1`（真）
- **常见错误**：把 `==` 写成 `=`（赋值）

```c
if (a = 5) { ... }    // 永远为真！a 被赋值为 5
if (a == 5) { ... }   // 正确：判断 a 是否等于 5
```

---

### 逻辑运算符

<style scoped>
  table {
    font-size: 22px;
  }
</style>

| 运算符 | 含义 | 示例 | 结果 |
|:---:|:---|:---|:---|
| `&&` | 逻辑与 | `1 && 0` | `0` |
| `||` | 逻辑或 | `1 || 0` | `1` |
| `!` | 逻辑非 | `!1` | `0` |

**短路求值**：

```c
if (p != NULL && p->value > 0) { ... }
// 若 p == NULL，则 p->value 不会执行，避免空指针解引用

if (x > 0 || y > 0) { ... }
// 若 x > 0 为真，y > 0 不会计算
```

- `&&`：左操作数为 0 时，右操作数**不计算**
- `||`：左操作数非 0 时，右操作数**不计算**

---

### 赋值运算符

<style scoped>
  table {
    font-size: 22px;
  }
</style>

| 运算符 | 等价写法 | 示例 |
|:---:|:---|:---|
| `=` | — | `a = 5` |
| `+=` | `a = a + b` | `a += 3` |
| `-=` | `a = a - b` | `a -= 3` |
| `*=` | `a = a * b` | `a *= 3` |
| `/=` | `a = a / b` | `a /= 3` |
| `%=` | `a = a % b` | `a %= 3` |
| `<<=` | `a = a << b` | `a <<= 2` |
| `>>=` | `a = a >> b` | `a >>= 2` |
| `&=` | `a = a & b` | `a &= mask` |
| `|=` | `a = a | b` | `a |= flag` |
| `^=` | `a = a ^ b` | `a ^= key` |

---

### 条件运算符（三目运算符）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**语法**：`表达式1 ? 表达式2 : 表达式3`

- 若 `表达式1` 为真（非 0），整个表达式的值为 `表达式2`
- 否则为 `表达式3`

```c
int max = (a > b) ? a : b;       // 取较大值
int abs_val = (x >= 0) ? x : -x; // 绝对值
```

**嵌套**（可读性差，不推荐）：

```c
int grade = (score >= 90) ? 'A' :
            (score >= 60) ? 'B' : 'C';
```

---

### 逗号运算符

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**语法**：`表达式1, 表达式2, ..., 表达式n`

- 从左到右依次求值，整个逗号表达式的值为**最后一个**表达式的值

```c
int a = (1, 2, 3);   // a = 3
```

**常见用途**：`for` 循环中同时操作多个变量

```c
for (int i = 0, j = 10; i < j; i++, j--) {
    printf("i=%d, j=%d\n", i, j);
}
```

> 注意区分：`int a = 1, b = 2;` 中的逗号是**声明分隔符**，不是逗号运算符。

---

### sizeof 运算符

<style scoped>
  li {
    font-size: 24px;
  }
</style>

- 求类型或变量所占**字节数**
- 编译时求值，不运行代码
- 对数组求值返回整个数组占用的字节数

```c
int arr[10];
printf("%zu\n", sizeof(arr));       // 40 (10 × 4)
printf("%zu\n", sizeof(arr[0]));    // 4
printf("%zu\n", sizeof(arr) / sizeof(arr[0]));  // 10，数组元素个数

int n = 0;
printf("%zu\n", sizeof(n++));      // 4，n++ 不会执行！
```

---

## 运算符优先级（常用）

<style scoped>
  table {
    font-size: 18px;
  }
</style>

| 优先级 | 运算符 | 结合性 |
|:---:|:---|:---|
| 1 (最高) | `()` `[]` `->` `.` | 左到右 |
| 2 | `!` `~` `++` `--` `+` `-` `*` `&` `(type)` `sizeof` | **右到左** |
| 3 | `*` `/` `%` | 左到右 |
| 4 | `+` `-` | 左到右 |
| 5 | `<<` `>>` | 左到右 |
| 6 | `<` `<=` `>` `>=` | 左到右 |
| 7 | `==` `!=` | 左到右 |
| 8 | `&` | 左到右 |
| 9 | `^` | 左到右 |
| 10 | `|` | 左到右 |
| 11 | `&&` | 左到右 |
| 12 | `||` | 左到右 |
| 13 | `?:` | 右到左 |
| 14 | `=` `+=` `-=` 等 | 右到左 |
| 15 (最低) | `,` | 左到右 |

> **技巧**：拿不准优先级时，**加括号**——既清晰又安全。

---

## 位运算

<style scoped>
  li {
    font-size: 24px;
  }
</style>

位运算直接操作二进制位，常用于底层编程、硬件控制、加密算法

| 运算符 | 含义 | 示例（8位） | 结果 |
|:---:|:---|:---|:---|
| `&` | 按位与 | `0b1100 & 0b1010` | `0b1000` |
| `|` | 按位或 | `0b1100 | 0b1010` | `0b1110` |
| `^` | 按位异或 | `0b1100 ^ 0b1010` | `0b0110` |
| `~` | 按位取反 | `~0b1100` | 取决于类型 |
| `<<` | 左移 | `0b0011 << 2` | `0b1100` |
| `>>` | 右移 | `0b1100 >> 2` | `0b0011` |

- 左移 `n` 位 ≈ 乘以 $2^n$（无溢出时）
- 右移 `n` 位 ≈ 除以 $2^n$（对正数）
- 右移对**有符号数**：算术移位（补符号位）还是逻辑移位（补 0），取决于编译器

---

### 位运算典型应用

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**1. 掩码（Mask）—— 取出特定位**

```c
unsigned int flags = 0xA5;         // 10100101
unsigned int mask  = 0x0F;         // 00001111
unsigned int low   = flags & mask; // 00000101，取出低4位
```

**2. 置位（Set bit）—— 将某位置 1**

```c
flags |= (1 << 3);     // 将第3位置1
```

**3. 清位（Clear bit）—— 将某位清 0**

```c
flags &= ~(1 << 3);    // 将第3位清0
```

**4. 翻转（Toggle bit）**

```c
flags ^= (1 << 3);     // 将第3位取反
```

**5. 判断某位是否为 1**

```c
if (flags & (1 << 3)) { /* 第3位为1 */ }
```

---

### 位运算实例：权限控制

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```c
#include <stdio.h>

#define PERM_READ    (1 << 0)  // 0001
#define PERM_WRITE   (1 << 1)  // 0010
#define PERM_EXEC    (1 << 2)  // 0100

int main(void) {
    unsigned int user_perm = PERM_READ | PERM_EXEC;  // 读+执行: 0101

    // 检查权限
    if (user_perm & PERM_READ)  printf("可读\n");
    if (user_perm & PERM_WRITE) printf("可写\n");   // 不输出
    if (user_perm & PERM_EXEC)  printf("可执行\n");

    // 添加写权限
    user_perm |= PERM_WRITE;

    // 移除执行权限
    user_perm &= ~PERM_EXEC;

    return 0;
}
```

---

### 位运算实例：交换两个变量（不用临时变量）

```c
a = a ^ b;
b = a ^ b;   // b = (a^b)^b = a
a = a ^ b;   // a = (a^b)^a = b
```

**原理**：异或的性质
- `x ^ x = 0`
- `x ^ 0 = x`
- 异或满足交换律和结合律

> 实际工程中不推荐这种写法——可读性差，且现代编译器对临时变量方式优化后效率一样。

---

## 类型转换

### 自动类型转换（隐式转换）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

在算术运算中，"低级"类型自动转换为"高级"类型：

```
高 ←───────────────────── 低
double → float → unsigned long → long → unsigned int → int → char/short
```

```c
int    i = 3;
double d = 2.5;
double r = i + d;    // i 自动转为 double，r = 5.5

int a = 5, b = 2;
double c = a / b;    // 先做整数除法得 2，再转为 2.0
double d = (double)a / b;  // a 先转为 2.0，然后做浮点除法得 2.5
```

---

### 强制类型转换（显式转换）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**语法**：`(类型名)表达式`

```c
double pi = 3.14159;
int n = (int)pi;          // n = 3，截断小数部分

int a = 7, b = 2;
double avg = (double)a / b;  // avg = 3.5

// 指针类型转换（高级用法，谨慎使用）
int x = 0x41424344;
char *p = (char *)&x;
printf("%c\n", *p);      // 依赖字节序，结果可能为 'D' 或 'A'
```

**注意事项**：
- 浮点→整数：**截断**（不是四舍五入），用 `(int)(x + 0.5)` 可实现四舍五入
- 大类型→小类型：可能**溢出**或**丢失精度**
- 指针类型转换：容易导致**对齐问题**和**未定义行为**

---

### 整数溢出

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**有符号整数溢出**：未定义行为（UB），编译器可能做任何事

```c
int x = INT_MAX;   // 2147483647
int y = x + 1;     // 未定义行为！可能回绕，可能崩溃
```

**无符号整数回绕**：明确定义的行为

```c
unsigned int u = 0;
unsigned int v = u - 1;    // v = UINT_MAX（4294967295），合法
```

**防范**：

```c
// 加法溢出检查
if (a > INT_MAX - b) { /* 会溢出 */ }

// 乘法溢出检查
if (b != 0 && a > INT_MAX / b) { /* 会溢出 */ }
```

---

## 本章小结

<style scoped>
  li {
    font-size: 22px;
  }
</style>

1. **字符集与标识符**：C 语言基本符号、命名规则
2. **数据类型**：整型（char/short/int/long/long long）、浮点型（float/double）、布尔型（bool）
3. **常量与变量**：字面常量、`#define`、`const`；变量先定义后使用
4. **运算符**：算术、关系、逻辑、赋值、条件、逗号、sizeof
5. **位运算**：与/或/异或/取反/移位——掩码、置位、清位的经典模式
6. **类型转换**：隐式（低→高）、显式（强制）、溢出风险
7. **优先级**：拿不准就加括号

**下一章**：第3章 格式化输入与输出
