def parse_input(input_string, max_values=10):
    """
    Converte a entrada do usuário em uma lista de floats.
    Aceita até 'max_values' números.
    """
    parts = input_string.replace(",", ".").split()

    if not parts:
        raise ValueError("Nenhum valor foi informado.")

    if len(parts) > max_values:
        raise ValueError(f"Você pode inserir no máximo {max_values} valores.")

    values = []

    for p in parts:
        try:
            values.append(float(p))
        except ValueError:
            raise ValueError(f"Valor inválido encontrado: '{p}'")

    return values


def ask_for_values():
    """
    Solicita valores ao usuário até receber uma entrada válida.
    """
    while True:
        try:
            raw = input("\nDigite de 1 até 10 valores numéricos separados por espaço:\n> ")
            values = parse_input(raw)

            if len(values) < 1:
                raise ValueError("Informe pelo menos um valor.")

            return values