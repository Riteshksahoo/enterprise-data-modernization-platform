from snowflake.snowpark import Session
from config import connection_parameters
from snowflake.snowpark.types import StructType, StructField, StringType, IntegerType, FloatType, DateType  
from snowflake.snowpark.functions import sum

session = Session.builder.configs(connection_parameters).create()
sales_df = session.table(
    "CURATED.SALES_CURATED"
)

region_sales = (
                sales_df.group_by
                (
                    "REGION"
                )
                .agg(
                        sum("SALES").alias("TOTAL_SALES")
                     )
               )  

region_sales.show()

region_sales.write.mode("overwrite").save_as_table(
    "ANALYTICS.REGION_SALES"
)
print("REGION_SALES table created successfully!")