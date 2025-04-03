import tabula
import pandas as pd

# Ange sökvägen till din PDF-fil
pdf_path = "fil.pdf"

# Extrahera alla tabeller från PDF:en
dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Visa antal tabeller som hittades
print(f"Antal tabeller hittade: {len(dfs)}")

# Om du vet att PDF:en bara innehåller en tabell eller du vill jobba med den första tabellen:
if dfs:
    df = dfs[0]
    # Visa de första raderna i tabellen
    print(df.head())
    
    # Spara DataFrame till en Excel-fil
    df.to_excel("utdata.xlsx", index=False)
else:
    print("Inga tabeller hittades i PDF:en.")

