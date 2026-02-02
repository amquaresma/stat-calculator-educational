from utils import ask_for_values
import stats


def show_welcome():
    print("=" * 60)
    print("📊 CALCULADORA ESTATÍSTICA EDUCACIONAL")
    print("=" * 60)
    print(
        "Este programa foi criado para ajudar estudantes e iniciantes\n"
        "a entenderem como funcionam as principais medidas estatísticas.\n\n"
        "Você poderá inserir até 10 valores numéricos e visualizar\n"
        "os resultados de forma clara e explicada.\n\n"
        "O foco aqui não é apenas o cálculo, mas o ENTENDIMENTO.\n"
    )
    print("=" * 60)


def show_results(values):
    print("\n📥 Valores analisados:")
    print(values)

    m = stats.mean(values)
    med = stats.median(values)
    moda = stats.mode(values)
    var = stats.variance(values)
    std = stats.standard_deviation(values)
    minimo = stats.minimum(values)
    maximo = stats.maximum(values)
    amp = stats.amplitude(values)
    q1, q2, q3 = stats.quartiles(values)
    cv = stats.coefficient_of_variation(values)

    print("\n" + "=" * 60)
    print("📈 RESULTADOS ESTATÍSTICOS")
    print("=" * 60)

    print(f"\n📌 MÉDIA: {m:.2f}")
    print("Representa o valor médio do conjunto.")

    print(f"\n📌 MEDIANA: {med:.2f}")
    print("Divide os dados ordenados ao meio.")

    if moda:
        print(f"\n📌 MODA: {moda}")
        print("Valor(es) mais frequente(s) do conjunto.")
    else:
        print("\n📌 MODA: Não existe")
        print("Todos os valores aparecem apenas uma vez.")

    print(f"\n📌 VARIÂNCIA: {var:.2f}")
    print("Mede o grau de dispersão dos dados.")

    print(f"\n📌 DESVIO PADRÃO: {std:.2f}")
    print("Indica o afastamento médio em relação à média.")

    print(f"\n📌 MÍNIMO: {minimo}")
    print(f"📌 MÁXIMO: {maximo}")

    print(f"\n📌 AMPLITUDE: {amp}")
    print("Diferença entre o maior e o menor valor.")

    print("\n📌 QUARTIS:")
    print(f"Q1 (25%): {q1}")
    print(f"Q2 (50% - Mediana): {q2}")
    print(f"Q3 (75%): {q3}")

    if cv is not None:
        print(f"\n📌 COEFICIENTE DE VARIAÇÃO: {cv:.2f}%")
        print("Ajuda a comparar a dispersão entre conjuntos.")
    else:
        print("\n📌 COEFICIENTE DE VARIAÇÃO: Indefinido (média zero)")

    print("\n" + "=" * 60)
    print(
        "🧠 INTERPRETAÇÃO FINAL:\n"
        "Essas medidas permitem compreender tanto o valor central\n"
        "quanto a distribuição e a variabilidade dos dados analisados."
    )
    print("=" * 60)


def run():
    show_welcome()
    values = ask_for_values()
    show_results(values)

    input("\nPressione ENTER para encerrar...")
