
import re
from colorama import init, Fore, Back, Style
init()

agenda = {}
regex_nombre = r'^[a-zA-Z][a-zA-Z0-9\s\W]*$'
regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
# regex_telefono =  re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
regex_telefono =  re.compile(r"(\+\d{1,5})?")


#?  **************************** Función para Validar Nombre *******************************************

def validar_nombre(nombre):
    
    if len(nombre) < 2 or len(nombre) >= 50:
        return False
    else:
        if re.match(regex_nombre, nombre):
            return True
        else:
            return False
    

#?  **************************** Función para Validar Email **************************************************

def validar_email(email):
    if re.fullmatch(regex_email, email):
        return True
    else:
        return False
        
#?  **************************** Función para Validar Telefono **************************************************

def validar_telf(telefono):
    if re.search(regex_telefono, telefono):
        return True
    else:
        return False

#? 1. **************************** Función para Agregar un Contacto nuevo *******************************************
def agregar_contacto(agenda):
    nombre = input('Por favor introduzca el nombre del contacto: ')
    nombre = nombre.upper()
    nombre_validado = validar_nombre(nombre)
    if nombre_validado:
        telefono = input('Por favor introduzca el teléfono del contacto: ')
        telef_validado = validar_telf(telefono)
        if telef_validado:
            email = input('Por favor introduzca el email del contacto: ')
            email = email.lower()
            email_validado = validar_email(email)
            if email_validado:
                agenda[nombre] = {'telefono': telefono, 'email': email}
                print(f'¡Se ha agregado el contacto: {nombre} exitosamente!')           
            else:
                print('El email ingresado es inválido')
        else:
            print('El número de telefono ingresado es inválido')
    else:
        print('El nombre ingresado es inválido')        


#? 2. **************************** Función para Modificar Contacto Existente **** *******************************************



#? 3. **************************** Función para  Buscar Contacto ************************************************************



#? 4. **************************** Función Lista de Contactos ***************************************************************



#? 5. **************************** Función para Eliminar un Contacto ********************************************************
def eliminar_contacto(agenda):
    nombre = input('Ingrese el nombre del contacto que desee Eliminar: ')
    if nombre in agenda:
        del agenda[nombre]
        print(f'El contacto: {nombre} ha sido eliminado correctamente')
    else:
        print('El contacto: {nombre} no existe...')




#? **************************** Función Menú de la Agenda ********************************************************************
def mostrar_menu_agenda():
    print(Fore.LIGHTYELLOW_EX + '\nAgenda de Contactos\n')
    print('1. Agregar Nuevo Contacto')
    print('2. Modificar Contacto Existente')
    print('3. Buscar Contacto')
    print('4. Lista de Contactos')
    print('5. Eliminar Contacto')
    print('6. Salir' + Style.RESET_ALL)



#? **************************** Función Switch Case de la agenda ************************************************
def switch_case_agenda(opcion):
    match(opcion):
        case 1:
            print(Fore.LIGHTYELLOW_EX + '\nAGREGAR CONTACTO')
            agregar_contacto(agenda)
        case 2:
            print(Fore.LIGHTYELLOW_EX + '\nMODIFICAR CONTACTO')
            # modificar_contacto()
            # pass
        case 3:
            print(Fore.LIGHTYELLOW_EX + '\nBUCAR CONTACTO')
            # buscar_contacto()
            # pass
        case 4:
            print(Fore.LIGHTYELLOW_EX + '\nLISTA DE CONTACTOS')
            # lista_contactos()
            # pass    
        case 5:
            print(Fore.LIGHTYELLOW_EX + '\nELIMINAR CONTACTO')
            # eliminar_contacto()
            # pass
        case 6:
            print(agenda)
            print(Fore.LIGHTYELLOW_EX + '\nSaliendo del sistema...')
        case _:
            print(Fore.LIGHTRED_EX + '\nIntroduzca un valor válido...' + Style.RESET_ALL)


#? **************************** Función Principalde la agenda ************************************************

def main_agenda_contactos():
    opc = 1000
    while opc != 6:
        mostrar_menu_agenda()
        try:
            opc = int(input('\nElija una Opción (1-6): '))
            switch_case_agenda(opc)      
        except ValueError:
            print(Fore.LIGHTRED_EX + '\nOpción Incorecta')


if __name__ == "__main__":
    main_agenda_contactos()
   

