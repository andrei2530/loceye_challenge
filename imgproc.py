import os
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def rgb2hex(rgb):
    hex = "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))
    return hex
 
def get_palette(img_path):
    
    CLUSTERS = 6 #number of colors to detect (max 8)

    image = Image.open(img_path)

    
    custom_width = 300
    if(image.size[0] > custom_width ): #resize image if too big
        wpercent = (custom_width/float(image.size[0]))
        hsize = int((float(image.size[1])*float(wpercent)))
        image = image.resize((custom_width,hsize), Image.ANTIALIAS)


    img_array = np.array(image)
    img_vector = img_array.reshape((img_array.shape[0] * img_array.shape[1], 3)) 

    #https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

    model = KMeans(n_clusters=CLUSTERS)
    model.fit_predict(img_vector)
    
    hex_colors = []
    for center in model.cluster_centers_:
        hex_colors.append(rgb2hex(center))

    return hex_colors
