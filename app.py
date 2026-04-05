import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------- PAGE ----------
st.set_page_config(page_title="AI App Growth", layout="centered")

st.title("📈 AI App User Growth Model")

st.write("This app shows user growth using Logistic Growth Model")

# ---------- INPUT ----------
K = st.slider("Market Size (K)", 1000, 100000, 50000)
P0 = st.slider("Initial Users (P0)", 10, 1000, 100)
r = st.slider("Growth Rate (r)", 0.01, 1.0, 0.2)
days = st.slider("Days", 10, 100, 50)

# ---------- MODEL ----------
t = np.linspace(0, days, days)

users = K / (1 + ((K - P0) / P0) * np.exp(-r * t))

# ---------- OUTPUT ----------
st.subheader("📊 Result")

st.write("Peak Users:", int(max(users)))

# ---------- GRAPH ----------
fig, ax = plt.subplots()

ax.plot(t, users)
ax.set_xlabel("Days")
ax.set_ylabel("Users")
ax.set_title("User Growth Curve")

st.pyplot(fig)