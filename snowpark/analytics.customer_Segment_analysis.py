from snowflake.snowpark import Session
from snowflake.snowpark.functions import sum
from config import connection_parameters

session = Session.builder.configs( connection_parameters ).create()

sales_df = session.table( "CURATED.SALES_CURATED" )

segment_df = (
    sales_df
    .group_by(
        "SEGMENT"
        ).agg(
                sum("SALES").alias("TOTAL_SALES"),
                sum("PROFIT").alias("TOTAL_PROFIT")
            )
            )

segment_df.show()

segment_df.write.mode("overwrite").save_as_table("ANALYTICS.SEGMENT_ANALYSIS")

print("SEGMENT_ANALYSIS table created successfully.")