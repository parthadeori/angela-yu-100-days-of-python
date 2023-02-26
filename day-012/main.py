# Namespaces: Local vs. Global Scope

################### Scope ###################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

################### Local Scope ###################

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

################### Global Scope ###################

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori