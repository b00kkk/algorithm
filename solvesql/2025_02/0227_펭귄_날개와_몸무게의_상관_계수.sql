-- solvesql correlation-penguin
SELECT species,
ROUND((n*sum_xy-sum_x*sum_y)/(SQRT(n*sum_xx-sum_x*sum_x)*SQRT(n*sum_yy-sum_y*sum_y)),3) AS corr
FROM
(SELECT species, COUNT(*) AS n, SUM(flipper_length_mm) AS sum_x, SUM(body_mass_g) AS sum_y,
SUM(flipper_length_mm*body_mass_g) AS sum_xy,
SUM(flipper_length_mm*flipper_length_mm) AS sum_xx,
SUM(body_mass_g*body_mass_g) AS sum_yy
FROM penguins
WHERE flipper_length_mm IS NOT NULL
AND body_mass_g IS NOT NULL
GROUP BY species)