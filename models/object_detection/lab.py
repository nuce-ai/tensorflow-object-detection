import os
import pandas as pd 
from object_detection_processing import output_object_detection

image_path = "E:\\nuce-ai\\object-detection\\object_detection\\test_images\\image2.jpg"
results = output_object_detection(image_path)

x = results['coordinates']
y = results['labels']

df_ = pd.DataFrame(y,columns=['label'])
df =pd.DataFrame(x,columns=['ymin','xmin','ymax','xmax'])
df = df.join(df_)

output = 'E:/nuce-ai/server/tensorflow'
df.to_json(output + '/test.json',orient='records')