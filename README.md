# simple compiler
## 0.简介
编译原理课程作业。实现一个“程序设计语言子集”的编译系统，包括：词法分析、语法分析、语义分析（中间代码生成）、符号表、出错处理等。

## 1.词法分析
0. 输入：字符流
1. 输出：token列表
2. token共分为五类：字面量LITERAL，关键字KEYWORD，标识符IDENTIFIER，操作符OPERATOR，界符BOUNDS
3. token内容：名称、类型、位置(行,列)、值

## 2.语法分析
0. 语法分析：LL(1)文法，自上而下分析
1. 输入：token_list
2. 输出：语法树
3. LL(1)文法
> 0. program -> statements
> 1. statements -> {statements} | statement;staetments 
> 2. statement -> assign; | branch | loop | callstatement; | define; | returnstatement;
> 3. assign -> id := expression
> 4. 
> - 0. expression0 -> literal | id | (expression) | id[expression]
> - 1. expression1 -> expression0 ++ | expression0 -- | expression0
> - 2. expression2 -> !expression1 | ++expression1 | --expression1  | expression1
> - 3. expression3 -> expression2 + expression2 | expression2 - expression2  | expression2
> - 4. expression4 -> expression3 < expression3 | expression3 > expression3 | expression3 < = expression3 | expression3 >= expression3 | expression3
> - 5. expression5 -> expression4 == expression4 | expression4 != expression4 | expression4
> - 6. expression6 -> expression5 && expression5 | expression5
> - 7. expression7 -> expression6 || expression6 | expression6,expression6 | expression6
> - 8. expression -> expression7 
> 5. branch -> if (expression) then {statements} else {statements} | if (expression) then {statements}
> 6. loop -> do{statements}while(expression) | while(expression)do{statements}
> 7. call -> call id()
> 8. 
> - 1. define0 -> ,id | $
> - 2. define -> type id define0 
> - 3. type -> int | float | char | boolean 
> 9. returnstatement -> return expression

4. 参考资料
> 1.  C++写的一个简单的语法分析器（分析C语言） http://blog.csdn.net/niuox/article/details/8216186
> 2. 一个简单语法分析器的C语言实现 http://blog.csdn.net/rill_zhen/article/details/7731711
> 3. 编译原理实习（应用预测分析法LL(1)实现语法分析）http://blog.csdn.net/zjsyhjh/article/details/27102121


## 3.语义分析
0. 输出：符号表，四元组
1. 最后分析的结果，包括四元式，符号表，token列表可以放在一个类里面进行，方便调试

## 4.错误处理

#### *附1：要求*

1. 语言成分：
- (1) 数据类型：整型、实型、字符型、布尔型；
- (2) 简单变量；
- (3) 算术表达式（+、++、-、--、×）；
- (4) 关系表达式（＜、≤、＝、≠、＞、≥）；
- (5) 布尔表达式（∧、∨、┐）；
- (6) 语句：
```
    a) 赋值语句（含多维数组元素引用）；
    b) 分支语句（if-then、if-then-else、case）；
    c) 循环语句（while-do、do-while）；
    d) 过程调用语句；
    e) 定义语句等。
```
2. 输入方式：文本文件（如：.txt）。
3. 输出内容：
- (1) 如果输入串是合法的程序段，则输出相应中间代码、符号表等相关信息；
- (2) 如果输入串是非法的程序段，则指出错误位置及错误原因（如词法错、语法错、语义错等）。
4. 输出方式：除直接在监视器上显示结果之外，还应将结果输出到文件中。

#### *附2：可供参考示例*
1. lexical/grammar analysis of c++ (词法语法分析器) 
> https://github.com/Tachone/Compiler

2. A single-pass, recursive decent LL(1) compiler written by hand for a made-up language. 
> https://github.com/evansneath/compiler

3. Pico-Language & Pictorial Illustrated Compiler Organization by Layer 
> https://git.io/picol 

> https://github.com/Jack-Q/picol

4. PL0_Plus_Compiler 
> https://github.com/hydragon/PL0_Plus_Compiler

5. SimpleCompiler
> https://github.com/naraka/SimpleCompiler
