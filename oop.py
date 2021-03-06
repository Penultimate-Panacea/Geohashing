# coding=utf-8
"""temporary function definition file, will eventually be different files for better separation of concerns"""



def create_hash(closing):
    """Creates the hash from the users location and closing price of the Dow Jones Industrial Index"""
    from datetime import date
    from hashlib import md5
    pre_hash = date.today().strftime("%Y-%m-%d") + "-" + str(closing)
    digest = md5((pre_hash).encode()).hexdigest()
    lat_add = int(digest[:16], 16) / 16 ** 16
    lon_add = int(digest[16:], 16) / 16 ** 16
    return lat_add, lon_add


def create_goal(home, hash_add):
    """Determines the goal for the geohash"""
    lat_full = home[0] + hash_add[0]
    lon_full = home[1] + hash_add[1]
    lat = round(lat_full, 5)
    lon = round(lon_full, 5)
    return lat, lon





# TODO 30W fix
# TODO 0001-0930 fix
# TODO allow for historical dates
# TODO confusion matrix testing
# TODO GUI
