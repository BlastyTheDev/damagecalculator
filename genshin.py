import math

def main():
    character_level = int(input("character level: "))
    enemy_level = int(input("enemy level: "))
    enemy_res = float(input("enemy resistance percent: ")) / 100
    base_dmg = float(input("base damage: "))
    base_dmg_multiplier = float(input("base damage multiplier percent: ")) / 100
    additive_base_dmg_bonus = float(input("additive base damage bonus (0 if you dont know): "))
    dmg_bonus_multiplier = 1 + (float(input("damage bonus percent: ")) / 100)
    crit_dmg = float(input("crit dmg: ")) / 100

    enemy_defense = get_enemy_defense(enemy_level)
    enemy_defense_multiplier = 1 - (enemy_defense / (enemy_defense + 5 * character_level + 500))

    enemy_res_multiplier = get_res_multiplier(enemy_res)

    dmg = ((base_dmg * base_dmg_multiplier) + additive_base_dmg_bonus) * dmg_bonus_multiplier * enemy_defense_multiplier * enemy_res_multiplier
    crit = get_crit_hit(dmg, crit_dmg)

    print(f"without crit: {math.floor(dmg)}")
    print(f"with crit: {math.floor(crit)}")


def get_res_multiplier(res_percentage: float) -> float:
    if res_percentage < 0:
        return 2 - 100 / (100 - res_percentage)
    if 0 <= res_percentage < 0.75:
        return 1 - res_percentage
    return 1 / (4 * res_percentage + 1)


def get_enemy_defense(enemy_level: int) -> int:
    return 5 * enemy_level + 500


def get_crit_hit(dmg: float, crit_dmg_percent: float) -> float:
    return dmg * (1 + crit_dmg_percent)


if __name__ == "__main__":
    main()
