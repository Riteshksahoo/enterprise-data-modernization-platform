from snowflake.snowpark import Session
from snowflake.snowpark.functions import sum
from config import connection_parameters

session = Session.builder.configs(connection_parameters).create()

print("Session created successfully!")

sales_df = session.table(
    "CURATED.SALES_CURATED"
)

category_performance = (
    sales_df
    .group_by(
        "CATEGORY"
        )
    .agg(
        sum("SALES").alias("TOTAL_SALES"),
        sum("PROFIT").alias("TOTAL_PROFIT")
    )
)

category_performance.show()

category_performance.write.mode("overwrite").save_as_table("ANALYTICS.CATEGORY_PERFORMANCE")

print("CATEGORY_PERFORMANCE table created successfully.")

