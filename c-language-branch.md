---
marp: true
theme: gaia
title: C语言程序设计 - 第4章 流程控制
paginate: true
math: katex
---

<!-- _class: lead -->

# 第4章 流程控制

**C语言程序设计**

---

## 本章内容

- 程序的三种基本结构
- 条件语句（if、switch）
- 循环语句（while、do-while、for）
- 转移语句（break、continue、goto）
- 流程控制应用实例
- 程序调试技巧

---

## 程序的三种基本结构

<style scoped>
  li {
    font-size: 24px;
  }
</style>

任何程序都可以由三种基本结构组合而成：

1. **顺序结构**：语句按先后顺序依次执行
2. **选择结构**：根据条件选择执行路径
3. **循环结构**：重复执行某段代码

**结构化程序设计**的核心思想：
- 每个结构只有**一个入口**和**一个出口**
- 不使用 `goto` 跳转
- 自顶向下，逐步求精

> 1966年，Böhm 和 Jacopini 证明了：任何算法都可以用这三种结构表示。

---

## if 语句

### 单分支 if

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**语法**：

```c
if (条件表达式) {
    语句块;
}
```

**示例**：判断成绩是否及格

```c
if (score >= 60) {
    printf("及格\n");
}
```

**注意**：
- 条件表达式为**非 0** 时执行（不局限于 `true`/`1`）
- 即使只有一条语句，也建议用花括号——防止后续添加语句时遗忘

---

### 双分支 if-else

**语法**：

```c
if (条件表达式) {
    语句块1;
} else {
    语句块2;
}
```

**示例**：判断奇偶

```c
if (num % 2 == 0) {
    printf("%d 是偶数\n", num);
} else {
    printf("%d 是奇数\n", num);
}
```

---

### 多分支 if-else if-else

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**语法**：

```c
if (条件1) {
    语句块1;
} else if (条件2) {
    语句块2;
} else if (条件3) {
    语句块3;
} else {
    语句块n;
}
```

**示例**：成绩等级

```c
if (score >= 90) {
    printf("优秀\n");
} else if (score >= 80) {
    printf("良好\n");
} else if (score >= 70) {
    printf("中等\n");
} else if (score >= 60) {
    printf("及格\n");
} else {
    printf("不及格\n");
}
```

---

### if 的嵌套与悬空 else

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**悬空 else 问题**（Dangling Else）：

```c
// 缩进具有误导性
if (a > 0)
    if (b > 0)
        printf("both positive\n");
    else
        printf("a <= 0\n");    // 这行实际上属于内层 if！
```

**C 语言规则**：`else` 与**最近的未匹配的** `if` 配对

**正确写法**：用花括号明确意图

```c
if (a > 0) {
    if (b > 0) {
        printf("both positive\n");
    }
} else {
    printf("a <= 0\n");       // 现在属于外层 if
}
```

> **经验法则**：嵌套 if 时，**始终使用花括号**。

---

## switch 语句

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**语法**：

```c
switch (表达式) {           // 表达式必须是整型（含 char）
    case 常量表达式1:
        语句1;
        break;              // 跳出 switch
    case 常量表达式2:
        语句2;
        break;
    // ...
    default:                // 所有 case 都不匹配时执行
        语句n;
        break;
}
```

**示例**：根据运算符执行运算

```c
switch (op) {
    case '+': result = a + b; break;
    case '-': result = a - b; break;
    case '*': result = a * b; break;
    case '/': result = a / b; break;
    default:  printf("不支持的运算符\n"); break;
}
```

---

### switch 的穿透特性（Fall-through）

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**没有 `break` 时，执行会"穿透"到下一个 case**：

```c
switch (month) {
    case 1: case 3: case 5: case 7:
    case 8: case 10: case 12:
        days = 31; break;
    case 4: case 6: case 9: case 11:
        days = 30; break;
    case 2:
        days = is_leap ? 29 : 28; break;
}
```

**反面教材**——忘记 break 导致 bug：

```c
switch (grade) {
    case 'A': printf("优秀\n");    // 忘记 break！
    case 'B': printf("良好\n");    // 会穿透到这里
    case 'C': printf("及格\n");    // 还会穿透到这里
}
// 输入 'A' 会输出三行，而不是一行
```

> **规则**：每个 case 末尾必须有 `break`，除非有意利用穿透。

---

### switch vs if-else

<style scoped>
  table {
    font-size: 22px;
  }
</style>

| 特性 | switch | if-else |
|:---|:---|:---|
| 条件类型 | 整型/字符型常量 | 任意表达式 |
| 范围判断 | 不支持（如 `60 <= x < 90`） | 支持 |
| 浮点判断 | 不支持 | 支持 |
| 执行效率 | 跳转表，O(1) 查找 | 逐条判断，O(n) |
| 可读性 | 多值分支清晰 | 复杂逻辑更灵活 |

**选择原则**：
- 对离散值做等值判断 → `switch`
- 范围判断、浮点比较、复杂条件 → `if-else`

---

## while 循环

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**语法**：

```c
while (条件表达式) {
    循环体;
}
```

- **先判断，后执行**：条件为真则执行循环体，否则跳过
- 循环体可能**一次也不执行**

**示例**：计算 1+2+...+100

```c
int sum = 0, i = 1;
while (i <= 100) {
    sum += i;
    i++;
}
printf("sum = %d\n", sum);   // 5050
```

---

## do-while 循环

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**语法**：

```c
do {
    循环体;
} while (条件表达式);    // 注意末尾的分号！
```

- **先执行，后判断**：循环体至少执行一次
- 适合"先做一次再判断"的场景

**示例**：反复输入直到合法

```c
int n;
do {
    printf("请输入一个正整数：");
    scanf("%d", &n);
} while (n <= 0);    // 输入非正数则重新输入
```

---

## for 循环

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**语法**：

```c
for (初始化; 条件; 更新) {
    循环体;
}
```

**执行流程**：

```
初始化 → 判断条件 → [真] → 循环体 → 更新 → 判断条件 → ...
                  → [假] → 退出
```

**等价的 while 形式**：

```c
初始化;
while (条件) {
    循环体;
    更新;
}
```

**示例**：

```c
for (int i = 0; i < 10; i++) {
    printf("%d ", i);    // 输出 0 1 2 ... 9
}
```

---

### for 循环的灵活性

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**三个部分都可以省略**（但分号不能省）：

```c
// 省略初始化
int i = 0;
for (; i < 10; i++) { ... }

// 省略条件（死循环）
for (int i = 0; ; i++) {
    if (i >= 10) break;
}

// 省略更新
for (int i = 0; i < 10; ) {
    printf("%d ", i++);
}

// 全部省略（死循环）
for (;;) { ... }    // 等价于 while (1) { ... }
```

**C99 允许在初始化中声明变量**（推荐写法）：

```c
for (int i = 0; i < n; i++) {
    // i 的作用域仅限于 for 循环
}
```

---

### 三种循环的选择

| 循环类型 | 特点 | 适用场景 |
|:---|:---|:---|
| `while` | 先判断后执行 | 循环次数不确定 |
| `do-while` | 先执行后判断 | 至少执行一次 |
| `for` | 初始化/条件/更新一体化 | 循环次数确定 |

> 实际上三种循环可以互相转换，`for` 最常用，`while` 次之，`do-while` 较少。

---

## break 语句

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**作用**：跳出当前**最近一层**的 `switch` 或循环

```c
// 判断素数
int is_prime = 1;
for (int i = 2; i * i <= n; i++) {
    if (n % i == 0) {
        is_prime = 0;
        break;       // 发现因子，提前退出
    }
}
```

**注意**：`break` 只跳出**一层**循环

```c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        if (condition) {
            break;    // 只跳出内层循环，外层继续
        }
    }
}
```

---

## continue 语句

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**作用**：跳过本次循环的剩余语句，直接进入**下一次**循环

```c
// 输出 1~100 中所有不是 3 的倍数的数
for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0) {
        continue;     // 跳过 3 的倍数
    }
    printf("%d ", i);
}
```

**`continue` 在三种循环中的行为**：

| 循环 | `continue` 跳转到 |
|:---|:---|
| `while` | 条件判断 |
| `do-while` | 条件判断 |
| `for` | 更新表达式（然后条件判断） |

> `for` 中的 `continue` 会执行更新表达式，`while` 中的 `continue` 不会——可能导致死循环！

---

### continue 导致 while 死循环的陷阱

```c
int i = 0;
while (i < 10) {
    if (i == 5) {
        continue;    // i 永远是 5，条件永远为真 → 死循环！
    }
    i++;
}
```

**修正**：把更新放在 `continue` 之前

```c
int i = 0;
while (i < 10) {
    i++;            // 先更新
    if (i == 5) {
        continue;   // 现在安全了
    }
    printf("%d ", i);
}
```

---

## goto 语句

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**语法**：

```c
goto 标签名;
// ...
标签名: 语句;
```

**合理使用场景**——跳出多层嵌套循环：

```c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        if (found) {
            goto done;    // 直接跳出两层循环
        }
    }
}
done:
    printf("搜索结束\n");
```

**不推荐使用的原因**：
- 破坏结构化程序的单入口/单出口原则
- 导致代码流程难以追踪（"意大利面条"代码）
- **规则**：仅用于跳出多层循环，绝不向前跳转

> Linus Torvalds："I think goto's are fine, and they are often more readable than large amounts of indentation."

---

## 经典算法实例

### 1. 九九乘法表

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```c
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= i; j++) {
        printf("%d×%d=%-4d", j, i, i * j);
    }
    printf("\n");
}
```

输出：

```
1×1=1
1×2=2   2×2=4
1×3=3   2×3=6   3×3=9
...
1×9=9   2×9=18  3×9=27  ...  9×9=81
```

---

### 2. 判断素数

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```c
#include <stdio.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int main(void) {
    for (int i = 2; i <= 100; i++) {
        if (is_prime(i)) {
            printf("%d ", i);
        }
    }
    return 0;
}
```

优化：只检查到 $\sqrt{n}$，跳过偶数

---

### 3. 最大公约数（辗转相除法）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**算法**（欧几里得算法）：

```
gcd(a, b) = gcd(b, a % b)，直到 a % b == 0
```

```c
int gcd(int a, int b) {
    while (b != 0) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

// 递归版本
int gcd_rec(int a, int b) {
    return b == 0 ? a : gcd_rec(b, a % b);
}
```

示例：`gcd(48, 18)` → `gcd(18, 12)` → `gcd(12, 6)` → `gcd(6, 0)` → `6`

---

### 4. 猜数字游戏

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand((unsigned)time(NULL));    // 设置随机种子
    int target = rand() % 100 + 1;  // 1~100 的随机数
    int guess, attempts = 0;

    printf("猜一个 1~100 之间的数字\n");
    do {
        printf("你的猜测：");
        scanf("%d", &guess);
        attempts++;

        if (guess > target) {
            printf("太大了！\n");
        } else if (guess < target) {
            printf("太小了！\n");
        } else {
            printf("恭喜！%d 次猜中！\n", attempts);
        }
    } while (guess != target);

    return 0;
}
```

---

### 5. 斐波那契数列

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**定义**：$F(1)=1, F(2)=1, F(n)=F(n-1)+F(n-2)$

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("输入 n：");
    scanf("%d", &n);

    long long a = 1, b = 1;
    printf("前 %d 项：", n);
    for (int i = 1; i <= n; i++) {
        printf("%lld ", a);
        long long next = a + b;
        a = b;
        b = next;
    }
    printf("\n");

    return 0;
}
```

输出（n=10）：`1 1 2 3 5 8 13 21 34 55`

> 注意：`int` 只能存到第 46 项左右，更大需用 `long long`

---

### 6. 穷举法：百钱买百鸡

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**问题**：公鸡 5 元/只，母鸡 3 元/只，小鸡 1 元/3 只，100 元买 100 只，各有几只？

```c
// x: 公鸡, y: 母鸡, z: 小鸡
for (int x = 0; x <= 20; x++) {         // 最多 20 只公鸡
    for (int y = 0; y <= 33; y++) {     // 最多 33 只母鸡
        int z = 100 - x - y;            // 总数 100
        if (z % 3 == 0 &&               // 小鸡必须是 3 的倍数
            5 * x + 3 * y + z / 3 == 100) {  // 总价 100
            printf("公鸡%d只，母鸡%d只，小鸡%d只\n", x, y, z);
        }
    }
}
```

穷举法：枚举所有可能，筛选满足条件的解

---

## 程序调试技巧

### 1. 打印调试法（printf Debugging）

<style scoped>
  li {
    font-size: 22px;
  }
</style>

最基本也最常用的方法——在关键位置插入 `printf`

```c
for (int i = 0; i < n; i++) {
    printf("[DEBUG] i=%d, arr[i]=%d, sum=%d\n", i, arr[i], sum);
    sum += arr[i];
}
```

**技巧**：
- 用 `fprintf(stderr, ...)` 输出到标准错误流，不会被重定向干扰
- 用 `__FILE__`、`__LINE__`、`__func__` 宏标记位置：

```c
fprintf(stderr, "%s:%d [%s] x=%d\n", __FILE__, __LINE__, __func__, x);
```

---

### 2. 断言（assert）

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```c
#include <assert.h>

double safe_sqrt(double x) {
    assert(x >= 0);    // 若 x < 0，程序终止并打印错误信息
    return sqrt(x);
}
```

- 条件为假时，程序**中止**并打印：文件名、行号、条件表达式
- 在 `#include <assert.h>` 之前定义 `NDEBUG` 可**禁用所有断言**：

```c
#define NDEBUG
#include <assert.h>    // 所有 assert 变为空操作
```

- **用于开发阶段**检查不变量，不要用 assert 处理运行时错误

---

### 3. GDB 基础

<style scoped>
  li {
    font-size: 22px;
  }
</style>

编译时加 `-g` 生成调试信息：`gcc -g -o prog prog.c`

| 命令 | 作用 |
|:---|:---|
| `gdb ./prog` | 启动调试 |
| `run` / `run arg1 arg2` | 运行程序 |
| `break main` / `break prog.c:20` | 设置断点 |
| `next`（`n`） | 单步执行（不进入函数） |
| `step`（`s`） | 单步执行（进入函数） |
| `print x` | 查看变量值 |
| `continue`（`c`） | 继续运行到下一个断点 |
| `backtrace`（`bt`） | 查看调用栈 |
| `quit` | 退出 GDB |

---

### 4. 常见错误类型

<style scoped>
  li {
    font-size: 22px;
  }
</style>

| 错误类型 | 示例 | 排查方法 |
|:---|:---|:---|
| 语法错误 | 漏分号、括号不匹配 | 编译器报错，逐行检查 |
| 逻辑错误 | 条件写反、差一错误 | 打印中间值、手动模拟 |
| 越界访问 | `arr[10]` 但数组只有 10 个元素 | GDB 观察、AddressSanitizer |
| 死循环 | 忘记更新循环变量 | GDB 中 Ctrl+C 查看位置 |
| 未初始化变量 | 局部变量未赋值 | 编译警告 `-Wall`、Valgrind |
| 整数溢出 | `int` 乘法结果超出范围 | 用更大类型或检查边界 |

**编译选项推荐**：

```bash
gcc -Wall -Wextra -std=c11 -g -fsanitize=address -o prog prog.c
```

`-fsanitize=address`：运行时检测数组越界和内存泄漏

---

## 本章小结

<style scoped>
  li {
    font-size: 22px;
  }
</style>

1. **三种基本结构**：顺序、选择、循环——结构化编程的基石
2. **if-else**：注意悬空 else，始终使用花括号
3. **switch**：整型/字符型等值判断，必须加 `break`（除非有意穿透）
4. **三种循环**：`while`（先判断）、`do-while`（先执行）、`for`（最常用）
5. **break** 跳出最近一层循环/switch，**continue** 跳过本次循环
6. **goto**：仅用于跳出多层循环，绝不向前跳转
7. **经典算法**：九九表、素数、GCD、斐波那契、穷举
8. **调试**：printf、assert、GDB、AddressSanitizer

**下一章**：第5章 函数
