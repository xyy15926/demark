
# %%
import datetime
import random
from pyecharts.charts import (Grid, Calendar, Funnel, Gauge, Graph, Liquid,
        Parallel, Pie, Polar, Radar, Sankey, Sunburst, ThemeRiver, WordCloud)
import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from pyecharts.globals  import WarningType, SymbolType
WarningType.ShowWarning = True


# %% [markdown]
# ## 基本图表
# ### Bar

bar = Bar(init_opts=init_opts)
y1, y2 = Faker.values(), Faker.values()
bar.add_xaxis(Faker.animal)
bar.add_yaxis(
    "zoo1",
    y1,
    is_selected=True,
    stack="s1",
    category_gap="50%",
    # markpoints
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max", name="最大值"),
            opts.MarkPointItem(type_="min", name="最小值"),
            opts.MarkPointItem(type_="average", name="均值")
        ]
    )
)
bar.add_yaxis(
    "zoo2",
    y2,
    is_selected=False,
    stack="s1",
    category_gap="50%"
)
bar.set_series_opts(
    label_opts = opts.LabelOpts(
        position="inside",
        formatter=JsCode("function(x) {return Number(x.value / 2) + '%';}")
    ),
    # 此`markpoint_opts`会覆盖之前设置，而不是补充`data`
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(name="DIY MarkPoint", coord=[Faker.animal[2], y1[2]], value=y1[2]),
            opts.MarkPointItem(type_="max", name="最大值"),
            opts.MarkPointItem(type_="min", name="最小值"),
            opts.MarkPointItem(type_="average", name="均值")
        ]
    ),
    markline_opts=opts.MarkLineOpts(
        data=[
            opts.MarkLineItem(name="DIY MarkLine", y=50),
            opts.MarkLineItem(type_="max", name="最大值"),
            opts.MarkLineItem(type_="min", name="最小值"),
            opts.MarkLineItem(type_="average", name="均值"),
        ]
    )
)
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=90)
    ),
    brush_opts=opts.BrushOpts(),
    datazoom_opts=[
        opts.DataZoomOpts(orient="vertical", pos_right="3%"),
        opts.DataZoomOpts(type_="inside")
    ],
    toolbox_opts=opts.ToolboxOpts()
)
bar.render_notebook()


# %% [markdown]
# ## 选项
init_opts = opts.InitOpts(
    width="1000px",
    height="800px",
    theme=ThemeType.MACARONS,
    animation_opts=opts.AnimationOpts(
        animation_delay=1000,
        animation_easing="elasticOut"
    )
)
init_opts_bg = opts.InitOpts(
    theme=ThemeType.MACARONS,
    bg_color={
        "type": "pattern",
        "image": JsCode("img"),
        "repeat": "repeat"
    }
)
