import pyocr
import pyocr.builders
from PIL import Image
import re

tool = pyocr.get_available_tools()[0]


line_boxes = tool.image_to_string(
    Image.open('1.jpg'),
    lang="eng",

)




with open('test.csv', 'w') as f:
    line_boxes=line_boxes.split("\n")
    print(line_boxes)
    di= {"Invoice No.": line_boxes[19], "Date" : line_boxes[35]}
    for key in di.keys():
        f.write("%s,%s\n"%(key,di[key]))
        
f.close()


