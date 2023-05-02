# VEGA深度使用

<!--ts-->


<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Tue May  2 07:24:36 UTC 2023 -->

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

## 编写好的py脚本

~~~admonish tip title='puml_mindmap_json'
```python
{{#include ../../../scripts/puml_mindmap_json.py:1:}}
```
~~~

## 两种格式：svg和canvas

- svg本质上是xml数据，它渲染的可视化图片会分成很多节点DOM。好处在于节点操作更顺畅，坏处在于更加占资源
- canvas只有一个DOM，正好与svg相反。
- 二者互补，节点多优先选canvas

## 两种渲染方式

~~~admonish tip title='embed'
```html
<head>
    <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
</head>
<body>
<div id="vis"/>
</code>
<script>
    vegaEmbed(
        '#vis',
        'vega/tree.vg.json'
    );
</script>
</body>
```
~~~

~~~admonish tip title='embed'
```html
<head>
    <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
</head>
<body>
<div id="view"></div>
<script type="text/javascript">
    var view;

    fetch('vega/circle_packing.vg.json')
        .then(res => res.json())
        .then(spec => render(spec))
        .catch(err => console.error(err));

    function render(spec) {
        view = new vega.View(vega.parse(spec), {
            renderer:  'svg',  // renderer (canvas or svg)
            container: '#view',   // parent DOM container
            hover:     true       // enable hover processing
        });
        return view.runAsync();
    }
</script>
</body>
```
~~~

```admonish warn title='优先选embed'
view组件方式不支持hover等特性，放弃
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


- [Amazon.com: Making Data Visual: A Practical Guide to Using Visualization for Insight eBook : Fisher, Danyel, Meyer, Miriah: Kindle Store](https://www.amazon.com/Making-Data-Visual-Practical-Visualization-ebook/dp/B078JG191M)
- [MakingDataVisual/makingdatavisual.github.io: Executable Examples for Making Data Visual](https://github.com/MakingDataVisual/makingdatavisual.github.io)
- [List of Figures | Making Data Visual](https://makingdatavisual.github.io/figurelist.html#related)
- [local marginnote](marginnote3app://note/C95A594C-4FC8-4C3E-AAFE-05AF760FEFD1)
    - [Chapter 5: Single Views](marginnote3app://note/BFF3AEAC-D3B8-49A6-A36C-AFDF62E4D85C)

```admonish tip title='这本书最大的特点是根据数据特点提供对应的图表类型'
- Four Views of the Same Data: Scatterplot, Clustered Barchart, Clustered Barchart, Stacked Barchart
- Question: How Is a Value Distributed?: Categorical Histogram , Quantitative Histogram , Smoothed Histogram , Box Plot, Categorical Density Plot, Continuous Density Plot
- Question: How Do Groups Differ from Each Other?: Bar Chart, Paired (or Multiple) Series Bar Chart, Pie (or Doughnut ) Chart, Heatmap
- Question: Do Invidual Items Fall Into Groups? Is There a Relationship Between Attributes of Items?: Scatterplot, Line Chart, Stacked Area Chart
- Question: How Are Objects Related To Each Other in a Network or Hierarchy?: Node-Link View (Force-Directed Layout), Circular Network Layout, Adjacency Matrix, Tree View, Treemap, Sunburst plot
- Question: Where Are Objects Located?: Choropleth, Dotplot map
- Question: What Is In This Text?: Word Cloud
- Chapter 6: Multiviews: Small Multiples, Split by Dimension, Small Multiples, Showing Different Measures, SPLOM, Cross-Selection
```