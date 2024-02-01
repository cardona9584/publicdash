import streamlit as st
import pandas as pd 



# Write directly to the app
st.title("Example Streamlit App :balloon:")

url="https://pasteur.epa.gov/uploads/10.23719/1528686/SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv"
df =pd.read_csv(url)


df['Supply Chain Emission Factors without Margins'].fillna(0, inplace=True)
df['Supply Chain Emission Factors without Margins'] = df['Supply Chain Emission Factors without Margins'].astype(str)



Emissions = st.slider(
    "Supply Chain Emission Factors without Margins",
    min_value=0.1,
    max_value=2.0,
    value=(0.1,2.0),
    step=0.2
)


start_sec = min(Emissions)
end_sec = max(Emissions)

filtro_emisiones = f"`Supply Chain Emission Factors without Margins` >= '{start_sec}' and `Supply Chain Emission Factors without Margins`<= '{end_sec}'"
filtered_df= df.query(filtro_emisiones)







st.write(filtered_df)


