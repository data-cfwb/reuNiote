import streamlit as st
import time
import datetime as dt
import humanize
import pytz

humanize.i18n.activate("fr_FR")

# define the timezone
tz = pytz.timezone("Europe/Brussels")


st.set_page_config(layout="centered", page_icon="💸", page_title="Coûts d'une réunion")

left, right = st.columns([4, 1])
left.title("💸 Coûts d'une réunion")

# stats of 2022-09-01
median_hourly_wage = 29.582
average_hourly_wage = 31.760

hourly_rate = 41.2

left.markdown("""
    Cette application permet d'estimer le coût réel d'une réunion pour le contribuable.
    """
)

right.image("https://raw.githubusercontent.com/data-cfwb/.github/main/logo_data_office.png", width=150)

placeholder = st.empty()
placeholder_conclusion = st.empty()

with placeholder.form("template_form"):
    col1, col2 = st.columns([3, 2])
    nb_personnes = col1.slider("Nombre de personnes présentes à la réunion", min_value=2, max_value=40, value=4, step=1)
    duree = col2.time_input('Durée estimée de la réunion', dt.time(1, 30), help="Durée estimée de la réunion")

    start_reunion = st.form_submit_button("Lancer la réunion")
    placeholder_conclusion = st.empty()


    if start_reunion:
        placeholder.empty()
        placeholder_conclusion.empty()

if start_reunion:
    # add stop button
    stop_reunion = st.button("Arrêter la réunion")

    status_text = st.empty()

    cola1, cola2 = st.columns([5, 2])

    metric_a1 = cola1.empty()
    metric_a2 = cola2.empty()

    colb1, colb2, colb3 = st.columns([3, 2, 2])

    metric_b1 = colb1.empty()
    metric_b2 = colb2.empty()
    metric_b3 = colb3.empty()
    
    start_time = dt.datetime.now(tz)
    end_time = start_time + dt.timedelta(hours=duree.hour, minutes=duree.minute)

    # convert duree to seconds
    duree_in_secs = duree.hour * 3600 + duree.minute * 60
    total_price = hourly_rate * nb_personnes * (duree_in_secs / 60 / 60)     

    my_bar = st.progress(0)

    # start the counter
    for counter in range(0, duree_in_secs):

        price = hourly_rate * nb_personnes * (counter / 60 / 60)     
        percent = (counter + 1) / duree_in_secs * 100
        diffForHumans = humanize.naturaltime(dt.datetime.now(tz) - start_time)
        
        diffForHumansStart2End = humanize.precisedelta(end_time - start_time)

        my_bar.progress(int(percent))

        #  # Update status text.
        # status_text.markdown("""
        # # La réunion a débuté.
        # """)
        status_text.info("Lancement de la réunion de " + str(nb_personnes) + " personnes à " + str(start_time.strftime("%H:%M:%S")) + " jusqu'à " + str(end_time.strftime("%H:%M:%S")) + " pour une durée prévue de " + str(diffForHumansStart2End) + ".")
    
        time.sleep(1)
        metric_a1.metric(label="🕰 Durée prévue", value=diffForHumansStart2End)
        metric_a2.metric(label="💰 Coût estimé", value="{} €".format(round(total_price, 2)), help="(hors frais d'infrastructure et frais généraux)")

        metric_b1.metric(label="🕰 A démarré", value=diffForHumans)
        metric_b2.metric(label="⏳ Complétion", value="{} %".format(str(round(percent, 1))))
        metric_b3.metric(label="💰 Coûts", value="{} €".format(round(price, 2)), delta="{} €".format(round(price - total_price, 2)), delta_color="inverse")

        
    # stop du timer
    if stop_reunion:
        # open modal
        status_text.info("Arrêt de la réunion à : " + str(dt.datetime.now().strftime("%H:%M:%S")) + "!")
        print("Arrêt de la réunion à : " + str(dt.datetime.now().strftime("%H:%M:%S")) + "!")
        placeholder_conclusion.markdown("""
            # 🎉 Félicitations, la réunion est terminée !

            """
        )

        # # show the results
        # st.write("Montant de la réunion : {} €".format(round(price, 1)))
        # st.write("Fin de la réunion à : ", dt.datetime.now().strftime("%H:%M:%S"), "!")
        # st.write("Durée de la réunion : {} minutes".format(duree_in_secs / 60))    
  
# align right
st.markdown("""
This app is a work in progress and has been made by the [Data Office](https://github.com/data-cfwb) of CFWB. 

Source code is available on [GitHub](https://github.com/data-cfwb/reuNiote/).
""")