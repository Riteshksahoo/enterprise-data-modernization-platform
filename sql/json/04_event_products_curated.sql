USE DATABASE RETAIL_DB;
USE SCHEMA CURATED;

CREATE OR REPLACE TABLE EVENT_PRODUCTS_CURATED AS
SELECT
    event.value:event_id::INTEGER AS EVENT_ID,
    event.value:event_name::STRING AS EVENT_NAME,
    event.value:event_type::STRING AS EVENT_TYPE,
    event.value:event_date::DATE AS EVENT_DATE,
    event.value:region::STRING AS REGION,
    product.value:product_id::STRING AS PRODUCT_ID,
    product.value:discount::INTEGER AS DISCOUNT
FROM RETAIL_DB.RAW.STORE_EVENTS_RAW,
LATERAL FLATTEN(INPUT => EVENT_DATA) event,
LATERAL FLATTEN(INPUT => event.value:products) product;

SELECT * FROM CURATED.EVENT_PRODUCTS_CURATED;