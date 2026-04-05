import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------- TITLE ----------
st.title("🚗 Traffic Flow Simulation")
st.write("Simulates vehicle flow and congestion on a road")

# ---------- INPUT ----------
total_vehicles = st.number_input("Total Vehicles", 50, 1000, 200)
road_capacity = st.number_input("Road Capacity", 50, 500, 100)
entry_rate = st.slider("Vehicle Entry Rate", 1, 50, 10)
exit_rate = st.slider("Vehicle Exit Rate", 1, 50, 8)
time_steps = st.slider("Time Steps", 10, 100, 50)

# ---------- BUTTON ----------
if st.button("Run Simulation"):

    vehicles_on_road = [0]
    congestion = []

    for t in range(time_steps):

        entering = entry_rate
        exiting = min(exit_rate, vehicles_on_road[-1])

        current = vehicles_on_road[-1] + entering - exiting

        # limit by road capacity
        if current > road_capacity:
            congestion.append(current - road_capacity)
            current = road_capacity
        else:
            congestion.append(0)

        vehicles_on_road.append(current)

    # ---------- OUTPUT ----------
    st.subheader("📊 Results")

    st.write(f"Max Vehicles on Road: {int(max(vehicles_on_road))}")
    st.write(f"Total Congestion: {int(sum(congestion))}")

    # ---------- GRAPH ----------
    st.subheader("📈 Traffic Graph")

    fig, ax = plt.subplots()
    ax.plot(vehicles_on_road, label="Vehicles on Road")
    ax.plot(congestion, label="Congestion")
    ax.legend()

    ax.set_xlabel("Time")
    ax.set_ylabel("Vehicles")

    st.pyplot(fig)