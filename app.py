from PIL import Image
import streamlit as st
from pagina_de_depresion import mostrar_pagina_de_Depresión
from pagina_de_bipolaridad import Mostrar_pagina_de_Bipolaridad
from pagina_principal import mostrar_pagina_principal
import pickle
import numpy as np
import pandas as pd
import sklearn as sk

Navigate = st.sidebar.selectbox("Navigate",("Home","Depresión","Bipolaridad"))

Pagina = Navigate

if Pagina == "Depresión":
    mostrar_pagina_de_Depresión()
if Pagina == "Bipolaridad":
    Mostrar_pagina_de_Bipolaridad()
if Pagina == "Home":
    mostrar_pagina_principal()