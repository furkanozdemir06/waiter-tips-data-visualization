import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Waiter Tips", page_icon="🍽️", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv("waitertips.csv")
    df["tip_percent"] = df["tip"] / df["total_bill"] * 100
    return df


df = load_data()

st.title("🍽️ Waiter Tips Analysis")
st.caption("What drives the tip? Explore bills, party sizes and customer profiles.")

# Sidebar filters
d = df
for col, label in [("day", "Day"), ("time", "Meal time"), ("sex", "Sex"), ("smoker", "Smoker")]:
    options = sorted(df[col].unique())
    d = d[d[col].isin(st.sidebar.multiselect(label, options, default=options))]

if d.empty:
    st.warning("No data for these filters.")
    st.stop()

# KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("Parties", len(d))
c2.metric("Avg bill", f"${d.total_bill.mean():.2f}")
c3.metric("Avg tip", f"${d.tip.mean():.2f}")
c4.metric("Avg tip %", f"{d.tip_percent.mean():.1f}%")

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Compare groups", "Breakdown", "Data"])

with tab1:
    col1, col2 = st.columns(2)
    col1.plotly_chart(px.histogram(d, x="tip", nbins=25, title="Tip distribution"), use_container_width=True)
    fig = px.scatter(d, x="total_bill", y="tip", color="sex", title="Total bill vs tip")
    if len(d) > 1:
        m, b = np.polyfit(d.total_bill, d.tip, 1)
        xs = [d.total_bill.min(), d.total_bill.max()]
        fig.add_scatter(x=xs, y=[m * x + b for x in xs], mode="lines", name="Trend",
                        line=dict(color="black", dash="dash"))
    col2.plotly_chart(fig, use_container_width=True)
    corr = d[["total_bill", "tip", "size", "tip_percent"]].corr()
    st.plotly_chart(px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r",
                              title="Correlation matrix"), use_container_width=True)

with tab2:
    group = st.selectbox("Compare by", ["day", "time", "sex", "smoker", "size"])
    col1, col2 = st.columns(2)
    avg = d.groupby(group)[["tip", "tip_percent"]].mean().reset_index()
    col1.plotly_chart(px.bar(avg, x=group, y="tip", title=f"Average tip ($) by {group}"),
                      use_container_width=True)
    col2.plotly_chart(px.box(d, x=group, y="tip_percent", title=f"Tip % by {group}"),
                      use_container_width=True)

with tab3:
    st.plotly_chart(px.sunburst(d, path=["day", "time", "sex", "smoker"], values="tip",
                                title="Total tips: day > meal time > sex > smoker"),
                    use_container_width=True)

with tab4:
    st.dataframe(d, use_container_width=True)
    st.download_button("Download filtered CSV", d.to_csv(index=False), "tips_filtered.csv")