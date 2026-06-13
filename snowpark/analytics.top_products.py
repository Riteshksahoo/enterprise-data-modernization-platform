from snowflake.snowpark import Session
from snowflake.snowpark.functions import sum, col
from config import connection_parameters

session = Session.builder.configs(connection_parameters).create()

print("Session created successfully!")

sales_df = session.table( "CURATED.SALES_CURATED")


top_products = (
    sales_df
            .group_by(
                "PRODUCT_NAME"
                     )
                        .agg(
                                sum("SALES").alias("TOTAL_SALES")
                             ).sort(col("TOTAL_SALES").desc()).limit(10)
                )

top_products.show()
top_products.write.mode("overwrite").save_as_table("ANALYTICS.TOP_PRODUCTS")

print("TOP_PRODUCTS table created successfully!")