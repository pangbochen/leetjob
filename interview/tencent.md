Q：一个1T的文件，每行是一个Query，通过一个1G内存的单机获取查询频率Top 1000 的Query
yingpan
node 
int cnt
string s

max_headp (lambda x: x.cnt)




dict 
query : cnt 


divide and conquer (map then reduce)

1T / 1G = 10^3
1 T -> 10^5 or 10^4 -> 100M ~
 
100M top 500(as K) for 1 G memory


for the unit solution top query for the tiny file 
: heapq to find the top node(string: cnt)
: storage : skip over the tiny file for 1 G memory :dict {string:cnt} (100M+, safe stable)  {or dict{string_hash:cnt} idx_dict{string_hash:string}, with conflict risk}or tire tree to reduce memory cost(tree node , not safe)

group and conquer stage
: around 1000 for each : maybe less 1M for one file
: 1-stage or 2-stage brouse is enough, could less then 1 G with heapq-solution

storage to reduce memory