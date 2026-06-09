---
marp: true
theme: gaia
title: C语言程序设计 - 第5章 函数
paginate: true
math: katex
---

<!-- _class: lead -->

# 第5章 函数

**C语言程序设计**

---

## 本章内容

- 模块化程序设计
- 函数定义、声明与调用
- 参数传递机制
- 变量的存储类型
- 递归
- 多文件程序

---

## 5.1 模块化程序设计

<style scoped>
  li {
    font-size: 24px;
  }
</style>

将一个问题逐步细化分解为若干子问题，用函数实现子问题

**优点**：
- 程序编制方便，易于管理、修改和调试
- 增强可读性、可维护性、可扩充性
- 函数可公用，避免重复代码
- 提高软件可重用性

**自顶向下，逐步求精**：

```
解决问题 → 分解为子问题1, 子问题2, ... → 每个子问题用函数实现
```

> "One function, one task." — 每个函数只做一件事

---

### 蒙特卡罗模拟：猜数游戏

<style scoped>
  li {
    font-size: 24px;
  }
</style>

- **模拟算法**：模拟随机事件（抛硬币、掷骰子等）
- **随机数**：具有不确定性和偶然性
- **应用领域**：软件测试、加密系统、网络验证码
- **随机数发生器**：`int rand(void);`（在 `<stdlib.h>` 中）

---

### 主程序结构

```c
do {
    magic = GetNum();      // 产生随机数
    GuessNum(magic);       // 猜数
    printf("Play again? (Y/N) ");
    scanf(" %c", &cmd);
} while (cmd == 'y' || cmd == 'Y');
```

- `GetNum()` — 子任务：产生随机数
- `GuessNum()` — 子任务：猜数交互
- `main` 只负责**流程控制**，具体逻辑交给子函数

---

### 子任务：GetNum

```c
int GetNum(void) {
    int x;
    printf("A magic number between 1 and %d has been chosen.\n",
           MAX_NUMBER);
    x = rand();
    x = x % MAX_NUMBER + 1;
    return x;
}
```

- `rand()` 产生 $0$ ~ `RAND_MAX` 之间的伪随机整数
- `x % MAX_NUMBER + 1` 映射到 $1$ ~ `MAX_NUMBER`

---

### 完整程序

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX_NUMBER 100

int GetNum(void);
void GuessNum(int magic);

int main(void) {
    char command;
    int magic;
    srand((unsigned)time(NULL));     // 初始化随机种子
    do {
        magic = GetNum();
        GuessNum(magic);
        printf("Play again? (Y/N) ");
        scanf(" %c", &command);
    } while (command == 'y' || command == 'Y');
    return 0;
}
```

---

### 伪随机数算法

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**线性同余法**（最常用的伪随机数生成算法）：

$$a_0 = \text{seed}, \quad a_n = (A \cdot a_{n-1} + B) \bmod M, \quad n \geq 1$$

- 种子参数 `seed` 决定随机序列
- 初始化种子：`srand((unsigned)time(NULL));`
- `time(NULL)` 返回自 1970-01-01 以来的秒数
- 需包含头文件 `<time.h>`

> 不调用 `srand` 时，默认种子为 1——每次运行产生相同的序列

---

### 练习：蒙特卡罗法求圆周率

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**思路**：在单位正方形内随机投点，落在内切圆内的比例 ≈ $\pi/4$

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, hits = 0;
    printf("投点次数：");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        double x = (double)rand() / RAND_MAX;   // [0, 1)
        double y = (double)rand() / RAND_MAX;
        if (x * x + y * y <= 1.0) hits++;
    }
    printf("π ≈ %f\n", 4.0 * hits / n);
    return 0;
}
```

---

## 5.2 自定义函数

<style scoped>
  li {
    font-size: 24px;
  }
</style>

使用自定义函数的三个步骤：

1. **定义**函数：编写函数体
2. **声明**函数（原型）：告诉编译器函数的返回类型和参数
3. **调用**函数：执行函数

---

### 函数的定义

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**语法**：

```c
返回类型 函数名(参数列表) {
    声明部分;
    语句部分;
}
```

**示例**：

```c
int max(int x, int y) {     // 返回两个整数中的较大值
    return x > y ? x : y;
}
```

- 无参数：写 `void`，如 `int GetNum(void)`
- 无返回值：类型为 `void`，如 `void GuessNum(int magic)`
- `return` 执行后立即返回调用处

---

### 函数返回值

<style scoped>
  li {
    font-size: 24px;
  }
</style>

```c
return;           // void 函数中，提前返回
return 表达式;    // 有返回值的函数
```

- `void` 函数可以不写 `return`（函数体执行完自动返回）
- `return` 的表达式类型会自动转换为函数返回类型
- 一个函数可以有多个 `return`（但建议保持单一出口）

```c
int abs_val(int x) {
    if (x >= 0) return x;     // 两个 return
    return -x;
}
```

---

### 函数声明（函数原型）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**语法**：`返回类型 函数名(参数类型表);`

```c
int max(int x, int y);    // 完整原型
int max(int, int);         // 省略参数名（也可以）
```

**为什么要声明？**

```c
int main(void) {
    int result = max(3, 5);    // 此时编译器还不知道 max 的存在
    return 0;
}

int max(int x, int y) {         // 定义在 main 之后
    return x > y ? x : y;
}
// 编译报错：implicit declaration of function 'max'
```

**解决**：在调用之前给出声明（或把定义放在调用之前）

---

### 函数调用与参数传递

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**调用语法**：`函数名(实参列表);`

```c
putchar(c);                   // 库函数调用
c = getchar();
printf("%f", sqrt(x));        // 嵌套调用
GuessNum(GetNum());           // 函数作实参
```

**C 语言的参数传递——值传递（Pass by Value）**：

- 实参的**值**复制给形参
- 形参的改变**不影响**实参

```c
void swap_wrong(int a, int b) {
    int temp = a; a = b; b = temp;   // 只交换了副本！
}
```

**要在函数内修改实参，必须传地址**（指针，第8章详述）：

```c
void swap(int *a, int *b) {
    int temp = *a; *a = *b; *b = temp;   // 通过指针操作原变量
}
```

---

### 实参的求值顺序

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**C 语言未规定实参的求值顺序**——不同编译器可能不同

```c
int i = 3;
printf("%d %d\n", i++, i++);   // 未定义行为！
// 可能输出 "3 4" 或 "4 3"，取决于编译器
```

**规则**：不要在同一个函数调用中，对同一变量使用有副作用的表达式

**传地址调用**（提前预告）：

```c
int x;
scanf("%d", &x);   // 传递变量地址，scanf 通过地址修改 x
```

---

## 5.3 变量的存储类型

<style scoped>
  li {
    font-size: 24px;
  }
</style>

存储类型决定变量的：
- **作用域**：哪里可以访问
- **存储分配方式**：静态/动态
- **生命周期**：何时创建、何时销毁
- **初始化方式**：默认值

四个存储类别关键字：`auto`、`extern`、`static`、`register`

---

### 自动变量（auto）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

```c
auto int a;   // 等价于 int a;（auto 可省略）
```

| 属性 | 说明 |
|:---|:---|
| 作用域 | 定义所在的 `{}` 块内 |
| 存储方式 | 动态分配（栈上） |
| 生命周期 | 函数调用期间 |
| 默认值 | **未定义**（必须手动初始化） |

- 局部变量默认就是 `auto`
- 每次进入函数时重新创建，退出时销毁

---

### 外部变量（extern）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

```c
extern int seed;    // 引用性声明：告诉编译器 seed 在别处定义
int seed = 0;       // 定义性声明：分配内存并初始化
```

| 属性 | 说明 |
|:---|:---|
| 作用域 | 从定义处到文件尾（可用 `extern` 扩展到其他文件） |
| 存储方式 | 静态分配（数据段） |
| 生命周期 | 整个程序运行期间 |
| 默认值 | 0 |

**注意**：全局变量虽然方便，但应尽量少用——降低模块独立性

---

### 静态变量（static）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

```c
static int count = 0;    // 静态变量
```

**两种用法**：

| 用法 | 作用域 | 生命周期 | 含义 |
|:---|:---|:---|:---|
| 静态**局部**变量 | 函数内部 | 程序全程 | 函数结束后值**保留** |
| 静态**外部**变量 | 本文件内部 | 程序全程 | 限制其他文件访问 |

**示例**——统计函数调用次数：

```c
void counter(void) {
    static int count = 0;    // 只初始化一次
    count++;
    printf("called %d times\n", count);
}
```

---

### 寄存器变量（register）

<style scoped>
  li {
    font-size: 24px;
  }
</style>

```c
register int i;    // 建议编译器将变量存入寄存器
```

- 仅为**建议**，编译器可以忽略
- 不能对 `register` 变量取地址（`&i` 非法）
- 现代编译器自动优化寄存器分配，很少手动使用

---

### 存储类型对比

<style scoped>
  table {
    font-size: 20px;
  }
</style>

| 存储类型 | 关键字 | 作用域 | 生命周期 | 默认初值 | 存储位置 |
|:---|:---|:---|:---|:---|:---|
| 自动 | `auto` | 块内 | 函数调用期间 | 未定义 | 栈 |
| 外部 | `extern` | 文件内（可扩展） | 程序全程 | 0 | 数据段 |
| 静态局部 | `static` | 块内 | 程序全程 | 0 | 数据段 |
| 静态外部 | `static` | 本文件 | 程序全程 | 0 | 数据段 |
| 寄存器 | `register` | 块内 | 函数调用期间 | 未定义 | 寄存器/栈 |

---

## 5.4 递归

<style scoped>
  li {
    font-size: 24px;
  }
</style>

**递归**：函数直接或间接调用自身

**递归三要素**：
1. **递归条件**：什么情况下调用自身
2. **递归步骤**：每次调用规模**缩小**
3. **终止条件**：何时停止递归（必须有！）

```c
void prn_int(int n) {
    if (n > 0) {
        printf("%d ", n);
        prn_int(n - 1);      // 递归调用，规模缩小
    }
    printf("%d ", n);         // 回溯时输出
}
// prn_int(4) 输出: 4 3 2 1 0 1 2 3 4
```

---

### 递归法求 n!

<style scoped>
  li {
    font-size: 24px;
  }
</style>

$$n! = \begin{cases} 1 & n = 0 \text{ 或 } 1 \\ n \times (n-1)! & n \geq 2 \end{cases}$$

```c
long fact(int n) {
    if (n == 0 || n == 1)
        return 1;             // 终止条件
    else
        return n * fact(n - 1);  // 递归步骤
}
```

**执行过程**：`fact(4)`

```
fact(4) → 4 * fact(3) → 4 * 3 * fact(2) → 4 * 3 * 2 * fact(1)
→ 4 * 3 * 2 * 1 → 4 * 3 * 2 → 4 * 6 → 24
```

---

### 迭代实现

```c
long factorial_iter(int n) {
    long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
```

| 特性 | 递归 | 迭代 |
|:---|:---|:---|
| 代码简洁性 | ✅ 简洁 | 一般 |
| 运行效率 | ❌ 函数调用开销大 | ✅ 高效 |
| 内存占用 | ❌ 栈空间 O(n) | ✅ O(1) |
| 适用场景 | 递归数据结构、分治 | 简单循环 |

---

### 递归法求斐波那契数列

$$F(n) = \begin{cases} 1 & n = 1 \text{ 或 } 2 \\ F(n-1) + F(n-2) & n \geq 3 \end{cases}$$

**朴素递归**（大量重复计算，效率极低）：

```c
long long fibo(int n) {
    if (n == 1 || n == 2) return 1;
    return fibo(n - 1) + fibo(n - 2);   // fibo(5) 会重复计算 fibo(3) 两次
}
```

时间复杂度：$O(2^n)$——不可接受

---

### 优化1：记忆化搜索

<style scoped>
  li {
    font-size: 22px;
  }
</style>

用数组保存已计算的结果，避免重复计算：

```c
long long fibo_memo(int n) {
    static long long memo[100] = {0, 1, 1};   // static 只初始化一次
    if (memo[n] != 0) return memo[n];           // 已计算过，直接返回
    memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2);
    return memo[n];
}
```

时间复杂度：$O(n)$

---

### 优化2：迭代法

```c
long long fibo_iter(int n) {
    if (n <= 2) return 1;
    long long a = 1, b = 1, c;
    for (int i = 3; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

时间复杂度 $O(n)$，空间复杂度 $O(1)$——**最优方案**

---

### 优化3：尾递归

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**尾递归**：递归调用是函数的最后一步操作

```c
long long fibo_tail(int n, long long first, long long second) {
    if (n <= 1) return first;
    return fibo_tail(n - 1, second, first + second);
}

// 调用方式：fibo_tail(10, 1, 1)
```

- 部分编译器（如 GCC `-O2`）可对尾递归做**尾调用优化**（TCO）
- 优化后等价于迭代，不消耗额外栈空间
- 但 C 标准不保证 TCO，可移植性不如直接用迭代

---

### 汉诺塔问题

<style scoped>
  li {
    font-size: 24px;
  }
</style>

将 $n$ 个盘子从 A 借助 B 移到 C：
1. 每次只能移动一个盘子
2. 大盘不能放在小盘上

**递归策略**：
1. 将上面 $n-1$ 个盘子从 A → B（借助 C）
2. 将最下面的盘子从 A → C
3. 将 $n-1$ 个盘子从 B → C（借助 A）

```c
void hanoi(int n, char from, char via, char to) {
    if (n == 1) {
        printf("%c --> %c\n", from, to);
        return;
    }
    hanoi(n - 1, from, to, via);    // 步骤1
    printf("%c --> %c\n", from, to); // 步骤2
    hanoi(n - 1, via, from, to);    // 步骤3
}
```

---

### 汉诺塔执行示例（n=3）

```
hanoi(3, A, B, C)
  hanoi(2, A, C, B)
    hanoi(1, A, B, C)  → A --> C
    A --> B
    hanoi(1, C, A, B)  → C --> B
  A --> C
  hanoi(2, B, A, C)
    hanoi(1, B, C, A)  → B --> A
    B --> C
    hanoi(1, A, B, C)  → A --> C
```

移动次数：$2^n - 1$，即 $n=3$ 时需 7 步

---

### 字符串的递归处理

```c
int str_len(const char s[]) {
    if (s[0] == '\0') return 0;
    return 1 + str_len(s + 1);
}
```

**递归练习**：

1. **逆序输出整数**：`reverse(123)` → 输出 `321`

   ```c
   void reverse_print(int n) {
       if (n < 10) { printf("%d", n); return; }
       printf("%d", n % 10);
       reverse_print(n / 10);
   }
   ```

2. **判断回文字符串**：`is_palindrome("Level")` → 返回 `1`

   ```c
   bool is_palindrome(const char s[], int left, int right) {
       if (left >= right) return true;
       if (s[left] != s[right]) return false;
       return is_palindrome(s, left + 1, right - 1);
   }
   ```

---

### 整数分划问题

<style scoped>
  li {
    font-size: 22px;
  }
</style>

将正整数 $M$ 划分为一系列正整数之和（按字典序不增排列）

示例：$M=6$

```
6
5+1
4+2, 4+1+1
3+3, 3+2+1, 3+1+1+1
2+2+2, 2+2+1+1, 2+1+1+1+1
1+1+1+1+1+1
```

```c
void split(int n, int min, int a[], int cur) {
    if (n == 0) {
        // 输出 a[0] ~ a[cur-1]
        return;
    }
    for (int i = (n < min ? n : min); i >= 1; i--) {
        a[cur] = i;
        split(n - i, i, a, cur + 1);
    }
}
```

---

### 八皇后问题

<style scoped>
  li {
    font-size: 22px;
  }
</style>

在 $8 \times 8$ 棋盘上放置 8 个皇后，使其互不攻击

```c
#include <stdbool.h>

int queen[8];   // queen[i] = 第i行皇后所在的列

bool safe(int row, int col) {
    for (int i = 0; i < row; i++) {
        if (queen[i] == col ||
            queen[i] - i == col - row ||
            queen[i] + i == col + row)
            return false;
    }
    return true;
}

void solve(int row) {
    if (row == 8) { /* 输出一个解 */ return; }
    for (int col = 0; col < 8; col++) {
        if (safe(row, col)) {
            queen[row] = col;
            solve(row + 1);
        }
    }
}
```

---

## 5.5 多文件程序

<style scoped>
  li {
    font-size: 24px;
  }
</style>

大型程序通常拆分为多个源文件：

```
project/
├── main.c        // 主程序
├── utils.c       // 工具函数实现
├── utils.h       // 工具函数声明（头文件）
└── Makefile      // 构建脚本
```

**编译**：

```bash
gcc -Wall -std=c11 -o prog main.c utils.c
```

**头文件规范**：

```c
// utils.h
#ifndef UTILS_H       // 防止重复包含
#define UTILS_H

int max(int x, int y);
void swap(int *a, int *b);

#endif
```

---

## 本章小结

<style scoped>
  li {
    font-size: 22px;
  }
</style>

1. **模块化设计**：自顶向下，逐步求精，一个函数一个任务
2. **函数三步**：定义 → 声明（原型） → 调用
3. **参数传递**：C 语言只有**值传递**，要修改实参需传指针
4. **存储类型**：`auto`（栈）、`extern`（全局）、`static`（持久化/限制作用域）、`register`（建议寄存器）
5. **递归三要素**：递归条件、规模缩小、终止条件
6. **递归优化**：记忆化搜索、尾递归、迭代替代
7. **经典问题**：阶乘、斐波那契、汉诺塔、整数分划、八皇后
8. **多文件**：`.h` 声明 + `.c` 实现，用 `#ifndef` 防止重复包含

**下一章**：第6章 编译预处理
