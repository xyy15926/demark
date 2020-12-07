# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ##  PyCharts基本图表

# %%
from pyecharts import options as opts 
from pyecharts.charts import (Bar, Line, Pie, Line, Boxplot, Scatter,
    Grid, Kline, Calendar, Funnel, Gauge, Graph, Liquid, Parallel, EffectScatter,
    Polar, Radar, Sankey, Sunburst, ThemeRiver, WordCloud, Timeline, Tree, TreeMap)
from pyecharts.faker import Faker 
from pyecharts.commons.utils import JsCode
from pyecharts.globals import WarningType, SymbolType
import datetime
import random
import json

# %% [markdown]
# ### Bar -- 条形图

bar = Bar()
# 添加x轴
bar.add_xaxis(Faker.animal)
bar.add_yaxis("zoo1", Faker.values())
bar.add_yaxis("zoo2", Faker.values())
bar.render_notebook()

# %% [markdown]
# #### 堆叠条形图

bar = Bar()
# 添加x轴
bar.add_xaxis(Faker.animal)
# 添加2组y轴数据
# `stack` 指明所属堆叠组
bar.add_yaxis("zoo1", Faker.values(), stack="s1")
bar.add_yaxis("zoo2", Faker.values(), stack="s1")
bar.render_notebook()

# %% [markdown]
# ### 线图

line = Line()
line.add_xaxis(Faker.choose())
line.add_yaxis("A", Faker.values()).add_yaxis("B", Faker.values())
line.render_notebook()

# %% [markdown]
# ### Pie -- 饼图

pie = Pie()
# 添加数据，格式为`[(name, value), ...]`
pie.add("", list(zip(Faker.choose(), Faker.values())))
pie.render_notebook()

# %% [markdown]
# #### 环形玫瑰图

pie = Pie()
pie.add(
    "Cat1",
    list(zip(Faker.choose(), Faker.values())),
    # 设置饼图（环形图）半径范围，单位为百分比
    radius=[0, 40]
)
pie.add(
    "Cat2",
    list(zip(Faker.choose(), Faker.values())),
    rosetype="radius",
    radius=[60, 100]
)
pie.render_notebook()

# %% [markdown]
# ### Scatter -- 散点图

scatter = Scatter()
scatter.add_xaxis(Faker.choose())
scatter.add_yaxis("cat1", Faker.values())
scatter.add_yaxis("cat2", Faker.values())
scatter.render_notebook()

# %% [markdown]
# #### Scatter -- 气泡图（大小标识数量）

scatter = Scatter()
scatter.add_xaxis(Faker.choose())
scatter.add_yaxis("cat1", Faker.values())
scatter.add_yaxis("cat2", Faker.values())
scatter.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        type_="size"
    )
)
scatter.render_notebook()

# %% [markdown]
# #### EffectScatter -- 涟漪散点图

effect_scatter = EffectScatter()
effect_scatter.add_xaxis(Faker.choose())
effect_scatter.add_yaxis("", Faker.values(), symbol=SymbolType.ARROW)
effect_scatter.render_notebook()

# %% [markdown]
# ### Boxplot -- 箱线图

boxplot = Boxplot()
boxplot.add_xaxis(Faker.choose())
# 计算数据的最大、最小、中位、四分位数
dt1 = boxplot.prepare_data(list(zip(*[Faker.values() for i in range(20)])))
dt2 = boxplot.prepare_data(list(zip(*[Faker.values() for i in range(20)])))
boxplot.add_yaxis("cat1", dt1)
boxplot.add_yaxis("cat2", dt2)
boxplot.render_notebook()

# %% [markdown]
# ### Polar -- 极坐标

import math
data=[]
# 生成数据，满足格式`[r, \theta]`，即可以认为角度为自变量、径向为因变量
for i in range(0, 360):
    data.append([100 * math.sin(i/180 * math.pi), i])
polar = Polar()
polar.add("", data)
# 调整角度坐标轴样式
polar.add_schema(
    angleaxis_opts=opts.AngleAxisOpts(
        interval=90,
        max_=360
    )
)
polar.render_notebook()

# %% [markdown]
# #### 极坐标柱状图

polar = Polar()
polar.add("", list(zip(Faker.choose(), Faker.values())), type_="bar")
polar.add_schema(
    radiusaxis_opts=opts.RadiusAxisOpts(type_="category"),
    angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True)
)
polar.render_notebook()

# %% [markdown]
# #### 极坐标玫瑰图

polar = Polar()
polar.add("A", list(zip(Faker.values(), Faker.animal)), type_="bar", stack="g1")     .add("B", list(zip(Faker.values(), Faker.animal)), type_="bar", stack="g1")     .add("C", list(zip(Faker.values(), Faker.animal)), type_="bar", stack="g1")
# 添加分类型角度坐标轴
polar.add_schema(angleaxis_opts=opts.AngleAxisOpts(type_="category"))
polar.render_notebook()

