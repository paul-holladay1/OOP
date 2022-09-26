import InsectClass as i

houseFly = i.insect(2,4)               #creates 2 separate instances, Housefly and misquito
mosquito = i.insect(4,8)

houseFly.calculate_flight()
mosquito.calculate_flight()

print("The housefly can fly up to ", houseFly.get_flight())
print("The misquito can fly up to ", mosquito.get_flight())