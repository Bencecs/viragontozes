def szamit_ontozesi_ido(ontozoviz_adag, intenzitas):
    """
    Számolja ki az öntözési időt.

    Args:
    ontzoviz_adag (float): Az öntözővíz adag mm-ben.
    intenzitas (float): Az öntözés intenzitása mm/óra-ban.

    Returns:
    float: Az öntözési idő (óra).
    """
    # Ellenőrzés, hogy az értékek pozitívak-e
    if ontzoviz_adag <= 0 or intenzitas <= 0:
        raise ValueError("Az öntözővíz adag és az intenzitás értékeinek is pozitívnak kell lenniük.")
    
    # Számoljuk ki az öntözési időt
    ontzesi_ido = ontzoviz_adag / intenzitas
    return ontzesi_ido

# Bemutató
try:
    ontzoviz_adag = float(input("Add meg az öntözővíz adagot mm-ben: "))
    intenzitas = float(input("Add meg az öntözés intenzitását mm/órában: "))
    
    ontzesi_ido = szamit_ontozesi_ido(ontzoviz_adag, intenzitas)
    print(f"Az öntözési idő {ontzesi_ido:.2f} óra.")
except ValueError as e:
    print(f"Hiba: {e}")
