import streamlit as st
import pandas as pd
import numpy as np
import random
from st_clickable_images import clickable_images


def img_d(x):
    x = x.replace('-','_')
    url = "https://secure-images.nike.com/is/image/DotCom/{}_A_PREM?wid=900&resMode=sharp2&fmt=png-alpha".format(x)
    return url

styles = ['DZ4137-106','DV5464-001','FB5060-100'] ## pull sample of predicted class 3 shoes here 
imgs = (random.sample(styles, 2))

img_0 = img_d(imgs[0])
img_1 = img_d(imgs[1])

st.title('SNKRS Forecast Surveys')
clicked = clickable_images(
    [
       img_0,
       img_1
    

    ],
    titles=[imgs[0],imgs[1]],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "350px"},
)


