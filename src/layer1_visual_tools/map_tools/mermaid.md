# mermaid使用示例

<!--ts-->
* [mermaid使用示例](#mermaid使用示例)
   * [介绍](#介绍)
   * [示例](#示例)
      * [思维导图](#思维导图)
      * [流程图](#流程图)
      * [时序图](#时序图)
      * [甘特图](#甘特图)
      * [类图](#类图)
      * [状态图](#状态图)
      * [饼图](#饼图)
      * [gitgraph(experimental in v9)](#gitgraphexperimental-in-v9)
      * [日记图](#日记图)
      * [C4架构图(experimental in v9)](#c4架构图experimental-in-v9)
   * [参考资源](#参考资源)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sat Jul 23 04:56:33 UTC 2022 -->

<!--te-->

## 介绍

![](https://mermaid-js.github.io/mermaid/img/header.png)

```admonish info title='mermaid'
mermaid本身是一种mindmap+UML的语法, 其灵感来源于markdown语法的渲染机制。
```

## 示例
### 思维导图
默认不支持，虽然Mermaid本身暂未支持思维导图的绘制，但是考虑到Mermaid对流程图的支持，可以用Mermaid绘制极简单的思维导图

```mermaid
graph TD
A(工业用地效率)-->B1(土地利用强度)
A-->B2(土地经济效益)
B1-->C1(容积率)
B1-->C2(建筑系数)
B1-->C3(亩均固定资本投入)
B2-->D1(亩均工业产值)
B2-->D2(亩均税收)
```

### 流程图

```mermaid
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```

### 时序图

```mermaid
sequenceDiagram
Alice->>John: Hello John, how are you?
loop Healthcheck
    John->>John: Fight against hypochondria
end
Note right of John: Rational thoughts!
John-->>Alice: Great!
John->>Bob: How about you?
Bob-->>John: Jolly good!
```

### 甘特图

```mermaid
gantt
    section Section
    Completed :done,    des1, 2014-01-06,2014-01-08
    Active        :active,  des2, 2014-01-07, 3d
    Parallel 1   :         des3, after des1, 1d
    Parallel 2   :         des4, after des1, 1d
    Parallel 3   :         des5, after des3, 1d
    Parallel 4   :         des6, after des4, 1d
```

### 类图

```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
<<Interface>> Class01
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
class Class10 {
  <<service>>
  int id
  size()
}
```

### 状态图

```mermaid
stateDiagram-v2
[*] --> Still
Still --> [*]
Still --> Moving
Moving --> Still
Moving --> Crash
Crash --> [*]
```

### 饼图

```mermaid
pie
"Dogs" : 386
"Cats" : 85.9
"Rats" : 15
```

### gitgraph(experimental in v9)

```mermaid
  gitGraph
    commit
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
    commit
```

### 日记图

```mermaid
  journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 3: Me
```

### C4架构图(experimental in v9)

```mermaid
C4Context
title System Context diagram for Internet Banking System

Person(customerA, "Banking Customer A", "A customer of the bank, with personal bank accounts.")
Person(customerB, "Banking Customer B")
Person_Ext(customerC, "Banking Customer C")
System(SystemAA, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

Person(customerD, "Banking Customer D", "A customer of the bank, <br/> with personal bank accounts.")

Enterprise_Boundary(b1, "BankBoundary") {

  SystemDb_Ext(SystemE, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

  System_Boundary(b2, "BankBoundary2") {
    System(SystemA, "Banking System A")
    System(SystemB, "Banking System B", "A system of the bank, with personal bank accounts.")
  }

  System_Ext(SystemC, "E-mail system", "The internal Microsoft Exchange e-mail system.")
  SystemDb(SystemD, "Banking System D Database", "A system of the bank, with personal bank accounts.")

  Boundary(b3, "BankBoundary3", "boundary") {
    SystemQueue(SystemF, "Banking System F Queue", "A system of the bank, with personal bank accounts.")
    SystemQueue_Ext(SystemG, "Banking System G Queue", "A system of the bank, with personal bank accounts.")
  }
}

BiRel(customerA, SystemAA, "Uses")
BiRel(SystemAA, SystemE, "Uses")
Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
Rel(SystemC, customerA, "Sends e-mails to")
```

## 参考资源

- [mermaid-js/mermaid: Generation of diagram and flowchart from text in a similar manner as markdown](https://github.com/mermaid-js/mermaid)
- [mermaid - Markdownish syntax for generating flowcharts, sequence diagrams, class diagrams, gantt charts and git graphs.](https://mermaid-js.github.io/mermaid/#/)
- [Online FlowChart & Diagrams Editor - Mermaid Live Editor](https://mermaid.live/edit#pako:eNpNkE9rwzAMxb-K8WmDtlmSLW1zGKx_YIfBoOutyUG1lcQssYsjrytJvvuclsJ0Eu_3npDUcWEk8pQXtTmLCiyxj12mma-3wztYmbPp9LXf4y_1bPWwM07LxxtfjYStuw0K1Sqjh5u8vgY-NfZsc9hh62piYf6f7c-mZ9s7i3I-4Q3aBpT0e3SjM-NUYYMZT30rwX5nPNOD97mTBMKtVGQsTwuoW5xwcGS-LlrwlKzDu2mjoLTQ3MXagESf6ThdTuPBpWrJTxRGF6ocdWdrL1dEpzYNghHPSkWVO86EaYJWyfE71c8yCZIoWUAUYzKP4SWOpTiGy0URPYeFnD-FEfBhGP4AHgtu4w)
- OS Awards 2019 得奖 🏆 : [JavaScript Open Source Awards - GitNation](https://osawards.com/javascript/2019)
- [mermaid - Markdownish syntax for generating flowcharts, sequence diagrams, class diagrams, gantt charts and git graphs.](https://mermaid-js.github.io/mermaid/#/./integrations)
- gitgraph从v9.0.0开始被支持：[Releases · mermaid-js/mermaid](https://github.com/mermaid-js/mermaid/releases)
  > 此处是源码
- 编译好的js文件下载：
  > [mermaid CDN by jsDelivr - A CDN for npm and GitHub](https://www.jsdelivr.com/package/npm/mermaid?path=dist)

```admonish tip title='mdbook 更新mermaid版本'
1. 下载好对应版本的mermaid.min.js文件
2. 替换book.toml中对应的additional-js中的mermaid.min.js文件
3. 注意要多刷新两次才能更新缓存
```