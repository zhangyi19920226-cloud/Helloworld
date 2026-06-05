distance_mi = 5
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = True
if not distance_mi:
    print('False')
elif distance_mi <= 1:
    print(not is_raining)
elif distance_mi <= 6:
    print(not is_raining and has_bike)
else:
    print(has_car or has_ride_share_app)

