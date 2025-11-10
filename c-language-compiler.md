---
marp: true
theme: gaia
title: 软件技术基础
# size: 4:3
math: katex
---

<!-- _class: lead -->

# 软件技术基础

## 编译预处理

**施展**
武汉光电国家研究中心 & 计算机学院
华中科技大学

---

## 本章重点

- 宏定义 `#define`
  - 无参宏定义
  - 带参宏定义 ✅
- 条件编译

---

## 基本概念

![w:1100](images/macro_in_compiling.svg)

**编译预处理**：对源程序进行编译之前所作的工作，它由预处理程序负责完成。编译时，系统将自动引用预处理程序对源程序中的预处理指令进行处理。

**预处理指令**：以"#"号开始的指令。

---

## 文件包含 `#include`

用指定文件的内容取代该预处理指令行，有2种一般形式：

### (1) `#include <文件名>`

在指定的标准目录下寻找被包含文件

### (2) `#include "文件名"`

首先在用户当前目录中寻找被包含文件，若找不到，再在指定的标准目录下寻找

---

## 宏定义 `#define`

用一个标识符来表示一个字符串

```c
#define 标识符 字符串
```

**宏名**：被定义的标识符。

**宏代换（宏展开）**：在编译预处理时，用字符串去取代宏名。

---

## 宏展开示例

<style scoped>
.columns {
  display: grid;
  grid-template-columns: 1fr 1fr; /* 创建两等宽的栏 */
  gap: 2rem; /* 设置两栏之间的间距 */
}
</style>

<div class="columns">

<div>

### 预处理前

```c
#define M (y*y+3*y)
void main(void)
{
    int s,y;
    printf("Input a number: ");
    scanf("%d",&y);
    s=3*M+4*M+y*M;
    printf("s=%d\n",s);
}
```

</div>

<div>

### 预处理后

```c
void main(void)
{
    int s,y;
    printf("Input a number: ");
    scanf("%d",&y);
    s=3*(y*y+3*y)+4*(y*y+3*y)+y*(y*y+3*y);
    printf("s=%d\n",s);
}
```

</div>

</div>

---

## 带参数的宏定义

```c
#define 标识符(标识符，标识符，…，标识符) 字符串
```

**宏调用**：给出实参

**宏展开**：

1. 用字符串替换宏
2. 用实参去替换形参

---

## 带参宏示例

```c
#define SQ(x) ((x)*(x))
```

**宏调用**：`SQ(a+1)`
**宏展开**：`((a+1) * (a+1))`

**宏调用**：`SQ(SQ(a))`
**宏展开**：`((((a)*(a))) * (((a)*(a))))`

---

## 为什么要这么多的括号？

### 错误示例1

```c
#define SQ(x) x*x
SQ(a+b)  // 展开为: a+b*a+b
```

### 错误示例2

```c
#define SQ(x) (x)*(x)
27/SQ(3)  // 展开为: 27/(3)*(3)
```

**正确做法**：表达式中的**每个参数用括号**括起来，**整个表达式也用括号**括起来。

---

## 注意：宏名和左括号之间不能有空格

```c
#define SQ (x) ((x)*(x))  // 错误！被认为是无参宏定义
```

或者说：**宏名之内不允许包含空格**

**宏调用**：`SQ(3)`  
**宏展开**：`(x) ((x)*(x)) (3)` // 显然错误的

---

## 宏的特点

- **优点**：节省函数调用的开销，程序运行速度更快，形式参数不分配内存单元，不必作类型说明
- **缺点**：宏展开后使源程序增长
- **适用场景**：经常使用的简短表达式，以及小的可重复的代码段
- **不适用场景**：任务复杂需要多行代码，或要求程序越小越好时，应该使用函数

简单来说，宏是"**即将成为代码的字符串**"

---

## 取消宏定义 `#undef`

终止宏名的作用域，形式为：

```c
#undef 标识符
```

效果：

```c
#define 标识符

…只有这一部分代码可以展开"标识符"…

#undef 标识符

…"标识符"于此处无效…
```

---

### 使用场景1：防止宏名冲突

```c
#include "everything.h"
#undef SIZE      // 取消everything.h中定义的SIZE
#define SIZE 100 // 重新定义
```

### 使用场景2：保证调用实际函数

```c
#undef getchar
int getchar(void) {…}
```

---

## 条件编译

预处理程序提供了条件编译指令，用于在预处理中进行条件控制，根据所求条件的值有选择地包含不同的程序部分，因而产生不同的目标代码。

**三种形式**：`#if`、`#ifdef`、`#ifndef`

注意几种形式的区别：

- `#if`：条件编译指令，用于在预处理时判断条件，并决定是否包含或取消包含指定代码。
- `#ifdef`：条件编译指令，用于在预处理时判断某个标识符是否被定义，并决定是否包含或取消包含指定代码。

<!-- 后面例程之中，如果还有三角形计算，应该怎么改？ -->

---

## 条件编译示例：计算圆形面积

<style scoped>
    h3 {
        font-size: 27px;
    }
.columns {
  display: grid;
  grid-template-columns: 1fr 1fr; /* 创建两等宽的栏 */
  gap: 2rem; /* 设置两栏之间的间距 */
}
</style>

<div class="columns">

<div>

### 预处理前（定义R）

```c
#define R
int main(void)
{
    float r, s;
    printf("input a number: ");
    scanf("%f", &r);
#ifdef R
    s = 3.14159 * r * r;
    printf("%f\n", s);
#else
    s = r * r;
    printf("%f\n", s);
#endif
    return 0;
}
```

</div>

<div>

### 预处理后（圆形）

```c
int main(void)
{
    float r, s;
    printf("input a number: ");
    scanf("%f ", &r);
    s = 3.14159 * r * r;
    printf("%f\n", s);
    return 0;
}
```

生成计算圆面积的目标程序

</div>

</div>

---

## 条件编译示例：计算方形面积

<style scoped>
    h3 {
        font-size: 27px;
    }
.columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}
</style>

<div class="columns">

<div>

### 预处理前（未定义R）

```c
//#define R
int main(void)
{
    float r, s;
    printf("input a number: ");
    scanf("%f", &r);
#ifdef R
    s = 3.14159 * r * r;
    printf("%f\n", s);
#else
    s = r * r;
    printf("%f\n", s);
#endif
    return 0;
}
```

</div>

<div>

### 预处理后（方形）

```c
//#define R
void main(void)
{
    float r, s;
    printf("input a number: ");
    scanf("%f", &r);
    s = r * r;
    printf("%f\n", s);
    return 0;
}
```

生成计算方形面积的目标程序

</div>

</div>

---

## 条件编译应用：调试程序

### 临时忽略代码

```c
#if 0
  …… // 不编译的代码
#endif
```

### 调试跟踪

```c
#define DEBUG  // 完成调试后，去掉该指令

#ifdef DEBUG
    printf("x=%d\n", x);
#endif

#ifdef DEBUG
    printf("y=%d\n", y);
#endif
```

---

## 条件编译应用：assert宏

在头文件`assert.h`中，测试表达式的值是否符合要求：

```c
assert(e)
```

### 执行流程

如果`n < 0`，会输出包含行号和文件名的错误信息并中断执行：

```log
Assertion failed: n >= 0, file test.c, line 32
```

---

## assert宏与防御性编程

**防御性编程**：使用户在运行程序（发布版本里）时，当出现意外情况时程序仍能继续工作。

**断言的作用**：看作一种简单的制造栅栏的方法，这种栅栏能使错误在穿过自己时暴露。

---

### 断言流程图

![bg right h:1600](images/assert_flow.svg)

执行流程：

---

### 总结

- 宏定义用于代码复用和性能优化。
- 条件编译用于跨平台、调试和代码裁剪。
- 断言用于开发和调试阶段的错误检测。
