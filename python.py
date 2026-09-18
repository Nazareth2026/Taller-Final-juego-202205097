# ==============================================================================
# PROYECTO DE PROGRAMACIÓN: LAS ESTRELLAS
# Estructura POO + Bucle While + Lógica de Diagrama de Flujo (8 Planetas)
# ==============================================================================

import time

# ------------------------------------------------------------------------------
# 1. PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# ------------------------------------------------------------------------------

# Clase Padre (Personaje)
class Personaje:
    def __init__(self, nombre, avatar="Traje Estelar Clásico"):
        self.nombre = nombre
        self.avatar = avatar

    def presentarse(self):
        print(f"👤 Nombre del Héroe: {self.nombre}")
        print(f"👕 Avatar / Vestimenta: {self.avatar}")


# Clase Hija (Heroe)
class Heroe(Personaje):
    def __init__(self, nombre, avatar="Traje Estelar Clásico", herramienta="Varita Estelar Básica", vidas=3):
        # Hereda del padre usando super().__init__()
        super().__init__(nombre, avatar)
        self.herramienta = herramienta
        self.vidas = vidas
        self.punteo = 0

    def usar_herramienta(self):
        print(f"\n✨ ¡Has equipado y usado tu [{self.herramienta}]!")
        print("💥 ¡Impacto directo! El enemigo ha sido derrotado con facilidad.")

    def recibir_dano(self):
        self.vidas -= 1
        print(f"💔 ¡Has recibido daño! Te quedan {self.vidas} vida(s).")


# ------------------------------------------------------------------------------
# 2. FUNCIONES DE BIENVENIDA Y CONFIGURACIÓN INICIAL
# ------------------------------------------------------------------------------

def mostrar_pantalla_bienvenida():
    print("=" * 65)
    print("           🌟 BIENVENIDO AL VIDEOJUEGO: LAS ESTRELLAS 🌟          ")
    print("=" * 65)
    print("Misión: Viajar por los 8 planetas del sistema, derrotar a los")
    print("enemigos de cada mundo y rescatar a la Princesa en la batalla final.\n")

    # Condicional de primer inicio
    while True:
        respuesta = input("¿Es la primera vez que juegas? (si/no): ").strip().lower()
        if respuesta in ["si", "s"]:
            print("\n---------------------------------------------------------")
            print("📜 [PERMISOS DE PRIVACIDAD]")
            print("Para continuar, debes aceptar los términos y condiciones.")
            input("Presiona ENTER para aceptar los Permisos de Privacidad...")
            
            print("\n👨‍👩‍👧 [VINCULAR CUENTA DE PADRES]")
            correo_padre = input("Ingresa el correo del tutor o padre para enviar avances: ")
            print(f"✅ ¡Cuenta ({correo_padre}) vinculada correctamente!")
            print("---------------------------------------------------------\n")
            break
        elif respuesta in ["no", "n"]:
            print("\n¡Bienvenido de vuelta, explorador estelar!\n")
            break
        else:
            print("⚠️ Opción no válida. Responde con 'si' o 'no'.")


def crear_personaje():
    print("=== CREACIÓN Y PERSONALIZACIÓN INICIAL DEL HÉROE ===")
    nombre = input("Ingresa el nombre de tu personaje: ").strip()
    if not nombre:
        nombre = "Guardián Estelar"
    
    print("\nElige tu traje inicial:")
    print("1. Traje Espacial Dorado")
    print("2. Túnica Cósmica")
    print("3. Armadura Neón")
    
    opc_traje = input("Selecciona una opción (1-3): ").strip()
    if opc_traje == "1":
        traje = "Traje Espacial Dorado"
    elif opc_traje == "2":
        traje = "Túnica Cósmica"
    else:
        traje = "Armadura Neón"

    jugador = Heroe(nombre=nombre, avatar=traje)
    print(f"\n🎉 ¡Personaje {jugador.nombre} creado con éxito!")
    return jugador


# ------------------------------------------------------------------------------
# 3. LÓGICA PRINCIPAL Y CICLO DE JUEGO (WHILE)
# ------------------------------------------------------------------------------

def iniciar_juego():
    # Paso 1: Bienvenida y Registro
    mostrar_pantalla_bienvenida()
    
    # Paso 2: Crear el Héroe
    jugador = crear_personaje()

    # Datos de los 8 planetas / niveles del juego
    planetas = [
        "Planeta 1: Mercurio (Rocas Ardientes)",
        "Planeta 2: Venus (Nubes Densas)",
        "Planeta 3: Tierra (Base de Control)",
        "Planeta 4: Marte (Dunas Rojas)",
        "Planeta 5: Júpiter (Tormenta Gigante)",
        "Planeta 6: Saturno (Anillos Brillantes)",
        "Planeta 7: Urano (Mundo Helado)",
        "Planeta 8: Neptuno (ENFRENTAMIENTO FINAL)"
    ]

    # Premios / Herramientas especiales por cada nivel
    premios_herramientas = [
        "Escudo Térmico de Mercurio",
        "Visor Nebular de Venus",
        "Propulsor Gravitacional",
        "Lanza de Plasma de Marte",
        "Rayo Eléctrico de Júpiter",
        "Bumerán de Anillos de Saturno",
        "Escáner Crio-Helado de Urano",
        "Corona de las Estrellas"
    ]

    juego_ejecutandose = True

    # BUCLE DEL MENÚ PRINCIPAL (Estructura While)
    while juego_ejecutandose:
        print("\n" + "=" * 50)
        print("                MENÚ PRINCIPAL                ")
        print("=" * 50)
        print("1. 🎮 [EMPEZAR JUEGO]")
        print("2. 👗 [Cambiar Avatar (Ropa y Herramientas)]")
        print("3. 📊 [Ver Avance y Estado del Héroe]")
        print("4. 🚪 [Salir del Juego]")
        print("=" * 50)

        opcion_menu = input("Selecciona una opción (1-4): ").strip()

        if opcion_menu == "1":
            print("\n🚀 Cargar Mundo 1... ¡Iniciando el viaje estelar!")
            nivel_actual = 0

            # BUCLE DE LOS 8 PLANETAS (Estructura While)
            while nivel_actual < len(planetas) and jugador.vidas > 0:
                print("\n" + "🌌" * 25)
                print(f"  📍 NIVEL EN CURSO: {planetas[nivel_actual]}")
                print("🌌" * 25)
                time.sleep(1)

                print("\n▶️ [Iniciar Nivel Activo]")
                print("Explorando el terreno del planeta...")

                # Evento de Encuentro con Enemigo
                print("\n⚠️ ¡ALERTA! Un enemigo alienígena ha bloqueado tu camino.")
                
                # Toma de decisión: Usar Herramienta
                usar_herram = input("¿Deseas usar tu herramienta para combatir? (si/no): ").strip().lower()

                if usar_herram in ["si", "s"]:
                    jugador.usar_herramienta()
                    print("👍 ¡Enemigo derrotado sin recibir ningún daño!")
                else:
                    print("\n🏃 Decidiste intentar [Saltar / Esquivar] al enemigo...")
                    logro_esquivar = input("¿Lograste esquivar a tiempo? (si/no): ").strip().lower()

                    if logro_esquivar in ["si", "s"]:
                        print("⚡ ¡Reflejos impresionantes! Esquivaste al enemigo con éxito.")
                    else:
                        print("💥 ¡El enemigo te golpeó!")
                        jugador.recibir_dano()

                # ¿Jugador pierde vida? Check de Game Over
                if jugador.vidas <= 0:
                    print("\n" + "💀" * 20)
                    print("     GAME OVER - ¡Te has quedado sin vidas!")
                    print("" + "💀" * 20)
                    print("Volviendo al Menú Principal...")
                    jugador.vidas = 3  # Reiniciar vidas para próximos intentos
                    break

                # Nivel Completado
                print("\n🎯 ¡Llegaste a la Meta! Nivel Completado con éxito.")
                
                # Entrega de Premio Especial
                herramienta_ganada = premios_herramientas[nivel_actual]
                jugador.herramienta = herramienta_ganada
                jugador.punteo += 100
                
                print(f"🎁 ¡Otorgar Premio Especial! Nueva Herramienta obtenida: [{herramienta_ganada}]")
                print("📡 (Actualizar avance de los padres automáticamente...)")

                # Evaluación de último mundo / último nivel
                if nivel_actual == len(planetas) - 1:
                    print("\n" + "👑" * 25)
                    print(" 🔥 ¡ENFRENTAMIENTO FINAL COMPLETADO! 🔥")
                    print(" 👸 ¡HAS RESCATADO A LA PRINCESA CON ÉXITO!")
                    print("" + "👑" * 25)
                    print(f"\n✨ PUNTAJE FINAL: {jugador.punteo} Puntos.")
                    print("🎬 [FIN: Créditos del Juego - Gracias por jugar Las estrellas]")
                    input("\nPresiona ENTER para regresar al Menú Principal...")
                else:
                    print("➡️ Avanzar al Siguiente Mundo...")
                    time.sleep(1)

                nivel_actual += 1

        elif opcion_menu == "2":
            print("\n--- CAMBIAR AVATAR Y EQUIPAMIENTO ---")
            nuevo_avatar = input("Ingresa la nueva ropa/estilo para tu personaje: ").strip()
            if nuevo_avatar:
                jugador.avatar = nuevo_avatar
                print(f"✅ ¡Ropa actualizada! Tu avatar ahora viste: {jugador.avatar}")

            nueva_herramienta = input("Ingresa una herramienta personalizada: ").strip()
            if nueva_herramienta:
                jugador.herramienta = nueva_herramienta
                print(f"✅ ¡Herramienta equipada!: {jugador.herramienta}")

        elif opcion_menu == "3":
            print("\n" + "📊" * 20)
            print("   ESTADO ACTUAL DEL HÉROE")
            print("📊" * 20)
            jugador.presentarse()
            print(f"🛠️ Herramienta Equipada: {jugador.herramienta}")
            print(f"❤️ Vidas Restantes: {jugador.vidas}")
            print(f"⭐ Punteo Acumulado: {jugador.punteo} pts")
            print("📊" * 20)
            input("\nPresiona ENTER para volver...")

        elif opcion_menu == "4":
            print("\n👋 Guardando partida y cerrando sesión... ¡Nos vemos en la galaxia!")
            juego_ejecutandose = False

        else:
            print("\n❌ Selección inválida. Por favor ingresa un número entre 1 y 4.")


# ------------------------------------------------------------------------------
# 4. EJECUCIÓN DEL PROGRAMA
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    iniciar_juego()