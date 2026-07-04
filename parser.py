def parsear(tokens):
    global pos, lista_tokens
    pos = 0
    lista_tokens = tokens
    # llama a la función raíz de la gramática
    print("se conecta con el parser!")
    print("Tokens a parsear:", lista_tokens)
    



def consumir(tipo_esperado, valor_esperado=None):
    #La función consumir se encarga de levantar errores de sintaxis cuando entra un token que no corresponde, o un valor no esperado para el token. Recibe de la función parse correspondiente el tipo de token que se espera y, para los casos de palabras reservadas, el valor que se espera. Si el token actual no coincide con lo esperado, se lanza una excepción con un mensaje de error.
    global pos 
    #guarda el token actual en caso de que no se haya llegado al final de la lista de tokens. De lo contrario, none.
    token_actual = lista_tokens[pos] if pos < len(lista_tokens) else None
    #Si el token actual es None, significa que no llegó el token siguiente que correspondería. Por tanto, lanza un error.
    if token_actual is None:
        raise Exception(f"Error de sintaxis: se esperaba {tipo_esperado} pero no hay más tokens.")

    tipo = token_actual.tipo
    valor = token_actual.valor
    linea = token_actual.linea
    columna = token_actual.columna
    
    if tipo != tipo_esperado:
        raise Exception(f"Error de sintaxis: se esperaba {tipo_esperado}, pero se encontró {tipo} en la línea {linea}, columna {columna}.")
    
    if valor_esperado is not None and valor != valor_esperado:
        raise Exception(f"Error de sintaxis: se esperaba el valor '{valor_esperado}', pero se encontró '{valor}' en la línea {linea}, columna {columna}.")
    
    pos += 1
    return token_actual


