import pandas as pd
import streamlit as st
import time
import datetime

st.set_page_config(layout="centered", page_icon="💸", page_title="ReuNiote")

left, right = st.columns([4, 1])
left.title("💸 ReuNiote")


left.markdown("""
    Cette application permet d'estimer le cout d'une réunion et de le comptabiliser.
    """
)

right.image("https://raw.githubusercontent.com/data-cfwb/.github/main/logo_data_office.png", width=150)

form = st.form("template_form")

# nombre de personnes
nb_personnes = form.slider("Nombre de personnes présentes à la réunion", min_value=1, max_value=20, value=1, step=1)

duree = form.time_input('Durée estimée de la réunion', datetime.time(1, 00), help="Durée estimée de la réunion")

submit = form.form_submit_button("Lancer la réunion")

if submit:
    # hide the form
    form.empty()
    # show the progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    chart = st.empty()

    # start the counter
    for i in range(10000):
        st.write("Lancement de la réunion à : ", datetime.datetime.now().strftime("%H:%M:%S"), "!")
        st.write("Démarrage de la réunion comprenant {} personnes".format(nb_personnes))
        # Update progress bar.
        progress_bar.progress(i + 1)
        # Update status text.
        
        status_text.write("Temps écoulé : {} secondes".format(i))
        # Pretend we're doing some computation that takes time.
        time.sleep(0.1)
        # Update the chart.
        chart_data = pd.DataFrame(
            [[i, 100 - i], [i, 100 - i]],
            columns=["x", "y"],
        )
        chart.line_chart(chart_data)
    # launch counter
  
    # start counter
    for i in range(0, 100):
        time.sleep(1)
        # replace with progress bar
        
    # stop du timer
    if st.button("Arrêter la réunion"):
        st.write("Arrêt de la réunion")
        st.write("Fin de la réunion")
    

  
# align right
st.markdown("""
This app is a work in progress and has been made by the [Data Office](https://github.com/data-cfwb) of CFWB. 

Source code is available on [GitHub](https://github.com/data-cfwb/reuNiote/).
""")