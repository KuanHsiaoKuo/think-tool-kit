# think-tool-kit

> TTK: 保持批判，有所取舍，知行合一, 方见真我

<img src="https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/see_mountain.jpeg" alt="see_mountain"  />

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

## 关于快速本地实时查看vega网页

> 为了和mdbook的路径一致，在src目录下执行

```shell
npm install -g http-server
http-server -c-1
```
