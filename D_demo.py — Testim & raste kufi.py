from B_llojete_biletave import BileteUrbane, BileteNderqytet, AbonimStudent
from C_raporte import totali, raport_per_origjine, fatura_detajuar

# Dataset testimi (≥ 6 bileta)
bileta = [
    BileteUrbane("Tiranë", "Tiranë", 100.0, zona=1),
    BileteUrbane("Tiranë", "Tiranë", 100.0, zona=3),  # kufi zona
    BileteNderqytet("Tiranë", "Shkodër", 200.0, km=100, tarife_per_km=2.5),
    BileteNderqytet("Durrës", "Vlorë", 150.0, km=200, tarife_per_km=1.8),  # km i madh
    AbonimStudent("Tiranë", "Tiranë", 150.0, zbritje=0),  # zbritje 0%
    AbonimStudent("Elbasan", "Tiranë", 150.0, zbritje=50)
]

# Print raportet
print("🧾 Fatura Detajuar:")
print(fatura_detajuar(bileta))
print("\n📊 Totali i të ardhurave:", round(totali(bileta), 2), "L")
print("📍 Bileta nga Tiranë:", raport_per_origjine(bileta, "Tiranë"))
