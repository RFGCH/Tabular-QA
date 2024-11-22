import sqlite3
import pandas as pd

conn = sqlite3.connect('casos.db')
c = conn.cursor()

#Tabla
c.execute('''
CREATE TABLE IF NOT EXISTS casos (
    n° INTEGER PRIMARY KEY,
    fecha TEXT,
    lugar TEXT,
    actor_o_grupo_social_emisor TEXT,
    institucion_y_cargo_actor_o_grupo_social_emisor TEXT,
    actor_o_grupo_social_involucrado_1 TEXT,
    institucion_y_cargo_actor_o_grupo_social_involucrado_1 TEXT,
    acontecimiento TEXT,
    posicion TEXT,
    area TEXT,
    studio_5_studio_5_noticias_ruben_valdes_alvarado_y_paola_Reynaga_97_7 NUMBER,
    ondas_del_huallaga_noticiero_ondas_del_Huallaga_jose_carlos_ponce_de_leon_88_9 NUMBER ,
    radio_noticias_del_peru_radio_noticias_huanuco_edicion_central_bequer_bejarano_y_nuvith_condezo_celis_y_juan_malpartida_102_5 NUMBER,
    primer_plano_rnp_italo_guillermo_y_silvia_salas_102_5 NUMBER,
    radio_nacional_cuatro_suyos_ronald_caceres_y_manuel_bejarano_100_9 NUMBER,
    radio_sinai_opinion_libre_jaime_herrera_echevarria_90_1 NUMBER,
    radio_rumba_peru_rtl_noticias_koko_giles_y_juan_manuel_95_3 NUMBER,
    radio_pulsar_el_informante_miguel_angel_domínguez_100_5 NUMBER,
    radio_llata_punto_de_encuentro_carlos_chavez_firma_92_3 NUMBER,
    radio_paraiso_96_9_aires_de_tradicion_andina_hector_facundo_damazo NUMBER,
    panorama_cultural_oyonense_maximo_samaniego_radio_oyon_102_5 NUMBER,
    noticiero_musical_hector_facundo_damazo_radio_sol_oyon NUMBER,
    radio_la_altura_7_9am NUMBER,
    radio_unheval_noticiero_96_1 NUMBER
)
''')


df = pd.read_excel('../../database/bd_conocimiento.xlsx')
column_map = {
    'N°': 'n°',
    'Fecha': 'fecha',
    'Lugar': 'lugar',
    'Actor o grupo social emisor': 'actor_o_grupo_social_emisor',
    'Institución y Cargo actor o grupo social emisor': 'institucion_y_cargo_actor_o_grupo_social_emisor',
    'Actor o grupo social Involucrado 1': 'actor_o_grupo_social_involucrado_1',
    'Institución y Cargo actor o grupo social involucrado 1': 'institucion_y_cargo_actor_o_grupo_social_involucrado_1',
    'Acontecimiento': 'acontecimiento',
    'Posición': 'posicion',
    'Área': 'area',
    'Studio 5 – Studio 5 Noticias – Rubén Valdés Alvarado, Paola Reynaga (97.7)': 'studio_5_studio_5_noticias_ruben_valdes_alvarado_y_paola_reynaga_97_7',
    'Ondas del Huallaga – Noticiero Ondas del Huallaga - José Carlos Ponce de León(88.9)':'ondas_del_huallaga_noticiero_ondas_del_Huallaga_jose_carlos_ponce_de_leon_88_9',
    'Radio Noticias del Perú – Radio Noticias Huánuco Edición Central – Bequer Bejarano, Nuvith Condezo Celis, Juan Malpartida (102.5)':'radio_noticias_del_peru_radio_noticias_huanuco_edicion_central_bequer_bejarano_y_nuvith_condezo_celis_y_juan_malpartida_102_5' ,
    'Primer Plano - RNP - Ítalo Guillermo, Silvia Salas (102.5)':'primer_plano_rnp_italo_guillermo_y_silvia_salas_102_5' ,
    'Radio Nacional – Cuatro Suyos – Ronald Cáceres / Manuel Bejarano (100.9)':'radio_nacional_cuatro_suyos_ronald_caceres_y_manuel_bejarano_100_9' ,
    'Radio Sinaí - Opinión Libre - Jaime Herrera  Echevarria (90.1)':'radio_sinai_opinion_libre_jaime_herrera_echevarria_90_1' ,
    'Radio Rumba Perú - RTL Noticias - Koko Giles/ Juan Manuel (95.3)':'radio_rumba_peru_rtl_noticias_koko_giles_y_juan_manuel_95_3' ,
    'Radio Pulsar - El Informante - Miguel Angel Domínguez (100.5)':'radio_pulsar_el_informante_miguel_angel_domínguez_100_5' ,
    'Radio Llata - Punto de Encuentro - Carlos Chavez Firma(92.3)':'radio_llata_punto_de_encuentro_carlos_chavez_firma_92_3' ,
    'Radio Paraiso 96.9 - Aires de Tradición Andina - Hector Facundo Damazo':'radio_paraiso_96_9_aires_de_tradicion_andina_hector_facundo_damazo' ,
    'Panorama Cultural Oyonense - Maximo Samaniego - Radio Oyon (102.5)':'panorama_cultural_oyonense_maximo_samaniego_radio_oyon_102_5',
    'Noticiero Musical - Hector Facundo Damazo - Radio Sol - Oyon':'noticiero_musical_hector_facundo_damazo_radio_sol_oyon' ,
    'Radio La Altura 7-9am':'radio_la_altura_7_9am' ,
    'Radio UNHEVAL – Noticiero (96.1)':'radio_unheval_noticiero_96_1' ,
}


df.rename(columns=column_map, inplace=True)
df = df.map(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, pd.Timestamp) else x)

for _, row in df.iterrows():
    c.execute('''
    INSERT INTO casos (
        n°, fecha, lugar, actor_o_grupo_social_emisor, 
        institucion_y_cargo_actor_o_grupo_social_emisor, actor_o_grupo_social_involucrado_1, 
        institucion_y_cargo_actor_o_grupo_social_involucrado_1, acontecimiento, 
        posicion, area, studio_5_studio_5_noticias_ruben_valdes_alvarado_y_paola_reynaga_97_7, 
        ondas_del_huallaga_noticiero_ondas_del_Huallaga_jose_carlos_ponce_de_leon_88_9, 
        radio_noticias_del_peru_radio_noticias_huanuco_edicion_central_bequer_bejarano_y_nuvith_condezo_celis_y_juan_malpartida_102_5, 
        primer_plano_rnp_italo_guillermo_y_silvia_salas_102_5, 
        radio_nacional_cuatro_suyos_ronald_caceres_y_manuel_bejarano_100_9, 
        radio_sinai_opinion_libre_jaime_herrera_echevarria_90_1, 
        radio_rumba_peru_rtl_noticias_koko_giles_y_juan_manuel_95_3, 
        radio_pulsar_el_informante_miguel_angel_domínguez_100_5, 
        radio_llata_punto_de_encuentro_carlos_chavez_firma_92_3, 
        radio_paraiso_96_9_aires_de_tradicion_andina_hector_facundo_damazo, 
        panorama_cultural_oyonense_maximo_samaniego_radio_oyon_102_5, 
        noticiero_musical_hector_facundo_damazo_radio_sol_oyon, 
        radio_la_altura_7_9am, radio_unheval_noticiero_96_1) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', tuple(row)
    )