from pyecharts.charts import Map
import pyecharts.options as opts

json_data = {}
with open('./长沙市.json', 'r', encoding='utf-8') as f:
    json_data = f.read()
# print(json_data)
data_pair = [["长沙县", 15477.48],
             ["宁乡市", 31686.1],
             ["望城区", 6992.6],
             ["开福区", 44045.49],
             ["芙蓉区", 40689.64],
             ["浏阳市", 37659.78], ["天心区", 37659.78], ["岳麓区", 37659.78],
             ["雨花区", 45180.97], ]
(Map(init_opts=opts.InitOpts(width='1000px', height='800px'))
 .add_js_funcs("echarts.registerMap('长沙市',{});".format(json_data))
 .add(series_name="长沙市", data_pair=data_pair, maptype="长沙市")
 .set_global_opts(title_opts=opts.TitleOpts(title="长沙")
                  , visualmap_opts=opts.VisualMapOpts(split_number=6, max_=50000, range_text=['高', '低'],
                                                      range_color=['red', 'yellow', 'green']))
 .render()
 )
