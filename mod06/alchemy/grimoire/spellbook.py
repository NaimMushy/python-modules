def record_spell(spell_name: str, ingredients: str) -> str:

    from .validator import validate_ingredients

    validation_result: str = validate_ingredients(ingredients)

    return (
        "Spell "
        f"{'rejected' if 'INVALID' in validation_result else 'recorded'}: "
        f"{spell_name} ({validation_result})"
    )
