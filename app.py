import streamlit as st
from rules import rules

FAQ_KEYS = ["offside", "red_card", "penalty_kick", "yellow_card", "handball_foul"]

st.set_page_config(page_title="Football Rules Explained Interactively")
st.title("Football Rules Explained Interactively")
st.write("Select a football scenario below and learn the rules!")

scenario = st.selectbox(
    "Choose a football scenario:",
    list(rules.keys()),
    format_func=lambda x: rules[x]["question"]
)

if scenario:
    st.subheader("Explanation")
    st.write(rules[scenario]["answer"])

st.markdown("## Frequently Asked Questions")
for key in FAQ_KEYS:
    st.markdown(f"**{rules[key]['question']}**  \n{rules[key]['answer']}")
