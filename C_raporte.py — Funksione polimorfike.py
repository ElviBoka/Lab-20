def totali(bileta: list) -> float:
    return sum(b.price() for b in bileta)

def raport_per_origjine(bileta: list, origj: str) -> int:
    return sum(1 for b in bileta if b.origjin == origj)

def fatura_detajuar(bileta: list) -> str:
    rreshta = []
    for b in bileta:
        rreshta.append(f"{b} | Çmimi: {b.price():.2f} L")
    return "\n".join(rreshta)
