import requests
from fhir.resources.condition import Condition
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference

BASE_URL = "https://hapi.fhir.org/baseR4"

def crear_recurso_condition(patient_id, codigo_snomed, descripcion, fecha_registro, estado, verificacion, asserter):
    condition = Condition(
        subject=Reference(reference=f"Patient/{patient_id}"),
        code=CodeableConcept(
            coding=[Coding(
                system="http://snomed.info/sct",
                code=codigo_snomed,
                display=descripcion
            )],
            text=descripcion
        ),
        clinicalStatus=CodeableConcept(
            coding=[Coding(
                system="http://terminology.hl7.org/CodeSystem/condition-clinical",
                code=estado,
                display=estado.capitalize()
            )]
        ),
        verificationStatus=CodeableConcept(
            coding=[Coding(
                system="http://terminology.hl7.org/CodeSystem/condition-ver-status",
                code=verificacion,
                display=verificacion.capitalize()
            )]
        ),
        recordedDate=fecha_registro, 
        asserter=Reference(reference=asserter)
    )


    payload = condition.json(indent=2)
    response = requests.post(
        f"{BASE_URL}/Condition",
        headers={"Content-Type": "application/fhir+json"},
        data=payload
    )

    print("\n>>> Resultado del servidor:")
    print("Código HTTP:", response.status_code)
    print(response.json())
    return response.json()


# ---------------- USO ------------------

diagnostico = crear_recurso_condition(
    patient_id="52960648",
    codigo_snomed="59621000",
    descripcion="Hipertensión arterial esencial",
    fecha_registro="2025-11-18",
    estado ="Activo",
    verificacion="Confirmado",
    asserter="Practitioner/example"
)
