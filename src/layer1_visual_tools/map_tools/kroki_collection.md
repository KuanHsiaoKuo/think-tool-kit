# kroki合集

<!--ts-->


<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sat May  6 14:52:08 UTC 2023 -->

<!--te-->
![image-20220715114804075](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220715114804075.png)

# kroki两种用法

## kroki-<target_format>

## 引入用法

```shell

\!\[title\]\(kroki-<target_format>\:file_relativepath)
```

## 使用注意

### 样式冲突

```admonist warn title='kroki-svgbob和其他格式一起会冲突'
kroki-svgbob会引入text样式，font-size固定为14px。
就导致其他格式渲染图像出现文字重叠问题
```

## 参考资源

## [Kroki!](https://kroki.io/#examples)

## [Kroki! Examples](https://kroki.io/examples.html)

## IntelliPikchr: IDEA内置插件

- [IntelliPikchr - IntelliJ IDEs Plugin | Marketplace](https://plugins.jetbrains.com/plugin/17624-intellipikchr)

> Split editor with preview pane for **.pikchr** files, using kroki.io or self-hosted server for rendering

## mdbook-kroki-preprocessor: 支持kroki渲染

> kroki可以看作多种图表语言的统一接口

- [mdbook-kroki-preprocessor - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-kroki-preprocessor)

```admonish info title='md语法'
The code block's language has to be kroki-<diagram type>.
- kroki-mermaid
- kroki-plantuml
```

```shell
cargo install mdbook-kroki-preprocessor
```

# kori支持范围

## 编码类

### Block Diagram

- [blockdiag - simple diagram images generator — blockdiag 1.0 documentation](http://blockdiag.com/en/index.html)

#### blockdiag

> kroki-blockdiag

![blockdiag sample](kroki-blockdiag:../../../materials/kroki-collections/blockdiag_sample.blockdiag)

#### Sequence diagram

> kroki-seqdiag


![seqdiag sample](kroki-seqdiag:../../../materials/kroki-collections/kroki-seqdiag.seqdiag)

#### Activity diagram

- [actdiag - simple activity-diagram image generator — blockdiag 1.0 documentation](http://blockdiag.com/en/actdiag/index.html)
- [Demo - interactive shell for actdiag — blockdiag 1.0 documentation](http://blockdiag.com/en/actdiag/demo.html#diagram-source)

> kroki-actdiag


![actdiag sample](kroki-actdiag:../../../materials/kroki-collections/kroki-actdiag.actdiag)

#### Network diagram

> kroki-nwdiag


![nwdiag sample](kroki-nwdiag:../../../materials/kroki-collections/kroki-nwdiag.nwdiag)

### pikchr:

> kroki-pikchr

- [Pikchr: Documentation](https://pikchr.org/home/doc/trunk/homepage.md)

#### Commit Graph

![pikchr commit graph sample](kroki-pikchr:../../../materials/kroki-collections/kroki-pikchr-commit-graph.pikchr)

#### Syntax diagram

![pikchr syntax diagram sample](kroki-pikchr:../../../materials/kroki-collections/kroki-pikchr-syntax-diagram.pikchr)

#### Impossible trident

![pikchr impossible trident sample](kroki-pikchr:../../../materials/kroki-collections/kroki-pikchr-impossible-trident.pikchr)

### Structurizr

```admonish info title='what is'
> Diagrams as code 2.0

Structurizr builds upon "diagrams as code", 
allowing you to create multiple diagrams from a single model, 
using a number of tools and programming languages. 

This Structurizr DSL example creates two diagrams, 
based upon a single set of elements and relationships.
- [Structurizr](https://structurizr.com/)
- [Structurizr - DSL](https://structurizr.com/dsl)
```

> kroki-structurizr

#### Contaner diagram

![structurizr sample](kroki-structurizr:../../../materials/kroki-collections/kroki-structurizr.structurizr)

### Plantuml

> kroki-plantuml

#### use case diagram

![kroki-plantuml-use-case-diagram sample](kroki-plantuml:../../../materials/kroki-collections/kroki-plantuml-use-case-diagram.puml)

#### work breakdown structure

![kroki plantuml work breakdown structure sample](kroki-plantuml:../../../materials/kroki-collections/kroki-plantuml-work-breakdown-structure.puml)

#### Mind Map

![kroki plantuml mind map sample](kroki-plantuml:../../../materials/kroki-collections/kroki-plantuml-mind-map.puml)

#### 引入文件不支持!include

> 可以直接在markdown里面引入

##### Component diagram

[//]: # (![kroki plantuml component diagram]&#40;kroki-plantuml:../../../materials/kroki-collections/kroki-plantuml-component-diagram.puml&#41;)

##### Context diagram

[//]: # (![kroki plantuml context diagram]&#40;kroki-plantuml:../../../materials/kroki-collections/kroki-plantuml-context-diagram.puml&#41;)

##### Container diagram

[//]: # (![kroki plantuml container diagram]&#40;kroki-plantuml:../../../materials/kroki-collections/kroki-plantuml-container-diagram.puml&#41;)

## 绘制类

### ~~Packet diagram~~: 可被plantuml替代

> Package diagram, a kind of structural diagram, shows the arrangement and organization of model elements in middle to
> large scale project. Package diagram can show both structure and dependencies between sub-systems or modules, showing
> different views of a system, for example, as multi-layered (aka multi-tiered) application - multi-layered application
> model.

- [Package Diagram Tutorial | Lucidchart](https://www.lucidchart.com/pages/uml-package-diagram/#discovery__top)

> kroki-packetdiag


![packetdiag sample](kroki-packetdiag:../../../materials/kroki-collections/kroki-packetdiag.packetdiag)

### Rack diagram

- [Blog - Create a rack diagram in diagrams.net](https://www.diagrams.net/blog/rack-diagrams)

> kroki-rackdiag

![rackdiag sample](kroki-rackdiag:../../../materials/kroki-collections/kroki-rackdiag.rackdiag)

### Object Oriented Graph

> kroki-graphviz

![object oriented graph](kroki-graphviz:../../../materials/kroki-collections/object-oriented-graph.graphviz)

### Entity Relationship Diagram

> kroki-erd

![erd sample](kroki-erd:../../../materials/kroki-collections/kroki-erd.erd)

### Diagramsnet/drawio

- [Architecture :: Kroki Documentation](https://docs.kroki.io/kroki/architecture/#_diagrams_net_experimental)

> kroki-diagramsnet:../../../materials/diagramsnet.drawio
> 还处于实验性质，测试未成功

### Excalidraw: hand-draw like diagrams

> kroki-excalidraw

![excalidraw sample](kroki-excalidraw:../../../materials/kroki-collections/kroki-excalidraw.excalidraw)

#### idea自带插件:

[Excalidraw Integration - IntelliJ IDEs Plugin | Marketplace](https://plugins.jetbrains.com/plugin/17096-excalidraw-integration)

> 更正：目前新版的Excalidraw Integration已经修复，修改后会直接更新源文件！

```admonish warn title='idea插件不适合kroki-excalidraw'
1. Excalidraw Integration只是一个画图工具：
- 没有保存文件按钮，只能导出为图片
- 哪怕打开画好的文件，也只能预览，修改之后不能保存更新源文件
> 那还不如用在线app
2. [在线excalidraw](https://excalidraw.com)的文件才是kroki-excalidraw可用的
- 可以载入第三方组件库
```

#### 在线绘制工具

[excalidraw/excalidraw: Virtual whiteboard for sketching hand-drawn like diagrams](https://github.com/excalidraw/excalidraw)

#### 将绘制步骤动态化

[dai-shi/excalidraw-animate: A tool to animate Excalidraw drawings](https://github.com/dai-shi/excalidraw-animate)

#### 好用的库

[excalidraw/excalidraw-libraries: Collection of publicly available libraries](https://github.com/excalidraw/excalidraw-libraries)

#### 创建幻灯片

[dai-shi/excalidraw-claymate: A tool based on Excalidraw to create stop motion animations and slides.](https://github.com/dai-shi/excalidraw-claymate)

### vega

> kroki-vega/vegalite

#### 相关资源

- [在线编辑器](https://vega.github.io/editor/#/edited)
- [Word Cloud Example | Vega](https://vega.github.io/vega/examples/word-cloud/)
- 还支持许多其他格式: [Example Gallery | Vega](https://vega.github.io/vega/examples/)

[![Vega Examples](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/68747470733a2f2f766567612e6769746875622e696f2f766567612f6173736574732f62616e6e65722e706e67.png)](https://vega.github.io/vega/examples)

- [GitHub - vega/vega: A visualization grammar.](https://github.com/vega/vega)

#### word cloud

![vega sample](kroki-vega:../../../materials/kroki-collections/kroki-vega.vega)

#### Diverging Stacked Bar Chart

![vegalite sample](kroki-vegalite:../../../materials/kroki-collections/kroki-vegalite.vegalite)

### Ditaa: Conjugate prior relationships

```admonish tip title='ditaa的含义'
ditaa 是 DIagrams Through Ascii Art，作者是 Stathis Sideris。
```

> 支持ascii图像渲染
> kroki-ditaa


![ditaa sample](kroki-ditaa:../../../materials/kroki-collections/kroki-ditaa.ditaa)

#### 相关资源

- [ditaa](http://ditaa.sourceforge.net/)
- plantuml支持使用ditaa语法：[Integration of Ditaa](https://plantuml.com/zh/ditaa)
- [前言 · ditaa 學習筆記](https://jeremykao.gitbooks.io/learning-ditaa/content/)
- [【图形描述语言】ditaa | 知行近思](https://www.annhe.net/article-4000.html)
- [字符画——ditaa使用指南，文本格式下作图 - 知乎](https://zhuanlan.zhihu.com/p/429506479)

### Mermaid

> kroki-mermaid

#### Sequence diagram

![mermaid sequence diagram sample](kroki-mermaid:../../../materials/kroki-collections/kroki-mermaid-sequence-diagram.mermaid)

#### Gantt

![mermaid gantt sample](kroki-mermaid:../../../materials/kroki-collections/kroki-mermaid-gantt.mermaid)

### Nomnoml: UML diagram

> kroki-nomnoml


![nomnoml sample](kroki-nomnoml:../../../materials/kroki-collections/kroki-nomnoml.nomnoml)

#### 相关资源

- [nomnoml](https://nomnoml.com/)

### BPMN

![bpmn-js](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/bpmn-js.gif)

```admonish info title='来历'
- 业务流程模型和标记法是一套图形化表示法，用于以业务流程模型详细说明各种业务流程。 

- 它最初由业务流程管理倡议组织开发，名称为"Business Process Modeling Notation"，

> 即“业务流程建模标记法”。
```

> kroki-bpmn


![bpmn sample](kroki-bpmn:../../../materials/kroki-collections/kroki-bpmn.bpmn)

#### 相关资源

- [企业业务流程建模——BPMN - 知乎](https://zhuanlan.zhihu.com/p/59587931)
- [Web-based tooling for BPMN, DMN, CMMN, and Forms | bpmn.io](https://bpmn.io/)
- [BPMN Editor | bpmn-js modeler Demo | demo.bpmn.io](https://demo.bpmn.io/)

### Bytefield

> kroki-bytefield, 不支持引入

[//]: # (![bytefield sample]&#40;kroki-bytefield:../../../materials/kroki-collections/kroki-bytefield.bytefield&#41;)

### WaveDrom: Digital Timing diagram

> kroki-wavedrom

![wavedrom sample](kroki-wavedrom:../../../materials/kroki-collections/kroki-wavedrom.wavedrom)

### Svgbob

> kroki-svgbob

#### connected Servers

![svgbob sample](kroki-svgbob:../../../materials/kroki-collections/kroki-svgbob.svgbob)

### UMlet

```admonish info title='what is'
UMLet is a free, open-source UML tool with a simple user interface: 
draw UML diagrams fast, build sequence and activity diagrams from plain text, 
export diagrams to eps, pdf, jpg, svg, and clipboard, share diagrams using Eclipse, 
and create new, custom UML elements. UMLet runs stand-alone or as 
Eclipse plug-in on Windows, OS X and Linux.
```

> kroki-umlet

- [UMLet - Free UML Tools for fast UML diagrams](https://www.umlet.com/)

#### State machine

![kroki umlet state machine sample](kroki-umlet:../../../materials/kroki-collections/kroki-umlet-state-machine.umlet)
