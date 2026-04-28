
SELECT SUM(Sales) AS Total_Revenue FROM sales_data;


SELECT Product, SUM(Sales) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC;


SELECT Region, SUM(Sales) AS Sales
FROM sales_data
GROUP BY Region;


SELECT Month, SUM(Sales) AS Monthly_Sales
FROM sales_data
GROUP BY Month;