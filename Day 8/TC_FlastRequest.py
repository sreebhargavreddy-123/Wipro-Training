import requests
get_url1="http://127.0.0.1:5000/users"
response = requests.get(get_url1)
print("get1")
print(response.status_code)
print(response.json())

post_url = "http://127.0.0.1:5000/users"
body1={"name":"Swathi"}


r1=requests.post(post_url,json=body1);
print("post")
print(r1.status_code)
print(r1.json())

put_url="http://127.0.0.1:5000/users/1"
body2={"name":"divya"}
r2=requests.put(put_url,json=body2);
print("put")
print(r2.status_code)
print(r2.json())

patch_url="http://127.0.0.1:5000/users/2"
body3={"name":"Deepak"}
r3=requests.patch(patch_url,json=body3);
print("patch")
print(r3.status_code)
print(r3.json())

delete_url="http://127.0.0.1:5000/users/2"
r4=requests.delete(delete_url)
print("delete")
print(r4.status_code)
print(r4.json())
