向量数据库主要用于存储和查询高维度向量。在自然语言处理（NLP）、计算机视觉或推荐系统等领域，数据（例如文本、图像或用户行为）常常会被转化为高维度向量（即embedding），这些向量就被存储在向量数据库中。所以，向量数据库主要包含以下几个部分：

1. **向量数据**：数据库中最主要的部分就是向量数据，它们通常是由embedding模型生成的高维向量。

2. **向量索引**：由于向量数据的高维性和大规模性，直接在所有向量上进行搜索是非常耗时的。因此，向量数据库通常会建立一个特定的索引结构（如K-D树、球树、哈希等），以加速向量的查找和比较。

3. **元数据**：元数据是与向量相关的额外信息。例如，在一个文本搜索系统中，每个向量可能对应一个文档，那么这个文档的标题、作者、发布日期等信息就是元数据。

4. **查询接口**：向量数据库还会提供一些查询接口，允许用户根据指定的相似度度量（如余弦相似性、欧氏距离等）来查询最相似的向量。

5. **数据管理接口**：此外，向量数据库还会提供接口来插入新的向量、删除现有向量、更新向量等。

常见的向量数据库包括Faiss（Facebook AI开发）、Milvus、Annoy（Spotify开发）等。这些数据库在处理大规模的嵌入查询问题上都非常高效，被广泛用于各种AI应用。