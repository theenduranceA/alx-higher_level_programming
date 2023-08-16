-- A script for Import in hbtn_0c_0 database this table dump:

SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month >= 7 AND month < 9 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
