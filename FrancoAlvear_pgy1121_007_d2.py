import funciones as fn


while True:
    fn.menu()
    opc = fn.opc
    if opc == 1:
        fn.comprar_entradas()
    elif opc == 2:
        fn.ver_ubicaciones()
    elif opc == 3:
        fn.validacion_asistentes
    elif opc == 4:
        fn.ganancias_totales()
    else:
        fn.salir()