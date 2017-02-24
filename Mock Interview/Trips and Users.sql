SELECT Day,ROUND(a.cnt/b.cnt,2) as 'Cancellation Rate' FROM (
SELECT Request_at as Day, COUNT(Request_at) as cnt FROM Trips where
Client_Id in (SELECT Users_Id FROM Users WHERE Banned = 'No' AND Role = 'client')
AND Status = 'cancelled_by_client' AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at ) a
LEFT JOIN (SELECT Request_at as Day,COUNT(Request_at) as cnt FROM Trips where
Client_Id in (SELECT Users_Id FROM Users WHERE Banned = 'No' AND Role = 'client')
AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at) b ON a.Day = b.Day ORDER BY Day


select
t.Request_at Day,
round(sum(case when t.Status like 'cancelled_%' then 1 else 0 end)/count(*),2) as 'Cancellation Rate'
from Trips t
inner join Users u
on t.Client_Id = u.Users_Id and u.Banned='No'
where t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at