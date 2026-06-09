---
marp: true
theme: gaia
title: C语言程序设计 - 第1章 概论
paginate: true
math: katex
---

<!-- _class: lead -->

# 第1章 概论

**C语言程序设计**

---

## 本章内容

- C语言的发展历史
- C语言的特点
- 简单C程序介绍
- C程序的开发过程
- 常用开发环境

---

## C语言的诞生

<style scoped>
  li {
    font-size: 24px;
  }
</style>

- 1969年，Ken Thompson 在 PDP-7 上用汇编语言写出了 **Unix** 的雏形
- 1970年，Dennis Ritchie 加入 Bell Labs，与 Thompson 合作开发 Unix
- 汇编语言可移植性差——换个硬件就得重写，于是需要一种**高级语言**
- 1972年，Ritchie 在 **B语言**（Ken Thompson 设计）基础上开发了 **C语言**
- C语言最初的目的：**用高级语言重写 Unix，使其可移植**

> "C is quirky, flawed, and an enormous success." — Dennis Ritchie

---

## C语言标准演进

<style scoped>
  table {
    font-size: 22px;
  }
</style>

| 年份 | 标准 | 别名 | 关键特性 |
|:---:|:---|:---|:---|
| 1978 | K&R | K&R C | Brian Kernighan & Dennis Ritchie 合著《The C Programming Language》，事实标准 |
| 1989 | ANSI X3.159-1989 | **C89** / ANSI C | 第一个正式标准：函数原型、`const`、`void *`、`size_t` |
| 1990 | ISO/IEC 9899:1990 | **C90** | C89 的 ISO 版本，内容一致 |
| 1999 | ISO/IEC 9899:1999 | **C99** | `//` 注释、`long long`、`_Bool`、变长数组、`snprintf`、`<stdbool.h>` |
| 2011 | ISO/IEC 9899:2011 | **C11** | `_Generic`、`_Static_assert`、多线程支持、匿名结构体 |
| 2018 | ISO/IEC 9899:2018 | **C17** | C11 缺陷修正版，无新特性 |
| 2024 | ISO/IEC 9899:2024 | **C23** | `nullptr`、`constexpr`、`#embed`、十进制浮点、改进属性语法 |

---

### 为什么关注标准？

<style scoped>
  li {
    font-size: 24px;
  }
</style>

- 编译器对标准的支持程度不同
  - GCC 默认 `-std=gnu17`（C17 + GNU 扩展）
  - MSVC 长期停留在 C89/C90，近年才逐步支持 C11
  - Clang 紧跟 GCC
- 本课程以 **C99/C11** 为基准
- 编译时可指定标准：`gcc -std=c99`、`gcc -std=c11`

---

## C语言的特点

<style scoped>
  li {
    font-size: 24px;
  }
</style>

| 优点 | 说明 |
|:---|:---|
| **简洁高效** | 关键字仅 32 个（C89），语法紧凑 |
| **底层访问** | 可直接操作内存（指针）、位运算、内联汇编 |
| **可移植** | 同一源码经重新编译可在不同平台运行 |
| **结构化** | 函数 + 作用域支持模块化设计 |
| **运行快** | 编译为原生机器码，接近手写汇编的性能 |

| 缺点 | 说明 |
|:---|:---|
| **内存安全** | 无自动边界检查，越界访问导致未定义行为 |
| **手动管理** | `malloc`/`free` 需程序员配对，泄漏/双重释放常见 |
| **类型弱** | 允许隐式转换，某些不安全操作只给警告 |

---

### C语言的应用领域

<style scoped>
  li {
    font-size: 22px;
  }
</style>

- **操作系统**：Linux 内核、Windows 内核（部分）、macOS（XNU）
- **嵌入式系统**：单片机、IoT 固件、RTOS
- **数据库**：MySQL、PostgreSQL、SQLite
- **语言运行时**：CPython、CPython 解释器、Lua VM
- **图形/游戏**：SDL、OpenGL、Unreal Engine（底层）
- **网络/安全**：OpenSSL、nginx、curl
- **科学计算**：很多数值库（BLAS/LAPACK）的 C 接口

> "C is the lingua franca of systems programming."

---

## 简单C程序介绍

```c
#include <stdio.h>          // 预处理指令：包含标准 I/O 头文件

int main(void) {             // 主函数：程序入口
    printf("Hello, World!\n"); // 库函数调用：输出字符串
    return 0;                  // 返回值 0 表示正常结束
}
```

- `#include <stdio.h>` — 预处理，将 `stdio.h` 的声明引入
- `int main(void)` — 标准定义，返回 `int`，参数 `void` 表示不接受命令行参数
- `printf` — 格式化输出函数，声明在 `stdio.h` 中
- `return 0` — 向操作系统报告退出状态，0 = 成功

---

### 程序结构解析

<style scoped>
  li {
    font-size: 22px;
  }
</style>

```
┌─────────────────────────────────────┐
│  预处理指令区                         │
│  #include <stdio.h>                  │
│  #define PI 3.14159                  │
├─────────────────────────────────────┤
│  全局声明区                           │
│  int global_var;                     │
├─────────────────────────────────────┤
│  函数定义区                           │
│  int main(void) {                    │
│      局部变量声明;                    │
│      执行语句;                        │
│      return 0;                       │
│  }                                   │
│  int add(int a, int b) { ... }      │
└─────────────────────────────────────┘
```

- 一个 C 程序**有且仅有一个** `main` 函数
- 函数由**函数头**（返回类型 + 函数名 + 参数表）和**函数体**（`{}` 包围的语句块）组成
- 语句以分号 `;` 结尾

---

### 带输入的程序

```c
#include <stdio.h>

int main(void) {
    int a, b, sum;

    printf("请输入两个整数：");
    scanf("%d%d", &a, &b);

    sum = a + b;
    printf("%d + %d = %d\n", a, b, sum);

    return 0;
}
```

- `scanf("%d%d", &a, &b)` — 从标准输入读两个整数，`&` 取地址
- `%d` — 格式控制符，表示十进制整数
- 运行示例：输入 `3 5`，输出 `3 + 5 = 8`

---

### 带自定义函数的程序

```c
#include <stdio.h>

int max(int a, int b) {        // 自定义函数：返回较大值
    return a > b ? a : b;
}

int main(void) {
    int x, y;

    printf("请输入两个整数：");
    scanf("%d%d", &x, &y);
    printf("较大者为 %d\n", max(x, y));

    return 0;
}
```

- 函数**先声明/定义，后调用**
- `a > b ? a : b` — 条件运算符（三目运算符）

---

## C程序的开发过程

<style scoped>
  p {
    text-align: center;
    font-size: 20px;
  }
</style>

```
  源文件(.c) ──→ [预处理] ──→ 展开后的源码 ──→ [编译] ──→ 汇编代码(.s) ──→ [汇编] ──→ 目标文件(.o) ──→ [链接] ──→ 可执行文件
                  cpp               cc1                 as                   ld               a.out / .exe
```

| 阶段 | 工具 | 输入 | 输出 | 做什么 |
|:---:|:---|:---|:---|:---|
| 预处理 | cpp | `.c` | `.i` | 展开 `#include`、`#define`，条件编译 |
| 编译 | cc1 | `.i` | `.s` | 词法/语法分析→中间码→汇编 |
| 汇编 | as | `.s` | `.o` | 汇编指令→机器码 |
| 链接 | ld | `.o` + 库 | `a.out` | 符号解析、地址重定位 |

---

### 一步编译 vs 分步编译

<style scoped>
  li {
    font-size: 22px;
  }
</style>

**一步到位**（最常用）：

```bash
gcc -o hello hello.c
```

**分步观察**（调试时有用）：

```bash
gcc -E hello.c -o hello.i    # 只预处理
gcc -S hello.i -o hello.s    # 只编译到汇编
gcc -c hello.s -o hello.o    # 只汇编
gcc    hello.o -o hello      # 只链接
```

- `-E` / `-S` / `-c` 分别停在预处理、编译、汇编阶段
- 不加 `-o` 则默认输出 `a.out`

---

### 常用 GCC 编译选项

<style scoped>
  table {
    font-size: 22px;
  }
</style>

| 选项 | 作用 |
|:---|:---|
| `-Wall` | 开启常用警告 |
| `-Wextra` | 额外警告 |
| `-Werror` | 警告视为错误 |
| `-std=c99` / `-std=c11` | 指定语言标准 |
| `-O0` / `-O1` / `-O2` / `-O3` | 优化等级 |
| `-g` | 生成调试信息（供 GDB 使用） |
| `-I path` | 添加头文件搜索路径 |
| `-L path` | 添加库搜索路径 |
| `-lm` | 链接数学库 `libm` |

推荐日常编译：

```bash
gcc -Wall -Wextra -std=c11 -g -o hello hello.c
```

---

## 常用开发环境

<style scoped>
  li {
    font-size: 24px;
  }
</style>

### 命令行 + 编辑器

- **GCC** (GNU Compiler Collection) — Linux/macOS 默认编译器
- **Clang** — macOS 默认，错误提示更友好
- **编辑器**：VS Code + C/C++ 扩展、Vim、Emacs

### 集成开发环境 (IDE)

- **Visual Studio** — Windows 上最强大，内置 MSVC 编译器
- **Code::Blocks** — 跨平台、轻量、自带 GCC
- **Dev-C++** — 简单易上手（教学常用，但已较旧）
- **CLion** — JetBrains 出品，CMake 项目支持好

---

### VS Code + GCC 配置要点

<style scoped>
  li {
    font-size: 22px;
  }
</style>

1. 安装 VS Code
2. 安装扩展：`C/C++`（Microsoft）、`Code Runner`
3. 安装编译器
   - Windows：安装 MinGW-w64 或 WSL
   - macOS：`xcode-select --install`
   - Linux：`sudo apt install gcc`
4. 验证：终端输入 `gcc --version`

```json
// .vscode/tasks.json 编译任务示例
{
    "version": "2.0.0",
    "tasks": [{
        "label": "build",
        "type": "shell",
        "command": "gcc",
        "args": ["-Wall", "-std=c11", "-g", "-o", "${fileDirname}/${fileBasenameNoExtension}", "${file}"]
    }]
}
```

---

## 编码规范入门

<style scoped>
  li {
    font-size: 24px;
  }
</style>

良好的编码习惯从第一天开始：

- **缩进**：统一 4 空格或 1 个 Tab（不要混用）
- **命名**：变量用小写+下划线 `student_count`，常量全大写 `MAX_SIZE`
- **花括号**：K&R 风格（开括号跟在同行）或 Allman 风格（开括号独占一行），**保持一致**
- **注释**：
  - `//` 单行注释（C99 起）
  - `/* ... */` 多行注释
- **一行一条语句**，避免 `a=1; b=2;` 挤在一行
- **先声明后使用**

> 代码是写给人看的，顺便让机器执行。

---

## 本章小结

<style scoped>
  li {
    font-size: 24px;
  }
</style>

1. C 语言诞生于 1972 年，为 Unix 而生，是系统编程的基石
2. 标准从 K&R → C89 → C99 → C11 → C23 不断演进
3. C 的核心优势：**高效、底层访问、可移植**
4. C 程序 = 预处理指令 + 全局声明 + 函数定义，`main` 是唯一入口
5. 编译四阶段：预处理 → 编译 → 汇编 → 链接
6. 推荐使用 GCC + VS Code，编译时加上 `-Wall -std=c11 -g`
7. 从第一天就养成良好编码习惯

**下一章**：第2章 基本元素——数据类型、常量变量、运算符和表达式
