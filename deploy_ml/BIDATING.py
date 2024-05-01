
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import pandas as pd

df_sorted = pd.read_csv("data_modelada.csv")
df_sorted = df_sorted['STATE,CITY,RATING,REVIEW_COUNT,RATING_HOTEL,PREDICTED_RATING_HOTEL'].str.split(',', expand=True)
df_sorted = df_sorted.drop(df_sorted.columns[-1], axis=1)
df_sorted.columns = ['STATE', 'CITY', 'RATING', 'REVIEW_COUNT', 'RATING_HOTEL', 'PREDICTED_RATING_HOTEL']
df_sorted['RATING'] = pd.to_numeric(df_sorted['RATING'], errors='coerce')
df_sorted['RATING'] = df_sorted['RATING'].astype(float)
df_sorted['RATING_HOTEL'] = df_sorted['RATING_HOTEL'].astype(float)
df_sorted['PREDICTED_RATING_HOTEL'] = df_sorted['PREDICTED_RATING_HOTEL'].astype(float)
df_sorted['REVIEW_COUNT'] = df_sorted['REVIEW_COUNT'].astype(float)
df_sorted['REVIEW_COUNT'] = df_sorted['REVIEW_COUNT'].round()
df_sorted['REVIEW_COUNT'] = df_sorted['REVIEW_COUNT'].astype(int)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def homepage():
    title = "Visualización Modelo de Recomendación"
    subtitle = "Plan de expansión Wyndham Hotels"
    image_path = "banner.jpeg"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <h2>{subtitle}</h2>
        <img src="{image_path}" alt="Banner">
        <br>
        <a href="/MODELO"><button>Ir al Modelo</button></a>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)

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
    cc_html = cc.to_html()
    return cc_html

@app.get("/participación-consumidor", response_class=HTMLResponse)
def participación_consumidor():
    pc = df_sorted.sort_values(by= ['REVIEW_COUNT', 'RATING'], ascending= (False, False)).head(20)
    pc_html = pc.to_html()
    return pc_html

@app.get("/val-competencia", response_class=HTMLResponse)
def val_competencia():
    vc = df_sorted.sort_values(by= ['RATING_HOTEL', 'RATING'], ascending= (False, False)).head(20)
    vc_html = vc.to_html()
    return vc_html

@app.get("/participación-competencia", response_class=HTMLResponse)
def participación_competencia():
    pc = df_sorted.sort_values(by= ['RATING_HOTEL', 'REVIEW_COUNT'], ascending= (True, False)).head(20)
    pc_html = pc.to_html()
    return pc_html
