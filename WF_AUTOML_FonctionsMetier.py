#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:13:14 2021

@author: stephane

Librairie des fonctions métiers 
"""

import pandas as pd                # a rappeler les lib utilisées dans la fonction juste avant la déclaration de ladite fonction
def extraire_la_premiere_lettre (serie):
    # Récupère une série en argument
    # retourne une dataframe pour la compatibilité de ColumnTransformer
    return pd.DataFrame(serie.str[0])
