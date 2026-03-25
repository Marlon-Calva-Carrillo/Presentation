      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. PRACTICA.
       AUTHOR. MARLON-CALVA.
       DATE-WRITTEN. 2026-15-03.

       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
      *Variables de primer menu (Datos cuenta)
       01 WS-MENU-LOGIN     PIC X(2).
       01 WS-MENU-OPC       PIC X(2).

      *Variables usuario y contraseña
       01 WS-USUARIO    PIC X(3).
       01 WS-PASSWORD   PIC X(4).

      *Variables del segundo menu (Funciones del programa)
       01 WS-OPCION   PIC 9 VALUE 0.
       01 WS-SALIR    PIC X VALUE 'N'.

      *Variables datos personales
       01 WS-DATOS-PERSONALES.
          05 WS-NOMBRE        PIC X(20).
          05 WS-APELLIDOPAT   PIC X(15).
          05 WS-APELLIDOMAT   PIC X(15).
       01 WS-FECHA-NACIMIENTO PIC 9(8).


       PROCEDURE DIVISION.

           DISPLAY "======================"
           DISPLAY "        TRINITY"
           DISPLAY "======================"
           DISPLAY "Bienvenido a Trinity, Tienes cuenta? (Si/No)"
           ACCEPT WS-MENU-LOGIN.
           IF WS-MENU-LOGIN = "Si" OR WS-MENU-LOGIN = "SI"
               DISPLAY "Ingresa usuario: "
               ACCEPT WS-USUARIO
               DISPLAY "Ingresa contrasena: "
               ACCEPT WS-PASSWORD
               IF WS-USUARIO = "Mar" AND WS-PASSWORD = "Mar5"
                   DISPLAY "======================"
                   DISPLAY "        TRINITY"
                   DISPLAY "======================"
                   DISPLAY "Bienvenido a Trinity, selecciona una opcion".
                   DISPLAY "1. Crear cuenta."
                   DISPLAY "2. Consultar datos de cuenta."
                   DISPLAY "3. Editar datos de cuenta."
                   DISPLAY "4. Iniciar deposito."
                   DISPLAY "5. Realizar transaccion."
                   DISPLAY "6. Eliminar cuenta."
                   DISPLAY "7. Salir."
                   ACCEPT WS-OPCION
                   IF WS-OPCION < 1 OR WS-OPCION > 7
                       DISPLAY "Ingresa una opcion valida"
                   ELSE
                       EVALUATE WS-OPCION
                           WHEN 1
                               DISPLAY "Seleccionaste crear cuenta."
                               DISPLAY "Ingresa los siguientes datos."
                               DISPLAY "Nombre."
                               DISPLAY "Apellido paterno."
                               DISPLAY "Apellido materno."
                               DISPLAY "Fecha de nacimiento (dd/mm/aa)."
                               DISPLAY "CURP."
                               DISPLAY "Direccion."
                               DISPLAY "Correo."
                               DISPLAY "Saldo."
                               DISPLAY "Usuario."
                               DISPLAY "Password."
                               DISPLAY "Final."
                           WHEN 2
                               DISPLAY "Seleccionaste consultar datos."
                           WHEN 3
                               DISPLAY "Seleccionaste editar datos."
                           WHEN 4
                               DISPLAY "Seleccionaste deposito."
                           WHEN 5
                               DISPLAY "Seleccionaste transaccion."
                           WHEN 6
                               DISPLAY "Eliminar cuenta."
                           WHEN 7
                               DISPLAY "Hasta luego"
                               MOVE 'S' TO WS-SALIR
                       END-EVALUATE
                   END-IF
                ELSE
                    DISPLAY "No es posible ingresar, hasta luego"
                END-IF
           ELSE
               DISPLAY "Lo siento, debes tener cuenta para acceder."
           END-IF.
       END PROGRAM PRACTICA.
|
