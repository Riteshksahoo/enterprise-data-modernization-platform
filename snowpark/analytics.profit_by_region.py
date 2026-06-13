from snowflake.snowpark import Session
from snowflake.snowpark.functions import sum
from config import connection_parameters

session = Session.builder.configs( connection_parameters ).create()

sales_df = session.table( "CURATED.SALES_CURATED" )

profit_region = (
    sales_df
            .group_by(
                "REGION"
                )
                    .agg(
                            sum("PROFIT").alias("TOTAL_PROFIT")
                         )              
                )

profit_region.show()

profit_region.write.mode("overwrite").save_as_table(
    "ANALYTICS.PROFIT_BY_REGION"
)

print("PROFIT_BY_REGION table created successfully.")