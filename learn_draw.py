from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)      #创建一个图形，尺寸100×100
s = String(50,50,'Hello World',textAnchor='middle')    #创建一个字符串，并设置尺寸位置属性

d.add(s)       #将字符串添加到图形中

renderPDF.drawToFile(d,'hello.pdf','A simple pdf file')  #把图形转换为PDF，图形d、文件名、描述