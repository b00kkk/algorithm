--solvesql summary-of-artworks-in-3-years
SELECT d.classification, COALESCE(a.'2014',0) '2014', COALESCE(b.'2015',0) '2015', COALESCE(c.'2016' ,0) '2016'
FROM
(SELECT classification
FROM artworks
GROUP BY classification
) d
LEFT JOIN
(SELECT classification,COUNT(*) as '2014'
FROM artworks
WHERE SUBSTR(acquisition_date,1,4)='2014'
GROUP BY classification
) a 
ON d.classification=a.classification
LEFT JOIN
(SELECT classification,COUNT(*) as '2015'
FROM artworks
WHERE SUBSTR(acquisition_date,1,4)='2015'
GROUP BY classification
) b
ON d.classification=b.classification
LEFT JOIN
(SELECT classification,COUNT(*) as '2016'
FROM artworks
WHERE SUBSTR(acquisition_date,1,4)='2016'
GROUP BY classification
) c
ON d.classification = c.classification
ORDER BY d.classification
