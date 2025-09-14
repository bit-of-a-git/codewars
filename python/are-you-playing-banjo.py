def are_you_playing_banjo(name):
    return (
        f"{name} plays banjo"
        if name.upper().startswith("R")
        else f"{name} does not play banjo"
    )
