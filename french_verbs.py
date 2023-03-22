def conjugate_verb(verb):
    """
    Conjugates a French verb in the present tense for all pronouns.
    """
    endings = {
        "er": ["e", "es", "e", "ons", "ez", "ent"],
        "ir": ["is", "is", "it", "issons", "issez", "issent"],
        "re": ["s", "s", "", "ons", "ez", "ent"]
    }
    stem = verb[:-2]
    ending_type = verb[-2:]
    if ending_type not in endings:
        return "Invalid verb ending. Only -er, -ir, and -re verbs are supported."
    present_tense = [f"{pronoun} {stem}{endings[ending_type][i]}" for i, pronoun in enumerate(("je", "tu", "il/elle/on", "nous", "vous", "ils/elles"))]
    return f"The conjugations of the verb {verb}: " + ", ".join(present_tense)

print(conjugate_verb("adorer"))