import facebook

# Makes a graph object connected with this user access token.
graph = facebook.GraphAPI(access_token = "your_access_token_here")

# Finds the list of 'authenticated' friends of the user having this ID
friends = graph.get_connections(id="your_profile_id", connection_name = "friends")
print len(friends["data"])


auth_friends = friends["data"]
list_friends = []
list_ids = []

# Extracting the names and IDs of the authenticated friends
for entry in auth_friends:
    list_ids.append(entry["id"])
    list_friends.append(entry["name"])

# Will find all connections regarding posts by the user having this ID

posts = graph.get_connections(id="736639463043996", connection_name = "posts")
print posts["data"]
