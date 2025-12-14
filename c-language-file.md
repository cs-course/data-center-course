---
marp: true
theme: gaia
title: 软件技术基础
# size: 4:3
math: katex
paginate: true
---

<!-- _class: lead -->

# 软件技术基础

## 文件

**施展**
武汉光电国家研究中心 & 计算机学院
华中科技大学

---

## 文件基本概念

- **变量**和**数组**中的数据存放于**内存**，随程序结束而消失
- **文件**用于永久保存大量数据
- 文件位于**外存**（如硬盘、固态盘、光盘）
- 本章：如何用C程序**建立、更新、处理**数据文件

---

## 主要内容

- 文件的打开与关闭  
  `fopen`、`fclose`、`freopen` 函数
- 文本文件的读写  
  `fgetc`、`fputc`、`fgets`、`fputs`、`fprintf`、`fscanf` 等函数
- 二进制文件的读写  
  `fread`、`fwrite` 函数
- 文件的随机读写  
  `fseek`、`rewind`、`ftell`、`fsetpos`、`fgetpos` 等文件指针定位函数

---

## 场景问题

> 从键盘输入若干行字符，保存到 `d:\a.txt` 中，该如何做？

![w:600](images/c-file-fig-01.svg)

### 方案：**savefile.exe** 运行示意

![w:600](images/c-file-fig-02.svg)

---

## 示例：将键盘输入写入文件

```c
#include<stdio.h>

int main() {
    FILE *fp;
    char ch;
    if ((fp = fopen("d:\\a.txt", "w")) == NULL) {
        printf("can't open the file!");
        return -1;
    }
    while ((ch = getchar()) != EOF)
        fputc(ch, fp);
    fclose(fp);
    return 0;
}
```

---

## 文件操作步骤

1. **打开文件** —— 建立文件指针与文件间联系
2. 通过**文件指针**对文件进行读写操作
3. **关闭文件** —— 取消文件指针与文件间的联系

**提示**：打开文件时，就已确定文件读写格式和读写方式！

---

## 打开文件函数 `fopen()`

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
</style>

```c
FILE *fopen(const char *filename, const char *mode);
```

按照`mode`方式打开文件`filename`  
成功：返回文件指针  
失败：返回`NULL`

<div class="columns">

<div>

```c
FILE *fp;
fp＝fopen("c:\\test.txt", "w");
```

</div>

<div>

![h:200](images/c-file-fig-03.svg)

</div>

</div>

---

## 文件结构体

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 3fr 2fr;
    gap: 2rem;
  }
</style>

<div class="columns">

<div>

```c
struct _iobuf {
    char  *_ptr;       // 文件当前读写位置指针
    int   _cnt;        // 当前读写位置剩余字节数
    char  *_base;      // 文件缓冲区起始位置
    int   _flag;       // 文件状态标志
    int   _file;       // 文件描述符
    int   _charbuf;    // 跟踪缓冲区状态
    int   _bufsiz;     // 文件缓冲区大小
    char  *_tmpfname;  // 临时文件名
};
typedef struct _iobuf FILE;
```

</div>

<div>

`FILE`是`stdio.h`中定义的结构类型，记录一个文件的相关信息。

←**文件描述符**是个普通整数，用以标明每一个被打开的文件。第一个打开的文件是0，第二个是1，依此类推。

</div>

</div>

---

## 文件指针

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 3fr 2fr;
    gap: 2rem;
  }
</style>

<div class="columns">

<div>

程序中仅用`FILE *`型变量: FILE指针

![h:380](images/c-file-fig-04.svg)

</div>

<div>

</div>

</div>

---

## 文件指针: **标准文件**

<style scoped>
  table {
    font-size: 0.7em;
  }
  .columns {
    display: grid;
    grid-template-columns: 3fr 2fr;
    gap: 2rem;
  }
</style>

<div class="columns">

<div>

程序中仅用`FILE *`型变量: FILE指针

![h:380](images/c-file-fig-04.svg)

</div>

<div>

C程序会自动打开3个标准文件

```c
#define stdin   (&_iob[0])
#define stdout  (&_iob[1])
#define stderr  (&_iob[2])
```

|标准文件|文件指针|默认值|
|:---:|:---:|:---:|
|标准输入文件|stdin|键盘|
|标准输出文件|stdout|显示器|
|标准错误文件|stderr|显示器|

</div>

</div>

---

## 打开方式 `mode`

<style scoped>
  table {
    font-size: 0.7em;
  }
</style>

模式字符串由 **访问权限** + **文本/二进制标识** 组合而成，核心标识如下：

| 模式字符 | 核心功能                                                                 |
|----------|--------------------------------------------------------------------------|
| `r`      | 只读（Read）：打开已存在的文件，文件不存在则报错（`fopen` 返回 `NULL`）  |
| `w`      | 只写（Write）：创建新文件；若文件已存在，**清空原有内容**（覆盖）         |
| `a`      | 追加（Append）：创建新文件；若文件已存在，写入内容追加到文件末尾         |
| `+`      | 读写扩展：附加在 `r/w/a` 后，开启“读+写”双权限（如 `r+` 表示读写）       |
| `t`      | 文本模式（Text）：**默认模式**（可省略），换行符会自动转换（`\n` 系统换行符） |
| `b`      | 二进制模式（Binary）：不转换换行符，按字节原样读写（如图片、视频文件）    |

---

## 打开方式 `mode` **常用组合**

<style scoped>
  table {
    font-size: 0.6em;
  }
</style>

| 完整模式 | 权限类型 | 文件不存在时 | 已存在文件时       | 适用场景                     |
|----------|----------|--------------|--------------------|------------------------------|
| `r`      | 只读     | 报错（NULL） | 正常打开，读文件   | 读取配置文件、日志文件等     |
| `w`      | 只写     | 创建文件     | 清空内容（覆盖）   | 生成新文件（如导出报表、日志） |
| `a`      | 只写（追加） | 创建文件   | 内容追加到末尾     | 日志追加、累计数据写入       |
| `r+`     | 读写     | 报错（NULL） | 保留原有内容       | 读写已存在的文件（不覆盖）   |
| `w+`     | 读写     | 创建文件     | 清空内容（覆盖）   | 新建可读写文件（如临时文件） |
| `a+`     | 读写（追加） | 创建文件   | 读：从开头读；写：追加到末尾 | 既要读历史内容，又要追加新内容 |
| `rb`     | 二进制只读 | 报错（NULL） | 按字节读文件       | 读取图片、音频、二进制数据   |
| `wb`     | 二进制只写 | 创建文件     | 清空并按字节写     | 写入图片、视频等二进制文件   |
| `ab`     | 二进制追加 | 创建文件     | 字节数据追加到末尾 | 追加二进制日志、数据流       |
| `rb+`/`wb+`/`ab+` | 二进制读写 | 同对应文本模式 | 同对应文本模式     | 二进制文件的读写操作         |

---

## 打开方式 `mode` **注意事项**

<style scoped>
  li {
    font-size: 0.8em;
  }
</style>

1. **模式大小写敏感**：必须小写（如 `R`/`W` 是错误的）。
2. **文本模式与二进制模式的区别**：
   - 文本模式（`t` 或省略）：Windows 系统中，`\n` 会自动转为 `\r\n`（换行+回车），读取时反向转换；Linux/Mac 无此转换。
   - 二进制模式（`b`）：完全按字节读写，不做任何转换，**必须用于非文本文件**（图片、压缩包等），否则会导致文件损坏。
3. **`r+` 与 `w+` 的核心差异**：
   - `r+` 要求文件已存在，不会清空内容；
   - `w+` 无论文件是否存在，都会创建新文件（覆盖原有）。
4. **`a+` 的特殊行为**：写入时永远追加到末尾，但读取时可以从文件开头开始（需手动调整文件指针，如 `fseek`）。
5. **模式兼容性**：部分系统（如 Linux）不区分文本/二进制模式（`t`/`b` 无实际效果），但为了跨平台兼容，建议明确指定（文本文件省略 `t`，二进制文件加 `b`）。

---

## 关闭文件函数 `fclose()`

```c
int fclose(FILE *stream);
```
关闭成功返回 `0`，失败返回 `EOF(-1)`

![h:300](images/c-file-fig-05.svg)

---

## 字符读写函数

- `int fgetc(FILE *stream);`
  - 从输入流`stream`当前位置读取一个字符，读写位置后移一个字符，返回读取的字符。到文件尾或读操作出错时返回`EOF`。
- `int fputc(int c, FILE *stream);`
  - 参数`c`转换成为`unsigned char`类型然后写到输出流`stream`的当前位置处。返回被写字符；如果写操作出错或遇到文件尾返回`EOF`。

`fgetc(stdin)` 即 `getchar()`
`fputc(c, stdout)` 即 `putchar(c)`

---

## 操作**标准输入和输出**文件

- `getchar`、`gets`和`scanf`函数从`stdin`文件读数据
- `putchar`、`puts`和`printf`函数向`stdout`文件写数据
- `freopen`函数可以重定向`stdin`和`stdout`，如:
  - `freopen("d:\\a.txt", "r", stdin);` 重定向输入
    - 将原本从键盘输入的数据将改为从"d:\a.txt"文件中读取
    - **常用于**: 测试输入数据，尤其是批量重复性检验
  - `freopen("d:\\a.txt", "w", stdout);` 重定向输出
    - 将原本向屏幕输出的数据改为向"d:\a.txt"文件中写入
    - **常用于**: 记录输出数据，方便集中观察分析

---

## 文件重定向函数 `freopen()`

```c
FILE *freopen(const char *filename, const char *mode, FILE *fp);
```
相当于：
```c
fclose(fp);
fp = fopen(filename, mode);
```

---

## 使用 `freopen` 重定向输出

```c
#include<stdio.h>

int main(void) {
    char ch;
    if (freopen("d:\\a.txt", "w", stdout) == NULL) {
        printf("can't open the file!");
        return -1;
    }
    while ((ch = getchar()) != EOF)
        putchar(ch);

  return 0;
}
```

---

## 读取文件内容并显示

```c
#include<stdio.h>

int main(void) {
    FILE *fp;
    char ch;

    if ((fp = fopen("d:\\a.txt", "r")) == NULL) {
        printf("can't open the file!");
        return -1;
    }

    while ((ch = fgetc(fp)) != EOF)
        putchar(ch);        /* 也可用 fputc(ch, stdout); */

    fclose(fp);
    return 0;
}
```

---

## **重定向**读取文件内容并显示

```c
#include<stdio.h>

int main(void) {    
    char ch;

    if (freopen("d:\\a.txt", "r"，stdin)  == NULL) {
        printf("can't open the file!");
        return -1;
    }

    while((ch = getchar()) != EOF)   
        putchar(ch);      

    return 0;
}
```

---

## 字符串读写函数

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
</style>

- `char *fgets(char *s, int n, FILE *stream);`
  - 从输入流`stream`当前位置读取一个字符串(`strlen(s) < n`>)，返回读取的字符串。到文件尾或读操作出错时返回`NULL`。 
- `int   fputs(const char *s, FILE *stream);`
  - 参数`s`写入输出流`stream`的当前位置处。返回被写入的字符数，如果写操作出错或遇到文件尾返回`EOF`。

<div class="columns">

<div>

```c
char s[10];          // 输入：hust
fgets(s, 10, stdin); // 换行符被读入
gets(s);             // 换行符不被读入
```

</div>

<div>

```c
fputs("hust", stdout); // 输出：hust
puts("hust"); // 追加输出换行符：hust
```

</div>

</div>

---

## 格式读写函数

- `int fprintf(FILE *stream, const char *format, …);`
  - 将输出参数列表中的数据按指定的格式写入到`stream`流中。写操作正常返回**输出字符个数**，写操作出错时返回负值。
- `int fscanf(FILE *stream, const char *format, …);`
  - 从`stream`流中，按指定的格式读去数据，并赋值给相应的参数变量。函数返回**已输入项数**，如果读操作出错返回`EOF`。

| 等价关系                        | 说明          |
|---------------------------------|---------------|
| `fscanf(stdin, "%d", &x)`       | `scanf("%d", &x)` |
| `fprintf(stdout, "%d", x)`      | `printf("%d", x)` |

---

## 文本文件的复制

- Windows 命令行：
  - `copy source_file target_file` 命令
- Linux 命令行：
  - `cp source_file target_file` 命令

---

```c
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char* argv[]) {
    int ch;
    FILE *fpin,*fpout;

    if(argc!=3) { /*命令行参数数目不等于3，说明命令行格式不对*/
        printf("Arguments error!\n");
        exit(-1);
    }
    if((fpin=fopen(argv[1],"r"))==NULL) { /* fpin指向source_file */
        printf("Can't open %s file!\n",argv[1]);
        exit(-1);
    }
    if((fpout=fopen(argv[2],"w"))==NULL) { /* fpout指向target_file */
        printf("Can't open %s file!\n",argv[2]);
        exit(-1);
    }
    while((ch=fgetc(fpin))!=EOF) /* 从source_file中读字符 */
        fputc(ch,fpout); /* 向target_file中写字符，实现拷贝复制 */

    fclose(fpin); /* 关闭source_file */
    fclose(fpout); /* 关闭target_file */
    return 0;
}
```

---

## 文本文件的分解

将一个大的文本文件以行为单位分解成为若干个较小的文本文件，文件名和分解的行数都由用户从命令行输入。

命令行：

```bash
parts abc.txt a.txt b.txt c.txt 10
```

> 把 `abc.txt` 每 10 行切成一个小文件

---

### 分解流程

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 3fr 1fr;
    gap: 2rem;
  }
</style>

<div class="columns">

<div>

0) 命令行: `parts abc.txt a.txt b.txt c.txt 10`
1) `len=`命令行中提取的行数`atoi(argv[argc-1])`
2) 以读方式打开源文件`fopen(argv[1], "r")`
3) 依次打开目标文件，从源文件读`len`行写入
  ```c
  for(i = 2; i < argc-1; i++) {
      以写方式打开文件 argv[i]
      从argv[1]读1行写入argv[i]直到写了len行或源文件到文件尾
      关闭 文件argv[i]
  }
  ```
4) 关闭源文件`argv[1]`

</div>

<div>

![w:200](images/c-file-fig-06.svg)

</div>

</div>

---

```c
#include<stdio.h>
#include<stdlib.h>

int main(int argc,char *argv[]) {
    FILE *fin, *fout;
    int len = atoi(argv[argc-1]);/*将行数字符串转换为整数*/
    int i, j;
    char a[81];
    if((fin = fopen(argv[1], "r")) == NULL){
        printf("can't open the %s file!\n", argv[1]);
        exit(-1);
    }
    for(i = 2; i < argc-1; i++){
        fout = fopen(argv[i], "w");/*打开argv[i]指定的文件进行写操作*/
        j=0;
        while((fgets(a, 80, fin)!= NULL) && j++<len)/*从fin中读一行到a中*/
            fputs(a, fout);/*将a中字符串写到fout中*/
        fclose(fout);/*写满len行后关闭文件*/
    }
    fclose(fin);
    return 0;
}
```

---

## 数据采集与处理程序

键盘输入: 商品名称、数量、单价 → 计算总金额 → 数据保存到 `d:\goods.txt`

```c
#include<stdio.h>
#include<stdlib.h>

void data_write(char *);         /* 数据采集并存盘 */
void data_cal(char *, float);    /* 从文件读入数据并进行计算 */ 

int main(void) {
    char a[20] = "d:\\goods.txt";
    data_write(a);
    data_cal(a);
    return 0;
}
```

---

### data_write：输入并保存

```c
void data_write(char *filename) {
    FILE *out;
    char name[20];
    int number;
    float price;

    if ((out = fopen(filename, "w")) == NULL)
        exit(-1);

    puts("input name、number and price please!");
    while (scanf("%s%d%f", name, &number, &price) != EOF) // 输入由用户分隔
        fprintf(out, "%s %d %f\n", name, number, price);  // 输出也要自备空格

    fclose(out);
}
```

---

### data_cal：读取并计算

```c
void data_cal(char *filename) {
    FILE *in;
    char name[5];
    int number;
    float price;

    if ((in = fopen(filename, "r")) == NULL)
        exit(-1);

    while (fscanf(in, "%s%d%f", name, &number, &price) != EOF)
        printf("%s\t%d\t%8.2f\n", name, number, price * number);

    fclose(in);
}
```

---

## 文本文件数据的间隔符

写入多个数据时需加**间隔符**，以便正确读取。

屏幕输出可读性，机器采集便于后续`scanf`使用。

```c
fprintf(out, "%s %d\n", name, number);
```

```c
fprintf(out, "%s\t%d\n", name, number);
```

---

## 文件类型

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 2rem;
  }
</style>

文件按照数据格式分为**文本文件**和**二进制文件**两类。

<div class="columns">

<div>

**文本文件**:

ASCII 字符序列

```bash
# head -n5 README.md
---
license: mit
---

This is a Llama 2 architecture ...
```

</div>

<div>

**二进制文件**:

与内存内容一致的原始数据序列

```bash
# xxd stories15M.bin | head
00000000: 2001 0000 0003 0000 0600 0000 0600 0000   ...............
00000010: 0600 0000 007d 0000 0001 0000 b00a 75bd  .....}........u.
...
```

</div>

</div>

---

## 存储空间举例

> 短整数 `x = 128` 分别占多少字节？

![w:1000](images/c-file-fig-07.svg)

---

## 二进制文件读写

文件直接输入输出又称为文件成组输入输出。

标准C为文件的直接输入输出提供了两个函数`fread`和`fwrite`，适用于二进制形式文件的读写 。

```c
typedef unsigned int size_t;
size_t fread(void *ptr, size_t size, size_t n, FILE *stream);
// ptr: 存储数据的指针，size: 每个元素大小，n: 元素个数,stream: 文件指针
// 返回实际读取的元素个数，<n 表示读到文件尾部，返回实际读取的元素个数
// 可以通过 feof() 函数判断文件是否读完，ferror() 函数判断文件是否出错
```

```c
size_t fwrite(const void *ptr, size_t size, size_t n, FILE *stream);
```

---

### 写示例

```c
int x[] = {12, 8, 34, 421};
FILE *fp = fopen("d:\\a.dat", "wb");

/* 写法 1：一次性写 4 个 int */
fwrite(x, sizeof(int), 4, fp);

/* 写法 2：循环写 */
for (int i = 0; i < 4; i++)
    fwrite(x + i, sizeof(int), 1, fp);

fclose(fp);
```

```bash
# xxd a.dat
00000000: 0c00 0000 0800 0000 2200 0000 a501 0000  ........".......
00000010: 0c00 0000 0800 0000 2200 0000 a501 0000  ........".......
```

---

### 读示例

```c
int x[10], i = 0;
FILE *fp = fopen("d:\\a.dat", "rb");

while (fread(x + i, sizeof(int), 1, fp) == 1)
    i++;

fclose(fp);
```

---

### 文本 vs 二进制读取差异

```c
short x;

/* 按二进制读 */
fread(&x, sizeof(short), 1, fp);   // x = 0x3231

/* 按文本读 */
fscanf(fp, "%hd", &x);             // x = 123
```

---

### 二进制文件无需间隔符

```c
short x;
fread(&x, sizeof(short), 1, fp); // 按二进制读入1个short数
                                 // x=0x3231, 低字节在前
fscanf(fp, "%hd", &x);  // 按文本格式读入1个short数
                        // x=123  
```

![w:1000](images/c-file-fig-08.svg)

---

### 文件尾测试函数`feof()`

文件尾测试函数`feof()`，如果到文件尾，返回非0值，否则返回0。

```c
#define  _IOEOF  0x0010 
#define  feof(_stream)  ((_stream) ->_flag & _IOEOF)  
```

---

### 使用`feof()`控制循环

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
</style>

<div class="columns">

<div>

```c
int x;
FILE *fp;

fp = fopen("d:\\a.dat", "rb");

fread(&x, sizeof(int), 1, fp);
while(!feof(fp)) {
    printf("%d ", x);
    fread(&x, sizeof(int), 1, fp);
}
```

</div>

<div>

```c
int x;
FILE *fp;

fp = fopen("d:\\a.dat", "rb");

while(!feof(fp)) {
    fread(&x, sizeof(int), 1, fp);
    printf("%d ", x);
}
```

</div>

</div>

从二进制文件读数据显示到屏幕，用哪个？

---

### 使用`feof()`控制循环…

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
</style>

<div class="columns">

<div>

```c
int x;
FILE *fp;

fp = fopen("d:\\a.dat", "rb");

fread(&x, sizeof(int), 1, fp);
while(!feof(fp)) {
    printf("%d ", x);
    fread(&x, sizeof(int), 1, fp);
}
```

</div>

<div>

```c
int x;
FILE *fp;

fp = fopen("d:\\a.dat", "rb");

while(!feof(fp)) { // 到EOF还会再来
    fread(&x, sizeof(int), 1, fp);
    printf("%d ", x); // 末尾输出2次
}
```

</div>

</div>

只有当文件位置指针到了**文件末尾**，然后**再发生读/写操作**时，标志位`(fp->_flag)`才会被置为含有`_IOEOF`

---

## 数据采集与处理程序**二进制版**

```c
#include<stdio.h>
#include<stdlib.h>
// 声明物品信息结构类型struct goods
struct goods {
    long code;        // 货物编码
    char name[20];    // 名称
    float price;      // 价格
};

void data_write(const char *filename);
void data_read(const char *filename);

int main(void) {
    char fname[]="goods_table.dat";
    data_write(fname); // 将结构体数组整体写入文件
    data_read(fname);  // 再从文件随机读取
    return 0;
}
```

---

### 输入商品信息写入磁盘文件

```c
void data_write(const char *filenamme) {
    struct goods g; // 声明 struct goods 类型结构变量
    FILE *out;

    if((out = fopen(filenamme, "wb")) == NULL)
        exit(-1);
    printf("输入货物编码、名称、价格\n");
    while(scanf("%ld%s%f", &g.code, g.name, &g.price) == 3) {
        fwrite(&g, sizeof(struct goods), 1, out); // 写入结构体变量g
    }
    fclose(out);
}
```

---

### 从磁盘读取商品信息显示到屏幕

```c
void data_read(const char *filenamme) {
    struct goods g;
    FILE *in;

    if((in = fopen(filenamme, "rb")) == NULL)
        exit(-1);
    printf("货物编码\t名称\t价格\n");
    fread(&g, sizeof(struct goods), 1, in);
    while(!feof(in)) { // 注意函数生效条件
        printf("%ld\t%s\t%f\n", g.code, g.name, g.price);
        fread(&g, sizeof(struct goods), 1, in); // 读入结构体变量g
    }
    fclose(in);
}
```

---

## 文件的读写方式: **顺序 vs 随机读写**

- 打开文件时，读写指针指向文件头，读写一个"数据"后，读写指针自动指向下一个"数据"。
- 文件的读写方式有两种: **顺序读写**和**随机读写**
  - **顺序读写**：从文件头到文件尾顺序读写数据。
  - **随机读写**：读写可以从指定的位置进行，不必每次从头顺序开始。

| 方式     | 特点                          | 适用文件 |
|----------|-------------------------------|----------|
| 顺序     | 读写指针自动后移              | 文本/二进制 |
| 随机     | 可定位任意位置读写            | 二进制   |

---

### 顺序读写示意

![w:1000](images/c-file-fig-09.svg)

按文本格式，读入1个short 数据和1个char数据

```c
fscanf(fp, "%hd", &i); // x = 123 
fscanf(fp,  "%c", &c); // x = 'a'
```

**文本文件只能顺序读写**，因为其数据非定长，不能直接定位。

---

### 随机读写示意

![w:1000](images/c-file-fig-10.svg)

- 二进制文件数据长度由明确类型给出，**既能顺序，也能随机读写**。
- 利用文件的**定位函数**和文件的读写函数，即可实现文件的随机读写。

---

## 文件定位函数

```c
int fseek(FILE *stream, long offset, int origin);
long ftell(FILE *stream);
void rewind(FILE *stream);
int fgetpos(FILE *stream, fpos_t *pos);
int fsetpos(FILE *stream, const fpos_t *pos);
```

---

### 文件定位函数`fseek`

<style scoped>
  .columns {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 2rem;
  }
</style>

```c
int fseek(FILE *stream, long offset, int origin);
```

- 将`stream`指向的文件之当前读写指针，定位到`origin + offset`
  - 如果正常定位，返回0，否则返回非0值。
  - `origin`和`offset`分别称为基准点和偏移量。

<div class="columns">

<div>

![w:350](images/c-file-fig-11.svg)

</div>

<div>

```c
// origin 基准点取值
#define SEEK_SET  0  // 文件起始位置为基准点 
#define SEEK_CUR  1  // 文件当前位置为基准点
#define SEEK_END  2  // 文件尾部位置为基准点
// 获取文件当前位置
long ftell(FILE *stream); // 当前位置相对于文件首的偏移字节数，出错时返回-1L
```

</div>

</div>

---

### 文件定位函数`fgetpos`和`fsetpos`

```c
int fgetpos(FILE *stream, fpos_t *pos);
```

将`stream`指向文件的读写指针当前值，保存到`pos`指针所指的`fpos_t`类型的对象中。成功保存，fgetpos返回0，否则返回非0值。

```c
int fsetpos(FILE *stream, const fpos_t *pos);
```

用`fgetpos`函数保存到`pos`指针所指对象中的值来设置`stream`所指向文件的当前位置。设置成功函数返回0，否则返回非0值。

---

### 文件定位函数`rewind`

```c
void rewind(FILE *stream);
```

将文件指针`stream`指向文件的读写指针重新定位到文件的起始位置，同时清除文件结束标志和出错标志。

---

## 其它文件操作

```c
int   fflush(FILE *stream); // 强制刷新缓冲区
int   setvbuf(FILE *stream, char *buf, int mode, size_t size); // 自定义缓冲区
void  setbuf(FILE *stream, char *buf); // 默认缓冲区
int remove(const char * filename);     // 删除文件
int rename(const char * oldname, const char * newname); // 重命名文件
FILE * tmpfile(void);        // 创建临时文件
char * tmpnam(char *s);      // 生成临时文件名
void clearerr(FILE *stream); // 清除错误标志
int ferror(FILE *stream);    // 测试文件错误
void perror(const char *s);  // 打印错误信息
```

---

## 总结

- 文件操作是C语言中重要的**数据持久化**手段
- 掌握**文本文件**和**二进制文件**的区别及适用场景
- 熟练使用各种文件**读写函数**（字符、字符串、格式、二进制）
- 理解**顺序读写**和**随机读写**的原理及应用
- 掌握**文件定位**和**错误处理**的方法
