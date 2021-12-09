
""" 
    Base de dados para poder usar melhor na aplicação
    Depois só queremos como csv mesmo pro enquanto.
"""
# %%
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt


# 91 ações da B3 #
acoes = ['PETR4.SA', 'VALE3.SA', 'CCRO3.SA', 'ITUB4.SA', 'BBDC4.SA', 'MGLU3.SA',
         'PETR3.SA', 'B3SA3.SA', 'ABEV3.SA', 'PRIO3.SA', 'BBAS3.SA', 'BIDI11.SA',
         'CSNA3.SA', 'USIM5.SA', 'GGBR4.SA', 'BPAC11.SA', 'SUZB3.SA', 'LWSA3.SA',
         'WEGE3.SA', 'RAIL3.SA', 'LREN3.SA', 'RENT3.SA', 'EQTL3.SA', 'TOTS3.SA',
         'JBSS3.SA', 'NTCO3.SA', 'AZUL4.SA', 'BRAP4.SA', 'ITSA4.SA', 'CSAN3.SA',
         'VBBR3.SA', 'VIIA3.SA', 'MULT3.SA', 'AMER3.SA', 'CVCB3.SA', 'CASH3.SA',
         'GOAU4.SA', 'BRKM5.SA', 'HAPV3.SA', 'PETZ3.SA', 'EMBR3.SA', 'ELET3.SA',
         'GNDI3.SA', 'BRFS3.SA', 'BBDC3.SA', 'BIDI4.SA', 'LAME4.SA', 'BRML3.SA',
         'COGN3.SA', 'TIMS3.SA', 'VIVT3.SA', 'MRFG3.SA', 'KLBN11.SA', 'CPFE3.SA',
         'BBSE3.SA', 'GOLL4.SA', 'ENGI11.SA', 'SULA11.SA', 'RADL3.SA', 'HYPE3.SA',
         'CMIG4.SA', 'ALPA4.SA', 'UGPA3.SA', 'RDOR3.SA', 'ECOR3.SA', 'SANB11.SA',
         'CPLE6.SA', 'ENBR3.SA', 'YDUQ3.SA', 'BPAN4.SA', 'EZTC3.SA', 'CYRE3.SA',
         'CRFB3.SA', 'TAEE11.SA', 'CIEL3.SA', 'LCAM3.SA', 'ELET6.SA', 'SBSP3.SA',
         'EGIE3.SA', 'PCAR3.SA', 'DXCO3.SA', 'IRBR3.SA', 'IGTA3.SA', 'ASAI3.SA',
         'BEEF3.SA', 'SOMA3.SA', 'ENEV3.SA', 'MRVE3.SA', 'FLRY3.SA', 'QUAL3.SA',
         'JHSF3.SA']
end = dt.datetime.now()  # fim da pandemia #
start = '2020-03-11'  # Inicio da pandemia #

df = yf.download(acoes, end, start, progress=False)

# %%
df
# %%
