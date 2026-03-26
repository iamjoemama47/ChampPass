import mysql.connector
from classes.dbconfig import Connect
import classes.gemeente


def test_database():
    # 1. Verbinding maken
    try:
        db_connector = Connect()
        the_db = db_connector.getConnection()
        print("✅ Verbinding succesvol!")
    except Exception as e:
        print(f"❌ Verbinding mislukt: {e}")
        return

    # 2. Test: Gemeente aanmaken
    print("\n--- Test Create ---")
    nieuwe_stad = Gemeente(None, "TestStad", "9999", "BE")
    nieuwe_stad.createGemeente(the_db)
    the_db.commit() # Belangrijk om de wijziging op te slaan!
    print("✅ Gemeente 'TestStad' toegevoegd.")

    # 3. Test: Eén gemeente lezen
    print("\n--- Test Read ---")
    stad = Gemeente.readGemeente(the_db, "TestStad")
    if stad:
        print(f"✅ Gevonden: ID:{stad.gemeente_ID}, Naam:{stad.gemeenteNaam}")
    else:
        print("❌ Gemeente niet gevonden (check je SQL query!).")

    # 4. Test: Lijst ophalen
    print("\n--- Test Lijst ---")
    alle_steden = Gemeente.lijst_gemeentes(the_db)
    print(f"✅ Totaal aantal gemeentes in DB: {len(alle_steden)}")
    for g in alle_steden[:3]: # Toon de eerste 3
        print(f" - {g.gemeenteNaam} ({g.postcode})")

# Voer de test uit
if __name__ == "__main__":
    test_database()