import matplotlib.pyplot as plt

alunos_aura = [
    "pietro",
    "wilmar",
    "kayo",
    "alice",
    "rosinha"
]

volume_de_aura = [500, 300, 200, 100, 50]

plt.title("quantidade de aura por aluno")

plt.xlabel("alunos aura")
plt.ylabel("quantidade de aura")

plt.grid(axis="y", linestyle="--", alpha=0.7)

barras = plt.bar(alunos_aura, volume_de_aura)

for barra in barras:
    altura = barra.get_height()
    
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 10,
        f"{altura}",
        ha="center",
        va="bottom"
    )

plt.show()