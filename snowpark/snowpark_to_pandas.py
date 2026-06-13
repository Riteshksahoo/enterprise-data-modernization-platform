from snowflake.snowpark import Session
from config import connection_parameters

session = Session.builder.configs( connection_parameters ).create()

df = session.table( "ANALYTICS.REGION_SALES" )
pd_df = df.to_pandas()
print(pd_df)
