import json

followingdata = open("following.json").read()
newfdata = json.loads(followingdata)
followinglist = []

for x in range(len(newfdata["relationships_following"])):
         followinglist.append(newfdata["relationships_following"][x]["string_list_data"][0]["value"])


followersdata = open("followers.json").read()
newffdata = json.loads(followersdata)
followerslist = []

for x in range(len(newffdata["relationships_followers"])):
         followerslist.append(newffdata["relationships_followers"][x]["string_list_data"][0]["value"])


for x in range(len(followinglist)):
    if followinglist[x] in followerslist:
        pass
    else:
        print(f" @{followinglist[x]} ")