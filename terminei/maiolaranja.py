import matplotlib.pyplot as plt

meios_de_denuncia = [
    "Disque 100",
    "Conselho Tutelar",
    "Polícia"
]

volume_de_atendimento = [500, 300, 200]

plt.title("Maio: Canais de Apoio / Denúncia")

plt.xlabel("Canais de Apoio / Denúncias")
plt.ylabel("Volume de Atendimento Registrado")

plt.grid(axis="y", linestyle="--", alpha=0.7)

barras = plt.bar(meios_de_denuncia, volume_de_atendimento)

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