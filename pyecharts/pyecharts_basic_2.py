# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
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
# ### HeatMap -- 热力图

# 生成大小为24 * 7的随机数据
value = [(i, j, random.randint(0, 100)) for i in range(24) for j in range(7)]
heatmap = HeatMap()
heatmap.add_xaxis(Faker.clock)
heatmap.add_yaxis("", Faker.week, value)
heatmap.render_notebook()

# %% [markdown]
# ### Calendar -- 日历图

# 生成随机数据
begin, end = datetime.date(2019, 1, 1), datetime.date(2020, 12, 31)
dt_ming = [
    [str(begin + datetime.timedelta(days=d)), random.randint(10, 2500)]
    for d in range((end - begin).days + 1)
]
dt_hong = [
    [str(begin + datetime.timedelta(days=d)), random.randint(10, 2500)]
    for d in range((end - begin).days + 1)
]
calendar = Calendar()
calendar.add("小明", dt_ming)
calendar.add("小红", dt_hong, calendar_opts=opts.CalendarOpts(range_=2020))
# 设置热度图颜色区间
calendar.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        min_=10,
        max_=2500,
        pos_top="center"
    )
)
calendar.render_notebook()

# %% [markdown]
# ### Funnel -- 漏斗图

funnel = Funnel()
funnel.add("", list(zip(*[Faker.choose(), Faker.values()])))
funnel.render_notebook()

# %% [markdown]
# ### Gauge -- 仪表盘图

gauge = Gauge()
gauge.add("", [["OK", 75]])
gauge.render_notebook()

# %% [markdown]
# ### Liquid -- 水球图

# Liquid().add("", [0.6, 0.66]).render_notebook()
liquid_1 = Liquid().add("", [0.6, 0.65], center=["20%", "50%"])
liquid_2 = Liquid().add("", [0.3, 0.4], shape="rect", center=["80%", "50%"])
grid = Grid()
grid.add(liquid_1, grid_opts=opts.GridOpts()).add(liquid_2, grid_opts=opts.GridOpts())
grid.render_notebook()

# %% [markdown]
# ### Parallel -- 趋势变化图 

data = [
    [1, 91, 45, 125, 0.82, 34, 23, "良"],
    [2, 65, 27, 78, 0.86, 45, 29, "良"],
    [3, 83, 60, 84, 1.09, 73, 27, "良"],
    [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [8, 89, 65, 78, 0.86, 51, 26, "良"],
    [9, 53, 33, 47, 0.64, 50, 17, "良"],
    [10, 80, 55, 80, 1.01, 75, 24, "良"],
    [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
    [12, 99, 71, 142, 1.1, 62, 42, "良"],
    [13, 95, 69, 130, 1.28, 74, 50, "良"],
    [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"],
]
schema = [
    opts.ParallelAxisOpts(dim=0, name="data"),
    opts.ParallelAxisOpts(dim=1, name="AQI"),
    opts.ParallelAxisOpts(dim=2, name="PM2.5"),
    opts.ParallelAxisOpts(dim=3, name="PM10"),
    opts.ParallelAxisOpts(dim=4, name="CO"),
    opts.ParallelAxisOpts(dim=5, name="NO2"),
    opts.ParallelAxisOpts(dim=6, name="CO2"),
    opts.ParallelAxisOpts(
        dim=7,
        name="等级",
        type_="category",
        data=["优", "良", "轻度污染", "中度污染", "重度污染", "严重污染"],
    ),
]
parallel = Parallel()
# 添加坐标轴和数据
parallel.add_schema(schema=schema).add("", data)
parallel.render_notebook()

# %% [markdown]
# ### Radar -- 雷达图

radar = Radar()
radar.add_schema(schema=[opts.RadarIndicatorItem(name=_k, max_=200) for _k in list("ABCDFG")])
radar.add("Expectation", [Faker.values()]).add("Reality", [Faker.values()])
radar.render_notebook()

# %% [markdown]
# ### ThemeRiver -- 流量图

themeriver = ThemeRiver()
with open("data/themeriver.json") as j:
    data = json.load(j)
cats = list(set([i[-1] for i in data]))
themeriver.add(cats, data, singleaxis_opts=opts.SingleAxisOpts(type_="time"))
themeriver.render_notebook()

