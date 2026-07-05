def parsear(tokens):
    global pos, lista_tokens
    pos = 0
    lista_tokens = tokens
    # llama a la función raíz de la gramática
    print("Tokens a parsear:", lista_tokens)
    parse_expresion()
    print("######################")
    print("STRING ACEPTADO! :)")
    print("######################")
    

#------------------------FUNCION CONSUMIR:
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
#-----------FIN FUNCIÓN CONSUMIR.

#---------------FUNCIONES DE PARSEO:

#PARSER DE CONDICIONES:
#def parse_condicion():


#PARSER DE EXPRESIONES:
def parse_expresion():
#Tipo de producción: EXPRESION -> (sensor o dispositivo) OPERADOR (valor correspondiente)
    #Parseo de SENSORES:
    if lista_tokens[pos].tipo == "SENSOR":
        token = consumir("SENSOR")
        subtipo = token.valor.split('_')[1]  # 'sensor_humo_cocina' → 'humo' (subtipo)
        match subtipo:
            case "humo":
                #Sensor de humo: sensor_humo_<id> OPERADOR BOOLEANO_SENSOR
                consumir("OPERADOR", "==")
                consumir("BOOLEANO_SENSOR")
            case "movimiento":
                consumir("OPERADOR","==")
                consumir("BOOLEANO_SENSOR")
            case "luz":
                consumir("OPERADOR")
                consumir("LUZ")
            case "humedad":
                consumir("OPERADOR")
                consumir("PORCENTAJE")
            case "temp":
                consumir("OPERADOR")
                consumir("TEMPERATURA")
    elif lista_tokens[pos].tipo == "DISPOSITIVO":
        token = consumir("DISPOSITIVO")
        dispositivo = token.valor.split('_')[0]  # 'foco_sala' → 'foco' (tipo de dispositivo)
        match dispositivo:
            case "foco":
                #Dispositivo foco: foco_<id> PUNTO ATRIBUTO
                consumir("PUNTO")
                atributo = consumir("ATRIBUTO").valor
                match atributo:
                    case "estado":
                        #Atributo estado de foco: foco_<id>.estado OPERADOR BOOLEANO_DISPOSITIVO
                        consumir("OPERADOR", "==")
                        consumir("BOOLEANO_DISPOSITIVO")
                    case "brillo":
                        #Atributo brillo de foco: foco_<id>.brillo OPERADOR PORCENTAJE
                        consumir("OPERADOR")
                        consumir("PORCENTAJE")
            case "aire":
                #Dispositivo aire: aire_<id> PUNTO ATRIBUTO
                consumir("PUNTO")
                atributo = consumir("ATRIBUTO").valor
                match atributo:
                    case "estado":
                        #Atributo estado de aire: aire_<id>.estado OPERADOR BOOLEANO_DISPOSITIVO
                        consumir("OPERADOR", "==")
                        consumir("BOOLEANO_DISPOSITIVO")
                    case "modo":
                        #Atributo modo de aire: aire_<id>.modo OPERADOR VALOR_DISCRETO
                        consumir("OPERADOR", "==")
                        consumir("VALOR_DISCRETO")
                    case "temp_obj":
                        #Atributo temp_obj de aire: aire_<id>.temp_obj OPERADOR TEMPERATURA
                        consumir("OPERADOR")
                        consumir("TEMPERATURA")
                    case "temp_act":
                        #Atributo temp_act de aire: aire_<id>.temp_act OPERADOR TEMPERATURA
                        consumir("OPERADOR")
                        consumir("TEMPERATURA")
            case "persiana":
                #Dispositivo persiana: persiana_<id> PUNTO ATRIBUTO OPERADOR PORCENTAJE
                consumir("PUNTO")
                consumir("ATRIBUTO", "posicion")
                consumir("OPERADOR")
                consumir("PORCENTAJE")
            case "cerradura":
                #Dispositivo cerradura: cerradura_<id> PUNTO ATRIBUTO OPERADOR BOOLEANO_DISPOSITIVO
                consumir("PUNTO")
                consumir("ATRIBUTO", "estado")
                consumir("OPERADOR", "==")
                consumir("BOOLEANO_DISPOSITIVO")
            case "reloj":
                #Dispositivo reloj: reloj_<id> PUNTO ATRIBUTO
                consumir("PUNTO")
                atributo = consumir("ATRIBUTO").valor
                match atributo:
                    case "hora":
                        #Atributo hora de reloj: reloj_<id>.hora OPERADOR HORA
                        consumir("OPERADOR")
                        consumir("HORA")
                    case "fecha":
                        #Atributo fecha de reloj: reloj_<id>.fecha OPERADOR FECHA
                        consumir("OPERADOR")
                        consumir("FECHA")
            case "altavoz":
                #Dispositivo altavoz: altavoz_<id> PUNTO ATRIBUTO
                consumir("PUNTO")
                atributo = consumir("ATRIBUTO").valor
                match atributo:
                    case "volumen":
                        #Atributo volumen de altavoz: altavoz_<id>.volumen OPERADOR PORCENTAJE
                        consumir("OPERADOR")
                        consumir("PORCENTAJE")
                    case "mute":
                        #Atributo mute de altavoz: altavoz_<id>.mute OPERADOR BOOLEANO_DISPOSITIVO
                        consumir("OPERADOR", "==")
                        consumir("BOOLEANO_DISPOSITIVO")
                    case "mensaje":
                        #Atributo mensaje de altavoz: altavoz_<id>.mensaje OPERADOR TEXTO
                        consumir("OPERADOR", "==")
                        consumir("TEXTO")
                    case "email_notif":
                        #Atributo email_notif de altavoz: altavoz_<id>.email_notif OPERADOR EMAIL
                        consumir("OPERADOR", "==")
                        consumir("EMAIL")
            case "alarma":
                #Dispositivo alarma: alarma_<id> PUNTO ATRIBUTO
                consumir("PUNTO")
                atributo = consumir("ATRIBUTO").valor
                match atributo:
                    case "estado":
                        #Atributo estado de alarma: alarma_<id>.estado OPERADOR BOOLEANO_DISPOSITIVO
                        consumir("OPERADOR", "==")
                        consumir("BOOLEANO_DISPOSITIVO")
                    case "activada":
                        #Atributo activada de alarma: alarma_<id>.activada OPERADOR BOOLEANO_DISPOSITIVO
                        consumir("OPERADOR", "==")
                        consumir("BOOLEANO_DISPOSITIVO")
    print("El token es: ",token)

#PARSER DE OPERADORES:
def parse_operador():
    return consumir("OPERADOR")
