import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from urllib.parse import urlencode

# Preloaded data (you can expand this later)
average_salaries = {
    "Nursing": 70000,
    "Engineering": 85000,
    "Arts": 40000,
    "Business": 60000,
    "Computer Science": 95000,
    "Pharmacy": 110000,
    "Psychology": 45000
}

# --- Get query params ---
query_params = st.query_params
major = query_params.get("major", [None])[0]
custom_salary = float(query_params.get("salary", [0])[0])
tuition_per_year = float(query_params.get("tuition", [8000])[0])
living_cost_per_year = float(query_params.get("living", [10000])[0])
years = int(query_params.get("years", [4])[0])

st.title("🎓 Degree ROI Calculator")
st.subheader("How long will it take your degree to pay for itself?")

# --- Inputs ---
major = st.selectbox("Choose your major", list(average_salaries.keys()), index=list(average_salaries.keys()).index(major) if major in average_salaries else 0)
custom_salary = st.number_input("Expected starting salary (leave 0 to use average)", value=custom_salary)
tuition_per_year = st.number_input("Tuition per year ($)", value=tuition_per_year)
living_cost_per_year = st.number_input("Living cost per year ($)", value=living_cost_per_year)
years = st.slider("Years to complete degree", 2, 10, years)

# --- Calculation ---
total_cost = (tuition_per_year + living_cost_per_year) * years
salary = custom_salary if custom_salary > 0 else average_salaries[major]

if salary > 0:
    payback_years = round(total_cost / salary, 2)
    roi = salary * 40 - total_cost  # Assuming 40-year career

    st.markdown(f"### Results:")
    st.write(f"💸 **Total Degree Cost:** ${total_cost:,.0f}")
    st.write(f"📈 **Estimated Starting Salary:** ${salary:,.0f}")
    st.write(f"⏳ **Time to Pay Off Degree:** {payback_years} years")
    st.write(f"💰 **Estimated Lifetime ROI:** ${roi:,.0f}")

    # --- Graph: Net Value Over Time ---
    st.subheader("📊 Net Value Over Time")
    years_list = list(range(1, 41))
    net_value = [(salary * y) - total_cost for y in years_list]

    fig, ax = plt.subplots()
    ax.plot(years_list, net_value)
    ax.axhline(0, color='red', linestyle='--')
    ax.set_xlabel("Years after graduation")
    ax.set_ylabel("Net gain ($)")
    ax.set_title("Cumulative Value of Your Degree")
    st.pyplot(fig)

    # --- Share URL ---
    params = {
        "major": major,
        "salary": custom_salary,
        "tuition": tuition_per_year,
        "living": living_cost_per_year,
        "years": years
    }
    share_url = f"https://degree-roi-calculator.streamlit.app/?{urlencode(params)}"

    st.markdown("### 📤 Share Your Results")
    st.text_input("Copy your link to share", share_url, key="copy_link", help="Click to copy your link!")
    st.success("✅ Link ready to copy and share!")



else:
    st.warning("Enter a valid expected salary.")