import tabula
import pandas as pd

# Ange sökvägen till din PDF-fil
pdf_path = "fil.pdf"

# Extrahera tabeller från alla sidor med stream=True (prova även lattice=True om det behövs)
dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, stream=True)
print("Antal tabeller hittade:", len(dfs))

# Kombinera alla extraherade DataFrames
combined_df = pd.concat(dfs, ignore_index=True)

# Om varje sida har en upprepad header, ta bort de raderna
# Här antas att den första raden i den kombinerade DataFrame är headern
header_row = combined_df.iloc[0]
combined_df = combined_df[combined_df.iloc[:,0] != header_row[0]]

# Nollställ indexet efter filtrering
combined_df.reset_index(drop=True, inplace=True)

# Spara den kombinerade DataFrame till en Excel-fil
combined_df.to_excel("utdata.xlsx", index=False)
print("Data har sparats till utdata.xlsx")

