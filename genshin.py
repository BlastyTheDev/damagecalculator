def main():
    scaling_stat_value: float = float(input('Scaling stat value: '))
    ability_scaling_percent: float = float(input('Ability scaling percent: ')) / 100
    base_dmg_multiplier: float = float(input('Base dmg multiplier: '))
    additive_base_dmg_bonus: float = float(input('Additive base dmg bonus: '))
    dmg_bonus_percent: float = float(input('Dmg bonus percent: '))

    level_character: int = int(input('Character level: '))
    level_enemy: int = int(input('Enemy level: '))

    res_base_enemy: float = float(input('Enemy base RES: '))
    res_bonus_enemy: float = float(input('Enemy bonus RES: '))
    res_debuffs_enemy: float = float(input('Enemy RES debuffs: '))

    defense_ignored: float = float(input('Defense ignored: '))
    defense_dmg_reduction = get_defense_dmg_reduction(scaling_stat_value, level_enemy)
    defense_multiplier_target = get_defense_multiplier(level_character, level_enemy, defense_dmg_reduction, defense_ignored)
    res_multiplier_target = get_res_multiplier(get_res_percentage(res_base_enemy, res_bonus_enemy, res_debuffs_enemy))
    amplifying_multiplier = 1  # 1 if no elemental reactions

    print(f'Raw DMG: {get_raw_dmg(ability_scaling_percent, scaling_stat_value, base_dmg_multiplier, additive_base_dmg_bonus,
                                  get_dmg_bonus_multiplier(dmg_bonus_percent, defense_dmg_reduction),
                                  defense_multiplier_target, res_multiplier_target, amplifying_multiplier)}')


def get_res_percentage(res_base: float, res_bonus: float, res_debuffs: float) -> float:
    return res_base + res_bonus - res_debuffs


def get_res_multiplier(res_percentage: float) -> float:
    if res_percentage < 0:
        return 2 - 100 / (100 - res_percentage)
    if 0 <= res_percentage < 0.75:
        return 1 - res_percentage
    return 1 / (4 * res_percentage + 1)


def get_base_dmg(ability_scaling_percent: float, scaling_stat_value: float) -> float:
    return ability_scaling_percent * scaling_stat_value


def get_dmg_bonus_multiplier(dmg_bonus_percent: float, dmg_reduction_target: float) -> float:
    return 1 + dmg_bonus_percent - dmg_reduction_target


def get_defense_dmg_reduction(defense: float, level_attacker: int) -> float:
    return defense / (defense + 5 * level_attacker + 500)


def get_enemy_defense(enemy_level: int) -> int:
    return 5 * enemy_level + 500


def get_defense_multiplier(level_character: int, level_enemy: int, defense_reduction: float, defense_ignored: float) -> float:
    return (level_character + 100) / ((1 - defense_reduction) * (1 - defense_ignored)) * (level_enemy + 100) + (level_character + 100)


def get_raw_dmg(ability_scaling_percent: float, scaling_stat_value: float, base_dmg_multiplier: float,
                additive_base_dmg_bonus: float, dmg_bonus_multiplier: float, def_multiplier_target: float,
                res_multiplier_target: float, amplifying_multiplier: float) -> float:
    return ((sum(get_base_dmg(ability_scaling_percent, scaling_stat_value),
                 base_dmg_multiplier) + additive_base_dmg_bonus)
            * dmg_bonus_multiplier * def_multiplier_target * res_multiplier_target * amplifying_multiplier)


def get_crit_hit(dmg: float, crit_dmg_percent: float) -> float:
    return dmg * (1 + crit_dmg_percent)


if __name__ == "__main__":
    main()
