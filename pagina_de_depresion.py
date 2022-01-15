
import sklearn as sk
import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("saved_stepsA.pkl", "rb") as file:
      data = pickle.load(file)
    return data

data = load_model()
model = data["model"]
le_criterio1 = data["le_criterio1"]
le_criterio2 = data["le_criterio2"]
le_criterio3 = data["le_criterio3"]
le_criterio4= data["le_criterio4"]
le_criterio5 = data["le_criterio5"]
le_criterio6 = data["le_criterio6"]
le_criterio7 = data["le_criterio7"]
le_criterio8 = data["le_criterio8"]
le_criterio9 = data["le_criterio9"]
le_criterio10 = data["le_criterio10"]

def mostrar_pagina_de_Depresion():
  st.title("Test de Depresión")
  st.subheader("Cinco (o más) de los síntomas siguientes han estado presentes durante el mismo período de dos semanas y representan un cambio del funcionamiento previo; al menos uno de los síntomas es estado de ánimo deprimido o pérdida de interés o de placer")
 
  Criterio1 = (
    "Si",
    "No"
  )
  Criterio2 = (
    "Si",
    "No"
  )
  Criterio3 = (
    "Si",
    "No"
  )
  Criterio4 = (
    "Si",
    "No"
  )
  Criterio5 = (
    "Si",
    "No"
  )
  Criterio6 = (
    "Si",
    "No"
  )
  Criterio7 = (
    "Si",
    "No"
  )
  Criterio8 = (
    "Si",
    "No"
  )
  Criterio9 = (
    "Si",
    "No"
  )
  Criterio10 = (
    "Si",
    "No"
  )
  
  Respuesta1 = st.selectbox("¿Últimamente se ha sentido decaído, triste o irritado durante la mayor parte del día siendo notable para su círculo social?", Criterio1,)
  Respuesta2 = st.selectbox("¿Últimamente ha perdido el interés o placer en actividades casi todo el día siendo notable para su círculo social?", Criterio2,)
  Respuesta3 = st.selectbox("¿Últimamente ha notado un cambio de peso corporal ya sea de aumento o disminución(esto debe representar una cantidad notable), o ha notado un aumento de apetito casi todos los días?", Criterio3,)
  Respuesta4 = st.selectbox("Últimamente ha notado insomnio(incapacidad de conciliar el sueño)?", Criterio4,)
  Respuesta5 = st.selectbox("¿Últimamente usted ha notado(esto también tiene que ser notable por su círculo social) que realiza movimientos sin finalidad alguna o que realiza acciones como hablar o moverse de forma más lenta?", Criterio5,)
  Respuesta6 = st.selectbox("¿Últimamente se ha sentido sin energía alguna o teniendo fatiga(mucho sueño y falta de energía) casi todo el día?", Criterio6,)
  Respuesta7 = st.selectbox("¿Últimamente	ha sentido una culpabilidad extrema sintiéndose como un fracaso o inutil(ej  casi todos los días?", Criterio7,)
  Respuesta8 = st.selectbox("¿Últimamente se ha sentido incapaz de concentrarse o realizar tareas simples , viendo que su capacidad para pensar se ha reducido?", Criterio8,)
  Respuesta9 = st.selectbox("¿Últimamente ha tenido pensamientos de muerte (ej. Usted cree que la única forma de liberarse del dolor emocional es la muerte o que su círculo social estaría feliz si usted muere) ha intentado suicidarse sin éxito, o en general ha presentado ideas suicidas de forma recurrente?", Criterio9,)
  Respuesta10 = st.selectbox("NO ha presentado episodios de hipomania o mania", Criterio10,)
  
  

 

  
  



  ok = st.button("Probabilidad de tener Depresion")
  if ok:
    x = np.array([[Respuesta1, Respuesta2, Respuesta3, Respuesta4, Respuesta5, Respuesta6, Respuesta7, Respuesta8, Respuesta9, Respuesta10]])
    x [:, 0] = le_criterio1.transform(x[:,0])
    x [:, 1] = le_criterio2.transform(x[:,1])
    x [:, 2] = le_criterio3.transform(x[:,2])
    x [:, 3] = le_criterio4.transform(x[:,3])
    x [:, 4] = le_criterio5.transform(x[:,4])
    x [:, 5] = le_criterio6.transform(x[:,5])
    x [:, 6] = le_criterio7.transform(x[:,6])
    x [:, 7] = le_criterio8.transform(x[:,7])
    x [:, 8] = le_criterio9.transform(x[:,8])
    x [:, 9] = le_criterio10.transform(x[:,9])
   

    x = x.astype(float)
    Probabilidad = model.predict(x)
    st.subheader(f"Usted tiene aproximadamente un {Probabilidad[0]} de padecer Depresión")
