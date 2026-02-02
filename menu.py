from utils import ask_for_values
import stats


def show_welcome():
    print("=" * 60)
    print("📊 CALCULADORA ESTATÍSTICA EDUCACIONAL")
    print("=" * 60)
    print(
        "Este programa ajuda você a entender, na prática,\n"
        "as principais medidas estatísticas.\n\n"
        "Escolha uma operação, informe até 10 valores\n"
        "e veja o resultado explicado de forma clara."
    )
    print("=" * 60)


def show_menu():
    print("\n📌 MENU DE OPERAÇÕES")
    print("1 - Média")
    print("2 - Mediana")
    print("3 - Moda")
    print("4 - Variância")
    print("5 - Desvio padrão")
    print("6 - Mínimo e Máximo")
    print("7 - Amplitude")
    print("8 - Quartis")
    print("9 - Coeficiente de variação")
    print("0 - Sair")


def process_choice(choice, values):
    if choice == "1":
        result = stats.mean(values)
        print(f"\n📊 MÉDIA: {result:.2f}")
        print("A média representa o valor médio do conjunto.")

    elif choice == "2":
        result = stats.median(values)
        print(f"\n📊 MEDIANA: {result:.2f}")
        print("Divide os dados ordenados ao meio.")

    elif choice == "3":
        result = stats.mode(values)
        if result:
            print(f"\n📊 MODA: {result}")
            print("Valor(es) mais frequente(s) do conjunto.")
        else:
            print("\n📊 MODA: Não existe")
            print("Todos os valores aparecem apenas uma vez.")

    elif choice == "4":
        result = stats.variance(values)
        print(f"\n📊 VARIÂNCIA: {result:.2f}")
        print("Indica o nível de dispersão dos dados.")

    elif choice == "5":
        result = stats.standard_deviation(values)
        print(f"\n📊 DESVIO PADRÃO: {result:.2f}")
        print("Mostra o afastamento médio em relação à média.")

    elif choice == "6":
        print(f"\n📊 MÍNIMO: {stats.minimum(values)}")
        print(f"📊 MÁXIMO: {stats.maximum(values)}")
        print("Mostram os extremos do conjunto.")

    elif choice == "7":
        result = stats.amplitude(values)
        print(f"\n📊 AMPLITUDE: {result}")
        print("Diferença entre o maior e o menor valor.")

    elif choice == "8":
        q1, q2, q3 = stats.quartiles(values)
        print("\n📊 QUARTIS")
        print(f"Q1 (25%): {q1}")
        print(f"Q2 (50%): {q2}")
        print(f"Q3 (75%): {q3}")
        print("Dividem os dados em quatro partes iguais.")

    elif choice == "9":
        cv = stats.coefficient_of_variation(values)
        if cv is not None:
            print(f"\n📊 COEFICIENTE DE VARIAÇÃO: {cv:.2f}%")
            print("Permite comparar a dispersão entre conjuntos.")
        else:
            print("\n📊 COEFICIENTE DE VARIAÇÃO: Indefinido (média zero)")

    else:
        print("\n❌ Opção inválida.")


def run():
    show_welcome()
    values = ask_for_values()

    while True:
        show_menu()
        choice = input("\nEscolha uma opção: ")

        if choice == "0":
            print("\n👋 Programa encerrado.")
            break

        process_choice(choice, values)
        input("\nPressione ENTER para continuar...")
