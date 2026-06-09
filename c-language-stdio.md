---
marp: true
theme: gaia
title: C语言程序设计 - 第3章 格式化输入与输出
paginate: true
math: katex
---

<!-- _class: lead -->

# 第3章 格式化输入与输出

**C语言程序设计**

---

## 本章内容

- 字符输入输出函数
- 格式化输出函数 printf
- 格式化输入函数 scanf
- 格式控制符详解
- 宽度、精度与对齐
- 输入输出常见陷阱
- 字符串格式化函数

---

## 字符输出函数 putchar

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**函数原型**：`int putchar(int c);`

- 向标准输出（stdout）输出一个字符
- 参数为字符的 ASCII 码值
- 成功时返回输出的字符，失败返回 `EOF`

```c
putchar('A');        // 输出: A
putchar(65);         // 输出: A（65 是 'A' 的 ASCII 码）
putchar('\n');       // 输出换行
char ch = 'Z';
putchar(ch);         // 输出: Z
```

> `putchar(c)` 等价于 `printf("%c", c)`，但更简洁高效

---

## 字符输入函数 getchar

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**函数原型**：`int getchar(void);`

- 从标准输入（stdin）读取一个字符
- 返回读取字符的 ASCII 码值（`int` 类型）
- 遇到文件末尾或出错返回 `EOF`（通常为 -1）

```c
int ch;                    // 注意：用 int 而不是 char
ch = getchar();            // 读取一个字符
putchar(ch);               // 输出该字符
```

**为什么要用 `int` 接收？**

```c
char ch = getchar();       // 错误示范
// 若返回 EOF（通常为 -1），赋给 char 后可能变成 255
// 导致无法正确判断文件结束
```

---

### getchar 的缓冲区特性

<style scoped>
  li {
    font-size: 22px;
  }
</style>

`getchar` 读取的是**行缓冲**输入——用户按回车后，整行字符才送入程序

```c
printf("请输入一个字符：");
int ch = getchar();     // 输入 "A\n"
// ch = 'A'，但 '\n' 仍留在缓冲区！
int next = getchar();   // next = '\n'，不会等待新输入
```

**清空输入缓冲区的常用方法**：

```c
int ch;
while ((ch = getchar()) != '\n' && ch != EOF)
    ;   // 读取并丢弃剩余字符
```

---

### 示例：统计字符数

```c
#include <stdio.h>

int main(void) {
    int count = 0;
    int ch;

    printf("请输入一行文字（回车结束）：\n");
    while ((ch = getchar()) != '\n' && ch != EOF) {
        count++;
    }
    printf("共输入 %d 个字符\n", count);

    return 0;
}
```

- `getchar()` 每次读一个字符
- `!= '\n'` 遇到回车停止
- `!= EOF` 防止文件重定向时死循环

---

## 格式化输出函数 printf

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**函数原型**：`int printf(const char *format, ...);`

- 按指定格式向标准输出设备输出数据
- 返回值：成功输出的**字符数**；出错返回负值
- 格式字符串包含**普通字符**（原样输出）和**格式控制符**（以 `%` 开头）

```c
int n = printf("Hello, %s!\n", "World");
// 输出: Hello, World!
// n = 14（含换行符）
```

**基本格式控制符**：

| 控制符 | 类型 | 示例 | 输出 |
|:---:|:---|:---|:---|
| `%d` | int | `printf("%d", 42)` | `42` |
| `%f` | double | `printf("%f", 3.14)` | `3.140000` |
| `%c` | char | `printf("%c", 'A')` | `A` |
| `%s` | 字符串 | `printf("%s", "hi")` | `hi` |

---

### 完整格式控制符语法

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```
%  [标志]  [宽度]  [.精度]  [长度修饰]  转换说明符
   - + 0    数字    .数字     h l ll
   空格 #
```

| 部分 | 作用 | 示例 |
|:---|:---|:---|
| 标志 | 控制对齐、符号、填充 | `-` 左对齐、`+` 显示正号、`0` 补零、`#` 替代形式 |
| 宽度 | 最小输出宽度 | `%10d` 占 10 位 |
| 精度 | 小数位数 / 字符串最大长度 | `%.2f` 2 位小数 |
| 长度修饰 | 指定参数大小 | `%ld`(long)、`%lld`(long long)、`%zu`(size_t) |
| 转换说明符 | 指定数据类型 | `d`、`f`、`c`、`s`、`x`、`o`、`p` |

---

### 整数格式控制符

<style scoped>
  table {
    font-size: 20px;
  }
</style>

| 控制符 | 含义 | 示例 | 输出 |
|:---|:---|:---|:---|
| `%d` / `%i` | 有符号十进制 | `printf("%d", 42)` | `42` |
| `%u` | 无符号十进制 | `printf("%u", 42U)` | `42` |
| `%o` | 无符号八进制 | `printf("%o", 10)` | `12` |
| `%x` | 无符号十六进制（小写） | `printf("%x", 255)` | `ff` |
| `%X` | 无符号十六进制（大写） | `printf("%X", 255)` | `FF` |
| `%#o` | 带前缀八进制 | `printf("%#o", 10)` | `012` |
| `%#x` | 带前缀十六进制 | `printf("%#x", 255)` | `0xff` |
| `%ld` | long 十进制 | `printf("%ld", 123456L)` | `123456` |
| `%lld` | long long 十进制 | `printf("%lld", 1LL<<40)` | `1099511627776` |

---

### 浮点数格式控制符

<style scoped>
  table {
    font-size: 20px;
  }
</style>

| 控制符 | 含义 | 示例 | 输出 |
|:---|:---|:---|:---|
| `%f` | 小数形式（默认6位） | `printf("%f", 3.14)` | `3.140000` |
| `%.2f` | 2位小数 | `printf("%.2f", 3.14159)` | `3.14` |
| `%e` | 科学计数法（小写e） | `printf("%e", 0.001)` | `1.000000e-03` |
| `%E` | 科学计数法（大写E） | `printf("%E", 0.001)` | `1.000000E-03` |
| `%g` | 自动选择 %f 或 %e | `printf("%g", 0.0001)` | `0.0001` |
| `%g` | 自动选择 | `printf("%g", 0.00001)` | `1e-05` |

**`%g` 的规则**：指数 < -4 或 ≥ 精度时用 `%e`，否则用 `%f`

---

### 宽度与精度控制

<style scoped>
  table {
    font-size: 20px;
  }
</style>

| 格式 | 含义 | 示例值 | 输出 |
|:---|:---|:---|:---|
| `%10d` | 最小宽度10，右对齐 | `42` | `        42` |
| `%-10d` | 最小宽度10，左对齐 | `42` | `42        ` |
| `%010d` | 最小宽度10，补零 | `42` | `0000000042` |
| `%+d` | 显示正负号 | `42` | `+42` |
| `% d` | 正数前加空格 | `42` | ` 42` |
| `%.4f` | 4位小数 | `3.14` | `3.1400` |
| `%10.2f` | 宽度10，2位小数 | `3.14159` | `      3.14` |
| `%-10.2f` | 左对齐 | `3.14159` | `3.14      ` |
| `%.5s` | 最多输出5个字符 | `"hello world"` | `hello` |

---

### 宽度与精度示例

```c
#include <stdio.h>

int main(void) {
    int i = 42;
    double d = 3.14159265;
    char *s = "Hello";

    printf("[%d]\n", i);           // [42]
    printf("[%10d]\n", i);         // [        42]
    printf("[%-10d]\n", i);        // [42        ]
    printf("[%010d]\n", i);        // [0000000042]
    printf("[%+d]\n", i);          // [+42]

    printf("[%.2f]\n", d);         // [3.14]
    printf("[%10.2f]\n", d);       // [      3.14]
    printf("[%-10.2f]\n", d);      // [3.14      ]

    printf("[%.3s]\n", s);         // [Hel]
    printf("[%10.3s]\n", s);       // [       Hel]

    return 0;
}
```

---

## 格式化输入函数 scanf

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**函数原型**：`int scanf(const char *format, ...);`

- 按指定格式从标准输入读取数据
- 返回值：成功匹配并赋值的**项数**；遇到文件末尾返回 `EOF`
- 参数必须是变量的**地址**（用 `&` 取地址）

```c
int a, b;
int ret = scanf("%d%d", &a, &b);
// 输入 "3 5"，ret = 2（成功读入2项）
// 输入 "3 abc"，ret = 1（只成功读入a）
```

---

### scanf 格式控制符

<style scoped>
  table {
    font-size: 20px;
  }
</style>

| 控制符 | 读取类型 | 参数类型 | 示例 |
|:---|:---|:---|:---|
| `%d` | 十进制整数 | `int *` | `scanf("%d", &n)` |
| `%ld` | long 整数 | `long *` | `scanf("%ld", &ln)` |
| `%lld` | long long 整数 | `long long *` | `scanf("%lld", &lln)` |
| `%f` | 浮点数 | `float *` | `scanf("%f", &f)` |
| `%lf` | 双精度浮点 | `double *` | `scanf("%lf", &d)` |
| `%c` | 单个字符 | `char *` | `scanf("%c", &ch)` |
| `%s` | 字符串（遇空白停止） | `char *` | `scanf("%s", str)` |
| `%x` | 十六进制整数 | `unsigned int *` | `scanf("%x", &hex)` |
| `%o` | 八进制整数 | `unsigned int *` | `scanf("%o", &oct)` |
| `%[]` | 字符集合 | `char *` | `scanf("%[a-z]", str)` |

> **重要**：`scanf` 读 `double` 必须用 `%lf`；`printf` 输出 `double` 用 `%f` 即可（自动提升）

---

### scanf 读取字符与字符串

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**`%c` 的问题**：会读取空白字符（包括换行符）

```c
char ch;
scanf("%d", &n);       // 输入 "42\n"
scanf("%c", &ch);      // ch = '\n'！不是等待新输入
```

**解决方法**：在 `%c` 前加空格，跳过空白

```c
scanf(" %c", &ch);     // 空格会跳过所有空白字符
```

**`%s` 的行为**：遇空白停止，自动加 `'\0'`

```c
char name[20];
scanf("%s", name);     // 输入 "Hello World"
// name = "Hello"，"World" 留在缓冲区
```

> **安全提示**：`scanf("%s", name)` 不检查长度，应改用 `scanf("%19s", name)` 或用 `fgets`

---

### scanf 的返回值与错误处理

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```c
int a, b;
int ret = scanf("%d%d", &a, &b);

if (ret == 2) {
    printf("成功读取: a=%d, b=%d\n", a, b);
} else if (ret == EOF) {
    printf("输入结束（Ctrl+D / Ctrl+Z）\n");
} else {
    printf("输入格式错误，仅成功读取 %d 项\n", ret);
    // 清除错误输入，防止死循环
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF)
        ;
}
```

**典型陷阱**：输入不匹配时，错误数据留在缓冲区，后续 `scanf` 反复失败

```
输入: abc
scanf("%d", &a)  → 返回 0，"abc" 留在缓冲区
scanf("%d", &a)  → 返回 0，"abc" 还在
...死循环
```

---

### scanf 的高级用法

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**1. 限制读取长度**

```c
char name[20];
scanf("%19s", name);      // 最多读19个字符，保留1位给 '\0'
```

**2. 扫描集 `%[]`**

```c
char str[100];
scanf("%[a-zA-Z]", str);     // 只读字母，遇非字母停止
scanf("%[^0-9]", str);        // 读到数字为止（^ 表示取反）
scanf("%[^\n]", str);         // 读整行（直到换行）
```

**3. 赋值抑制 `*`**

```c
int year, day;
scanf("%d%*c%d", &year, &day);  // %*c 读取但丢弃一个字符（如斜杠）
// 输入 "2024/15" → year=2024, day=15
```

---

## 字符串输入函数 gets 与 fgets

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**`gets`（已废弃，C11 移除）**：

```c
char line[100];
gets(line);     // 危险！不检查缓冲区长度，极易溢出
```

**`fgets`（推荐）**：

```c
char line[100];
fgets(line, sizeof(line), stdin);   // 最多读 sizeof(line)-1 个字符
```

- `fgets` 会把换行符也读入字符串（如果缓冲区放得下）
- 需要手动去除尾部换行符：

```c
fgets(line, sizeof(line), stdin);
size_t len = strlen(line);
if (len > 0 && line[len - 1] == '\n') {
    line[len - 1] = '\0';    // 去掉换行符
}
```

---

## 字符串格式化函数 sprintf / sscanf

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**`sprintf`**：将格式化数据写入字符串（而非 stdout）

```c
char buf[100];
int age = 20;
char name[] = "Alice";
sprintf(buf, "%s is %d years old.", name, age);
// buf = "Alice is 20 years old."
```

**`snprintf`**（安全版本，推荐）：

```c
char buf[10];
snprintf(buf, sizeof(buf), "Hello %s", "World");  // 自动截断，不会溢出
```

**`sscanf`**：从字符串中读取格式化数据

```c
char str[] = "2024-06-09";
int year, month, day;
sscanf(str, "%d-%d-%d", &year, &month, &day);
// year=2024, month=6, day=9
```

---

### sscanf 实用示例

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**解析 IP 地址**：

```c
char ip[] = "192.168.1.100";
int a, b, c, d;
sscanf(ip, "%d.%d.%d.%d", &a, &b, &c, &d);
printf("%d.%d.%d.%d\n", a, b, c, d);
```

**从字符串提取数值**：

```c
char info[] = "Score: 95, Rank: 3";
int score, rank;
sscanf(info, "Score: %d, Rank: %d", &score, &rank);
```

**分离整数和小数部分**：

```c
char num[] = "3.14159";
int integer;
double fraction;
sscanf(num, "%d.%lf", &integer, &fraction);
```

---

## 输入输出常见陷阱总结

<style scoped>
  li {
    font-size: 22px;
  }
</style>

| 陷阱 | 错误写法 | 正确写法 |
|:---|:---|:---|
| scanf 读 double 用 %f | `scanf("%f", &d)` | `scanf("%lf", &d)` |
| scanf %c 读到换行 | `scanf("%c", &ch)` | `scanf(" %c", &ch)` |
| gets 缓冲区溢出 | `gets(buf)` | `fgets(buf, sizeof(buf), stdin)` |
| scanf 不检查返回值 | `scanf("%d", &n)` | `if (scanf("%d", &n) != 1) { ... }` |
| 整数除法误用 | `double r = a / b` | `double r = (double)a / b` |
| printf %d 与 %f 混用 | `printf("%d", 3.14)` | `printf("%f", 3.14)` |
| scanf %s 不限长度 | `scanf("%s", buf)` | `scanf("%99s", buf)` |

---

## 综合练习

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**题目**：编写程序，输入学生姓名和三门课成绩，计算平均分并以表格形式输出

```c
#include <stdio.h>

int main(void) {
    char name[20];
    float s1, s2, s3;

    printf("请输入姓名：");
    scanf("%19s", name);
    printf("请输入三门课成绩（空格分隔）：");
    scanf("%f%f%f", &s1, &s2, &s3);

    float avg = (s1 + s2 + s3) / 3;

    printf("\n%-10s %6s %6s %6s %6s\n", "姓名", "课1", "课2", "课3", "平均");
    printf("%-10s %6.1f %6.1f %6.1f %6.2f\n", name, s1, s2, s3, avg);

    return 0;
}
```

---

## 本章小结

<style scoped>
  li {
    font-size: 22px;
  }
</style>

1. **字符 I/O**：`putchar`/`getchar`，注意 `getchar` 返回 `int` 和缓冲区特性
2. **printf**：格式控制符语法 `%[标志][宽度][.精度][长度]类型`
3. **scanf**：参数必须是地址（`&`），注意 `%lf` 读 double、`%c` 前加空格
4. **宽度与精度**：`%10d`、`%-10d`、`%010d`、`%.2f`、`%10.2f`
5. **安全输入**：用 `fgets` 替代 `gets`，用 `%99s` 限制 `scanf` 的 `%s` 长度
6. **字符串 I/O**：`sprintf`/`snprintf`（格式化写入字符串）、`sscanf`（从字符串读取）
7. **返回值**：`printf` 返回输出字符数，`scanf` 返回成功赋值项数

**下一章**：第4章 流程控制
