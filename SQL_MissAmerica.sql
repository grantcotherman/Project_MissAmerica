use SP23_ksgcother
go

DROP TABLE IF EXISTS TempTable

---Join the Two Tables using State/Region
SELECT * Into TempTable
FROM Project1.Miss_America ma JOIN Project1.TempCensus_Data cd ON ma.StateOfOrigin = cd.Region
ORDER BY Year

-- Drop the Redundant Region Column
ALTER TABLE TempTable
DROP COLUMN Region

--- Display Number of Wins by State (Top 15)
SELECT TOP 15 COUNT(StateOfOrigin) as Number_of_Wins, StateofOrigin
FROM TempTable
GROUP BY StateofOrigin
ORDER BY Number_of_Wins desc


---Display Number of Citizens (2019) per Historic Win (Top 15)
SELECT TOP 15 AVG(State_Population)/COUNT(StateOfOrigin) as CitizensPerWin, StateofOrigin
FROM TempTable
GROUP BY StateOfOrigin
ORDER BY CitizensPerWin

