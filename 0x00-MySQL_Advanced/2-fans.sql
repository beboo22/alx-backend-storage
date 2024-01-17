-- 3 first students in the Batch ID=3
SELECT origin AS origin , sum(fans) AS nb_fans
From metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
