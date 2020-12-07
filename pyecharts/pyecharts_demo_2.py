# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# 直角坐标系图表
# %% [markdown]
# 条形图（直方图）

# %%
from pyecharts import options as opts
from pyecharts.charts import (Bar, Timeline, Pie, Line, Boxplot, Scatter,
                            Grid, Kline)
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker


# %%
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
tooltip_opts = opts.TooltipOpts(
    is_show=True,
    trigger="axis",
    trigger_on="click",
    axis_pointer_type="cross"
)
rect_graph = opts.GraphicRect(
    graphic_item=opts.GraphicItem(
        left="center", top="center", z=100
    ),
    graphic_shape_opts=opts.GraphicShapeOpts(width=400, height=50),
    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
        fill="rgba(0,0,0,0.3)"
    ),
)
txt_graph = opts.GraphicText(
    graphic_item=opts.GraphicItem(
        left="center", top="center", z=100
    ),
    graphic_textstyle_opts=opts.GraphicTextStyleOpts(
        text="HAHA",
        font="bold 26px Microsoft YaHei",
        graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
            fill="#fff"
        ),
    ),
)
printer_graph_opt = opts.GraphicGroup(
    graphic_item=opts.GraphicItem(
        rotation=JsCode("Math.PI / 4"),
        bounding="raw",
        right=110,
        bottom=110,
        z=100,
    ),
    children=[rect_graph, txt_graph]
)
itemstyle_opts_jscolor=opts.ItemStyleOpts(
    color=JsCode(
"""
function(params){
    if (params.value > 0 && params.value < 50){
        return 'red';
    }else{
        return 'blue';
    }
}
""")
)
itemstyle_opts_jsall={
    "normal": {
        "color": JsCode(
"""
new echarts.graphic.LinearGradient(0, 0, 0, 1, [
    {
        offset: 0,
        color: 'rgba(0, 244, 255, 1)'
    },{
        offset: 1,
        color: 'rgba(0, 77, 167, 1)'
    }
], false)
"""
        ),
        "barBorderRadius": [30, 30, 30, 30],
        "shadowColor": "rgb(0, 160, 221)"
    }
}
itemstyle_opts = opts.ItemStyleOpts(
    color="#ec0000",
    color0="#00da3c",
    border_color="#8A0000",
    border_color0="#008F28"
)
splitarea_opts=opts.SplitAreaOpts(
    is_show=True, 
    areastyle_opts=opts.AreaStyleOpts(opacity=1)
)
datazoom_opts=[
    opts.DataZoomOpts(
        is_show=False,
        type_="inside",
        xaxis_index=[0, 0],
        range_start=0,
        range_end=100,
    ),
    opts.DataZoomOpts(
        is_show=True,
        type_="slider",
        is_realtime=False,
        orient="horizontal",
        xaxis_index=0,
        is_zoom_lock=False
    ),
        opts.DataZoomOpts(
        is_show=True,
        type_="slider",
        is_realtime=False,
        orient="vertical",
        yaxis_index=0,
        is_zoom_lock=False
    )
]

# %% [markdown]
# Bar

# %%
bar = Bar(init_opts=init_opts)
y1, y2 = Faker.values(), Faker.values()
bar.add_xaxis(Faker.animal)     .add_yaxis(
        "zoo1",
        y1,
        is_selected=True,
        stack="s1",
        category_gap="50%",
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
                opts.MarkPointItem(type_="average", name="均值")
            ]
        )
    ).add_yaxis("zoo2", y2, is_selected=False, stack="s1", category_gap="50%")

# 其他`markpoint_opts`会覆盖之前设置参数值，不是`data`补充
bar.set_series_opts(
    label_opts = opts.LabelOpts(
        position="inside",
        formatter=JsCode("function(x) {return Number(x.value / 2) + '%';}")
    ),
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
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90)),
    brush_opts=opts.BrushOpts(),
    datazoom_opts=[
        opts.DataZoomOpts(orient="vertical", pos_right="3%"),
        opts.DataZoomOpts(type_="inside")
    ],
    toolbox_opts=opts.ToolboxOpts()
)
bar.render_notebook()


# %%
import json
with open("data/gdp.json") as j:
    total_data = json.load(j)
provs = total_data["name_list"]
for idx in list(total_data.keys())[1:]:
    for year in total_data[idx].keys():
        total_data[idx][year] = [{"name": prov, "value": value} for prov, value in zip(provs, total_data[idx][year])]

def get_year_overlap_chart(year):
    bar = Bar(init_opts=init_opts).add_xaxis(xaxis_data=provs)
    for name, namek in [("GDP", "data_gdp"), ("金融", "data_financial"), ("房地产", "data_estate"), ("第一产业", "data_pi"), ("第二产业", "data_si"), ("第三产业", "data_ti")]:
        bar.add_yaxis(
            series_name=name,
            y_axis=total_data[namek][year],
            is_selected=True,
            label_opts=opts.LabelOpts(is_show=False)
        )
    bar.set_global_opts(
        tooltip_opts=tooltip_opts,
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90)),
        datazoom_opts=opts.DataZoomOpts(type_="inside")
    )
    pie = Pie().add(
        series_name="GDP占比",
        data_pair=[
            ["第一产业", sum([i["value"] for i in total_data["data_pi"][year]])],
            ["第二产业", sum([i["value"] for i in total_data["data_si"][year]])],
            ["第三产业", sum([i["value"] for i in total_data["data_ti"][year]])],
        ],
        center=["75%", "25%"],
        radius="28%"
    )
    return bar.overlap(pie)

timeline = Timeline(init_opts=init_opts)
timeline.add_schema(is_auto_play=False, play_interval=1000)
for y in range(2002, 2012):
    timeline.add(get_year_overlap_chart(str(y)), time_point=str(y))
timeline.render_notebook()


# %%
x_data = [f"11月{str(i)}日" for i in range(1, 12)]
y_total = [0, 900, 1245, 1530, 1376, 1376, 1511, 1689, 1856, 1495, 1292]
y_in = [900, 345, 393, "-", "-", 135, 178, 286, "-", "-", "-"]
y_out = ["-", "-", "-", 108, 154, "-", "-", "-", 119, 361, 203]
bar = Bar(
    init_opts=init_opts_bg,
)
bar.add_xaxis(xaxis_data=x_data)
bar.add_yaxis(
        series_name="",
        y_axis=y_total,
        stack="总量",
        itemstyle_opts=opts.ItemStyleOpts(color="rgba(0,0,0,0)"),
        yaxis_index=0,
    )
bar.add_yaxis(series_name="收入", y_axis=y_in, stack="总量", yaxis_index=0)
bar.add_yaxis(series_name="支出", y_axis=y_out, stack="总量", yaxis_index=1)
bar.set_global_opts(
    yaxis_opts=opts.AxisOpts(
        name="收入/支出",
        type_="value",
        position="left",
        axislabel_opts=opts.LabelOpts(formatter="{value} 元"),
        axistick_opts=opts.AxisTickOpts(is_show=True),
        splitline_opts=opts.SplitLineOpts(is_show=True)
    ),
    graphic_opts=[printer_graph_opt],
    tooltip_opts=tooltip_opts
)
bar.set_series_opts(
    itemstyle_opts=itemstyle_opts_jsall
)
bar.extend_axis(
    yaxis=opts.AxisOpts(
        name="余额",
        type_="value",
        axislabel_opts=opts.LabelOpts(formatter="{value} 元"),
        position="right",
        offset=40
    )
)
bar.extend_axis(
    yaxis=opts.AxisOpts(
        name="Remaint",
        type_="value",
        position="right"
    )
)
bar.add_js_funcs("img = new Image(); img.src='wcmask.png'")
line = Line().add_xaxis(xaxis_data=x_data)     .add_yaxis(
        series_name="余额",
        yaxis_index=2,
        y_axis=y_total
    )
bar.overlap(line).render_notebook()


# %%
import random
x_ori = random.choices(range(100), k=11)
x_ori = sorted(list(set(x_ori)))
x = list(zip(x_ori[:-1], x_ori[1:]))
bar_items = []
for idx, item in enumerate(x):
    if idx <= len(x) / 2:
        bar_items.append(opts.BarItem(
            name=item,
            value=100 // (item[1] - item[0]),
            itemstyle_opts=opts.ItemStyleOpts(color="#749F83")
        ))
    else:
        bar_items.append(opts.BarItem(
            name=item,
            value=100 // (item[1] - item[0]),
            itemstyle_opts=opts.ItemStyleOpts(color="#d48265")
        ))
bar = Bar().add_xaxis(x_ori)     .add_yaxis("", bar_items, category_gap=0, color=Faker.rand_color)
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        name="横坐标",
        type_="value",
        axislabel_opts=opts.LabelOpts(formatter="{value}"),
        axistick_opts=opts.AxisTickOpts(is_show=True),
        splitline_opts=opts.SplitLineOpts(is_show=True)
    )
)
bar.render_notebook()

# %% [markdown]
# Boxplot

# %%
v1 = [
    [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
    [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790],
    [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
    [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870],
]
scatter_data = [1000, 403, 404, 2000]
boxplot = Boxplot()
boxplot.add_xaxis(["expr1", "expr2", "expr3", "expr4"])
for yidx in range(10):
    boxplot.add_yaxis(
        series_name=f"A{yidx}",
        y_axis=boxplot.prepare_data(v1),
        tooltip_opts=opts.TooltipOpts(
            formatter=JsCode(
"""
function(param){
    return [
        'Experiment ' + param.name + ':',
        'idx: ' + param.data[0],
        'upper: ' + param.data[1],
        'Q1: ' + param.data[2],
        'median: ' + param.data[3],
        'Q3: ' + param.data[4],
        'lower: ' + param.data[5]
    ].join('<br/>')
}
"""
            )
        )
    )
boxplot.set_global_opts(
    tooltip_opts=tooltip_opts,
    xaxis_opts=opts.AxisOpts(
        type_="category",
        boundary_gap=True,
        splitarea_opts=opts.SplitAreaOpts(is_show=True),
        axislabel_opts=opts.LabelOpts(formatter="expr {value}"),
        splitline_opts=opts.SplitLineOpts(is_show=False)
    ),
    yaxis_opts=opts.AxisOpts(
        type_="value",
        name="km/s minus 299,000",
        splitarea_opts=opts.SplitAreaOpts(
            is_show=True,
            areastyle_opts=opts.AreaStyleOpts(opacity=1)
        )
    )
)
scatter = Scatter()
scatter.add_xaxis(["expr1", "expr2", "expr3", "expr4"])
scatter.add_yaxis("", y_axis=scatter_data)
grid = Grid()
grid.add(boxplot, grid_opts=opts.GridOpts())
grid.add(scatter, grid_opts=opts.GridOpts())
grid.render_notebook()

# %% [markdown]
# CandleStick

# %%
import json
with open("candlestick.json") as j:
    ori_data = json.load(j)
data = {
    "data": [rec[1:] for rec in ori_data],
    "times": [rec[0] for rec in ori_data],
    "vols": [int(rec[5]) for rec in ori_data],
    "macds": [rec[7] for rec in ori_data],
    "difs": [rec[8] for rec in ori_data],
    "deas": [rec[9] for rec in ori_data]
}
data["ma5"] = ["-" if idx < 4 else sum([_dt[0] for _dt in data["data"][idx-4:idx+1]])/5 for idx in range(len(data["data"]))]
vols_mark = [(0, 0, 0)]
_cur_vols = 0
for idx in range(len(data["data"])):
    if data["data"][idx][5] !=0:
        vols_mark.append(( _cur_vols, vols_mark[-1][-1], idx))
        _cur_vols = data["vols"][idx]
    else:
        _cur_vols += data["vols"][idx]
vols_mark = vols_mark[2:]


# %%
kline = Kline()
kline.add_xaxis(xaxis_data=data["times"])
kline.add_yaxis(
    series_name="",
    y_axis=data["data"],
    itemstyle_opts=itemstyle_opts,
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max", name="最大值"),
            opts.MarkPointItem(type_="min", name="最小值")
        ]
    ),
    markline_opts=opts.MarkLineOpts(
        label_opts=opts.LabelOpts(
            position="middle",
            color="blue",
            font_size=15
        ),
        data=[
            [
                {"xAxis": itm[1], "yAxis": data["data"][itm[1]][3], "value": itm[0]},
                {"xAxis": itm[2], "yAxis": data["data"][itm[2]][3]}
            ] for itm in vols_mark
        ],
        symbol=["circle", "none"]
    )
)

kline.set_global_opts(
    title_opts=opts.TitleOpts(title="Kline", pos_left="0"),
    xaxis_opts=opts.AxisOpts(
        type_="category",
        is_scale=True,
        boundary_gap=False,
        axisline_opts=opts.AxisLineOpts(is_on_zero=False),
        splitline_opts=opts.SplitLineOpts(is_show=False),
        split_number=20,
        min_="dataMin",
        max_="dataMax"
    ),
    yaxis_opts=opts.AxisOpts(
        is_scale=True,
        splitline_opts=opts.SplitLineOpts(is_show=True)
    ),
    tooltip_opts=tooltip_opts,
    datazoom_opts=[
        opts.DataZoomOpts(
            is_show=False,
            type_="inside",
            is_realtime=False,
            xaxis_index=[0, 1, 2],
            range_start=0,
            range_end=100,
        ),
        opts.DataZoomOpts(
            is_show=True,
            type_="slider",
            is_realtime=False,
            orient="horizontal",
            xaxis_index=[0, ],
            is_zoom_lock=False
        )
    ]
)

line = Line().add_xaxis(xaxis_data=data["times"])
line.add_yaxis(
    series_name="MA5",
    y_axis=data["ma5"],
    is_smooth=True,
    linestyle_opts=opts.LineStyleOpts(opacity=0.5),
    label_opts=opts.LabelOpts(is_show=False)
).set_global_opts(
    xaxis_opts=opts.AxisOpts(
        type_="category",
        grid_index=1,
        axislabel_opts=opts.LabelOpts(is_show=False)
    ),
    yaxis_opts=opts.AxisOpts(
        grid_index=0,
        split_number=3,
        axisline_opts=opts.AxisLineOpts(is_on_zero=False),
        axistick_opts=opts.AxisTickOpts(is_show=False),
        splitline_opts=opts.SplitLineOpts(is_show=False),
        axislabel_opts=opts.LabelOpts(is_show=True)
    )
)

kline.overlap(line)


# %%
bar_2 = Bar().add_xaxis(xaxis_data=data["times"])
bar_2.add_yaxis(
    series_name="MACD",
    y_axis=data["macds"],
    xaxis_index=2,
    yaxis_index=2,
    label_opts=opts.LabelOpts(is_show=False),
    itemstyle_opts=opts.ItemStyleOpts(
        color=JsCode("""
function(params){
    return (params['data'] >= 0) ? '#EF232a' : '#14B143';
}
        """)
    )
)
bar_2.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        type_="category",
        grid_index=0,
        axislabel_opts=opts.LabelOpts(is_show=False),
    ),
    yaxis_opts=opts.AxisOpts(
        grid_index=0,
        split_number=4,
        axisline_opts=opts.AxisLineOpts(is_on_zero=False),
        axistick_opts=opts.AxisTickOpts(is_show=False),
        splitline_opts=opts.SplitLineOpts(is_show=False),
        axislabel_opts=opts.LabelOpts(is_show=True),
    ),
    legend_opts=opts.LegendOpts(is_show=False),
)
line_2 = Line().add_xaxis(xaxis_data=data["times"])
line_2.add_yaxis(
    series_name="DIF",
    y_axis=data["difs"],
    xaxis_index=2,
    yaxis_index=2,
    label_opts=opts.LabelOpts(is_show=False),
).add_yaxis(
    series_name="DIF",
    y_axis=data["deas"],
    xaxis_index=2,
    yaxis_index=2,
    label_opts=opts.LabelOpts(is_show=False),
).set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
bar_2.overlap(line_2)


# %%
bar_1 = Bar().add_xaxis(xaxis_data=data["times"])
bar_1.add_js_funcs(f"var barData={data['data']};")
# bar_1.add_js_funcs("""
# var colorize=function(params){
#     var colorList;
#     if(barData[params['dataIndex']][1] > barData[params['dataIndex']][0]){
#         colorList = '#EF232a';
#     }else{
#         colorList = '#14b143';
#     }
#     return colorList;
# }
# """)
bar_1.add_yaxis(
    series_name="Volumn",
    y_axis=data["vols"],
    xaxis_index=1,
    yaxis_index=1,
    label_opts=opts.LabelOpts(is_show=False),
    itemstyle_opts=opts.ItemStyleOpts(
        color=JsCode("colorize")
    )
)
bar_1.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        type_="category",
        grid_index=1,
        axislabel_opts=opts.LabelOpts(is_show=False)
    ),
    legend_opts=opts.LegendOpts(is_show=False)
)


# %%
grid=Grid()
grid.add_js_funcs(f"var barData={data['data']}")
grid.add_js_funcs("""
var colorize=function(params){
    var colorList;
    if(barData[params['dataIndex']][1] > barData[params['dataIndex']][0]){
        colorList = '#EF232a';
    }else{
        colorList = '#14b143';
    }
    return colorList;
}
""")
grid.add(
    kline,
    grid_opts=opts.GridOpts(
        pos_left="3%",
        pos_right="1%",
        height="60%"
    )
)
grid.add(
    bar_1,
    grid_opts=opts.GridOpts(
        pos_left="3%",
        pos_right="1%",
        pos_top="71%",
        height="10%"
    )
)
grid.add(
    bar_2,
    grid_opts=opts.GridOpts(
        pos_left="3%",
        pos_right="1%",
        pos_top="82%",
        height="14%"
    )
)
grid.render("C:/Users/xyy15926/Code/statics/pyecharts/cdbl/kline.html")


# %%
def split_data_part():
    mark_line_data = []
    idx = 0
    tag = 0
    vols = 0
    for i in range(len(data["times"])):
        if data["data"][i][5] != 0 and tag == 0:
            idx = i
            vols = data["data"][i][4]
            tag = 1
        if tag == 1:
            vols += data["data"][i][4]
        if data["data"][i][5] != 0 or tag == 1:
            mark_line_data.append(
                [
                    {
                        "xAxis": idx,
                        "yAxis": float("%.2f" % data["data"][idx][3])
                        if data["data"][idx][1] > data["data"][idx][0]
                        else float("%.2f" % data["data"][idx][2]),
                        "value": vols,
                    },
                    {
                        "xAxis": i,
                        "yAxis": float("%.2f" % data["data"][i][3])
                        if data["data"][i][1] > data["data"][i][0]
                        else float("%.2f" % data["data"][i][2]),
                    },
                ]
            )
            idx = i
            vols = data["data"][i][4]
            tag = 2
        if tag == 2:
            vols += data["data"][i][4]
        if data["data"][i][5] != 0 and tag == 2:
            mark_line_data.append(
                [
                    {
                        "xAxis": idx,
                        "yAxis": float("%.2f" % data["data"][idx][3])
                        if data["data"][i][1] > data["data"][i][0]
                        else float("%.2f" % data["data"][i][2]),
                        "value": str(float("%.2f" % (vols / (i - idx + 1)))) + " M",
                    },
                    {
                        "xAxis": i,
                        "yAxis": float("%.2f" % data["data"][i][3])
                        if data["data"][i][1] > data["data"][i][0]
                        else float("%.2f" % data["data"][i][2]),
                    },
                ]
            )
            idx = i
            vols = data["data"][i][4]
    return mark_line_data


# %%
scatter = Scatter().add_xaxis(Faker.choose())
scatter.add_yaxis(
    "商家A",
    Faker.values(),
    label_opts=opts.LabelOpts(
        formatter=JsCode(
            "function(params){return params.value[1];}"
        )
    )
).add_yaxis(
    "商家B",
    Faker.values()
).set_global_opts(
    tooltip_opts=opts.TooltipOpts(
        formatter=JsCode(
            "function (params) {return params.name + ' : ' + params.value[2];}"
        )
    ),
    visualmap_opts=opts.VisualMapOpts(
        # type_="color",
        type_="size",
        max_=150,
        min_=20,
        dimension=1
    ),
    xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
    yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True))
)
scatter.render_notebook()


# %%
print(scatter.dump_options())


# %%



