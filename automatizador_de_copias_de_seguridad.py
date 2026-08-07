ids = []
nombres = []
origenes = []
destinos = []
tipos = []
frecuencias = []
fechas = []
horas = []
tamanos = []
estados = []
observaciones = []
historial_ids = []
historial_nombres = []
historial_fechas = []
historial_horas = []
historial_estados = []
#---------------------------------------------------------#
#--|menu_principal_automatizador_de_copias_de_seguridad|--#
#---------------------------------------------------------#
while True:
    print("menu principal automatizador de copias de seguridad")
    print("1) registrar copia")
    print("2) editar copia")
    print("3) eliminar copia")
    print("4) buscar copia")
    print("5) ejecutar copia")
    print("6) historial de copias")
    print("7) lista de datos")
    print("8) salir")
    opcion = input("seleccione una opción: ")
    #---------------------#
    #--|registrar_copia|--#
    #---------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_copia = 1
        else:
            id_copia = ids[-1] + 1
        nombre = input("nombre de la copia: ")
        origen = input("origen de los datos: ")
        destino = input("destino de la copia: ")
        print("tipos de copia")
        print("1) completa")
        print("2) incremental")
        print("3) diferencial")
        opcion_tipo = input("seleccione el tipo de copia: ")
        if opcion_tipo == "1":
            tipo = "completa"
        elif opcion_tipo == "2":
            tipo = "incremental"
        elif opcion_tipo == "3":
            tipo = "diferencial"
        else:
            tipo = "sin definir"
        print("frecuencias")
        print("1) diaria")
        print("2) semanal")
        print("3) mensual")
        print("4) manual")
        opcion_frecuencia = input(
            "seleccione la frecuencia: "
        )
        if opcion_frecuencia == "1":
            frecuencia = "diaria"
        elif opcion_frecuencia == "2":
            frecuencia = "semanal"
        elif opcion_frecuencia == "3":
            frecuencia = "mensual"
        elif opcion_frecuencia == "4":
            frecuencia = "manual"
        else:
            frecuencia = "sin definir"
        fecha = input("fecha programada: ")
        hora = input("hora programada: ")
        tamano = input("tamaño estimado: ")
        observacion = input("observación: ")
        estado = "programada"
        ids.append(id_copia)
        nombres.append(nombre)
        origenes.append(origen)
        destinos.append(destino)
        tipos.append(tipo)
        frecuencias.append(frecuencia)
        fechas.append(fecha)
        horas.append(hora)
        tamanos.append(tamano)
        estados.append(estado)
        observaciones.append(observacion)
        print("copia registrada correctamente.")
        print("id:", id_copia)
        print("tipo:", tipo)
        print("frecuencia:", frecuencia)
        print("estado:", estado)
    #------------------#
    #--|editar_copia|--#
    #------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen copias registradas.")
        else:
            print("editar copia")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{tipos[i]} | "
                    f"{frecuencias[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id de la copia: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("nombre:", nombres[posicion])
                print("origen:", origenes[posicion])
                print("destino:", destinos[posicion])
                print("tipo:", tipos[posicion])
                print("frecuencia:", frecuencias[posicion])
                print("fecha:", fechas[posicion])
                print("hora:", horas[posicion])
                print("tamaño:", tamanos[posicion])
                print("estado:", estados[posicion])
                nombres[posicion] = input(
                    "nuevo nombre: "
                )
                origenes[posicion] = input(
                    "nuevo origen: "
                )
                destinos[posicion] = input(
                    "nuevo destino: "
                )
                print("tipos de copia")
                print("1) completa")
                print("2) incremental")
                print("3) diferencial")
                opcion_tipo = input(
                    "seleccione el tipo de copia: "
                )
                if opcion_tipo == "1":
                    tipos[posicion] = "completa"
                elif opcion_tipo == "2":
                    tipos[posicion] = "incremental"
                elif opcion_tipo == "3":
                    tipos[posicion] = "diferencial"
                else:
                    tipos[posicion] = "sin definir"
                print("frecuencias")
                print("1) diaria")
                print("2) semanal")
                print("3) mensual")
                print("4) manual")
                opcion_frecuencia = input(
                    "seleccione la frecuencia: "
                )
                if opcion_frecuencia == "1":
                    frecuencias[posicion] = "diaria"
                elif opcion_frecuencia == "2":
                    frecuencias[posicion] = "semanal"
                elif opcion_frecuencia == "3":
                    frecuencias[posicion] = "mensual"
                elif opcion_frecuencia == "4":
                    frecuencias[posicion] = "manual"
                else:
                    frecuencias[posicion] = "sin definir"
                fechas[posicion] = input(
                    "nueva fecha: "
                )
                horas[posicion] = input(
                    "nueva hora: "
                )
                tamanos[posicion] = input(
                    "nuevo tamaño estimado: "
                )
                observaciones[posicion] = input(
                    "nueva observación: "
                )
                estados[posicion] = "programada"
                print(
                    "copia actualizada correctamente."
                )
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_copia|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen copias registradas.")
        else:
            print("eliminar copia")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{tipos[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id de la copia: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("nombre:", nombres[posicion])
                print("origen:", origenes[posicion])
                print("destino:", destinos[posicion])
                confirmacion = input(
                    "¿desea eliminar esta copia? (s/n): "
                )
                if confirmacion.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    origenes.pop(posicion)
                    destinos.pop(posicion)
                    tipos.pop(posicion)
                    frecuencias.pop(posicion)
                    fechas.pop(posicion)
                    horas.pop(posicion)
                    tamanos.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print(
                        "copia eliminada correctamente."
                    )
                else:
                    print(
                        "la copia no fue eliminada."
                    )
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_copia|--#
    #------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen copias registradas.")
        else:
            id_buscar = int(
                input("ingrese la id de la copia: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("información de la copia")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("origen:", origenes[posicion])
                print("destino:", destinos[posicion])
                print("tipo:", tipos[posicion])
                print("frecuencia:", frecuencias[posicion])
                print("fecha:", fechas[posicion])
                print("hora:", horas[posicion])
                print("tamaño:", tamanos[posicion])
                print("estado:", estados[posicion])
                print(
                    "observación:",
                    observaciones[posicion]
                )
            else:
                print("id no encontrada.")
    #--------------------#
    #--|ejecutar_copia|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen copias registradas.")
        else:
            print("ejecutar copia de seguridad")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{tipos[i]} | "
                    f"{estados[i]}"
                )
            id_ejecutar = int(
                input(
                    "ingrese la id de la copia: "
                )
            )
            if id_ejecutar in ids:
                posicion = ids.index(id_ejecutar)
                print(
                    "copia seleccionada:",
                    nombres[posicion]
                )
                print(
                    "origen:",
                    origenes[posicion]
                )
                print(
                    "destino:",
                    destinos[posicion]
                )
                print(
                    "tipo:",
                    tipos[posicion]
                )
                print("iniciando copia de seguridad...")
                print("✓ preparando copia")
                print("✓ analizando información")
                print("✓ copiando datos")
                print("✓ verificando respaldo")
                print("✓ copia completada")
                estados[posicion] = "completada"
                if len(historial_ids) == 0:
                    id_historial = 1
                else:
                    id_historial = historial_ids[-1] + 1
                historial_ids.append(id_historial)
                historial_nombres.append(
                    nombres[posicion]
                )
                historial_fechas.append(
                    fechas[posicion]
                )
                historial_horas.append(
                    horas[posicion]
                )
                historial_estados.append(
                    "completada"
                )
                print(
                    "copia de seguridad ejecutada correctamente."
                )
                print(
                    "estado:",
                    estados[posicion]
                )
            else:
                print("id no encontrada.")
    #-------------------------#
    #--|historial_de_copias|--#
    #-------------------------#
    elif opcion == "6":
        if len(historial_ids) == 0:
            print(
                "no existen copias ejecutadas."
            )
        else:
            print("historial de copias")
            for i in range(len(historial_ids)):
                print(
                    f"{historial_ids[i]} | "
                    f"{historial_nombres[i]} | "
                    f"{historial_fechas[i]} | "
                    f"{historial_horas[i]} | "
                    f"{historial_estados[i]}"
                )
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "7":
        if len(ids) == 0:
            print("no existen copias registradas.")
        else:
            completadas = 0
            programadas = 0
            pendientes = 0
            completas = 0
            incrementales = 0
            diferenciales = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{tipos[i]} | "
                    f"{frecuencias[i]} | "
                    f"{estados[i]}"
                )
                if estados[i].lower() == "completada":
                    completadas += 1
                elif estados[i].lower() == "programada":
                    programadas += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
                if tipos[i].lower() == "completa":
                    completas += 1
                elif tipos[i].lower() == "incremental":
                    incrementales += 1
                elif tipos[i].lower() == "diferencial":
                    diferenciales += 1
            print(
                "estadísticas automatizador de copias de seguridad"
            )
            print(
                "copias registradas:",
                len(ids)
            )
            print(
                "copias completadas:",
                completadas
            )
            print(
                "copias programadas:",
                programadas
            )
            print(
                "copias pendientes:",
                pendientes
            )
            print("tipos de copia")
            print("completas:", completas)
            print("incrementales:", incrementales)
            print("diferenciales:", diferenciales)
            print(
                "ejecuciones realizadas:",
                len(historial_ids)
            )
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "8":
        print(
            "gracias por utilizar el automatizador de copias de seguridad."
        )
        break
    else:
        print("opción no válida.")