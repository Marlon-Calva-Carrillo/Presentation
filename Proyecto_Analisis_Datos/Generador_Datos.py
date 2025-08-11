#GENERACION DE DATOS PERSONALES ALEATORIOS.
#El siguiente proyecto tiene como finalidad generar un archivo CSV con datos personales aleatorios.
#Es recomendable usarlo para pruebas de aplicaciones que requieran datos de usuarios, como bases de datos o sistemas de registro.
#Importo librerias necesarias.
from faker import Faker
from random import *
import csv

#Inicio Faker con localizacion mexicana
faker = Faker('es_MX')

#CODIGOS DE LOS ESTADOS DE LA REPUBLICA
#Creo un diccionario con los estados de la rep. Mexicana y sus codigos.
estados = {
    'Aguascalientes' : 'AG',
    'Baja California' : 'BC',
    'Baja California Sur' : 'BS',
    'Campeche' : 'CM',
    'Chiapas' : 'CS',
    'Chihuahua' : 'CH',
    'Ciudad de Mexico' : 'CX',
    'Coahuila' : 'CO',
    'Colima' : 'CL',
    'Durango' : 'DG',
    'Guanajuato' : 'GT',
    'Guerrero' : 'GR',
    'Hidalgo' : 'HG',
    'Jalisco' : 'JA',
    'Mexico' : 'EM',
    'Michoacan' : 'MI',
    'Morelos' : 'MO',
    'Nayarit' : 'NA',
    'Nuevo Leon' : 'NL',
    'Oaxaca' : 'OA',
    'Puebla' : 'PU',
    'Queretaro' : 'QT',
    'Quintana Roo' : 'QR',
    'San Luis Potosi' : 'SL',
    'Sinaloa' : 'SL',
    'Sonora' : 'SR',
    'Tabasco' : 'TB',
    'Tamaulipas' : 'TM',
    'Tlaxcala' : 'TL',
    'Veracruz': 'VE',
    'Yucatan': 'YU',
    'Zacatecas': 'ZA',
}

#Debido a que "Faker" no diferencia nombres masculinos y femeninos debemos especificarlos nosotros mismos.
#(Datos obtenidos de una pagina web)
nombres_femeninos = ['ABIGAIL', 'ABRIL', 'ADRIANA', 'ALEJANDRA', 'ALEXA', 'ALEXANDRA', 'ALICIA', 'ALMA', 'AMANDA', 'AMERICA',
'ANA', 'ANDREA', 'ANGELA', 'ANGELICA', 'ANITA', 'ANTONIA', 'ARACELI', 'ARIADNA', 'AURORA', 'AZUCENA',
'BEATRIZ', 'BELEN', 'BERENICE', 'BERTHA', 'BIANCA', 'BRENDA', 'BRIANA', 'CAMILA', 'CARLA', 'CARMEN',
'CAROLINA', 'CECILIA', 'CELESTE', 'CINTHIA', 'CLARA', 'CLAUDIA', 'CONCEPCION', 'CONNIE', 'CRISTINA', 'DAFNE',
'DAISY', 'DANIELA', 'DANNA', 'DEBORA', 'DELIA', 'DIANA', 'DULCE', 'EDITH', 'ELENA', 'ELISA',
'ELIZABETH', 'ELSA', 'EMILIA', 'EMILY', 'EMMA', 'ERIKA', 'ESMERALDA', 'ESTEFANIA', 'ESTELA', 'ESTRELLA',
'EUGENIA', 'EVELYN', 'FABIOLA', 'FATIMA', 'FERNANDA', 'FLOR', 'FRANCISCA', 'GABRIELA', 'GENOVEVA', 'GLORIA',
'GRACIELA', 'GUADALUPE', 'HELENA', 'ILIANA', 'INES', 'IRENE', 'IRMA', 'ISABEL', 'ISABELLA', 'ITZEL',
'JACQUELINE', 'JAZMÍN', 'JENNIFER', 'JESSICA', 'JIMENA', 'JOHANNA', 'JOSEFINA', 'JUANA', 'JULIA', 'JULIANA',
'JULIETA', 'KAREN', 'KARINA', 'KARLA', 'LAURA', 'LETICIA', 'LIDIA', 'LILIANA', 'LOURDES', 'LUCIA',]

nombres_masculinos = ['ADAN', 'ADOLFO', 'ADRIAN', 'AGUSTIN', 'ALDO', 'ALEJANDRO', 'ALFONSO', 'ALFREDO', 'ALONSO', 'ANDRES',
'ANGEL', 'ANTONIO', 'ARMANDO', 'ARTURO', 'AXEL', 'BALTASAR', 'BENJAMIN', 'BERNARDO', 'BRANDON', 'BRUNO',
'CAMILO', 'CARLOS', 'CESAR', 'CRISTIAN', 'CRISTOBAL', 'DAMIAN', 'DANIEL', 'DARIO', 'DAVID', 'DIEGO',
'DYLAN', 'EDGAR', 'EDUARDO', 'ELIAS', 'EMILIANO', 'EMILIO', 'ENRIQUE', 'ERICK', 'ERNESTO', 'ESTEBAN',
'EUGENIO', 'EUSTAQUIO', 'FACUNDO', 'FELIPE', 'FERNANDO', 'FIDEL', 'FRANCISCO', 'GABRIEL', 'GAEL', 'GASPAR',
'GERARDO', 'GERMAN', 'GILBERTO', 'GONZALO', 'GUILLERMO', 'GUSTAVO', 'HECTOR', 'HERNAN', 'HUGO', 'IGNACIO',
'ISAAC', 'ISMAEL', 'IVAN', 'JACOBO', 'JAIME', 'JAIR', 'JAVIER', 'JESUS', 'JOEL', 'JORGE',
'JOSE', 'JOSUE', 'JUAN', 'JULIAN', 'JULIO', 'KEVIN', 'LAZARO', 'LEANDRO', 'LEONARDO', 'LORENZO',
'LUIS', 'MANUEL', 'MARCO', 'MARCOS', 'MARIO', 'MARTIN', 'MATEO', 'MATIAS', 'MAXIMILIANO', 'MIGUEL',
'NESTOR', 'NICOLAS', 'NOE', 'OCTAVIO', 'OSCAR', 'PABLO', 'PEDRO', 'RAFAEL', 'RAMIRO', 'RAUL',]

apellidos = ['GARCIA', 'HERNANDEZ', 'MARTINEZ', 'LOPEZ', 'GONZALEZ', 'RODRIGUEZ', 'PEREZ', 'SANCHEZ', 'RAMIREZ', 'CRUZ',
'FLORES', 'GOMEZ', 'MORALES', 'VAZQUEZ', 'JIMENEZ', 'REYES', 'TORRES', 'DIAZ', 'GUTIERREZ', 'RUIZ',
'MENDOZA', 'AGUILAR', 'CASTILLO', 'ORTIZ', 'MORENO', 'RAMOS', 'CHAVEZ', 'ROMERO', 'ALVAREZ', 'MENDEZ',
'VILLARREAL', 'SILVA', 'SALAZAR', 'DELGADO', 'ROJAS', 'CORTES', 'GUZMAN', 'NAVARRO', 'MEJIA', 'SOSA',
'VALDEZ', 'CARRILLO', 'VELAZQUEZ', 'ROBLES', 'ARANDA', 'PACHECO', 'BUSTOS', 'CERVANTES', 'AVILA', 'CAMACHO',
'ESCAMILLA', 'LEON', 'VILLALOBOS', 'IBARRA', 'TOVAR', 'ZAVALA', 'MIRANDA', 'BARRERA', 'LOZANO', 'ROSAS',
'ACOSTA', 'GALVAN', 'SALGADO', 'FARIAS', 'BENITEZ', 'OLIVARES', 'MONTOYA', 'SOLIS', 'LUNA', 'ZUNIGA',
'BAUTISTA', 'RANGEL', 'FRANCO', 'VALENCIA', 'TREVINO', 'LARA', 'AREVALO', 'CUEVAS', 'ESCOBAR', 'NUNEZ',
'VILLALPANDO', 'QUIROZ', 'SAAVEDRA', 'MEDINA', 'MOLINA', 'LOAIZA', 'DE LA CRUZ', 'DE LA TORRE', 'MACIAS', 'BARAJAS',
'OBREGON', 'TORO', 'CISNEROS', 'ALVARADO', 'ESQUIVEL', 'BRAVO', 'MALDONADO', 'RIOS', 'PALACIOS', 'PENA']


#IMPORTANTE: Para generar el curp.
#Inicial y primer vocal interna del primer apellido (paterno); Inicial del segundo apellido, inicial del nombre.
#Fecha de nacimiento (Año, mes, dia).
#Sexo (H ó M).
#Entidad federativa.
#Primeras consonantes internas del primer apellido, del segundo apellido y del nombre.
#Homoclave y digito verificador (En este caso seran aleatorios ya que los asigna RENAPO).


#FUNCION PARA GENERAR CURP.
def generar_curp(nombre, apellido_pat, apellido_mat, fecha_nacimiento, genero, estado):
    inicial_ap_pat = apellido_pat[0].upper() #Primera letra del apellido paterno y en mayuscula.
    vocal_ap_pat = next((c.upper() for c in apellido_pat[1:] if c.upper() in 'AEIOU'), 'X')  #Primera vocal del apellido paterno
    inicial_ap_materno = apellido_mat[0].upper() #Primera letra del apellido materno y en mayuscula.
    inicial_nombre = nombre[0].upper()  #Primera letra del nombre y en mayuscula.
    fecha_nacimiento = fecha_nacimiento #Formato de fecha (año, mes y dia).
    genero = genero.upper()  #Genero en mayuscula (H/M).
    estado = estado.upper()  #Estado en mayuscula.
    consonante_ap_pat = next((c.upper() for c in apellido_pat[1:] if c.upper() not in 'AEIOU' and c.isalpha()), 'X')  #Primera consonante del apellido paterno
    consonante_ap_materno = next((c.upper() for c in apellido_mat[1:] if c.upper() not in 'AEIOU' and c.isalpha()), 'X')  #Primera consonante del apellido materno
    consonante_nombre = next((c.upper() for c in nombre[1:] if c.upper() not in 'AEIOU' and c.isalpha()), 'X')  #Primera consonante del nombre
    digitos_diferenciadores = f"{randint(0, 99):02d}"  #Dos dígitos aleatorios.
    curp = (
        f"{inicial_ap_pat}{vocal_ap_pat}{inicial_ap_materno}{inicial_nombre}" #Muestro iniciales.
        f"{fecha_nacimiento}{genero}{estado}" #Muestro fecha de nacimiento, genero y estado.
        f"{consonante_ap_pat}{consonante_ap_materno}{consonante_nombre}{digitos_diferenciadores}" #Muestro consonantes y numeros aleatorios.
    )
    return curp

#CREAR REGISTROS ALEATORIOS.
registros = [] #Creo una lista vacia para despues agregar los registros.
for r in range (15000): #Puedes cambiar el numero de registros que se generaran.
    listas_nombres = choice([nombres_masculinos, nombres_femeninos]) #Creo una lista combinando ambas listas de nombres.
    nombre = choice(listas_nombres) #A nombre se le da un valor aleatorio de la lista combinada.
    apellido_pat = choice(apellidos) #Selecciona un apellido al azar.
    apellido_mat = choice(apellidos) #Selecciona un apellido al azar.
    fecha_nacimiento = faker.date_of_birth(minimum_age=18, maximum_age=80).strftime('%y/%m/%d') #Genera fecha de nacimiento aleatoria entre 18 y 80 años.
    sexo = 'H' if nombre in nombres_masculinos else 'M' #Selecciona un genero dependiendo el nombre (lista de hombres o mujeres).
    estado = choice(list(estados.values())) #Selecciona un estado al azar.
    curp = generar_curp(nombre,apellido_pat, apellido_mat, fecha_nacimiento, sexo, estado) #Linea agregada para generar el curp.

    registros.append([nombre, apellido_pat, apellido_mat, fecha_nacimiento, sexo, estado, curp])  # Agrego el curp a los registros


#Codigo para mostrar en consola los registros generados.
for registro_nuevo in registros:
    print (registro_nuevo)

#ALMACENAR ARCHIVO CSV
#Guardar en CSV (Lo genero en este formato para despues representarlo en otras plataformas).
with open('Ejemplo.csv', mode='w', newline='', encoding='utf-8') as archivo: #Abro el archivo en modo escritura.
    writer = csv.writer(archivo) #Creo un objeto writer para escribir en el archivo CSV.
    writer.writerow(['Nombre', 'Apellido_Paterno', 'Apellido Materno', 'Fecha de nacimiento', 'Sexo', 'Estado', 'Curp']) #Creo los encabeados.
    writer.writerows(registros) #Escribo los registros generados en el archivo CSV.

#Condicion para verificar si los registros se generaron correctamente.
if not registros:
    print ("No se han generado los registros.")
else:
    print ("Se generaron los registros correctamente, tu archivo esta listo para consultas.")

