
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import pandas as pd

df_sorted = pd.read_csv("data_modelada.csv", header = 0)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def homepage():
    return "Bidating..."



@app.get("/MODELO/", response_class=HTMLResponse)
def formulario_variables():
    formulario = """
    <h1>Modelo recomendación Wyndham plan de expansión</h1>
    <h2>A continuación ingrese el criterio de recomendación a evaluar</h2>


    <form action="/caudal-consumo" method="get">
    <button type="submit">Por caudal de consumo</button>
    </form>

    <form action="/participación-consumidor" method="get">
    <button type="submit">Por participación de los consumidores</button>
    </form>

    <form action="/val-competencia" method="get">
    <button type="submit">Por valoración de competencia presente</button>
    </form>


    <form action="/participación-competencia" method="get">
    <button type="submit">Por participación de mercado de la competencia/button>
    </form>
    """
    return formulario

@app.get("/caudal-consumo", response_class=HTMLResponse)
def caudal_consumo():
    cc = df_sorted.sort_values(by= 'REVIEW_COUNT', ascending= False).head(20)
    return cc

@app.get("/participación-consumidor", response_class=HTMLResponse)
def participación_consumidor():
    pc = df_sorted.sort_values(by= ['REVIEW_COUNT', 'RATING'], ascending= (False, False)).head(20)
    return pc

@app.get("/val-competencia", response_class=HTMLResponse)
def val_competencia():
    vc = df_sorted.sort_values(by= ['RATING_HOTEL', 'RATING'], ascending= (False, False)).head(20)
    return vc

@app.get("/participación-competencia", response_class=HTMLResponse)
def participación_competencia():
    pc = df_sorted.sort_values(by= ['RATING_HOTEL', 'REVIEW_COUNT'], ascending= (True, False)).head(20)
    return pc
