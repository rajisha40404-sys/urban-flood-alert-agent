import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Urban Flood Alert Agent",
    page_icon="🌧️",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------

st.title("🌧️ Urban Flood Alert Agent")

st.write(
    "A rule-based intelligent agent that evaluates environmental "
    "conditions and estimates urban flood risk."
)

st.info(
    "ℹ️ Academic prototype: This application is designed for "
    "educational purposes and is not an official emergency warning system."
)

# -----------------------------
# Input Section
# -----------------------------

st.header("🌍 Environmental Conditions")

st.write(
    "Enter the current environmental conditions and allow the agent "
    "to determine the flood-risk level."
)

rainfall = st.selectbox(
    "🌧️ Rainfall Intensity",
    ["Low", "Moderate", "Heavy", "Very Heavy"]
)

water_level = st.selectbox(
    "💧 Water Level",
    ["Low", "Medium", "High", "Very High"]
)

drainage = st.selectbox(
    "🚧 Drainage Condition",
    ["Good", "Average", "Poor"]
)

weather_warning = st.selectbox(
    "⚠️ Weather Warning",
    ["No Warning", "Warning Issued"]
)

rain_duration = st.selectbox(
    "⏱️ Rain Duration",
    ["Short", "Medium", "Long"]
)

# -----------------------------
# Analyze Button
# -----------------------------

if st.button("🔍 Analyze Flood Risk", use_container_width=True):

    score = 0
    breakdown = []

    # Rainfall rules
    if rainfall == "Low":
        score += 1
        breakdown.append(("🌧️ Rainfall", "Low", 1))
    elif rainfall == "Moderate":
        score += 2
        breakdown.append(("🌧️ Rainfall", "Moderate", 2))
    elif rainfall == "Heavy":
        score += 3
        breakdown.append(("🌧️ Rainfall", "Heavy", 3))
    elif rainfall == "Very Heavy":
        score += 4
        breakdown.append(("🌧️ Rainfall", "Very Heavy", 4))

    # Water level rules
    if water_level == "Low":
        score += 1
        breakdown.append(("💧 Water Level", "Low", 1))
    elif water_level == "Medium":
        score += 2
        breakdown.append(("💧 Water Level", "Medium", 2))
    elif water_level == "High":
        score += 3
        breakdown.append(("💧 Water Level", "High", 3))
    elif water_level == "Very High":
        score += 4
        breakdown.append(("💧 Water Level", "Very High", 4))

    # Drainage rules
    if drainage == "Good":
        score += 0
        breakdown.append(("🚧 Drainage", "Good", 0))
    elif drainage == "Average":
        score += 2
        breakdown.append(("🚧 Drainage", "Average", 2))
    elif drainage == "Poor":
        score += 4
        breakdown.append(("🚧 Drainage", "Poor", 4))

    # Weather warning
    if weather_warning == "Warning Issued":
        score += 3
        breakdown.append(("⚠️ Weather Warning", "Warning Issued", 3))
    else:
        breakdown.append(("⚠️ Weather Warning", "No Warning", 0))

    # Rain duration
    if rain_duration == "Short":
        score += 1
        breakdown.append(("⏱️ Rain Duration", "Short", 1))
    elif rain_duration == "Medium":
        score += 2
        breakdown.append(("⏱️ Rain Duration", "Medium", 2))
    elif rain_duration == "Long":
        score += 3
        breakdown.append(("⏱️ Rain Duration", "Long", 3))

    # -----------------------------
    # Intelligent Agent Decision
    # -----------------------------

    if score <= 7:
        risk = "LOW"
        recommendation = (
            "Flood risk is currently low. Continue monitoring weather "
            "conditions and remain alert."
        )
        risk_icon = "🟢"

    elif score <= 11:
        risk = "MODERATE"
        recommendation = (
            "Moderate flood risk detected. Monitor water levels and "
            "avoid unnecessary travel through waterlogged areas."
        )
        risk_icon = "🟡"

    elif score <= 15:
        risk = "HIGH"
        recommendation = (
            "High flood risk detected. Avoid low-lying areas, stay alert "
            "for official warnings and prepare for possible evacuation."
        )
        risk_icon = "🟠"

    else:
        risk = "CRITICAL"
        recommendation = (
            "Critical flood risk detected. Move to a safer location "
            "and follow official emergency instructions."
        )
        risk_icon = "🔴"

    # -----------------------------
    # Results
    # -----------------------------

    st.divider()

    st.header("🤖 Agent Decision")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Flood Risk Level",
            f"{risk_icon} {risk}"
        )

    with col2:
        st.metric(
            "Risk Score",
            f"{score} / 18"
        )

    # Recommendation
    st.subheader("📢 Agent Recommendation")

    if risk == "CRITICAL":
        st.error(recommendation)
    elif risk == "HIGH":
        st.warning(recommendation)
    elif risk == "MODERATE":
        st.info(recommendation)
    else:
        st.success(recommendation)

    # -----------------------------
    # Decision Breakdown
    # -----------------------------

    st.subheader("🧠 Decision Breakdown")

    st.write(
        "The agent assigns risk points to each environmental condition. "
        "The points are combined to determine the final risk level."
    )

    for factor, value, points in breakdown:
        st.write(
            f"**{factor}:** {value} → **+{points} points**"
        )

    st.write(f"### Total Risk Score: {score} / 18")

    # -----------------------------
    # Decision Rules
    # -----------------------------

    st.subheader("📋 Agent Decision Rules")

    st.write("🟢 **0–7 points → LOW RISK**")
    st.write("🟡 **8–11 points → MODERATE RISK**")
    st.write("🟠 **12–15 points → HIGH RISK**")
    st.write("🔴 **16–18 points → CRITICAL RISK**")

    # -----------------------------
    # How the Agent Works
    # -----------------------------

    st.subheader("⚙️ How the Agent Works")

    st.write(
        "The agent follows the intelligent-agent cycle:"
    )

    st.code(
        "Environmental Input\n"
        "        ↓\n"
        "Input Processing\n"
        "        ↓\n"
        "Rule-Based Decision Engine\n"
        "        ↓\n"
        "Risk Score Calculation\n"
        "        ↓\n"
        "Flood Risk Classification\n"
        "        ↓\n"
        "Alert and Recommendation",
        language="text"
    )