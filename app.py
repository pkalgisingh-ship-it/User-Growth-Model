import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------- PAGE ----------
st.set_page_config(page_title="AI App Growth Model", layout="centered")

st.title("📈 AI App User Growth Simulator")
st.markdown("Simulate user growth of an AI app using Logistic Growth Model")

# ---------- SIDEBAR ----------
st.sidebar.header("⚙️ Controls")

market_size = st.sidebar.slider("Total Market Size", 100, 10000, 1000)
initial_users = st.sidebar.slider("Initial Users", 1, 500, 50)
growth_rate = st.sidebar.slider("Growth Rate (r)", 0.01, 1.0, 0.3)
drop_rate = st.sidebar.slider("Drop Rate (d)", 0.0, 0.5, 0.05)
time_steps = st.sidebar.slider("Time Steps", 10, 100, 50)

run = st.sidebar.button("🚀 Run Simulation")

# ---------- MODEL ----------
if run:

    active = [float(initial_users)]
    dropped = [0.0]

    for t in range(time_steps):

        current_active = active[-1]

        new_users = growth_rate * current_active * (1 - current_active / market_size)
        lost_users = drop_rate * current_active

        next_active = current_active + new_users - lost_users
        next_dropped = dropped[-1] + lost_users

        # Prevent negative values
        next_active = max(next_active, 0)

        active.append(next_active)
        dropped.append(next_dropped)

    # ---------- RESULTS ----------
    st.subheader("📊 Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Peak Users", int(max(active)))
    col2.metric("Final Active Users", int(active[-1]))
    col3.metric("Total Dropped Users", int(dropped[-1]))

    # ---------- GRAPH ----------
    st.subheader("📈 Growth Curve")

    fig, ax = plt.subplots()
    ax.plot(active, label="Active Users")
    ax.plot(dropped, label="Dropped Users")
    ax.set_xlabel("Time")
    ax.set_ylabel("Users")
    ax.legend()

    st.pyplot(fig)

    # ---------- INSIGHTS ----------
    st.subheader("🧠 Insights")

    if drop_rate > growth_rate:
        st.error("⚠️ Users are leaving faster than joining — unhealthy growth")
    elif max(active) > market_size * 0.8:
        st.warning("⚠️ Market saturation reached")
    else:
        st.success("✅ Healthy growth of the AI app")

else:
    st.info("👈 Set values from sidebar and run simulation")