# CALCULADORA FINANCIERA PERSONAL

# =============================================================================
# PASO 1: CREACION DE ESTRUCTURAS DE DATOS
# =============================================================================
# Aquí guardamos todos nuestros datos. Usamos listas de diccionarios porque:
# - Las listas pueden crecer (agregar más elementos)
# - Los diccionarios nos permiten guardar información organizada (como nombre y valor juntos)

lista_ingresos = []  # Esta lista guardará todos nuestros ingresos
lista_gastos = []    # Esta lista guardará todos nuestros gastos

# Lista de categorías para los gastos (como un menú de opciones)
categorias_gastos = ["alimentacion", "transporte", "entretenimiento", "salud", "educacion", "servicios"]

# =============================================================================
# PASO 2: FUNCIONES PARA VALIDAR DATOS
# =============================================================================
# Esta función se asegura de que el usuario escriba un número válido

def pedir_numero_positivo(mensaje):
    """
    Esta función pide un número al usuario y se asegura de que sea válido
    - Si el usuario escribe letras, le dice que está mal
    - Si escribe un número negativo, le dice que debe ser positivo
    - Solo sale de la función cuando el número está correcto
    """
    while True:  # Este bucle se repite hasta que el número sea correcto
        try:  # "try" significa "intenta hacer esto"
            numero = float(input(mensaje))  # Convertimos el texto a número decimal
            if numero <= 0:  # Si el número es cero o negativo
                print("❌ ERROR: El número debe ser mayor que cero")
                print("Por favor intente de nuevo\n")
            else:  # Si el número es positivo
                return numero  # Devolvemos el número y salimos de la función
        except ValueError:  # "except" significa "si algo sale mal, haz esto"
            print("❌ ERROR: Debe escribir solo números")
            print("Ejemplo correcto: 1500 o 1500.50")
            print("No escriba letras ni símbolos\n")

def pedir_opcion_menu(mensaje, maximo):
    """
    Esta función pide una opción de menú y verifica que sea válida
    """
    while True:
        try:
            opcion = int(input(mensaje))  # Convertimos a número entero
            if opcion < 1 or opcion > maximo:  # Si la opción está fuera del rango
                print(f"❌ ERROR: Debe elegir un número entre 1 y {maximo}")
            else:
                return opcion  # Devolvemos la opción válida
        except ValueError:
            print("❌ ERROR: Debe escribir solo números del menú")

# =============================================================================
# PASO 3: FUNCIÓN PARA REGISTRAR INGRESOS
# =============================================================================
def registrar_ingresos():
    """
    Esta función permite al usuario registrar sus ingresos
    Usa un bucle for para registrar varios ingresos de una vez
    """
    print("\n" + "="*50)
    print("           REGISTRAR INGRESOS")
    print("="*50)
    
    # Primero preguntamos cuántos ingresos quiere registrar
    cantidad = pedir_opcion_menu("¿Cuántos ingresos desea registrar?: ", 10)
    
    # Usamos un bucle for para repetir el proceso según la cantidad
    for i in range(cantidad):  # range(cantidad) crea una secuencia: 0, 1, 2, etc.
        print(f"\n--- Ingreso número {i+1} ---")  # i+1 porque empezamos desde 1, no 0
        
        # Pedimos la descripción del ingreso
        while True:  # Bucle para asegurar que no esté vacío
            descripcion = input("Descripción del ingreso (ej: salario, venta): ").strip()   #.strip()se usa para eliminar los espacios en blanco (u otros caracteres) al inicio y al final de una cadena de texto (string).
            if descripcion:  # Si no está vacío   #Equivalente a haber puesto if descripcion != "": 
                break  # Salimos del bucle
            else:
                print("❌ La descripción no puede estar vacía")
        
        # Pedimos el valor usando nuestra función de validación
        valor = pedir_numero_positivo("Valor del ingreso $: ")
        
        # Creamos un diccionario con los datos del ingreso
        nuevo_ingreso = {
            "descripcion": descripcion,
            "valor": valor
        }
        
        # Agregamos el diccionario a nuestra lista
        lista_ingresos.append(nuevo_ingreso)
        
        # Confirmamos que se guardó correctamente
        print(f"✅ Ingreso guardado: {descripcion} - ${valor:,.2f}")
        # ${valor:,.2f} formatea la variable valor (que debe ser un número) para mostrarla como un monto en dinero:
        # : indica que se va a aplicar un formato especial.
        # , añade separadores de miles (por ejemplo, 12345 se mostraría como 12,345).
        # .2f limita el número a dos decimales,
    
    print(f"\n🎉 Se registraron {cantidad} ingresos exitosamente!")

# =============================================================================
# PASO 4: FUNCIÓN PARA REGISTRAR GASTOS
# =============================================================================
def registrar_gastos():
    """
    Esta función permite registrar gastos con su categoría
    """
    print("\n" + "="*50)
    print("           REGISTRAR GASTOS")
    print("="*50)
    
    cantidad = pedir_opcion_menu("¿Cuántos gastos desea registrar?: ", 10)
    
    # Bucle for para registrar cada gasto
    for i in range(cantidad):
        print(f"\n--- Gasto número {i+1} ---")
        
        # Pedimos el nombre del gasto
        while True:
            nombre = input("Nombre del gasto (ej: supermercado, gasolina): ").strip()
            if nombre:
                break
            else:
                print("❌ El nombre no puede estar vacío")
        
        # Pedimos el valor
        valor = pedir_numero_positivo("Valor del gasto $: ")
        
        # Mostramos las categorías disponibles
        print("\nCategorías disponibles:")  #len se usa para contar el numero total de categorias 
        for j in range(len(categorias_gastos)):  # Bucle for para mostrar cada categoría
            print(f"{j+1}. {categorias_gastos[j].title()}")  # .title() pone la primera letra en mayúscula
        
        # Pedimos que elija una categoría
        opcion_categoria = pedir_opcion_menu("Seleccione el número de la categoría: ", len(categorias_gastos)) # len(categorias_gastos) establece el máximo permitido
        categoria_seleccionada = categorias_gastos[opcion_categoria - 1]  # -1 porque las listas empiezan en 0 Ej: Si usuario selecciona 1 → accede al índice 0 de la lista
        
        # Creamos el diccionario del gasto
        nuevo_gasto = {
            "nombre": nombre,
            "valor": valor,
            "categoria": categoria_seleccionada
        }
        
        # Lo agregamos a la lista
        lista_gastos.append(nuevo_gasto)
        
        print(f"✅ Gasto guardado: {nombre} - ${valor:,.2f} ({categoria_seleccionada.title()})")
    
    print(f"\n🎉 Se registraron {cantidad} gastos exitosamente!")

# =============================================================================
# PASO 5: FUNCIÓN PARA MOSTRAR EL RESUMEN
# =============================================================================
def mostrar_resumen():
    """
    Esta función calcula y muestra todo el resumen financiero
    Usa bucles for para recorrer las listas y sumar los valores
    """
    print("\n" + "="*60)
    print("              RESUMEN FINANCIERO MENSUAL")
    print("="*60)
    
    # Verificamos si hay datos para mostrar
    if len(lista_ingresos) == 0 and len(lista_gastos) == 0:
        print("📋 No hay datos registrados aún.")
        print("Primero registre algunos ingresos y gastos.")
        return  # Salimos de la función si no hay datos
    
    # CALCULAMOS EL TOTAL DE INGRESOS
    total_ingresos = 0  # Empezamos en cero
    for ingreso in lista_ingresos:  # Recorremos cada ingreso en la lista
        total_ingresos = total_ingresos + ingreso["valor"]  # Sumamos el valor
    
    # CALCULAMOS EL TOTAL DE GASTOS
    total_gastos = 0
    for gasto in lista_gastos:  # Recorremos cada gasto
        total_gastos = total_gastos + gasto["valor"]
    
    # CALCULAMOS EL SALDO
    saldo_disponible = total_ingresos - total_gastos
    
    # MOSTRAMOS LOS RESULTADOS BÁSICOS
    print(f"💰 Total de Ingresos:    ${total_ingresos:,.2f}")
    print(f"💸 Total de Gastos:      ${total_gastos:,.2f}")
    print("-" * 40)
    print(f"💳 Saldo Disponible:     ${saldo_disponible:,.2f}")
    
    # CALCULAMOS EL PORCENTAJE DE AHORRO
    if total_ingresos > 0:  # Solo si hay ingresos (para evitar división por cero)
        porcentaje_ahorro = (saldo_disponible / total_ingresos) * 100
        print(f"📊 Porcentaje de Ahorro: {porcentaje_ahorro:.1f}%")
    else:
        print("📊 Porcentaje de Ahorro: No calculable (sin ingresos)")
    
    # GASTOS POR CATEGORÍA (solo si hay gastos)
    if len(lista_gastos) > 0:
        print("\n" + "="*50)
        print("         GASTOS POR CATEGORÍA")
        print("="*50)
        
        # Creamos un diccionario para sumar por categoría
        gastos_por_categoria = {}
        
        # Recorremos todos los gastos
        for gasto in lista_gastos:
            categoria = gasto["categoria"]
            valor = gasto["valor"]
            
            # Si la categoría ya existe en el diccionario, sumamos
            if categoria in gastos_por_categoria:
                gastos_por_categoria[categoria] = gastos_por_categoria[categoria] + valor
            else:  # Si es la primera vez, la creamos
                gastos_por_categoria[categoria] = valor
        
        # Mostramos cada categoría con su total y porcentaje
        for categoria, total in gastos_por_categoria.items():
            if total_gastos > 0:  # Para evitar división por cero
                porcentaje = (total / total_gastos) * 100
                print(f"🏷️  {categoria.title():<15}: ${total:>8,.2f} ({porcentaje:.1f}%)")
    
    # RECOMENDACIONES AUTOMÁTICAS
    print("\n" + "="*50)
    print("           RECOMENDACIONES")
    print("="*50)
    
    if total_ingresos == 0:
        print("⚠️  No ha registrado ingresos. Comience por ahí.")
    else:
        # Calculamos qué porcentaje de los ingresos se está gastando
        porcentaje_gasto = (total_gastos / total_ingresos) * 100
        
        # Usamos if/elif/else para dar diferentes recomendaciones
        if porcentaje_gasto > 100:
            print("🚨 ¡ALERTA! Está gastando más de lo que gana.")
            print("   Debe reducir gastos urgentemente.")
        elif porcentaje_gasto > 80:
            print("⚠️  ¡Alerta! Está gastando más de lo recomendable.")
            print("   Trate de reducir algunos gastos.")
        elif porcentaje_gasto < 50:
            print("🌟 ¡Excelente! Tiene muy buenos hábitos financieros.")
            print("   Está ahorrando más del 50% de sus ingresos.")
        else:
            print("👍 Sus finanzas están en buen estado.")
            print("   Mantenga este equilibrio.")

# =============================================================================
# PASO 6: FUNCIONES PARA MODIFICAR Y ELIMINAR
# =============================================================================
def mostrar_lista_ingresos():
    """
    Muestra todos los ingresos con números para que el usuario pueda elegir
    """
    if len(lista_ingresos) == 0:
        print("📋 No hay ingresos registrados.")
        return False  # Devolvemos False para indicar que no hay datos
    
    print("\n--- LISTA DE INGRESOS ---")
    for i in range(len(lista_ingresos)):  # Bucle for con índices
        ingreso = lista_ingresos[i]
        print(f"{i+1}. {ingreso['descripcion']} - ${ingreso['valor']:,.2f}")
    
    return True  # Devolvemos True para indicar que sí hay datos

def mostrar_lista_gastos():
    """
    Muestra todos los gastos con números para que el usuario pueda elegir
    """
    if len(lista_gastos) == 0:
        print("📋 No hay gastos registrados.")
        return False
    
    print("\n--- LISTA DE GASTOS ---")
    for i in range(len(lista_gastos)):
        gasto = lista_gastos[i]
        print(f"{i+1}. {gasto['nombre']} - ${gasto['valor']:,.2f} ({gasto['categoria'].title()})")
    
    return True

def modificar_ingresos():
    """
    Permite modificar un ingreso existente
    """
    print("\n--- MODIFICAR INGRESOS ---")
    
    # Primero mostramos la lista
    if not mostrar_lista_ingresos():  # Si no hay ingresos
        return  # Salimos de la función
    
    # Pedimos cuál quiere modificar
    numero = pedir_opcion_menu("¿Cuál ingreso desea modificar? (número): ", len(lista_ingresos))
    indice = numero - 1  # Convertimos a índice de lista (empiezan en 0)
    
    # Mostramos el ingreso actual
    ingreso_actual = lista_ingresos[indice]
    print(f"\nIngreso actual: {ingreso_actual['descripcion']} - ${ingreso_actual['valor']:,.2f}")
    
    # Pedimos la nueva descripción (opcional)
    print("Deje en blanco si no quiere cambiar la descripción")
    nueva_descripcion = input("Nueva descripción: ").strip()
    if nueva_descripcion:  # Si escribió algo
        lista_ingresos[indice]["descripcion"] = nueva_descripcion
    
    # Pedimos el nuevo valor (opcional)
    print("Escriba 0 si no quiere cambiar el valor")
    try:
        nuevo_valor = float(input("Nuevo valor: "))
        if nuevo_valor > 0:
            lista_ingresos[indice]["valor"] = nuevo_valor
    except ValueError:
        print("Valor no válido, se mantiene el anterior")
    
    print("✅ Ingreso modificado exitosamente!")

def eliminar_ingresos():
    """
    Permite eliminar un ingreso
    """
    print("\n--- ELIMINAR INGRESOS ---")
    
    if not mostrar_lista_ingresos():
        return
    
    numero = pedir_opcion_menu("¿Cuál ingreso desea eliminar? (número): ", len(lista_ingresos))
    indice = numero - 1
    
    # Guardamos el ingreso que vamos a eliminar para confirmarlo
    ingreso_eliminado = lista_ingresos[indice]
    
    # Confirmamos la eliminación
    print(f"¿Está sure de eliminar: {ingreso_eliminado['descripcion']} - ${ingreso_eliminado['valor']:,.2f}?")
    confirmacion = input("Escriba 'SI' para confirmar: ").upper()
    
    if confirmacion == "SI":
        lista_ingresos.pop(indice)  # .pop() elimina el elemento en esa posición
        print("✅ Ingreso eliminado exitosamente!")
    else:
        print("❌ Eliminación cancelada")

def modificar_gastos():
    """
    Permite modificar un gasto existente
    """
    print("\n--- MODIFICAR GASTOS ---")
    
    if not mostrar_lista_gastos():
        return
    
    numero = pedir_opcion_menu("¿Cuál gasto desea modificar? (número): ", len(lista_gastos))
    indice = numero - 1
    
    gasto_actual = lista_gastos[indice]
    print(f"\nGasto actual: {gasto_actual['nombre']} - ${gasto_actual['valor']:,.2f} ({gasto_actual['categoria'].title()})")
    
    # Modificar nombre
    print("Deje en blanco si no quiere cambiar el nombre")
    nuevo_nombre = input("Nuevo nombre: ").strip()
    if nuevo_nombre:
        lista_gastos[indice]["nombre"] = nuevo_nombre
    
    # Modificar valor
    print("Escriba 0 si no quiere cambiar el valor")
    try:
        nuevo_valor = float(input("Nuevo valor: "))
        if nuevo_valor > 0:
            lista_gastos[indice]["valor"] = nuevo_valor
    except ValueError:
        print("Valor no válido, se mantiene el anterior")
    
    # Modificar categoría
    cambiar_categoria = input("¿Desea cambiar la categoría? (si/no): ").lower()
    if cambiar_categoria in ["si", "sí", "s"]:
        print("\nCategorías disponibles:")
        for j in range(len(categorias_gastos)):
            print(f"{j+1}. {categorias_gastos[j].title()}")
        
        opcion = pedir_opcion_menu("Seleccione nueva categoría: ", len(categorias_gastos))
        lista_gastos[indice]["categoria"] = categorias_gastos[opcion - 1]
    
    print("✅ Gasto modificado exitosamente!")

def eliminar_gastos():
    """
    Permite eliminar un gasto
    """
    print("\n--- ELIMINAR GASTOS ---")
    
    if not mostrar_lista_gastos():
        return
    
    numero = pedir_opcion_menu("¿Cuál gasto desea eliminar? (número): ", len(lista_gastos))
    indice = numero - 1
    
    gasto_eliminado = lista_gastos[indice]
    print(f"¿Está seguro de eliminar: {gasto_eliminado['nombre']} - ${gasto_eliminado['valor']:,.2f}?")
    confirmacion = input("Escriba 'SI' para confirmar: ").upper()
    
    if confirmacion == "SI":
        lista_gastos.pop(indice)
        print("✅ Gasto eliminado exitosamente!")
    else:
        print("❌ Eliminación cancelada")

def menu_modificar_eliminar():
    """
    Submenú para modificar o eliminar registros
    """
    while True:  # Bucle infinito hasta que el usuario elija salir
        print("\n" + "="*50)
        print("        MODIFICAR O ELIMINAR REGISTROS")
        print("="*50)
        print("1. Modificar Ingresos")
        print("2. Eliminar Ingresos")
        print("3. Modificar Gastos")
        print("4. Eliminar Gastos")
        print("5. Volver al Menú Principal")
        
        opcion = pedir_opcion_menu("Seleccione una opción: ", 5)
        
        # Usamos if/elif/else porque match-case lo usaremos solo en el menú principal
        if opcion == 1:
            modificar_ingresos()
        elif opcion == 2:
            eliminar_ingresos()
        elif opcion == 3:
            modificar_gastos()
        elif opcion == 4:
            eliminar_gastos()
        elif opcion == 5:
            break  # Salimos del bucle while y volvemos al menú principal

# =============================================================================
# PASO 7: FUNCIÓN PRINCIPAL DEL PROGRAMA
# =============================================================================
def menu_principal():
    """
    Esta es la función principal que controla todo el programa
    Usa un bucle while True para que el programa siga funcionando hasta que el usuario decida salir
    """
    # Mensaje de bienvenida (como el que ya tenías)
    print("="*60)
    print("    CALCULADORA FINANCIERA PERSONAL")
    print("="*60)
    print("Señor usuario, el siguiente programa le permitirá ver un")
    print("Resumen Financiero sobre sus Ingresos y Gastos mensuales\n")
    
    # Bucle principal del programa
    while True:  # Este bucle hace que el programa siga funcionando
        # Mostramos el menú (como el que ya tenías)
        print("\n" + "="*50)
        print("Menu Calculadora Financiera Personal:")
        print("="*50)
        print("1. Registrar Ingresos")
        print("2. Registrar Gastos")
        print("3. Ver Resumen Financiero")
        print("4. Modificar o Eliminar Registros")
        print("5. Salir del programa")
        print("="*50)
        
        # Pedimos la opción al usuario
        opcion = pedir_opcion_menu("Por favor digite el número de la opción que desea: ", 5)
        
        # Usamos match-case como pedían en los requisitos
        match opcion:
            case 1:
                registrar_ingresos()
            case 2:
                registrar_gastos()
            case 3:
                mostrar_resumen()
            case 4:
                menu_modificar_eliminar()
            case 5:
                # Mensaje de despedida
                print("\n" + "="*50)
                print("  GRACIAS POR USAR LA CALCULADORA FINANCIERA")
                print("="*50)
                print("¡Que tenga un excelente día! 💰")
                break  # Salimos del bucle while y terminamos el programa

# =============================================================================
# PASO 8: EJECUTAR EL PROGRAMA
# =============================================================================
# Esta línea hace que el programa empiece a funcionar
if __name__ == "__main__":
    menu_principal()  # Llamamos a la función principal