# kroki合集

<!--ts-->

* [kroki合集](#kroki合集)
* [两种用法](#两种用法)
    * [kroki-&lt;target_format&gt;](#kroki-target_format)
    * [引入用法](#引入用法)
* [参考资源](#参考资源)
    * [<a href="https://kroki.io/#examples" rel="nofollow">Kroki!</a>](#kroki)
    * [<a href="https://kroki.io/examples.html" rel="nofollow">Kroki! Examples</a>](#kroki-examples)
    * [IntelliPikchr: IDEA内置插件](#intellipikchr-idea内置插件)
    * [mdbook-kroki-preprocessor: 支持kroki渲染](#mdbook-kroki-preprocessor-支持kroki渲染)
    * [kori支持范围](#kori支持范围)
        * [Block Diagram](#block-diagram)
            * [blockdiag](#blockdiag)
            * [Sequence diagram](#sequence-diagram)
            * [Activity diagram](#activity-diagram)
            * [Network diagram](#network-diagram)
        * [Packet diagram](#packet-diagram)
        * [Rack diagram](#rack-diagram)
        * [Object Oriented Graph](#object-oriented-graph)
        * [pikchr:](#pikchr)
            * [Commit Graph](#commit-graph)
            * [Syntax diagram](#syntax-diagram)
            * [Impossible trident](#impossible-trident)
        * [Entity Relationship Diagram](#entity-relationship-diagram)
        * [Excalidraw: hand-draw like diagrams](#excalidraw-hand-draw-like-diagrams)
        * [vege: word cloud](#vege-word-cloud)
        * [Diverging Stacked Bar Chart](#diverging-stacked-bar-chart)
        * [Ditaa: Conjugate prior relationships](#ditaa-conjugate-prior-relationships)
        * [Mermaid](#mermaid)
            * [Sequence diagram](#sequence-diagram-1)
            * [Gantt](#gantt)
        * [Nomnoml: UML diagram](#nomnoml-uml-diagram)
        * [Plantuml](#plantuml)
            * [use case diagram](#use-case-diagram)
            * [work breakdown structure](#work-breakdown-structure)
            * [Mind Map](#mind-map)
            * [引入文件不支持!include](#引入文件不支持include)
                * [Component diagram](#component-diagram)
                * [Context diagram](#context-diagram)
                * [Container diagram](#container-diagram)
        * [BPMN](#bpmn)
        * [Bytefield](#bytefield)
        * [WaveDrom: Digital Timing diagram](#wavedrom-digital-timing-diagram)
        * [Svgbob](#svgbob)
            * [connected Servers](#connected-servers)
        * [Structurizr](#structurizr)
            * [Contaner diagram](#contaner-diagram)
        * [UMlet](#umlet)
            * [State machine](#state-machine)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sun Jul 24 16:53:49 UTC 2022 -->

<!--te-->
![image-20220715114804075](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220715114804075.png)

# 两种用法

## kroki-<target_format>

## 引入用法

```shell

\!\[title\]\(kroki-<target_format>\:file_relativepath)
```

# 使用注意

## 样式冲突

```admonist warn title='kroki-svgbob和其他格式一起会冲突'
kroki-svgbob会引入text样式，font-size固定为14px。
就导致其他格式渲染图像出现文字重叠问题
```

# 参考资源

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

## kori支持范围

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

### Packet diagram

- [Package Diagram Tutorial | Lucidchart](https://www.lucidchart.com/pages/uml-package-diagram/#discovery__top)

> kroki-packetdiag


![packetdiag sample](kroki-packetdiag:../../../materials/kroki-collections/kroki-packetdiag.packetdiag)

### Rack diagram

> kroki-rackdiag

![rackdiag sample](kroki-rackdiag:../../../materials/kroki-collections/kroki-rackdiag.rackdiag)

### Object Oriented Graph

> kroki-graphviz

![object oriented graph](kroki-graphviz:../../../materials/kroki-collections/object-oriented-graph.graphviz)

### pikchr:

> kroki-pikchr

#### Commit Graph

![pikchr commit graph sample](kroki-pikchr:../../../materials/kroki-collections/kroki-pikchr-commit-graph.pikchr)

#### Syntax diagram

![pikchr syntax diagram sample](kroki-pikchr:../../../materials/kroki-collections/kroki-pikchr-syntax-diagram.pikchr)

#### Impossible trident

![pikchr impossible trident sample](kroki-pikchr:../../../materials/kroki-collections/kroki-pikchr-impossible-trident.pikchr)

### Entity Relationship Diagram

> kroki-erd

![erd sample](kroki-erd:../../../materials/kroki-collections/kroki-erd.erd)

### Excalidraw: hand-draw like diagrams

> kroki-excalidraw
> idea自带插件

![excalidraw sample](kroki-excalidraw:../../../materials/kroki-collections/kroki-excalidraw.excalidraw)

### vege: word cloud

> kroki-vega


![vega sample](kroki-vega:../../../materials/kroki-collections/kroki-vega.vega)

### Diverging Stacked Bar Chart

> kroki-vegalite

![vegalite sample](kroki-vegalite:../../../materials/kroki-collections/kroki-vegalite.vegalite)

### Ditaa: Conjugate prior relationships

> 支持ascii图像渲染
> kroki-ditaa


![ditaa sample](kroki-ditaa:../../../materials/kroki-collections/kroki-ditaa.ditaa)

### Mermaid

> kroki-mermaid

#### Sequence diagram

![mermaid sequence diagram sample](kroki-mermaid:../../../materials/kroki-collections/kroki-mermaid-sequence-diagram.mermaid)

#### Gantt

![mermaid gantt sample](kroki-mermaid:../../../materials/kroki-collections/kroki-mermaid-gantt.mermaid)

### Nomnoml: UML diagram

> kroki-nomnoml


![nomnoml sample](kroki-nomnoml:../../../materials/kroki-collections/kroki-nomnoml.nomnoml)

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

### BPMN

> kroki-bpmn


![bpmn sample](kroki-bpmn:../../../materials/kroki-collections/kroki-bpmn.bpmn)

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

### Structurizr

> kroki-structurizr

#### Contaner diagram

![structurizr sample](kroki-structurizr:../../../materials/kroki-collections/kroki-structurizr.structurizr)

### UMlet

> kroki-umlet

#### State machine

![kroki umlet state machine sample](kroki-umlet:../../../materials/kroki-collections/kroki-umlet-state-machine.umlet)
