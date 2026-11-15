import seaborn as sns
import matplotlib.pyplot as plt

# Fikcyjne dane finansowe w tysiącach złotych
miesiace = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze", "Lip"]
przychody = [40, 45, 42, 55, 60, 65, 70]
koszty = [30, 32, 35, 38, 45, 48, 100]

# Wygląd wykresu
sns.set_theme(style="whitegrid")
plt.figure(figsize=(9, 5))

# Linie przychodów i kosztów
sns.lineplot(x=miesiace, y=przychody, marker="o", label="Przychody")
sns.lineplot(x=miesiace, y=koszty, marker="o", label="Koszty")

# Tytuł i opisy osi

plt.title("Przychody i koszty firmy Jakub")
plt.xlabel("Miesiąc")
plt.ylabel("Kwota (tys. $)")
plt.legend()

# Zapis i wyświetlenie wykresu
plt.tight_layout()
plt.savefig("finanse_firmy.png")
plt.show()