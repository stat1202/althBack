SELECT SUM(SCORE) AS SCORE,
        G.EMP_NO, 
        E.EMP_NAME,
        E.POSITION,
        E.EMAIL
    FROM HR_EMPLOYEES E
        INNER JOIN HR_GRADE G ON E.EMP_NO = G.EMP_NO
    WHERE YEAR = '2022'
    GROUP BY EMP_NO, YEAR
    ORDER BY SCORE DESC
    LIMIT 1
