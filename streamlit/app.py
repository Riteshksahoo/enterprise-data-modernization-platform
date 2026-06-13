import streamlit as st
from snowflake.snowpark import Session
import sys
import os

sys.path.append(
os.path.abspath(
os.path.join(os.path.dirname(__file__), "..", "snowpark")
))
from config import connection_parameters

st.set_page_config( page_title="Retail Analytics Dashboard", layout="wide")

session = Session.builder.configs( connection_parameters ).create()

st.title(" Retail Analytics Dashboard")
region_df = (
                session.table("ANALYTICS.REGION_SALES").to_pandas())

st.subheader("Region Sales")
st.bar_chart( region_df.set_index("REGION") )

sales_total = region_df["TOTAL_SALES"].sum()

col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Total Sales",
        f"{sales_total:,.2f}"
    )
with col2:
    st.metric(
        "Regions",
        len(region_df)
    )

category_df = session.table( "ANALYTICS.CATEGORY_PERFORMANCE" ).to_pandas()

st.subheader("Category Performance")
st.bar_chart( category_df.set_index("CATEGORY")["TOTAL_SALES"] )

top_products_df = session.table( "ANALYTICS.TOP_PRODUCTS" ).to_pandas()

st.subheader("Top Products")

st.dataframe(
    top_products_df[
        ["PRODUCT_NAME", "TOTAL_SALES"]
    ]
)

segment_df = session.table( "ANALYTICS.SEGMENT_ANALYSIS" ).to_pandas()

st.subheader("Customer Segment Analysis")
st.dataframe(segment_df)