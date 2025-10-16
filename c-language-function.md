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

## 本章内容

- 函数的概念和作用
- 函数的定义和调用
- 函数参数和返回值
- 变量的作用域和存储类别
- 递归函数
- 多文件程序组织

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 函数的概念和作用

- 函数是完成特定任务的独立代码块
- 提高代码的模块化程度
- 增强代码的可重用性
- 便于程序的调试和维护
- 有助于团队协作开发

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 函数的定义和调用

- 函数定义格式：
  ```
  返回值类型 函数名(参数列表) {
      函数体
      return 返回值;
  }
  ```
- 函数调用：
  - 无参函数：函数名();
  - 有参函数：函数名(实参列表);

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 函数参数和返回值

- 形参和实参：
  - 形参：函数定义中的参数
  - 实参：函数调用时传递的参数
- 参数传递方式：
  - 值传递：传递实参的值
  - 地址传递：传递实参的地址
- 返回值：
  - 使用return语句返回函数结果
  - void类型函数无返回值

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 变量的作用域和存储类别

- 作用域：
  - 局部变量：函数内部定义的变量
  - 全局变量：函数外部定义的变量
- 存储类别：
  - auto：自动变量
  - static：静态变量
  - register：寄存器变量
  - extern：外部变量

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 递归函数

- 递归函数是直接或间接调用自身的函数
- 必须有递归终止条件
- 递归过程分为递推和回归两个阶段
- 应用实例：阶乘计算、斐波那契数列

```c
int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}
```

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 多文件程序组织

- 将程序分解为多个源文件
- 使用头文件(.h)声明函数接口
- 在源文件(.c)中实现函数功能
- 通过#include指令包含头文件
- 编译时需要链接所有相关文件

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 总结

- 理解函数的概念和作用
- 掌握函数的定义和调用方法
- 熟悉参数传递和返回值机制
- 理解变量作用域和存储类别
- 学会使用递归和多文件组织程序
- 为后续学习复杂程序设计打下基础