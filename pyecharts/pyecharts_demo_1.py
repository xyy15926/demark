# %% [markdown]
# 基本

# %%
from pyecharts.charts import (Grid, Calendar, Funnel, Gauge, Graph, Liquid,
        Parallel, Pie, Polar, Radar, Sankey, Sunburst, ThemeRiver, WordCloud)
import datetime
import random
import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from pyecharts.globals  import WarningType, SymbolType
WarningType.ShowWarning = True

# %%
init_opts = opts.InitOpts(width="80%", height="300px")
tooltip_opts = opts.TooltipOpts(
    is_show=True,
    trigger="item",
    trigger_on="click",
    formatter="名称：{a} <br/> {b}: {c}%"
)
tooltip_opts_ax = opts.TooltipOpts(
    is_show=True,
    trigger="axis",
    trigger_on="mousemove",
    axis_pointer_type="cross"
)
label_opts = opts.LabelOpts(
    is_show=True,
    position="left",
    font_size=12,
    color="#999999",
    font_family="Micorsoft YaHei"
)
label_opts_rich = opts.LabelOpts(
    is_show=True,
    position="outside",
    formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
    background_color="#eee",
    border_color="#aaa",
    border_width=1,
    border_radius=4,
    rich={
        "a": {"color": "#999", "lineHeight": 18, "align": "center"},
        "abg": {
            "backgroundColor": "#e3e3e3",
            "width": "100%",
            "align": "right",
            "height": 22,
            "borderRadius": [4, 4, 0, 0],
        },
        "hr": {
            "borderColor": "#aaa",
            "width": "100%",
            "borderWidth": 0.5,
            "height": 0,
        },
        "b": {"fontSize": 12, "lineHeight": 18},
        "per": {
            "color": "#eee",
            "backgroundColor": "#334455",
            "padding": [2, 4],
            "borderRadius": 2,
        },
    },
)
itemsty_opts = opts.ItemStyleOpts(
    border_color="#ffffff",
    border_width=1
)
visualmap_opts_vertical = opts.VisualMapOpts(
    max_=2500,
    min_=10,
    pos_top="100px",
    orient="vertical",
    is_piecewise=False
),
visualmap_opts_horizontal = opts.VisualMapOpts(
    max_=2500,
    min_=10,
    orient="horizontal",
    is_piecewise=True,
    pos_left="center"
)
txt_opts = opts.TextStyleOpts(
    color="#fff"
)
title_opts = opts.TitleOpts(
    pos_top="10px",
    pos_left="center",
    title="基本图表",
    subtitle="subtitle",
    title_textstyle_opts=txt_opts
)
legend_opts_show = opts.LegendOpts(
    is_show=True,
    selected_mode="single"
)
legend_opts_hidden = opts.LegendOpts(
    is_show=False
)
linesty_opts = opts.LineStyleOpts(
    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")],
    width=10,
)
linesty_opts_curve = opts.LineStyleOpts(
    color="source",
    width=1,
    opacity=0.7,
    curve=0.3
)
axline_opts = opts.AxisLineOpts(
    linestyle_opts=linesty_opts,
)
angleax_opts_value = opts.AngleAxisOpts(
    type_="value",
    boundary_gap=True,
    start_angle=90,
    is_clockwise=True,
    interval=90,
    max_=360
)
angleax_opts_category = opts.AngleAxisOpts(
    data=Faker.animal,
    type_="category",
    boundary_gap=True,
    start_angle=0,
    is_clockwise=True
)
radiusax_opts_value = opts.RadiusAxisOpts(
    type_="value",
    boundary_gap=True,
    max_=100
)
radiusax_opts_category = opts.RadiusAxisOpts(
    data=Faker.animal,
    type_="category",
    boundary_gap=True
)
areasty_opts_opaque = opts.AreaStyleOpts(
    opacity=1
)
areasty_opts_glassy = opts.AreaStyleOpts(
    opacity=0.1
)
singleax_opts_time = opts.SingleAxisOpts(
    pos_right=10,
    pos_top=50,
    pos_bottom=50,
    # min_="2015-11-01",
    # max_="2015-12-01",
    type_="time"
)

# %% [markdown]
# 日历图

# %%
begin, end = datetime.date(2019, 1, 1), datetime.date(2020, 12, 31)
xming = [
    [str(begin + datetime.timedelta(days=d)), random.randint(10, 2500)]
    for d in range((end - begin).days + 1)
]
xhong = [
    [str(begin + datetime.timedelta(days=d)), random.randint(10, 2500)]
    for d in range((end - begin).days + 1)
]
calendar = Calendar(init_opts=init_opts)
calendar_opts = opts.CalendarOpts(
    pos_top = 120,
    pos_left =100,
    pos_right = 20,
    range_= 2020,
    yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
    monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
    daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn")
)
calendar.add(
    series_name="小明",
    yaxis_data=xming,
    is_selected=True,
    calendar_opts=calendar_opts
).add(
    series_name="小红",
    yaxis_data=xhong,
    is_selected=True,
)
calendar.set_global_opts(
    title_opts=title_opts,
    visualmap_opts=visualmap_opts_vertical
)

calendar.render_notebook()
# calendar.render("C:/Users/xyy15926/Desktop/sample.html")

# %% [markdown]
# 漏斗图

# %%
funnel = Funnel()
funnel.add(
    series_name = "产品",
    data_pair=[list(itm) for itm in zip(Faker.choose(), Faker.values())],
    gap=2,
    sort_="ascending",
    tooltip_opts=tooltip_opts,
    label_opts=label_opts,
    itemstyle_opts=itemsty_opts
)
funnel.set_global_opts(title_opts=title_opts)
funnel.render_notebook()

# %% [markdown]
# 仪表盘

# %%
gauge = Gauge(init_opts=init_opts)
gauge.add(
    "业务指标",
    [["完成率", 66.6]],
    split_number=5,
    axisline_opts=axline_opts,
    title_label_opts=label_opts,
    detail_label_opts=opts.LabelOpts(formatter="{value}"),
    radius="100%"
)
gauge.set_global_opts(
    legend_opts=legend_opts_hidden,
    tooltip_opts=tooltip_opts,
)
gauge.render_notebook()

# %% [markdown]
# 关系图

# %%
import itertools as itl
nodes = [
    {"name": "结点1", "symbolSize": 1},
    {"name": "结点2", "symbolSize": 2},
    {"name": "结点3", "symbolSize": 3},
    {"name": "结点4", "symbolSize": 4},
    {"name": "结点5", "symbolSize": 5},
    {"name": "结点6", "symbolSize": 4},
    {"name": "结点7", "symbolSize": 3},
    {"name": "结点8", "symbolSize": 2},
]
_node_names = [i.get("name") for i in nodes]
links = [{"source": i, "target": j, "value": 10} for i,j in itl.product(_node_names, _node_names)]
graph = Graph()
graph.add(
    "",
    nodes,
    links,
    repulsion=[0, 100],
    edge_label=opts.LabelOpts(
        is_show=True,
        position="middle",
        formatter="{b}'s > {c}"
    )
)
graph.render_notebook()


# %%
nodes_data = [
    opts.GraphNode(name="结点1", symbol="image://googlelogo.png", symbol_size=20),
    opts.GraphNode(name="结点2", symbol_size=2),
    opts.GraphNode(name="结点3", symbol_size=3),
    opts.GraphNode(name="结点4", symbol_size=4),
    opts.GraphNode(name="结点5", symbol_size=5),
    opts.GraphNode(name="结点6", symbol_size=6),
]
links_data = [
    opts.GraphLink(source="结点1", target="结点2", value=20),
    opts.GraphLink(source="结点2", target="结点3", value=30),
    opts.GraphLink(source="结点3", target="结点4", value=40),
    opts.GraphLink(source="结点4", target="结点5", value=50),
    opts.GraphLink(source="结点5", target="结点6", value=60),
    opts.GraphLink(source="结点6", target="结点1", value=70),
    opts.GraphLink(source="结点6", target="结点1", value=70),
    opts.GraphLink(source="结点5", target="结点3", value=70),
    opts.GraphLink(source="结点4", target="结点1", value=70),
]
graph = Graph(init_opts=init_opts)
graph.add(
    "",
    nodes_data,
    links_data,
    layout="circular",
    repulsion=[0,100],
    edge_label=opts.LabelOpts(
        is_show=True,
        position="middle",
        formatter="{b}'s > {c}"
    )
)
graph.set_global_opts(
    title_opts=title_opts
)
graph.render_notebook()


# %%
import json
with open("les-miserables.json", encoding="utf-8") as j:
    j = json.load(j)
    nodes, links, categories = j["nodes"], j["links"], j["categories"]
graph = Graph(init_opts=init_opts)
graph.add(
    "",
    nodes=nodes,
    links=links,
    categories=categories,
    layout="circular",
    is_rotate_label=True,
    linestyle_opts=linesty_opts_curve,
    label_opts=opts.LabelOpts(position="middle")
)
graph.render_notebook()


# %%
import json
with open("weibo.json", encoding="utf8") as j:
    nodes, links, categories, cnt, mid, userl = json.load(j)
graph = Graph(init_opts=opts.InitOpts(
    width="100%",
    height="1000px"
))
graph.add(
    "",
    nodes=nodes,
    links=links,
    categories=categories,
    repulsion=50,
    linestyle_opts=linesty_opts_curve,
    label_opts=opts.LabelOpts(is_show=False)
)
graph.set_global_opts(
    legend_opts = legend_opts_hidden
)
graph.render()


# %%
data = json.load(open("npmdepgraph.min10.json", encoding="utf8"))
nodes = [
    {
        "x": node["x"],
        "y": node["y"],
        "id": node["id"],
        "name": node["label"],
        "symbolSize": node["size"],
        "itemStyle": {"normal": {"color": node["color"]}}
    } for node in data["nodes"]
]
edges = [{"source": edge["sourceID"], "target": edge["targetID"]} for edge in data["edges"]]
graph = Graph(init_opts=opts.InitOpts(
    width="100%",
    height="1000px"
))
graph.add(
    "",
    nodes=nodes,
    links=edges,
    layout="none",
    is_roam=True,
    is_focusnode=True,
    label_opts=opts.LabelOpts(is_show=False),
    linestyle_opts=linesty_opts_curve
).render_notebook()


# %%
liquid1 = Liquid(init_opts=init_opts)
liquid1.add(
    "",
    [0.6, 0.6, 0.8],
    is_outline_show=False,
    shape=SymbolType.RECT,
    center=["60%", "50%"]
)
liquid2 = Liquid().add(
    "",
    [0.3254],
    center=["25%", "50%"],
    label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),
)
grid = Grid().add(liquid1, grid_opts=opts.GridOpts()).add(liquid2, grid_opts=opts.GridOpts())
grid.render_notebook()


# %%
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
parallel = Parallel(init_opts=init_opts)
parallel.add_schema(schema=schema).add("", data)
parallel.render_notebook()

# %% [markdown]
# Pie

# %%
pie = Pie()
data_pair = [list(z) for z in zip(Faker.choose(), Faker.values())]
pie.add(
    "a",
    data_pair,
    rosetype="radius",
    radius=["60%", "80%"],
    center=["50%", "50%"],
    label_opts=label_opts_rich,
),
pie.add(
    "b",
    data_pair[:4],
    radius=[0, 40],
    label_opts=opts.LabelOpts(position="inner")
)
# pie.set_colors(["blue", "green", "yellow", "red", "pink", "orange", "cyan"])
pie.set_series_opts(
    tooltip_opts=opts.TooltipOpts(trigger="item"))
pie.set_global_opts(
    legend_opts=opts.LegendOpts(type_="scroll", orient="vertical", pos_left="10%")
)
pie.render_notebook()

# %% [markdown]
# 极坐标

# %%
import math
data=[]
for i in range(0, 360):
    data.append([100 * math.sin(i/180 * math.pi), i])
polar_vv = Polar()
polar_vv.add(
    "",
    data,
    symbol_size=1,
).add_schema(
    radiusaxis_opts=radiusax_opts_value,
    angleaxis_opts=angleax_opts_value
).set_global_opts(tooltip_opts=tooltip_opts_ax)
polar_vv.render_notebook()


# %%
polar_radius_cat = Polar()
polar_radius_cat.add(
    "",
    list(zip(Faker.animal, Faker.values())),
    type_="bar"
).add_schema(
    radiusaxis_opts=radiusax_opts_category,
    angleaxis_opts=angleax_opts_value
)
polar_radius_cat.render_notebook()


# %%
polar_angle_cat = Polar()
polar_angle_cat.add_schema(
    radiusaxis_opts=radiusax_opts_value,
    angleaxis_opts=angleax_opts_category
).add("A", list(zip([i % 30 for i in Faker.values()], Faker.animal)), type_="bar", stack="g1") \
.add("B", list(zip([i % 30 for i in Faker.values()], Faker.animal)), type_="bar", stack="g1") \
.add("C", list(zip([i % 30 for i in Faker.values()], Faker.animal)), type_="bar", stack="g1")
polar_angle_cat.render_notebook()


# %%
radar = Radar()
radar.set_colors(["#4587E7"])
radar.add_schema(
    schema=[opts.RadarIndicatorItem(name=_k, max_=150) for _k in list("ABCDEFG")],
    shape="circle",
    # center=["50%", "80%"],
    radius="80%",
    angleaxis_opts=opts.AngleAxisOpts(
        min_=0,
        max_=360,
        is_clockwise=False,
        # interval=5,
        axistick_opts=opts.AxisTickOpts(is_show=False),
        axislabel_opts=opts.LabelOpts(is_show=False),
        axisline_opts=opts.AxisLineOpts(is_show=False),
        splitline_opts=opts.SplitLineOpts(is_show=False),
    ),
    radiusaxis_opts=opts.RadiusAxisOpts(
        min_=0,
        max_=150,
        interval=50,
        splitarea_opts=opts.SplitAreaOpts(
            is_show=True,
            areastyle_opts=opts.AreaStyleOpts(opacity=1)
        )
    ),
    polar_opts=opts.PolarOpts(),
    splitarea_opt=opts.SplitAreaOpts(is_show=False),
    splitline_opt=opts.SplitLineOpts(is_show=False)
)
radar.add(
    "Reality",
    [Faker.values()],
    areastyle_opts=areasty_opts_glassy,
    linestyle_opts=linesty_opts_curve
).add(
    "Expectation",
    [Faker.values()],
    color="#F9713C",
    areastyle_opts=areasty_opts_glassy,
    linestyle_opts=linesty_opts_curve,
)
radar.set_global_opts(legend_opts=legend_opts_show)
radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
radar.render_notebook()


# %%
import json
with open("energy.json") as j:
    data = json.load(j)
sankey = Sankey()
sankey.add(
    "",
    is_selected=True,
    nodes=data["nodes"],
    links=data["links"],
    focus_node_adjacency="allEdges",
    node_align="left",
    levels=[
        opts.SankeyLevelsOpts(
            depth=0,
            itemstyle_opts=opts.ItemStyleOpts(color="#333333"),
            linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.6)
        ),
        opts.SankeyLevelsOpts(
            depth=1,
            itemstyle_opts=opts.ItemStyleOpts(color="#999999"),
            linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.6)
        ),
        opts.SankeyLevelsOpts(
            depth=3,
            itemstyle_opts=opts.ItemStyleOpts(color="#ffffff"),
            linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.6)
        ),
    ],
    itemstyle_opts=itemsty_opts,
    linestyle_opt=linesty_opts_curve,
    label_opts=label_opts,
    tooltip_opts=tooltip_opts
)
sankey.render_notebook()

# %% [markdown]
# Sunburst

# %%
import json
with open("drink_flavors.json") as f:
    data = json.load(f)
sunburst = Sunburst(init_opts=opts.InitOpts(width="100%"))
sunburst.add(
    "",
    data_pair=data,
    radius=[0, "95%"],
    sort_="null",
    levels=[
        {},
        {
            "r0": "15%",
            "r": "35%",
            "itemStyle": {"borderWidth": 2},
            "label": {"rotate": "tangential"},
        },
        {"r0": "35%", "r": "70%", "label": {"align": "right"}},
        {
            "r0": "70%",
            "r": "72%",
            "label": {"position": "outside", "padding": 3, "silent": False},
            "itemStyle": {"borderWidth": 3},
        },
    ],
    # label_opts=opts.LabelOpts(formatter="{b}")
).render("sunburst.html")

# %% [markdown]
# ThemeRiver

# %%
with open("themeriver.json") as j:
    data = json.load(j)
cats = list(set([i[-1] for i in data]))
themeriver = ThemeRiver()
themeriver.add(
    cats,
    data=data,
    singleaxis_opts=singleax_opts_time
)
themeriver.render_notebook()

# %% [markdown]
# WordCloud

# %%
with open("wordcloud.json", encoding="utf8") as f:
    words = json.load(f)
wordcloud = WordCloud()
wordcloud.add(
    "",
    words,
    word_size_range=[1, 55],
    shape="circle",
    textstyle_opts=txt_opts,
    mask_image="wcmask.png"
)
wordcloud.render_notebook()


# %%



