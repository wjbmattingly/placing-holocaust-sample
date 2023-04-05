import streamlit as st
import json
import pandas as pd
st.set_page_config(layout="wide")

st.title("Sample Database Query for PH")

@st.cache_data
def load_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as f:
        firms = json.load(f)
    
    firm_names = [firms[firm]["Standard"]+f" ({firm})" for firm in firms]
    camp_names = []
    for firm, data in firms.items():
        # print(data)
        for link in data["links"]:
            camp_names.append(link[1])
    camp_names = list(set(camp_names))
    camp_names.sort()
    return firms, firm_names, camp_names
    

firms, firm_names, camp_names = load_data("data/firms_database.json")

col1, col2 = st.columns(2)
selected_firms = col1.multiselect("Select Firm(s)", firm_names)
selected_camps = col2.multiselect("Select Camp(s)", camp_names)

if selected_firms:
    firm_index = [int(firm.split("(")[-1].replace(")", "")) for firm in selected_firms]
else:
    firm_index = [int(firm) for firm in firms]
    firm_index = firm_index
st.header("Data for Firms")
firm_hits = []
for firm in firm_index:
    temp = firms[str(firm)]
    camp_links = []
    for link in temp["links"]:
        camp_links.append(link[1])
    if temp["ParentFirm"]:
        temp["ParentFirm"] = firms[str(int(temp["ParentFirm"]))]["Standard"]
    temp["links"] = camp_links
    firm_hits.append(temp)

final = []
if selected_camps:
    for hit in firm_hits:
        found = False
        for link in hit["links"]:
            if link in selected_camps:
                found=True
        if found==True:
            final.append(hit)
else:
    final = firm_hits

df = pd.DataFrame(final)
# st.markdown(df.to_markdown())
st.dataframe(df, width=1500, height=1000)
