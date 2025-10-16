---
marp: true
theme: gaia
title: C语言程序设计 - 第4章 流程控制
paginate: true
---

<!-- _class: lead -->

# 第4章 流程控制

**C语言程序设计**

---

## 本章内容

- 条件语句(if、switch)
- 循环语句(while、do-while、for)
- 转移语句(break、continue、goto)
- 流程控制应用实例
- 程序调试技巧

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 条件语句

- if语句：
  - 单分支：if(条件) 语句;
  - 双分支：if(条件) 语句1; else 语句2;
  - 多分支：if(条件1) 语句1; else if(条件2) 语句2; ... else 语句n;
- switch语句：
  - 多分支选择结构
  - 格式：switch(表达式) {case 常量1: 语句1; break; ... default: 语句n;}

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 循环语句

- while循环：
  - 格式：while(条件) {循环体;}
  - 先判断条件，后执行循环体
- do-while循环：
  - 格式：do {循环体;} while(条件);
  - 先执行循环体，后判断条件
- for循环：
  - 格式：for(初始化; 条件; 更新) {循环体;}
  - 适用于已知循环次数的情况

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 转移语句

- break语句：
  - 跳出当前循环或switch语句
- continue语句：
  - 结束本次循环，继续下一次循环
- goto语句：
  - 无条件转移到指定标号处
  - 不建议频繁使用

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 流程控制应用实例

```c
#include <stdio.h>

int main() {
    int score;
    
    printf("请输入成绩：");
    scanf("%d", &score);
    
    if (score >= 90) {
        printf("优秀\n");
    } else if (score >= 80) {
        printf("良好\n");
    } else if (score >= 60) {
        printf("及格\n");
    } else {
        printf("不及格\n");
    }
    
    return 0;
}
```

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 程序调试技巧

- 使用printf语句输出中间结果
- 分段调试，逐步缩小问题范围
- 注意边界条件和特殊情况
- 使用注释临时屏蔽部分代码
- 理解程序执行流程

---

<style scoped>
  section {
    font-size: 24px;
  }
</style>

## 总结

- 掌握各种流程控制语句的语法和使用场景
- 理解不同循环语句的特点和适用情况
- 学会合理使用转移语句
- 通过实例练习提高编程能力
- 下一章将学习函数的相关知识