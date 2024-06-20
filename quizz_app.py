
import streamlit as st
import pandas as pd
import random
import time

# Función para cargar preguntas desde un archivo CSV
def cargar_preguntas(archivo_csv):
    return pd.read_csv(archivo_csv)

# Mostrar resultado con GIF
def mostrar_resultado(correcta):

    ok_list = ['https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExb20zZTFyYnZ2ZWxzMTRiZWxjOG9qajFxYWM2bjRrYndlZmtjdnIxeiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tItIlCGySM0ieKKW6b/200.webp',
               'https://media3.giphy.com/media/tsgNNs93oIbwk/200.webp?cid=790b7611i8styvuju08gd266z9syvxfyfzew5rfe99dwj0ki&ep=v1_gifs_search&rid=200.webp&ct=g',
               'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW9pcHM5YzFicXoyNDIzMzFiMnE1dzV6bXl5NzR5dG5seHAyeHU0YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7abKhOpu0NwenH3O/giphy.webp',
               'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm4wMTQybHJnaG1oNmw1Z3Q2b2d0aDMwMXF0MDd6dWFoc2hrejl2biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xQQP4ahKiyuxHy/giphy.webp',
               'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXF0Z3JscHVyNG1lYnAydGhrYmo3MDUzcmFuajBibjdidzRydHI2ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RLW9YEaSBfBMt79fm4/giphy.webp',
               'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHh5bThkMTMwNjFxb2VubjQ3amF2eGNndjl6ZnVyeWRoZWNoNm40biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Id312uyNwfrzO/giphy.webp',
               'https://media.giphy.com/media/111ebonMs90YLu/giphy.gif',
               'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmpqNW83M2VnZW0zOG9tY3V3bGZ0c2VzdjZ0eHQ1MzJpd3o0bDE1YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yJFeycRK2DB4c/giphy.webp',
               'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzh5cWxnMWFwZ3NkZnlpeGJyYXAwaGY4Z2VsdGgybjN6anBzcDVrYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pCO5tKdP22RC8/giphy.webp',
               'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDNhYm1jMGFqcnk0M3F1b2htdHhtNTVlMWt3MHVtZGRvaDUydzlmOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/q5J2HfnH8mCvS/giphy.webp'
               ]
    nok_list = ['https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3gwN3Q1ZmF6Nnp5cGRhYmNtbWw4YXozeWNhd2RueTJ6d2IxOHNvYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0HlvtIPzPdt2usKs/200.webp',
                'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWE4aWRpYWtvZXE5d3JudHNraTNhNHR3dTZwZjR3djRmYXFhdGN6cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nR4L10XlJcSeQ/200.webp',
                'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmlxM2sxeHk3enB0OTQ5enFtOWE0ZXpzajllbzZ0b3FwMXc1eGd0eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/q49YSnLzrvghiyKBAR/giphy.webp',
                'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzlpYmk2MDA0eTVqYnJmdnhncG9jdWhmZDhrZnE5dXVqcWFmdnYzaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fXnRObM8Q0RkOmR5nf/giphy.webp',
                'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExajJ1dWYxcWk4emlwcGNocHo2YXE0d29mNmF4YXRvdWk3dmxweTIwayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d2ZcfODrNWlA5Gg0/giphy.webp',
                'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWtzNHE4NWFjbWp6ZDZoYWhhbDRkaWc3N2RraHNiaWs2OHZ2YXFjNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eKrgVyZ7zLvJrgZNZn/giphy.webp',
                'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3FxN3M4NnN0Mm12NG5qdG5zMTI3MXRiM3M5eWtmYml2aDc2eDZzcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1zSz5MVw4zKg0/giphy.webp',
                'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDJnbWgyMWNmYm42NWxvNHVodm00ejI1YjJwNnAxMjNjcTNrYW9yYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/O9BPkYr89lK2A/200.webp',
                'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnU3c2I0ZDF0b3gydDd2bmZkOWphcHBndXIwcThhM3pwYTliajIyMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wofftnAdDtx4s/giphy.webp',
                'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2dtdmUwMXllNnAyazA4dDA3YnY4bDVndm85ZzdjZTdwZjR0MGRweSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ch1pcRhEb0c1y/200.webp']

    if correcta:
        st.write("¡Correcto!")
        st.image(random.choice(ok_list), width=400)
        st.session_state.puntaje += 1
    else:
        st.write("Incorrecto, ¡sigue intentando!")
        st.image(random.choice(nok_list), width=400)

    # Añadir un pequeño retraso
    time.sleep(1)
    st.session_state.mostrar_gif = False
    st.session_state.pregunta_actual += 1
    st.session_state.respuesta_seleccionada = None
    st.rerun()

# Cargar preguntas
preguntas = cargar_preguntas('https://raw.githubusercontent.com/Freegalado/cuestionario_esgrima24/main/preguntas_esgrima.csv')
num_preguntas = len(preguntas) + 1

# Inicializar estado de la aplicación
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = [None] * num_preguntas
if 'mostrar_gif' not in st.session_state:
    st.session_state.mostrar_gif = False
if 'respuesta_seleccionada' not in st.session_state:
    st.session_state.respuesta_seleccionada = None
if 'puntaje' not in st.session_state:
    st.session_state.puntaje = 0

# Estilo CSS para la imagen de fondo
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.imgur.com/kqeW2e6.png");
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Crear columnas para alinear elementos horizontalmente
col1, col2, col3 = st.columns([1, 2, 1])

# Mostrar imagen en la primera columna
with col1:
    st.image("https://i.imgur.com/3dkadPo.png", width=200)

# Mostrar imagen en la tercera columna
with col3:
    st.image("https://i.imgur.com/9VAuZT1.png", width=200)

st.markdown("<h1 style='text-align: center; font-size: 50px; font-weight: bold;'>Preguntas para el esgrima</h1>", unsafe_allow_html=True)

pregunta_actual = st.session_state.pregunta_actual

if pregunta_actual < num_preguntas:
    row = preguntas.iloc[pregunta_actual]
    st.markdown(
        f"<h2 style='text-align: center; font-size: 15px; font-weight: bold;'>Pregunta {pregunta_actual+1}: <br/>{row['pregunta']}</h2>",
        unsafe_allow_html=True
    )

    # Opciones de respuesta
    opciones = ['A', 'B', 'C', 'D']
    opciones_mapeadas = {opcion: row[opcion] for opcion in opciones}
    opciones_mostradas = [opciones_mapeadas[opcion] for opcion in opciones]
    random.shuffle(opciones_mostradas)

    # Mostrar opciones de respuesta
    #seleccionada = st.radio(
    #    "Selecciona la respuesta correcta:",
    #    options=opciones_mostradas,
    #    index=opciones_mostradas.index(st.session_state.respuesta_seleccionada) if st.session_state.respuesta_seleccionada else 0,
    #    key='respuesta',
    #    on_change=lambda: st.session_state.update({'respuesta_seleccionada': st.session_state.respuesta}),
    #    format_func=lambda x: f"**{x}**",
    #    help="Formato de opciones de respuesta"
    #

    seleccionada = st.radio(
        "Selecciona la respuesta correcta:",
        options=opciones_mostradas,
        index=opciones_mostradas.index(st.session_state.respuesta_seleccionada) if st.session_state.respuesta_seleccionada else None,
        key='respuesta',
        on_change=lambda: st.session_state.update({'respuesta_seleccionada': st.session_state.respuesta}),
        format_func=lambda x: f"**{x}**",
        help="Formato de opciones de respuesta"
    )

    if st.button('Enviar'):
        opcion_correcta = opciones_mapeadas[row['respuesta']]
        correcta = st.session_state.respuesta == opcion_correcta

        print(f"Correcta {st.session_state.respuesta_seleccionada == opcion_correcta}: {st.session_state.respuesta_seleccionada} == {opcion_correcta}")
        mostrar_resultado(correcta)
        st.session_state.respuestas[pregunta_actual] = st.session_state.respuesta_seleccionada
        st.session_state.mostrar_gif = True

else:
    # Mostrar resultados finales
    puntaje = st.session_state.puntaje
    print(num_preguntas)
    st.markdown(f"<h2 style='text-align: center; font-size: 50px;'>Has respondido correctamente {puntaje} de {num_preguntas} preguntas.</h2>", unsafe_allow_html=True)

    num_correctas = (puntaje / num_preguntas) * 100

    eft_co, cent_co,last_co = st.columns(3)
    with cent_co:
      if num_correctas == 100:
          st.balloons()
          st.image('https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdncwMzJjaGJ0cXhnZzc2ZjVuNXc2MWh2NDg1em40ZXU3NW1temFlaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yoJC2JaiEMoxIhQhY4/200.webp', width=400)
      elif (num_correctas >= 90) & (num_correctas <= 99):
          st.balloons()
          st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHgxZ2tyM3VzYXdjbWhtemU2c2twYTd3dW1rcXNjOGVxank1NzFseCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NEvPzZ8bd1V4Y/giphy.webp', width=400)
      elif (num_correctas >= 70) & (num_correctas <= 89):
          st.balloons()
          st.image('https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGN1OHdudWZiejBoZDc0Y2R6bW1yODZkZnI1MDhlOXRiOWRlemo4aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cWqLabDPjRJKf2kTFC/giphy.webp', width=400)
      elif (num_correctas >= 50) & (num_correctas <= 69):
          st.balloons()
          st.image('https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGQ4amcxYXBzdTM2dXVweThqb25maXloc2ZhcXhsNWh4dXBxcG1tdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT0xeD17zCkPu9E0Uw/giphy.webp', width=400)
      else:
          st.balloons()
          st.image('https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGljZ3M4bHZ0NWh5ZWZwZm9oeDJ2ODNwNnc0ZGtkazZweHVoZWNlMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f72BA6kQXT4uQ/giphy.webp', width=400)

    # Botón para reiniciar el cuestionario
    if st.button('Reiniciar'):
        st.session_state.pregunta_actual = 0
        st.session_state.respuestas = [None] * num_preguntas
        st.session_state.mostrar_gif = False
        st.session_state.respuesta_seleccionada = None
        st.session_state.puntaje = 0
        st.rerun()
