from PIL import Image
import streamlit as st
from pagina_de_depresion import mostrar_pagina_de_Depresión
from pagina_de_bipolaridad import Mostrar_pagina_de_Bipolaridad
from pagina_principal import mostrar_pagina_principal
import pickle
import numpy as np
import pandas as pd
import sklearn as sk
import streamlit as st
from streamlit_option_menu import option_menu
img = Image.open("Icon.png")
st.set_page_config(page_title= "Tests de Bipolaridad y Depresión", page_icon=img)

with st.sidebar:
    selected = option_menu("Contenidos", ["Home", 'Depresión', "Bipolaridad"], 
        icons=['house', 'diamond-fill','diamond-half'], menu_icon="columns", default_index=0)
    


if selected == "Depresión":
    mostrar_pagina_de_Depresión()
if selected == "Bipolaridad":
    Mostrar_pagina_de_Bipolaridad()
if selected == "Home":
    mostrar_pagina_principal()