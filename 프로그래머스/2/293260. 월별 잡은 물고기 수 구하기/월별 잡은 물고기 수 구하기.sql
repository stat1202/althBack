-- 코드를 작성해주세요
SELECT COUNT(IFNULL(LENGTH, 1)) AS FISH_COUNT,MONTH(TIME) AS MONTH
    FROM FISH_INFO
    GROUP BY MONTH(TIME)
    ORDER BY MONTH(TIME)