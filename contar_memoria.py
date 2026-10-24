#!/usr/bin/env python3
"""
Entrenador Mental - Ejercicios de Memorización de Alta Intensidad
Basado en las técnicas de Ramón Campayo

Este script incluye ejercicios diseñados para mejorar la memoria
y las capacidades cognitivas mediante técnicas de memorización avanzadas.
"""

import random
import time
import os
import json
from datetime import datetime
import sys

class EntrenadorMental:
    def __init__(self):
        self.puntuacion_total = 0
        self.nivel = 1
        self.ejercicios_completados = 0
        self.record_personal = 0
        self.cargar_progreso()
        
        # Palabras para ejercicios de memorización
        self.palabras = [
            "elefante", "montaña", "computadora", "mariposa", "universidad",
            "teatro", "biblioteca", "restaurante", "hospital", "aeropuerto",
            "playa", "bosque", "ciudad", "pueblo", "carretera",
            "puente", "río", "lago", "océano", "desierto",
            "volcán", "cascada", "cueva", "isla", "península",
            "continente", "país", "provincia", "región", "territorio"
        ]
        
        # Imágenes para ejercicios visuales
        self.imagenes = [
            "casa roja", "coche azul", "árbol verde", "flor amarilla", "libro marrón",
            "mesa blanca", "silla negra", "ventana grande", "puerta pequeña", "escalera",
            "lámpara moderna", "cuadro antiguo", "reloj digital", "teléfono móvil", "televisión",
            "radio", "guitarra", "piano", "trompeta", "violín",
            "pincel", "lienzo", "escultura", "fotografía", "dibujo"
        ]

    def limpiar_pantalla(self):
        """Limpia la pantalla del terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def mostrar_titulo(self):
        """Muestra el título del programa"""
        print("=" * 60)
        print("ENTRENADOR MENTAL - RAMÓN CAMPAYO")
        print("=" * 60)
        print("Ejercicios de Memorización de Alta Intensidad")
        print("=" * 60)

    def mostrar_tecnicas_campayo(self):
        """Muestra información sobre las técnicas de Ramón Campayo"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\nTÉCNICAS DE RAMÓN CAMPAYO")
        print("=" * 60)
        print("MÉTODO DE ASOCIACIONES INVEROSÍMILES")
        print("-" * 40)
        print("• Crea imágenes vívidas y exageradas")
        print("• Usa asociaciones inverosímiles")
        print("• Combina elementos de forma absurda")
        print("• Añade movimiento y acción")
        print("• Incluye emociones intensas")
        print()
        print("TÉCNICA PARA NÚMEROS:")
        print("-" * 30)
        print("• Asocia cada número con una imagen")
        print("• Crea historias con los números")
        print("• Usa el método de grupos de 4")
        print("• Practica la retentiva diariamente")
        print()
        print("CONSEJOS PRÁCTICOS:")
        print("-" * 25)
        print("• Concentración total durante 15-20 minutos")
        print("• Descanso de 5 minutos entre sesiones")
        print("• Repaso mental antes de dormir")
        print("• Competición contigo mismo")
        print()
        print("OBJETIVO: Memorizar 100 números en 5 minutos")
        print("PROGRESIÓN: De 10 a 20, 30, 50, 100 números")
        
        input("\nPresiona Enter para continuar...")

    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        print("\nMENÚ PRINCIPAL")
        print("1. Ejercicio de Números (Básico)")
        print("2. Ejercicio de Números (Avanzado)")
        print("3. Ejercicio de Palabras")
        print("4. Ejercicio de Secuencias")
        print("5. Ejercicio de Imágenes")
        print("6. Ver Estadísticas")
        print("7. Ver Record Personal")
        print("8. Técnicas de Ramón Campayo")
        print("9. Salir")
        print("-" * 60)

    def mostrar_estadisticas(self):
        """Muestra las estadísticas del usuario"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\nESTADÍSTICAS")
        print(f"Puntuación Total: {self.puntuacion_total}")
        print(f"Nivel Actual: {self.nivel}")
        print(f"Ejercicios Completados: {self.ejercicios_completados}")
        print(f"Record Personal: {self.record_personal}")
        
        if self.ejercicios_completados > 0:
            promedio = self.puntuacion_total / self.ejercicios_completados
            print(f"Promedio por Ejercicio: {promedio:.2f}")
        
        input("\nPresiona Enter para continuar...")

    def ejercicio_numeros(self):
        """Ejercicio de memorización de números - Técnicas de Ramón Campayo"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\nEJERCICIO DE NÚMEROS - RAMÓN CAMPAYO")
        print("Técnicas de memorización avanzada")
        print("Memoriza el número completo en 1 segundo")
        print("-" * 60)
        
        # Dificultad gradual según el nivel
        if self.nivel <= 2:
            # Nivel 1-2: 6 dígitos
            longitud = 6
            tipo_ejercicio = "NÚMERO CORTO"
        elif self.nivel <= 4:
            # Nivel 3-4: 8 dígitos
            longitud = 8
            tipo_ejercicio = "NÚMERO MEDIO"
        elif self.nivel <= 6:
            # Nivel 5-6: 10 dígitos
            longitud = 10
            tipo_ejercicio = "NÚMERO LARGO"
        elif self.nivel <= 8:
            # Nivel 7-8: 12 dígitos
            longitud = 12
            tipo_ejercicio = "NÚMERO MUY LARGO"
        else:
            # Nivel 9-10: 15 dígitos
            longitud = 15
            tipo_ejercicio = "NÚMERO EXTREMO"
        
        numeros = [random.randint(0, 9) for _ in range(longitud)]
        numero_completo = ''.join(map(str, numeros))
        
        print(f"{tipo_ejercicio} - {longitud} DÍGITOS")
        print(f"Nivel actual: {self.nivel}")
        print("CONSEJO: Crea asociaciones visuales rápidas")
        print("=" * 60)
        print()
        print("PREPARA TU MENTE...")
        print("El número aparecerá en:")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(0.5)
        
        print()
        print("¡MEMORIZA AHORA!")
        print("=" * 60)
        print(f"{numero_completo}")
        print("=" * 60)
        
        # Solo 1 segundo para memorizar
        time.sleep(1)
        
        # Limpiar pantalla inmediatamente
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\nEJERCICIO DE NÚMEROS - RAMÓN CAMPAYO")
        print("¡TIEMPO COMPLETADO!")
        print("=" * 60)
        print()
        print("ESCRIBE EL NÚMERO COMPLETO:")
        print("-" * 60)
        
        # Obtener respuesta del usuario
        respuesta = input("Número: ").strip()
        
        # Verificar respuesta
        numeros_usuario = [int(d) for d in respuesta if d.isdigit()]
        correctos = sum(1 for i, num in enumerate(numeros) if i < len(numeros_usuario) and numeros_usuario[i] == num)
        
        # Calcular puntuación con bonificación por dificultad
        porcentaje_correcto = correctos / len(numeros)
        puntuacion_base = int(porcentaje_correcto * 100)
        
        # Bonificación por números largos
        if longitud >= 12 and porcentaje_correcto >= 0.8:
            puntuacion_base += 25
        elif longitud >= 10 and porcentaje_correcto >= 0.85:
            puntuacion_base += 15
        elif longitud >= 8 and porcentaje_correcto >= 0.9:
            puntuacion_base += 10
        
        puntuacion = min(100, puntuacion_base)
        self.puntuacion_total += puntuacion
        self.ejercicios_completados += 1
        
        print(f"\nRESULTADOS:")
        print(f"Dígitos correctos: {correctos}/{len(numeros)}")
        print(f"Porcentaje de acierto: {porcentaje_correcto:.1%}")
        print(f"Puntuación: {puntuacion}/100")
        print(f"Número correcto: {numero_completo}")
        print(f"Tu respuesta: {respuesta}")
        
        # Feedback específico según el rendimiento
        if puntuacion >= 95:
            print("PERFECTO! Memoria excepcional")
            if self.nivel < 10:
                self.nivel += 1
                print(f"Subiste al nivel {self.nivel}!")
        elif puntuacion >= 80:
            print("EXCELENTE! Las técnicas están funcionando")
            if self.nivel < 10:
                self.nivel += 1
                print(f"Subiste al nivel {self.nivel}!")
        elif puntuacion >= 60:
            print("Buen trabajo, sigue practicando")
        else:
            print("No te rindas. Practica más la velocidad")
        
        # Consejos específicos de Ramón Campayo
        print(f"\nCONSEJO DE RAMÓN CAMPAYO:")
        if puntuacion < 50:
            print("   - Practica con números más cortos primero")
            print("   - Usa asociaciones visuales rápidas")
            print("   - Concentra toda tu atención en el número")
        elif puntuacion < 80:
            print("   - Mejora la velocidad de asociación")
            print("   - Practica la retentiva a corto plazo")
            print("   - Usa el método de grupos mentales")
        else:
            print("   - ¡Excelente! Ahora practica con números más largos")
            print("   - Entrena la memoria fotográfica")
            print("   - Compite contigo mismo para mejorar")
        
        self.guardar_progreso()
        input("\nPresiona Enter para continuar...")

    def ejercicio_numeros_avanzado(self):
        """Ejercicio avanzado de memorización de números con técnicas específicas"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print(f"\nEJERCICIO AVANZADO DE NÚMEROS")
        print("Técnicas de Ramón Campayo: Velocidad Extrema")
        print("MODO CONTINUO - Solo se puede salir terminando el programa")
        print("-" * 60)
        
        # Dificultad extrema según el nivel
        if self.nivel <= 3:
            longitud = 8
        elif self.nivel <= 6:
            longitud = 10
        else:
            longitud = 12
        
        print(f"VELOCIDAD EXTREMA - {longitud} DÍGITOS")
        print(f"Nuevo número cada 2 segundos")
        print(f"Nivel: {self.nivel}")
        print("=" * 60)
        print()
        print("PREPARA TU MENTE...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(0.3)
        
        print()
        print("VELOCIDAD MÁXIMA - MODO CONTINUO")
        print("=" * 60)
        
        # Variables para el modo continuo
        numeros_memorizados = []
        respuestas_usuario = []
        puntuacion_total = 0
        ronda = 1
        
        try:
            while True:
                # Generar nuevo número
                numeros = [random.randint(0, 9) for _ in range(longitud)]
                numero_completo = ''.join(map(str, numeros))
                numeros_memorizados.append(numero_completo)
                
                print(f"\nRONDA {ronda}")
                print("=" * 60)
                print(f"{numero_completo}")
                print("=" * 60)
                
                # Esperar 1 segundo para memorizar
                time.sleep(1)
                
                # Limpiar pantalla
                self.limpiar_pantalla()
                self.mostrar_titulo()
                print("\nEJERCICIO AVANZADO DE NÚMEROS")
                print("MODO CONTINUO - Solo se puede salir terminando el programa")
                print("-" * 60)
                print(f"VELOCIDAD EXTREMA - {longitud} DÍGITOS")
                print(f"1 segundo para memorizar, 2 segundos para pasar")
                print(f"Nivel: {self.nivel}")
                print("=" * 60)
                print()
                print("VELOCIDAD MÁXIMA - MODO CONTINUO")
                print("=" * 60)
                
                print(f"ESCRIBE EL NÚMERO DE LA RONDA {ronda}:")
                print("-" * 60)
                
                # Obtener respuesta
                respuesta = input("Número: ").strip()
                respuestas_usuario.append(respuesta)
                
                # Verificar respuesta
                numeros_usuario = [int(d) for d in respuesta if d.isdigit()]
                correctos = sum(1 for i, num in enumerate(numeros) if i < len(numeros_usuario) and numeros_usuario[i] == num)
                
                puntuacion_ronda = int((correctos / len(numeros)) * 100)
                puntuacion_total += puntuacion_ronda
                
                print(f"\nRESULTADOS RONDA {ronda}:")
                print(f"Correctos: {correctos}/{len(numeros)}")
                print(f"Puntuación ronda: {puntuacion_ronda}/100")
                print(f"Número correcto: {numero_completo}")
                print(f"Tu respuesta: {respuesta}")
                print(f"Puntuación total: {puntuacion_total}")
                
                if puntuacion_ronda >= 90:
                    print("VELOCIDAD EXTREMA! Tu memoria es increíble")
                elif puntuacion_ronda >= 70:
                    print("MUY BUENO! La velocidad está mejorando")
                else:
                    print("Sigue practicando la velocidad de memorización")
                
                print("\nPreparando siguiente número en 2 segundos...")
                time.sleep(2)
                
                ronda += 1
                
        except KeyboardInterrupt:
            print("\n\nEJERCICIO INTERRUMPIDO")
            print("=" * 60)
            print(f"RESUMEN FINAL:")
            print(f"Rondas completadas: {ronda - 1}")
            print(f"Puntuación total: {puntuacion_total}")
            if ronda > 1:
                promedio = puntuacion_total / (ronda - 1)
                print(f"Promedio por ronda: {promedio:.1f}/100")
            
            # Mostrar todos los números y respuestas
            print(f"\nHISTORIAL COMPLETO:")
            print("-" * 60)
            for i in range(len(numeros_memorizados)):
                print(f"Ronda {i+1}:")
                print(f"   Número: {numeros_memorizados[i]}")
                if i < len(respuestas_usuario):
                    print(f"   Tu respuesta: {respuestas_usuario[i]}")
                print()
        
        # Actualizar estadísticas
        self.puntuacion_total += puntuacion_total
        self.ejercicios_completados += 1
        
        # Subir nivel si el rendimiento fue bueno
        if ronda > 1:
            promedio = puntuacion_total / (ronda - 1)
            if promedio >= 80 and self.nivel < 10:
                self.nivel += 1
                print(f"Subiste al nivel {self.nivel}!")
        
        self.guardar_progreso()
        input("\nPresiona Enter para continuar...")

    def ejercicio_palabras(self):
        """Ejercicio de memorización de palabras"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\nEJERCICIO DE PALABRAS")
        print("Memoriza las palabras que aparecerán")
        print("Tendrás 5 segundos para memorizar cada palabra")
        print("-" * 60)
        
        # Seleccionar palabras según el nivel
        num_palabras = min(3 + self.nivel, 8)  # Máximo 8 palabras
        palabras_ejercicio = random.sample(self.palabras, num_palabras)
        
        print(f"Memoriza estas {num_palabras} palabras:")
        print("=" * 40)
        
        # Mostrar palabras una por una
        for i, palabra in enumerate(palabras_ejercicio, 1):
            print(f"Palabra {i}: {palabra.upper()}")
            time.sleep(5)  # 5 segundos para memorizar
            self.limpiar_pantalla()
            self.mostrar_titulo()
            print("\nEJERCICIO DE PALABRAS")
            print("Memoriza las palabras que aparecerán")
            print("Tendrás 5 segundos para memorizar cada palabra")
            print("-" * 60)
            print(f"Memoriza estas {num_palabras} palabras:")
            print("=" * 40)
        
        print("¡Tiempo de memorización completado!")
        print("Ahora escribe las palabras en orden:")
        print("-" * 40)
        
        # Obtener respuestas del usuario
        palabras_usuario = []
        for i in range(num_palabras):
            respuesta = input(f"Palabra {i+1}: ").strip().lower()
            palabras_usuario.append(respuesta)
        
        # Verificar respuestas
        correctas = sum(1 for i, palabra in enumerate(palabras_ejercicio) 
                       if i < len(palabras_usuario) and palabras_usuario[i] == palabra)
        
        puntuacion = int((correctas / len(palabras_ejercicio)) * 100)
        self.puntuacion_total += puntuacion
        self.ejercicios_completados += 1
        
        print(f"\nResultado: {correctas}/{len(palabras_ejercicio)} palabras correctas")
        print(f"Puntuación: {puntuacion}/100")
        print(f"Palabras correctas: {', '.join(palabras_ejercicio)}")
        
        if puntuacion >= 80:
            print("Excelente! Tu memoria está mejorando")
            if self.nivel < 10:
                self.nivel += 1
                print(f"Subiste al nivel {self.nivel}!")
        elif puntuacion >= 60:
            print("Buen trabajo, sigue practicando")
        else:
            print("No te rindas, la práctica hace al maestro")
        
        self.guardar_progreso()
        input("\nPresiona Enter para continuar...")

    def ejercicio_secuencias(self):
        """Ejercicio de secuencias lógicas"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\nEJERCICIO DE SECUENCIAS")
        print("Completa la secuencia lógica")
        print("Tienes 30 segundos para resolver cada secuencia")
        print("-" * 60)
        
        # Generar secuencia según el nivel
        if self.nivel <= 3:
            # Secuencia simple: números pares
            inicio = random.randint(2, 20)
            secuencia = [inicio + i*2 for i in range(5)]
            respuesta_correcta = secuencia[-1] + 2
            tipo = "números pares"
        elif self.nivel <= 6:
            # Secuencia: multiplicar por 2
            inicio = random.randint(1, 10)
            secuencia = [inicio]
            for i in range(4):
                secuencia.append(secuencia[-1] * 2)
            respuesta_correcta = secuencia[-1] * 2
            tipo = "multiplicar por 2"
        else:
            # Secuencia: Fibonacci
            secuencia = [1, 1, 2, 3, 5]
            respuesta_correcta = 8
            tipo = "Fibonacci"
        
        print(f"Tipo de secuencia: {tipo}")
        print(f"Secuencia: {secuencia}")
        print("¿Cuál es el siguiente número?")
        print("-" * 40)
        
        # Dar tiempo para resolver
        tiempo_inicio = time.time()
        respuesta = input("Tu respuesta: ").strip()
        tiempo_total = time.time() - tiempo_inicio
        
        # Verificar respuesta
        try:
            respuesta_num = int(respuesta)
            if respuesta_num == respuesta_correcta:
                puntuacion = max(50, 100 - int(tiempo_total * 2))  # Menos puntos si tarda mucho
                print(f"\n¡Correcto! El siguiente número es {respuesta_correcta}")
                print(f"Tiempo: {tiempo_total:.1f} segundos")
                print(f"Puntuación: {puntuacion}/100")
            else:
                puntuacion = 0
                print(f"\nIncorrecto. La respuesta correcta era {respuesta_correcta}")
                print(f"Puntuación: 0/100")
        except ValueError:
            puntuacion = 0
            print(f"\nRespuesta inválida. La respuesta correcta era {respuesta_correcta}")
            print(f"Puntuación: 0/100")
        
        self.puntuacion_total += puntuacion
        self.ejercicios_completados += 1
        
        if puntuacion >= 80:
            print("Excelente! Tu lógica está mejorando")
            if self.nivel < 10:
                self.nivel += 1
                print(f"Subiste al nivel {self.nivel}!")
        elif puntuacion >= 50:
            print("Buen trabajo, sigue practicando")
        else:
            print("No te rindas, la práctica hace al maestro")
        
        self.guardar_progreso()
        input("\nPresiona Enter para continuar...")

    def ejercicio_imagenes(self):
        """Ejercicio de memorización de imágenes"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\nEJERCICIO DE IMÁGENES")
        print("Memoriza las imágenes que aparecerán")
        print("Tendrás 4 segundos para memorizar cada imagen")
        print("-" * 60)
        
        # Seleccionar imágenes según el nivel
        num_imagenes = min(3 + self.nivel, 6)  # Máximo 6 imágenes
        imagenes_ejercicio = random.sample(self.imagenes, num_imagenes)
        
        print(f"Memoriza estas {num_imagenes} imágenes:")
        print("=" * 40)
        
        # Mostrar imágenes una por una
        for i, imagen in enumerate(imagenes_ejercicio, 1):
            print(f"Imagen {i}: {imagen.upper()}")
            time.sleep(4)  # 4 segundos para memorizar
            self.limpiar_pantalla()
            self.mostrar_titulo()
            print("\nEJERCICIO DE IMÁGENES")
            print("Memoriza las imágenes que aparecerán")
            print("Tendrás 4 segundos para memorizar cada imagen")
            print("-" * 60)
            print(f"Memoriza estas {num_imagenes} imágenes:")
            print("=" * 40)
        
        print("¡Tiempo de memorización completado!")
        print("Ahora escribe las imágenes en orden:")
        print("-" * 40)
        
        # Obtener respuestas del usuario
        imagenes_usuario = []
        for i in range(num_imagenes):
            respuesta = input(f"Imagen {i+1}: ").strip().lower()
            imagenes_usuario.append(respuesta)
        
        # Verificar respuestas (más flexible para imágenes)
        correctas = 0
        for i, imagen in enumerate(imagenes_ejercicio):
            if i < len(imagenes_usuario):
                # Verificar si la respuesta contiene palabras clave de la imagen
                palabras_clave = imagen.split()
                respuesta_usuario = imagenes_usuario[i]
                if any(palabra in respuesta_usuario for palabra in palabras_clave):
                    correctas += 1
        
        puntuacion = int((correctas / len(imagenes_ejercicio)) * 100)
        self.puntuacion_total += puntuacion
        self.ejercicios_completados += 1
        
        print(f"\nResultado: {correctas}/{len(imagenes_ejercicio)} imágenes correctas")
        print(f"Puntuación: {puntuacion}/100")
        print(f"Imágenes correctas: {', '.join(imagenes_ejercicio)}")
        
        if puntuacion >= 80:
            print("Excelente! Tu memoria visual está mejorando")
            if self.nivel < 10:
                self.nivel += 1
                print(f"Subiste al nivel {self.nivel}!")
        elif puntuacion >= 60:
            print("Buen trabajo, sigue practicando")
        else:
            print("No te rindas, la práctica hace al maestro")
        
        self.guardar_progreso()
        input("\nPresiona Enter para continuar...")

    def cargar_progreso(self):
        """Carga el progreso guardado"""
        try:
            with open('progreso_mental.json', 'r') as f:
                datos = json.load(f)
                self.puntuacion_total = datos.get('puntuacion_total', 0)
                self.nivel = datos.get('nivel', 1)
                self.ejercicios_completados = datos.get('ejercicios_completados', 0)
                self.record_personal = datos.get('record_personal', 0)
        except FileNotFoundError:
            pass

    def guardar_progreso(self):
        """Guarda el progreso actual"""
        datos = {
            'puntuacion_total': self.puntuacion_total,
            'nivel': self.nivel,
            'ejercicios_completados': self.ejercicios_completados,
            'record_personal': max(self.record_personal, self.puntuacion_total),
            'ultima_actualizacion': datetime.now().isoformat()
        }
        
        with open('progreso_mental.json', 'w') as f:
            json.dump(datos, f, indent=2)

    def mostrar_record(self):
        """Muestra el record personal"""
        self.limpiar_pantalla()
        self.mostrar_titulo()
        print("\nRECORD PERSONAL")
        print(f"Puntuación más alta: {self.record_personal}")
        print(f"Puntuación actual: {self.puntuacion_total}")
        
        if self.puntuacion_total > self.record_personal:
            print("NUEVO RECORD! Felicidades!")
            self.record_personal = self.puntuacion_total
            self.guardar_progreso()
        
        input("\nPresiona Enter para continuar...")

    def ejecutar(self):
        """Ejecuta el programa principal"""
        while True:
            self.limpiar_pantalla()
            self.mostrar_titulo()
            self.mostrar_menu_principal()
            
            try:
                opcion = input("Selecciona una opción (1-9): ").strip()
                
                if opcion == '1':
                    self.ejercicio_numeros()
                elif opcion == '2':
                    self.ejercicio_numeros_avanzado()
                elif opcion == '3':
                    self.ejercicio_palabras()
                elif opcion == '4':
                    self.ejercicio_secuencias()
                elif opcion == '5':
                    self.ejercicio_imagenes()
                elif opcion == '6':
                    self.mostrar_estadisticas()
                elif opcion == '7':
                    self.mostrar_record()
                elif opcion == '8':
                    self.mostrar_tecnicas_campayo()
                elif opcion == '9':
                    print("\n¡Gracias por entrenar tu mente!")
                    print("Recuerda: la práctica constante es la clave del éxito.")
                    break
                else:
                    print("Opción inválida. Por favor, selecciona 1-9.")
                    time.sleep(2)
                    
            except KeyboardInterrupt:
                print("\n\n¡Hasta luego! Sigue entrenando tu mente.")
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2)

def main():
    """Función principal"""
    entrenador = EntrenadorMental()
    entrenador.ejecutar()

if __name__ == "__main__":
    main()