SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') DATE_OF_BIRTH
FROM member_profile
WHERE MONTH(date_of_birth) = 03 AND tlno is not null and gender = 'W'
ORDER BY member_id ASC;