def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    if food in person["favourites"]["snacks"]:
        return True
    else:
        return False
    
def add_friend(person,friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(people):
    total = 0
    for person in people:
        total += person["monies"]    
    return total

def lend_money(lender, borrower, amount_of_money):
    lender["monies"] -= amount_of_money
    borrower["monies"] += amount_of_money

def all_favourite_foods(people):
    all_foods = []
    for person in people:
        for food in person["favourites"]["snacks"]:
            all_foods.append(food)
    return all_foods

def find_no_friends(people):
    lonely = []
    for person in people:
        if len(person["friends"]) == 0:
            lonely.append(person)
    return lonely

def unique_favourite_tv_shows(people):
    fav_shows = []
    for person in people:
        if not person["favourites"]["tv_show"] in fav_shows:
            fav_shows.append(person["favourites"]["tv_show"])
    return fav_shows

# Bonus question: set(fav_shows) returns a set of unique unordered values
# set expects a list as an argument

   