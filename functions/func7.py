# def weather_report(temp):
#     if temp>30:
#         print("It's a hot day! Stay hydrated.")
#     elif 20<temp<=30:
#         print("Nice and warm outside!")
#     else:
#         print("It's a bit chilly today")
# # weather_report(35)

def weather_report(temp):
    if temp>30:
        return "It's a hot day! Stay hydrated."
    elif 20<temp<=30:
        return "Nice and warm outside!"
    else:
        return "It's a bit chilly today"
print(weather_report(23))



