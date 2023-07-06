> [Rust流处理新秀，即将抗衡Flink霸主地位 - 知乎](https://zhuanlan.zhihu.com/p/620335346)



<img src="../../../../../../Migrations/writing_materials/v2-aa2920a8617696cf806d5009c7ad8e7b_1440w.jpg" style="zoom:25%;" />

`Arroyo`是一个使用Rust编写的分布式流处理引擎，旨在高效地对数据流进行有状态的计算。 与传统的批处理不同，流处理引擎可以同时处理有界和无界的数据源，并在结果可用时立即发出。

**简而言之**：`Arroyo`可让你对大量实时数据提出复杂问题，并在亚秒级时间内获得结果。

> 说到这里，感觉就是Flink在Rust中的完美替代品。如果真的可以稳定使用，那么将是Rust撼动Java在大数据流式处理计算的第一枪。

### **官方标榜主要特性有:**

- 支持SQL和Rust流水线
- 可扩展到每秒数百万事件
- 支持状态操作，如窗口和连接
- 支持状态检查点功能，以实现流水线的容错和恢复
- 通过Dataflow模型进行及时的流处理

### **用例**

- 检测欺诈和安全事件
- 实时产品和业务分析
- 实时数据摄取到您的数据仓库或数据湖中
- 实时机器学习特征生成

### **为什么选择Arroyo**

现在已经有一些现有的流引擎，包括`Apache Flink`, `Spark streaming`和`Kafka Streams`。为什么要搞一个新的呢？

官方也给出了具体的说明：（可以说非常炸裂）

- 无服务器运维：`Arroyo`管道被设计为在现代云环境中运行，支持无缝扩展、恢复和重新调度。
- 高性能SQL：SQL是一流的关注点，具有始终优秀的性能。
- 专为非专家设计：`Arroyo`从其内部实现中清晰地分离了管道API。使用者不需要成为流处理专家即可构建实时数据pipeline。

### **如何开始**

可以通过运行以下`Docker`命令来使用只有单个节点的`Arroyo`群集：

```shell
$ docker run -p 8000:8000 -p 8001:8001 ghcr.io/arroyosystems/arroyo-single:multi-arch
```

然后可以在浏览器打开： [http://localhost:8000](https://link.zhihu.com/?target=http%3A//localhost%3A8000/)

### **深入学习**

[官方文档](https://link.zhihu.com/?target=https%3A//doc.arroyo.dev/getting-started)：看了下，文档写的非常好

### **使用复杂SQL构建你的第一个pipeline**

[https://doc.arroyo.dev/tutorial/first-pipeline](https://link.zhihu.com/?target=https%3A//doc.arroyo.dev/tutorial/first-pipeline)

### **总结**

之前也有Rust尝试做大数据套件，但是都没有很成功的案例。 或许`Arroyo`将是第一个用`Rust`编写的分布式流处理引擎成功的案例，这样将再次证明Rust在大数据基建领域的可行性。

后面我也会继续关注`Arroyo`，并写一系列的使用教程发布到本公众号，并做一些`Flink`和`Arroyo`的深入对比。