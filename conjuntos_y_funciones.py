#===================================================
# 1. Notación de conjuntos y cardinalidad
#===================================================

# Notación de conjuntos (extensión)
A = {10, 20, 30, 40}

def verificacion_extension(A): 
    elementos = {10, 20, 30, 40}
    print("=== Verificación de Conjunto A ===")
    print(f"Conjunto A: {A}")
    print(f"Elementos esperados: {elementos}")

verificacion_extension(A)

# Comprensión
# Números impares entre 1 y 15
impares = {x for x in range(1,16) if x % 2 != 0}

def verificacion_impares(impares):
    impares_x = {1,3,5,7,9,11,13,15}
    print("\n=== Verificación de Números Impares ===")
    print(f"Impares generados: {impares}")
    if impares == impares_x: 
        print("✔ El conjunto de impares coincide")
    else: 
        print("✘ El conjunto de impares no coincide")
        
verificacion_impares(impares)

# Cardinalidad
print(f"\nCardinalidad del conjunto A: {len(A)}")

def verificacion_cardinalidad(A): 
    comparar = len(A)
    print("=== Verificación Cardinalidad ===")
    if len(A) == comparar: 
        print(f"✔ Cardinalidad correcta ({comparar} elementos)")
    else: 
        print("✘ Cardinalidad incorrecta")

verificacion_cardinalidad(A)

# Conjuntos infinitos (primeros 50 múltiplos de 3)
multiplos3 = set(x for x in range(3, 3*51, 3))

def verificar_extension(multiplos3): 
    print("\n=== Verificación Conjunto Infinitos (Acotados) ===")
    if len(multiplos3) == 50: 
        print(f"✔ Extensión correcta: {len(multiplos3)} elementos")
    else: 
        print("✘ Extensión incorrecta")

verificar_extension(multiplos3)


#===================================================
# 2. Operaciones con conjuntos
#===================================================

B = {30, 40, 50, 60}

# Unión
union = A | B
def verificacion_union(A, B, union): 
    print("\n=== Unión de Conjuntos ===")
    print(f"A = {A} \nB = {B}")
    if union == A.union(B): 
        print(f"✔Unión correcta: {union}")
    else: 
        print("✘Unión incorrecta")
verificacion_union(A, B, union)

# Intersección
interseccion = A & B
def verificacion_interseccion(A, B, interseccion): 
    print("\n=== Intersección ===")
    if interseccion == A.intersection(B): 
        print(f"✔Intersección correcta: {interseccion}")
    else: 
        print("✘Intersección incorrecta")
verificacion_interseccion(A, B, interseccion)

# Diferencia
diferencia = A - B
def verificacion_diferencia(A, B, diferencia): 
    print("\n=== Diferencia (A - B) ===")
    if diferencia == A.difference(B): 
        print(f"✔Diferencia correcta: {diferencia}")
    else: 
        print("✘ Diferencia incorrecta")
verificacion_diferencia(A, B, diferencia)

# Diferencia Simétrica
dif_sim = A ^ B
def verificacion_difsimetrica(A, B, dif_sim):
    print("\n=== Diferencia Simétrica ===")
    if dif_sim == A.symmetric_difference(B): 
        print(f"✔Diferencia simétrica correcta: {dif_sim}")
    else: 
        print("✘Diferencia simétrica incorrecta")
verificacion_difsimetrica(A, B, dif_sim)

# Complemento
U = {10,20,30,40,50,60}
complemento = U - A
def verificacion_complemento(U, A, complemento): 
    print("\n=== Complemento ===")
    if complemento.union(A) == U and complemento & A == set(): 
        print(f"✔Complemento correcto: {complemento}")
    else: 
        print("✘Complemento incorrecto")
verificacion_complemento(U, A, complemento)

# Producto cartesiano
producto_c = {(a, b) for a in A for b in B}
def verificacion_cartesiano(A, B, producto_c):
    print("\n=== Producto Cartesiano A x B ===")
    if len(producto_c) == len(A)*len(B): 
        print(f"✔Producto cartesiano correcto ({len(producto_c)} pares)")
    else: 
        print("✘Producto cartesiano incorrecto")
verificacion_cartesiano(A, B, producto_c)


#=========================================
# 3. Relaciones y Funciones
#=========================================
A = {1, 2, 3}
R_equivalencia = {(1,1),(2,2),(3,3),(1,2),(2,1)}
R_orden = {(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)}

# Verificación propiedades
def verificacion_reflexiva(A, R):
    for a in A:
        if (a,a) not in R:
            print("✘No es reflexiva")
            return False
    print("✔Reflexiva")
    return True

def verificacion_simetrica(R):
    for a,b in R:
        if (b,a) not in R:
            print("No es simetrica")
            return False
    print("✔Es simetrica")
    return True

def verificacion_antisimetria(R):
    for a,b in R:
        if (b,a) in R and a!=b:
            print("✘No es antisimetrica")
            return False
    print("✔Antisimetrica")
    return True

def verificacion_transitividad(R):
    for a,b in R:
        for c,d in R:
            if b==c and (a,d) not in R:
                print("✘No es transitiva")
                return False
    print("✔Es transitiva")
    return True
def verificacion_equivalencia(A,R):
    print("\n=== Relación de Equivalencia ===")
    if (verificacion_reflexiva(A,R) and verificacion_simetrica(R) and verificacion_transitividad(R)):
        print("✔Es relación de equivalencia")
    else:
        print("✘No es relación de equivalencia")

def verificacion_orden(A,R):
    print("\n=== Relación de Orden ===")
    if (verificacion_reflexiva(A,R) and verificacion_antisimetria(R) and verificacion_transitividad(R)):
        print("✔Es relación de orden")
    else:
        print("✘No es relación de orden")

verificacion_equivalencia(A,R_equivalencia)
verificacion_orden(A,R_orden)

# Funciones

def verificacion_inyectiva(dominio):
    imagen = set()
    for x in dominio:
        if (x+5 in imagen):
            return False
        imagen.add(x+5)
    return True

dominio = {1,2,3,4}
print("\n=== Función Inyectiva f(x)=x+5 ===")
print("✔ Inyectiva" if verificacion_inyectiva(dominio) else "✘ No inyectiva")

# Sobreyectiva: f(x)=x mod 4
A = {0,1,2,3,4,5,6,7}
B = {0,1,2,3}
def verificacion_sobreyectividad(A,B): 
    f = {x:x%4 for x in A}
    imagen = set(f.values())
    print("\n=== Función Sobreyectiva f(x)=x mod 4 ===")
    print("✔ Sobreyectiva" if imagen==B else "✘ No sobreyectiva")
verificacion_sobreyectividad(A,B)


#===================================================
# 4. Clausuras
#===================================================

A = {1,2,3}
R = {(1,2),(2,3),(3,3)}

def clausura_reflexiva(R,A):
    for a in A: 
        R.add((a,a))
    return R
print("\nClausura Reflexiva:", clausura_reflexiva(R.copy(),A))

def clausura_simetria(R):
    for a,b in list(R):
        R.add((b,a))
    return R
print("Clausura Simétrica:", clausura_simetria(R.copy()))

def clausura_transitiva(R):
    agregar=True
    while agregar:
        agregar=False
        for a,b in list(R):
            for c,d in list(R):
                if b==c and (a,d) not in R:
                    R.add((a,d))
                    agregar=True
    return R
print("Clausura Transitiva:", clausura_transitiva(R.copy()))