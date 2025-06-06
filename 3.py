from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
import pyecharts.options as opts

data_dict = {}
f = open('年度数据1.csv','r',encoding='GB2312')
lines = f.readlines()
f.close()
line = lines.pop(0)
for i in lines:
    years = int(i.split(',')[0])
    name = i.split(',')[1]
    trea = float(i.split(',')[2])
    try:
        data_dict[years].append([name,trea])
    except KeyError:
        data_dict[years] = []
        data_dict[years].append([name,trea])
my_list = sorted(data_dict.keys())
timeline = Timeline({'them':ThemeType.LIGHT})
for years in my_list:
    data_dict[years].sort(key=lambda element:element[1],reverse=True)
    year_data = data_dict[years]
    name = []
    trea = []
    for name_trea in year_data:
        name.append(name_trea[0])
        trea.append(name_trea[1])
    name.reverse()
    trea.reverse()
    bar = Bar()
    bar.add_xaxis(name)
    bar.add_yaxis('2005-2016年矿产储量',trea,label_opts=opts.LabelOpts(position='right'))
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title=f'{years}矿产储量')
    )
    bar.reversal_axis()
    timeline.add(bar,str(years))
    timeline.add_schema(
        play_interval=1000,
        is_timeline_show=True,
        is_auto_play=True,
        is_loop_play=True
    )
    timeline.render('2005-2016年矿产资源.html')