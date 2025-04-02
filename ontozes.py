def szamit_ontozesi_fordulo(ontozoviz_adag, et):
    """
    Számolja ki az öntözési fordulót.

    Args:
    ontzoviz_adag (float): Az öntözővíz adag mm-ben.
    et (float): Az evapotranspiráció (ET) érték mm/nap-ban.

    Returns:
    float: Az öntözési forduló, vagyis hány napig elég az öntözővíz.
    """
    # Ellenőrzés, hogy az értékek pozitívak-e
    if ontzoviz_adag <= 0 or et <= 0:
        raise ValueError("Az öntözővíz adag és az ET értékének is pozitívnak kell lennie.")
    
    # Számoljuk ki az öntözési fordulót
    ontzesi_fordulo = ontzoviz_adag / et
    return ontzesi_fordulo

# Bemutató
try:
    ontzoviz_adag = float(input("Add meg az öntözővíz adagot mm-ben: "))
    et = float(input("Add meg az ET értéket mm/nap-ban: "))
    
    ontzesi_fordulo = szamit_ontozesi_fordulo(ontzoviz_adag, et)
    print(f"Az öntözési forduló {ontzesi_fordulo:.2f} nap.")
except ValueError as e:
    print(f"Hiba: {e}")
