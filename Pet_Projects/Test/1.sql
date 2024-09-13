# goods: id, name, price, amount 
SELECT name, AVG(goods.price) FROM goods

GROUP BY name;

SELECT name, price, amount, AVG(goods.price) as condition FROM goods
WHERE goods.price > condition 
ORDER BY goods.price;
