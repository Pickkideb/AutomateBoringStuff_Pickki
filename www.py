#Hotel_Cost Function Start
def hotel_cost(nights):
  return 140*nights
#Hotel_Cost Function Ends

#Plane_Ride_Cost Function Starts
def plane_ride_cost(city):
  if city=="Charlotte":
    return 183
  elif city=="Tampa":
    return 220
  elif city=="Pittsburgh":
    return 222
  elif city=="Los Angeles":
    return 475
#Plane_Ride_Cost Function Ends\

#Return_car_cost Function Starts
def rental_car_cost(days):
  if days>=7:
    return (days*40)-50
  elif days>=3:
    return (days*40)-20
  else:
  	return (days*40)
#Return_car_cost Function Ends

#trip_Cost Function Starts
def trip_cost(city,days,spending_money):
  
  return "to "+ city+" for "+str(days)+" days with an extra "+str(spending_money)+" dollars of spending money"

	
#trip_Cost Function Ends
print trip_cost("Los Angeles",5,1955)
