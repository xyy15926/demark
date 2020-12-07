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
# ### Sankey

with open("data/energy.json") as j:
    data = json.load(j)
sankey = Sankey()
sankey.add("", nodes=data["nodes"], links=data["links"])
sankey.render_notebook()

# %% [markdown]
# ### Sunburst

with open("data/drink_flavors.json") as f:
    data = json.load(f)
sunburst = Sunburst()
sunburst.add("", data)
sunburst.render_notebook()
# sunburst.render("output/sunburst.html")

# %% [markdown]
# ### Graph -- 关系图

import itertools as itl
nodes = [
    {"name": "N1", "symbolSize": 1},
    {"name": "N2", "symbolSize": 2},
    {"name": "N3", "symbolSize": 3},
    {"name": "N4", "symbolSize": 4},
    {"name": "N5", "symbolSize": 5},
    {"name": "N6", "symbolSize": 4},
    {"name": "N7", "symbolSize": 3}
]
_node_names = [i.get("name") for i in nodes]
links = [{"source": i, "target": j, "value": 10} for i,j in itl.product(_node_names, _node_names)]
graph = Graph()
graph.add("", nodes, links)
graph.render_notebook()

# %% [markdown]
# ### KLine -- K线图

with open("data/candlestick.json", encoding="utf8") as j:
    ori_data = json.load(j)
    data = {
        "data": [rec[1:] for rec in ori_data],
        "times": [rec[0] for rec in ori_data],
        "vols": [int(rec[5]) for rec in ori_data],
        "macds": [rec[7] for rec in ori_data],
        "difs": [rec[8] for rec in ori_data],
        "deas": [rec[9] for rec in ori_data]
    }
kline = Kline()
kline.add_xaxis(data["times"][-100:])
kline.add_yaxis("", data["data"][-100:])
kline.render_notebook()

# %% [markdown]
# ### WordCloud -- 词云图

with open("data/wordcloud.json", encoding="utf8") as f:
    words = json.load(f)
wordcloud = WordCloud()
wordcloud.add("", words)
wordcloud.render_notebook()

# %% [markdown]
# ### Timeline

with open("data/gdp.json") as j:
    total_data = json.load(j)
provs = total_data["name_list"]
for idx in list(total_data.keys())[1:]:
    for year in total_data[idx].keys():
        total_data[idx][year] = [{"name": prov, "value": value} for prov, value in zip(provs, total_data[idx][year])]
# 绘制2002 - 2011年各省份GDP柱状图，并添加至时间轴
timeline = Timeline()
for year in range(2002, 2012):
    bar = Bar().add_xaxis(provs)
    for name, namek in [("GDP", "data_gdp"), ("金融", "data_financial"), ("房地产", "data_estate"), ("第一产业", "data_pi"), ("第二产业", "data_si"), ("第三产业", "data_ti")]:
        bar.add_yaxis(
            series_name=name,
            y_axis=total_data[namek][str(year)],
            label_opts=opts.LabelOpts(is_show=False)
        )
    bar.set_global_opts(tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"))
    timeline.add(bar, str(year))
timeline.render_notebook()
# timeline.render("output/timeline.html")

# %% [markdown]
# ### Tree -- 树

data = [
    {
        "children": [
            {"name": "B"},
            {
                "children": [{"children": [{"name": "I"}], "name": "E"}, {"name": "F"}],
                "name": "C",
            },
            {
                "children": [
                    {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                    {"name": "H"},
                ],
                "name": "D",
            },
        ],
        "name": "A",
    }
]
tree = Tree()
tree.add("", data).render_notebook()


# %% [markdown]
# #### MapTree

data = [
    {"value": 40, "name": "我是A"},
    {
        "value": 180,
        "name": "我是B",
        "children": [
            {
                "value": 76,
                "name": "我是B.children",
                "children": [
                    {"value": 12, "name": "我是B.children.a"},
                    {"value": 28, "name": "我是B.children.b"},
                    {"value": 20, "name": "我是B.children.c"},
                    {"value": 16, "name": "我是B.children.d"},
                ],
            }
        ],
    },
]
maptree = TreeMap()
maptree.add("", data).render_notebook()

