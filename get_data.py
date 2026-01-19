from urllib.request import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
from reportlab.lib import colors

data = []
URL = 'https://spaceweather.gc.ca/solar_flux_data/daily_flux_values/fluxtable.txt'
ch = '#:'

for line in urlopen(URL).readlines():
    line = line.decode('utf-8')
    if not line.isspace() and line[0] not in ch:
        try:
            data.append([float(n) for n in line.split()])
        except ValueError:
            pass

drawing = Drawing(400,200)
obsflux = [row[4] for row in data]
adjflux = [row[5] for row in data]
ursi = [row[6] for row in data]
times = [row[0] for row in data]

lp = LinePlot()        #创建折线图
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times,obsflux)),list(zip(times,adjflux)),list(zip(times,ursi))]     #x y 轴数据
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(200,150,'sunports',fontSize=14,fillColor=colors.red,textAnchor='middle'))

renderPDF.drawToFile(drawing,'sunports.pdf')
