# Vega-Lite 简明语法教程

## 1."data"

&emsp;&emsp;
<font size=3>
data是用来确定绘图的数据。可以是通过内嵌的数值来决定，也可以通过一个url来获取数据。
</font>

```python
#通过values来进行内嵌，这里默认a代表x轴，b代表y轴
{
  "data": {
    "values": [
      {"a": "C", "b": 2},
      {"a": "C", "b": 7},
      {"a": "D", "b": 1},
      {"a": "D", "b": 2},
    ]
  }
}
```
```python
#通过url来获取数据
{
  "data": {"url": "data/seattle-weather.csv"},...
}
```      
&emsp;

## 2."mark"

&emsp;&emsp;
<font size=3>
mark是用来确定绘制图表的类型。以下给出部分Vega-Lite中能够绘制的图表类型。
</font>

```python
#通过url来获取数据
{
  "data":{...},
  "mark":"point"/"bar"/"line"/"area"/"text"/"tick"/"rect"
}
```
&emsp;&emsp;
<font size=3>
mark中对应的中文名称如下。
</font>

| 关键字 | 对应名称      |
|:--------:|:---------------:|
| point  | 散点图        |
| bar    | 条形图        |
| line   | 折线图        |
| area   | 区域填充图    |
| text   | 纯文本        |
| tick   | 刻度图        |
| rect   | 直方图/热力图 |
  

&emsp;&emsp;
<font size=3>
这里有一个<b>注意事项</b>：事实上，Vega-Lite 为数组中的<font color=red><b>每个对象</b></font>渲染<b>一个点</b>，但它们都是<b>重叠</b>的，因为我们没有<b>指定每个点的位置</b>。</font>
</font>

&emsp;&emsp;
<font size=3>
以上内容都只是对于数据进行了视觉上的编码。从上述注意事项我们可以得知：为了直观地分隔点，我们可以用channal对数据的变量进行编码，它表示点的x位置。我们可以通过添加一个对象，其键映射到描述变量的channal上。于是引入了"encoding"。
</font>

&emsp;

## 3."encoding"

&emsp;&emsp;
<font size=3>
这里"x"表示x轴，"x"中的"field"表示x轴轴名，"type"表示x轴标签名的类型。
</font>

```python
...
"encoding": 
{
  "x": {"field": "a", "type": "nominal"/"quantitative"/"temporal"/"ordinal"...}
}
...
#列出了常见的type类型
```

&emsp;&emsp;
<font size=3>
type中对应的中文名称如下。
</font>

| 关键字       | 对应名称 |
|:--------------:|:----------:|
| nominal      | 字符串   |
| quantitative | 数量     |
| temporal     | 时间日期 |
| ordinal      | 默认类型 |

&emsp;&emsp;
<font size=3>
同时，Vega-Lite还支持对数据进行聚合处理(Aggregation)。
</font>

```python
{
  "data": {
    "values": [
      {"a": "C", "b": 2}, {"a": "C", "b": 7}, {"a": "C", "b": 4},
      {"a": "D", "b": 1}, {"a": "D", "b": 2}, {"a": "D", "b": 6},
      {"a": "E", "b": 8}, {"a": "E", "b": 4}, {"a": "E", "b": 7}
    ]
  },
  "mark": "point",
  "encoding": {
    "x": {"field": "a", "type": "nominal"},
    "y": {"aggregate": "average", "field": "b", "type": "quantitative"}
  }
}
#这里的处理是对y轴的数值取平均值
```

&emsp;&emsp;
<font size=3>
如果需要对数据进行聚合处理，那么就是需要在对应的x,y中添加"aggregate"，并指出如何对数据进行处理。以下是常用的关键字。
</font>

| 关键字    | 作用         |
|:-----------:|:--------------:|
| sum       | 求和         |
| product   | 求乘积       |
| mean      | 求平均值     |
| average   | 求平均值     |
| variance  | 求样本方差   |
| variancep | 求总体方差   |
| stdev     | 求样本标准差 |
| stdevp    | 求总体标准差 |
| median    | 求中位数     |

&emsp;&emsp;
<font size=3>
在对于轴的操作中，还存在一个"bin"的选项。bin的主要作用是将数据进行分箱处理。例如离散的数据在0~100中每隔0.2或0.3刻度左右就会出现一个数据，而bin的作用则是将整个范围进行划分统计，与直方图的频数分布类似。
</font>

```python
{
  "data": {"url": "data/seattle-weather.csv"},
  "mark": "bar",
  "encoding": {
    "x": {"bin": true, "field": "precipitation"},
    "y": {"aggregate": "count"}
  }
}
```
&emsp;  

&emsp;&emsp;
<font size=3>
至此本教程结束，该教程会随着Vega-Lite的学习进度而更新，更新时间不定，后续可能会与Streamlit相结合用以快速给出可视化图形。
</font>
