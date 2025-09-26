---
marp: true
theme: gaia
title: 软件技术基础
# size: 4:3
math: katex
---

<!-- _class: lead -->

# 软件技术基础

## 数组

**施展**
武汉光电国家研究中心 & 计算机学院
华中科技大学

---

## 主要内容

- 一维/二维数组的声明、初始化和使用  
- 数组作为函数参数的使用  
- 字符串数组  
- 多维数组  

---

## 7.1 数组概述

**数组**：固定数量的同类型元素的集合。

```c
#define SIZE 30
int score[SIZE];  // 含有30个int型元素的数组
```

- 下标从0开始：`score[0]` ~ `score[29]`
- 内存中连续存放
- 所占内存：`sizeof(int) * SIZE`

---

## 7.2 一维数组

### 声明格式

```c
存储类型 类型说明符 数组名[常量] = {初值表};
```

示例：
```c
int score[SIZE];
static int y[10];
extern double s[2];
// C99支持：int n=4, a[n];
```

---

### 一维数组元素的引用

```c
数组名[下标表达式]
```

示例：
```c
a[2], a[i], a[i+j], a[max(a,b)]
```

**注意**：下标不要越界！

```c
// 错误示例：越界
int a[4], i;
for(i = 0; i <= 4; i++)  // 应改为 i < 4
    a[i] = i + 1;
```

---

### 一维数组的初始化

```c
// 全部初始化
int x[5] = {1, 2, 3, 4, 5};
int x[] = {1, 2, 3, 4, 5};  // 自动确定长度

// 部分初始化
int z[6] = {1, 2, 3, 4};  // 前4个元素赋值，其余为0
```

---

### 一维数组作为函数参数

```c
void fun(int y[], int n) {
    for(int i = 0; i < n; i++) 
        y[i]++;
}

int main() {
    int x[5] = {1, 2, 3, 4, 5};
    fun(x, 5);  // 传递数组名（首地址）
    // 相当于“传址”，形参和实参共享内存
}
```

---

## 排序问题：冒泡排序

```c
void BubbleSort(int a[], int n) {
    int i, j, t;
    for(i = 1; i < n; i++) {
        for(j = 0; j < n - i; j++) {
            if(a[j] > a[j + 1]) {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
}
```

---

## 二分查找（折半查找）

```c
int BinarySearch(int a[], int x, int n) {
    int left = 0, right = n - 1, mid;
    while(left <= right) {
        mid = (left + right) / 2;
        if(x < a[mid]) right = mid - 1;
        else if(x > a[mid]) left = mid + 1;
        else return mid;
    }
    return -1;
}
```

---

## 分治法与递归

```c
// 递归实现二分查找
int BinarySearch(int a[], int x, int left, int right) {
    if(left > right) return -1;
    int mid = (left + right) / 2;
    if(x == a[mid]) return mid;
    else if(x > a[mid])
        return BinarySearch(a, x, mid + 1, right);
    else
        return BinarySearch(a, x, left, mid - 1);
}
```

---

## 快速排序（分治策略）

```c
void QuickSort(int a[], int left, int right) {
    if(left < right) {
        int split = partition(a, left, right);
        QuickSort(a, left, split - 1);
        QuickSort(a, split + 1, right);
    }
}
```

---

## 7.3 二维数组

### 声明与使用

```c
int score[30][4];  // 30行4列
```

- 逻辑结构：矩阵/表格
- 存储方式：按行存放

---

### 二维数组初始化

```c
// 按行初始化
int x[2][3] = {{85, 91, 0}, {82, 95, 0}};
int b[][3] = {{1, 3}, {5, 6, 7}};

// 按顺序初始化
int a[2][2] = {85, 91, 82, 95};
```

---

### 二维数组作为函数参数

```c
// 方式1：固定列数
void fun(int a[][M+1], int n);

// 方式2：动态列数（C99）
void fun(int n, int m, int a[][m]);
```

---

## 7.4 n维数组

### 多维数组的概念

- **三维数组**：可以描述空间中的点集
- **n维数组**：用来描述n维线性空间中的n维向量

### 三维数组示例

```c
int a[][3][3] = { 
    { {81, 82, 90}, {73, 94, 90}, {65, 70, 80} },
    { {80, 86, 87}, {78, 90, 80}, {89, 60, 70} }
};
```

### 构造n阶旋转方阵

n维数组在数学和科学计算中有广泛应用，如构造旋转方阵等高级数据结构。

---

## 7.5 字符数组和字符串

### 字符数组声明

```c
char s[81];  // 最多存放80个字符 + '\0'
```

### 字符串构造

```c
char Capital[27];
for(int i = 0; i < 26; i++)
    Capital[i] = 'A' + i;
Capital[26] = '\0';  // 结尾加'\0'
```

---

### 字符串初始化

```c
char s1[8] = {'W','u','h','a','n','\0'};
char s2[] = "Computer Science";  // 自动加'\0'
char s3[] = "Com\0puter";  // strlen=3, sizeof=10
```

---

### 字符串处理函数（自定义实现）

```c
// 字符串长度
int mystrlen(char s[]) {
    int j = 0;
    while(s[j] != '\0') j++;
    return j;
}

// 字符串反转
void mystrrev(char s[]) {
    for(int i = 0, j = strlen(s)-1; i < j; i++, j--) {
        char c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}
```

---

### 字符串匹配（BF算法）

```c
int mystrstr(char s[], char t[]) {
    for(int i = 0; s[i] != '\0'; i++) {
        int j = i, k = 0;
        while(t[k] != '\0' && s[j] == t[k]) {
            j++; k++;
        }
        if(t[k] == '\0') return i;
    }
    return -1;
}
```

---

### 数字串与数值转换

```c
// 字符串转整数
int myatoi(char s[]) {
    int num = 0;
    for(int j = 0; s[j] != '\0'; j++)
        num = num * 10 + (s[j] - '0');
    return num;
}

// 整数转字符串
void myitoa(int n, char s[]) {
    int sign = n, j = 0;
    if(n < 0) n = -n;
    do {
        s[j++] = n % 10 + '0';
    } while((n /= 10) > 0);
    if(sign < 0) s[j++] = '-';
    s[j] = '\0';
    strrev(s);
}
```

---

## 二维字符数组（字符串数组）

```c
char devices[][12] = {"hard disk", "CRT", "keyboard"};
```

- 可引用单个字符：`devices[2][3]` → `'b'`
- 可引用整个字符串：`devices[i]`

```c
printf("%s", devices[1]);  // 输出 "CRT"
scanf("%s", devices[1]);   // 输入新字符串
```

---

# 总结

- **数组基本概念** - 定义、特点
- **一维数组** - 声明、初始化、使用、函数参数
- **多维数组** - 逻辑结构、存储方式、函数参数
- **字符数组与字符串** - 特点、常用函数、转换函数
- **重要算法** - 排序、查找、字符串处理
- **编程要点** - 边界检查、字符串结尾、参数传递
- **应用场景** - 数据处理、文本处理、算法实现
