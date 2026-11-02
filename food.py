RESTAURANTS = [
("Mango Rice", 4.2, 25),
("Pad Thai House", 4.8, 40),
("Chicken Rice", 4.6, 15),
("Som Tam Corner", 4.6, 25),
("Boat Noodles", 4.8, 30),
]    

def by_rating(r):
    return (-r[1], r[2])

def by_time(r):
    return (r[2], r[1])
key_dict = {"rating" : by_rating, "time": by_time}

sortby = input("Sort by (rating/time): ").lower()
if sortby not in {"rating", "time"}:
    print("Unknown option")
else:
    rest_sorted = sorted(RESTAURANTS, key=key_dict[sortby])

    for i, (name, rating, time) in enumerate(rest_sorted):
        print(f"{i + 1}. {name}, {rating} stars, {time} min")
