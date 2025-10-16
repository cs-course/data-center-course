---
marp: true
theme: gaia
title: C语言程序设计 - 第3章 格式化输入与输出
paginate: true
---

<!-- _class: lead -->

# 第3章 格式化输入与输出

**C语言程序设计**

---

## 本章内容

- 字符输入输出函数
- 格式化输出函数printf
- 格式化输入函数scanf
- 格式控制符详解
- 输入输出应用实例

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 字符输入输出函数

- putchar()函数：
  - 向标准输出设备输出一个字符
  - 格式：putchar(ch);
- getchar()函数：
  - 从标准输入设备获取一个字符
  - 格式：ch = getchar();

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 格式化输出函数printf

- printf()函数：
  - 按指定格式向标准输出设备输出数据
  - 格式：printf("格式控制字符串", 输出项列表);
- 常用格式控制符：
  - %d 或 %i：十进制整数
  - %c：字符
  - %f：浮点数
  - %s：字符串
  - %x：十六进制整数

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 格式化输入函数scanf

- scanf()函数：
  - 按指定格式从标准输入设备读取数据
  - 格式：scanf("格式控制字符串", 地址列表);
- 注意事项：
  - 格式控制字符串中的空格会跳过输入中的空白字符
  - 需要使用地址符&获取变量地址
  - 对于字符输入需要注意缓冲区问题

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 格式控制符详解

- 整数格式：
  - %d：十进制有符号整数
  - %u：十进制无符号整数
  - %o：八进制整数
  - %x：十六进制整数
- 浮点数格式：
  - %f：小数形式
  - %e：指数形式
  - %g：自动选择%f或%e

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 输入输出应用实例

```c
#include <stdio.h>

int main() {
    int a, b;
    float x;
    char ch;
    
    printf("请输入两个整数：");
    scanf("%d%d", &a, &b);
    
    printf("请输入一个浮点数：");
    scanf("%f", &x);
    
    printf("请输入一个字符：");
    scanf(" %c", &ch);  // 注意前面的空格
    
    printf("结果：a=%d, b=%d, x=%.2f, ch='%c'\n", a, b, x, ch);
    
    return 0;
}
```

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 总结

- 熟练掌握字符输入输出函数
- 理解格式化输入输出函数的使用方法
- 掌握常用格式控制符的含义和用法
- 注意输入函数的缓冲区问题
- 下一章将学习流程控制语句