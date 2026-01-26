def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation_result: str = validate_ingredients(ingredients)
    if "INVALID" in validation_result:
        return f"spell rejected: {spell_name} {validation_result}"
    else:
        return f"spell recorded: {spell_name} {validation_result}"
