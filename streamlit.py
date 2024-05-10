import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

@st.experimental_memo
def load_data():
    return shap.datasets.adult()

@st.experimental_memo
def load_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    d_train = xgboost.DMatrix(X_train, label=y_train)
    d_test = xgboost.DMatrix(X_test, label=y_test)
    params = {
        "eta": 0.01,
        "objective": "binary:logistic",
        "subsample": 0.5,
        "base_score": np.mean(y_train),
        "eval_metric": "logloss",
        "n_jobs": -1,
    }
    model = xgboost.train(params, d_train, 10, evals = [(d_test, "test")], verbose_eval=100, early_stopping_rounds=20)
    return model

st.title("`streamlit-shap` para exibir gráficos SHAP em uma aplicação Streamlit")

with st.expander('Sobre'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) é um componente Streamlit que fornece um wrapper para exibir gráficos [SHAP](https://github.com/slundberg/shap) no [Streamlit](https://streamlit.io/). 
                    A biblioteca é desenvolvida por [Snehan Kekre](https://github.com/snehankekre) da nossa equipe interna, que também mantém o site da [documentação do Streamlit](https://docs.streamlit.io/).
                ''')

st.header('Entrada:')
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

with st.expander('Sobre os dados'):
    st.write('Os dados do censo de adultos são usados ​​como o conjunto de dados de exemplo.')
with st.expander('X'):
    st.dataframe(X)
with st.expander('y'):
    st.dataframe(y)

st.header('Saída SHAP ')

# train XGBoost model
model = load_model(X, y)

# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Gráfico Waterfall'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Gtáfico Beeswarm'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Gráfico Force'):
    st.subheader('Primeira instância de dados')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('Primeiras 1000 instâncias de dados')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
