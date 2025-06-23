SELECT i.FLAVOR
FROM FIRST_HALF f, ICECREAM_INFO i
WHERE (f.flavor = i.flavor) AND (i.INGREDIENT_TYPE = 'fruit_based' AND f.total_order > 3000)
ORDER BY f.total_order desc;
