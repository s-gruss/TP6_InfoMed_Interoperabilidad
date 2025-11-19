from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, buscar_paciente_por_dni

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    #family_name = "Juan"
    #given_name = "Perez"
    #birth_date = "1999-01-01"
    #gender = "male"
    #phone = None
    #ni = 38394200 

    # Crear y enviar el recurso de paciente
    #patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, dni)
    #patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    #if patient_id:
    #    get_resource_from_hapi_fhir(patient_id,'Patient')
    
    SYSTEM_DNI = "https://www.argentina.gob.ar/interior/renaper"
    DNI = "38394200"
    buscar_paciente_por_dni(DNI, SYSTEM_DNI)