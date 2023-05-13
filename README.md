# think-tool-kit

> TTK: 保持批判，有所取舍，知行合一, 方见真我

<img src="https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/see_mountain.jpeg" alt="see_mountain"  />

<!--ts-->


<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sat May 13 08:50:12 UTC 2023 -->

<!--te-->

## 用意

在多方面整理自己掌握的内容时，一再感受到思维工具的重要性，而这才是核心本质所在，因而起了这本书。

## 关于puml->data.json->html的转换

1. 执行scripts/puml_midmap_json.py获取data.json
2. 在data.vg.json中使用data.json
3. 在data.html中使用data.vg.json
4. 如果相对路径有变化，需要多往上走一级来验证，比如:

```shell
../../../../../layer1_visual_tools/map_tools/vega/collections/data_json/rust.json
```

- 向上走到src那个目录
- 然后一步步定位到文件

## puml与vega语法映射

1. `*` -> `#`: name
2. 链接: link
3. 悬浮弹窗注释: note, 格式为`<code>note content</code>`

- 要有`:`
- 要以`;`结尾

```puml
**:node name
<code>
note content
</code>;
```

4. 节点颜色

```json
  {
  "id": 3,
  "color": "",
  "name": "",
  "link": "",
  "parent": 1,
  "note": ""
}
```

5. 考虑到plantuml的';'是元素结束符，所以这里将'";"'换成';'
```python
   notes = [note.replace('";"', ';') for note in notes]
```

## 关于快速本地实时查看vega网页

> 为了和mdbook的路径一致，在src目录下执行

```shell
npm install -g http-server
http-server -c-1
```

## mdbook的定位是从src目录下开始的

1. 相对路径：需要向上一直走到src目录，然后再一步步定位到文件
2. 绝对路径：直接从src目录开始定位

## 关于修改路径后兼容http-server本地和mdbook在线链接的流程图。

> 目前已知mdbook在github page发布后使用静态资源需要从src目录开始定位，而且要加上项目名称。也就是

```shell
/<项目名称>/<从src开始的定位>
```

为了本地的http-server可以兼容这个路径（因为http-server在本地的src根目录运行，静态资源不带<项目名>）

> 这里使用http-proxy写了一个代理：

```text
┌─────────────┐                  ┌─────────────┐
│             │   Proxy Request  │             │
│  Client     ├─────────────────►│  Proxy      │
│             │                  │             │
└───────┬─────┘                  └───────┬─────┘
        │                                │
        │                                │
        ▼                                ▼
┌─────────────┐                  ┌─────────────┐
│             │Proxy Request with│             │
│  Proxy      │ modified req.url │  Server     │
│             ├─────────────────►│             │
└───────┬─────┘                  └───────┬─────┘
        │                                │
        │                                │
        ▼                                ▼
┌─────────────┐                  ┌─────────────┐
│             │ Server Response  │             │
│  Proxy      │◄─────────────────┤  Server     │
│             │                  │             │
└─────────────┘                  └─────────────┘
        │                                │
        │                                │
        ▼                                ▼
┌─────────────┐                  ┌─────────────┐
│             │ Proxy Response   │             │
│  Client     │◄─────────────────┤  Proxy      │
│             │                  │             │
└─────────────┘                  └─────────────┘
```

- /scripts/local_proxy_server.js

## vega强化

### 悬浮弹窗

```json
          "tooltip": {
            "signal": "{'相关笔记': datum.note}"
          }
```

### markdown渲染

