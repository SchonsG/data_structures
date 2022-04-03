from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "seller"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["seller"] = []

def person_is_seller(name):
    if "seller" in name:
        return True
    else:
        return False
    
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    print("mango seller not found!")
    return False


search("you")