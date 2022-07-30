# VEGA深度使用

<!--ts-->

* [VEGA深度使用](#vega深度使用)
    * [缘起](#缘起)
    * [基础使用方法（基于kroki-vega）](#基础使用方法基于kroki-vega)
    * [参考资源](#参考资源)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sat Jul 30 14:49:23 UTC 2022 -->

<!--te-->

## 缘起

一直以来，mindmap、UML（plantuml）、excalidraw这些工具只能表达少量概念之间的联系，缺少可以看到更加全面知识点联系的工具。

在尝试scapple之后，它的局限性太明显，无法和在线文档结合起来。这时候我在学习kroki的使用时，发现vege这个工具。

![img](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/68747470733a2f2f766567612e6769746875622e696f2f766567612f6173736574732f62616e6e65722e706e67-20220729172109699.png)

```admonish info title='A visualization grammar'
vega在github上面的口号就深得我心，直接定位可视化语法。
```

## 基础使用方法（基于kroki-vega）

```admonish warn title='⚠️kroki不支持文件内再导入其他文件'
\!\[\tree map])\kroki-vega\:\../../../materials/vega/radial-tree.json)
```

```plantuml
{{#include ../../../materials/plantuml/vega-steps.puml:1:}}
```

## 参考资源

- [vega/vega: A visualization grammar.](https://github.com/vega/vega)

- 编辑器源码：[vega/editor: Editor/IDE for Vega and Vega-Lite](https://github.com/vega/editor)

```shell
yarn 
yarn start
```

- [A Visualization Grammar | Vega](https://vega.github.io/vega/)

- [Example Gallery | Vega](https://vega.github.io/vega/examples/)

- [Usage | Vega](https://vega.github.io/vega/usage/)

- [Tutorials | Vega](https://vega.github.io/vega/tutorials/)

- [Parameter Types | Vega](https://vega.github.io/vega/docs/types/#URL)

- [Triggers | Vega](https://vega.github.io/vega/docs/triggers/)

- [Transforms | Vega](https://vega.github.io/vega/docs/transforms/)

- [Marks | Vega](https://vega.github.io/vega/docs/marks/)

- [Signals | Vega](https://vega.github.io/vega/docs/signals/)

- [Text Mark | Vega](https://vega.github.io/vega/docs/marks/text/)

- [Expressions | Vega](https://vega.github.io/vega/docs/expressions/)

- [Thinking with Joins](https://bost.ocks.org/mike/join/)

- vega的底层是d3:[D3.js - Data-Driven Documents](https://d3js.org/)

    - [Tree, Radial Tidy / D3 / Observable](https://observablehq.com/@d3/radial-tree)

    