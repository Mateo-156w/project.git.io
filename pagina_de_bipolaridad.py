
import streamlit as st
import sklearn as sk
import pickle
import numpy as np

def load_model():
    with open("saved_stepsC.pkl", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()
model = data["model"]
le_criterio1 = data["le_criterio1"]
le_criterio2 = data["le_criterio2"]
le_criterio3 = data["le_criterio3"]
le_criterio4 = data["le_criterio4"]
le_criterio5 = data["le_criterio5"]
le_criterio6 = data["le_criterio6"]
le_criterio7 = data["le_criterio7"]
le_criterio8 = data["le_criterio8"]

def Mostrar_pagina_de_Bipolaridad():
    st.title("Test de Bipolaridad")
    st.subheader("Para un diagnóstico de trastorno bipolar I, es necesario que se cumplan los criterios siguientes para un episodio maníaco. Antes o después del episodio maníaco pueden haber existido episodios hipomaníacos o episodios de depresión mayor.")
    
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
    Tipo =(
        "Si",
        "No"
    )
    


    Respuesta1 = st.selectbox("¿Últimamente ha notado que su autoestima se elevó (su seguridad se elevó y sus pensamientos sobre sí mismo son de grandeza)?", Criterio1,)
    Respuesta2 = st.selectbox("¿Últimamente ha notado una disminución de su necesidad de dormir(ej se siente bien tan solo durmiendo 3 horas)?", Criterio2,)
    Respuesta3 = st.selectbox("¿Últimamente le han dicho que está hablando más de lo normal y que presiona para mantener una conversación?", Criterio3,)
    Respuesta4 = st.selectbox("¿Últimamente ha notado que sus ideas aparecen de forma fugaz teniendo cambios bruscos de estas(cambia de tema de forma repentina)? Estos cambios ocurren antes de que una idea haya sido finalizada", Criterio4,)
    Respuesta5 = st.selectbox("¿Últimamente ha notado que su atención cambia de forma repentina con cosas irrelevantes y que no puede mantener su atención de forma sencilla?(Esto tambien tiene o tuvo que ser notado por otras personas)", Criterio5,)
    Respuesta6 = st.selectbox("¿Últimamente ha notado su actividad dirigida a un objetivo ej.estudiar/entrenar/jugar más de lo normal) o se ha sentido inquieto o realizando movimientos que no tienen propósito como frotarse la piel o tirar de su ropa?", Criterio6,)
    Respuesta7 = st.selectbox("¿Últimamente ha realizado actividades con un riesgo alto de forma desenfrenada (ej. Ha gastado mucho dinero en compras de forma compulsiva)?", Criterio7,)
    Respuesta8 = st.selectbox("¿Ha presentado un episodio de depresión mayor?", Criterio8,)
    TipodeBi = st.selectbox("Los síntomas presentados fueron tan disruptivos que afectaron a su espacio de estudio/círculo social", Tipo)
    bipolaridad = TipodeBi

    if bipolaridad == "Si":
        bipolaridad = "1"
    if bipolaridad == "No":
        bipolaridad = "2"


    ok = st.button("Probabilidad de Tener Bipolaridad")
    if ok:
        x = np.array([[Respuesta1,Respuesta2,Respuesta3,Respuesta4,Respuesta5,Respuesta6,Respuesta7,Respuesta8]])
        x [:, 0] = le_criterio1.transform(x[:,0])
        x [:, 1] = le_criterio1.transform(x[:,1])
        x [:, 2] = le_criterio1.transform(x[:,2])
        x [:, 3] = le_criterio1.transform(x[:,3])
        x [:, 4] = le_criterio1.transform(x[:,4])
        x [:, 5] = le_criterio1.transform(x[:,5])
        x [:, 6] = le_criterio1.transform(x[:,6])
        x [:, 7] = le_criterio1.transform(x[:,7])
        x = x.astype(float)
        Probabilidad = model.predict(x)
        st.subheader(f"Usted tiene aproximadamente un {Probabilidad[0]} de padecer Bipolaridad Tipo {bipolaridad[0]}")
        

