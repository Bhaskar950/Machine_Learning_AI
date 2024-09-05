# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f'inside enemies {enemies}')

# increase_enemies()
# print(f"outside enemies {enemies}")



# player_health = 10
# potion_strength = 999

# def drink_potion():
#     potion_strength = 4
#     print(potion_strength)

#     print(player_health)
    
# drink_potion()
# print(potion_strength)
# print(player_health)


# player_health = 10
# potion_strength = 999


# def game():
#     def drink_potion():
#         potion_strength = 4
#         print(potion_strength)
#         print(player_health)
    
#     return drink_potion()
# print(game())

# print(potion_strength)
# print(player_health)




num1  = 5

def cal_parent():
    def cal_child(n):
        return n * n
    
    result1 = cal_child(4)

    result2 = cal_child(num1)
    print(result2)
    return result1
    

calculate = cal_parent()
print(calculate)
print(num1 * num1)



