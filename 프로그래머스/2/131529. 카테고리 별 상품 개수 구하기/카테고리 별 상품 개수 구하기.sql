SELECT SUBSTRING(PRODUCT_CODE, 1, 2) AS category, COUNT(SUBSTRING(PRODUCT_CODE, 1, 2)) PRODUCTS
FROM PRODUCT
GROUP BY category;