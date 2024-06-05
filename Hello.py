import streamlit as st

st.set_page_config(
    page_title="CropSafe",
)

st.write("# CropSafe: Drought Severity Prediction Tool")

st.markdown(
"""
## About
Prolonged droughts severely impact the agriculture sector by causing crop failures and financial losses for farmers,
agribusinesses, and associated supply chains. The uncertainty and inability to predict droughts accurately make it
challenging for these stakeholders to implement effective water management and crop selection strategies in
advance, leading to inefficient use of resources and increases vulnerability to drought conditions. Water supply
companies also face challenges, as droughts can lead to water shortages, triggering costly emergency actions and
harming customer relations. Additionally, insurance companies experience a rise in claims related to agricultural
losses and water supply issues during droughts, affecting their financial health and pricing strategies.

## Objectives
This tool predicts drought severity score using a machine learning model trained on diverse meteorological and topographical data sources, including wind speeds, humidity levels, etc. This tool would help:
1. **Farmers** with precision farming tools for smarter crop and irrigation choices, adapting to upcoming drought
conditions.
2. **Insurance Companies** to craft precise, risk-reflective insurance products by integrating drought forecasts
into their models.
3. **Municipalities** to enhance water resource management through proactive conservation strategies ahead
of droughts.

## Contributors:
1. John Fitzgerald
2. Katy Shih
3. Kevin Sianto
4. Kshitiz Sahay
5. Vincent Feng
  
"""
)