# Script Generador de UML desde un Esquema OpenAPI

## Descripción
Este script en Python, toma un archivo **OpenAPI** en formato **YAML** y genera un representación de clases en UML. La representación generada muestra las diferentes propiedades de los diferentes esquemas, relaciones entre estos(anidados) y los campos que son obligatorios.

## Requisitos Previos
1)	Tener Python instalado (versión 3.1 o superior)

## Instalación
1) Clonar el repositorio o descargar los archivos en la maquina local
 
```
git clone  https://github.com/Daniel7R/Yaml2UmlConverter.git
cd Yaml2UmlConverter
```
2)	Instalar las dependencias necesarias, estas se encuentran el el archivo req.txt, se instalan de la siguiente manera:
```
pip install -r req.txt
```
## Uso
1)	Coloca el contenido de tu archivo YAML con especificación OpenAPI en el archivo **openapi.yaml**
2)	Ejecuta el script:
```
python main.py
```

## Ejemplo de ejecución
Suponiendo que el archivo openapi.yaml tiene el siguiente contenido:  
```
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        friends:
          type: array
          items:
            $ref: '#/components/schemas/User'
      required:
        - id
        - name
```
La salida esperada del script sería la siguiente:
```
@startuml
class User {
    +string id *
    +string name *
    +List<User> friends
}
User --> User
@enduml
```
## visualización
Para la visualización se copia el texto UML de la consola que comienza con ***@startuml*** y finaliza con ***@enduml***.
Abre el visor online de PlantUML con el siguiente enlace: [PlantUML Web Server](https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa700001). Después de abrir el visor, se reemplaza el texto UML y para mejores efectos visuales se selecciona formato SVG y, por último, se presiona el botón de generación (o presionar Ctrl + Enter).
  
## Resultados Esperados
El diagrama generado mostrara las clases con:
•	Propiedades y tipos
•	Indicador de obligatoriedad (*)
•	Relaciones entre schemas mediante listas o referencias($ref)

## Recomendaciones
•	Usar nombres descriptivos y consistentes en los esquemas para facilitar la comprensión del UML
•	Verificar que las referencias ($ref) estén bien configuradas en el YAML


Historial de Versiones
|Versión|	Rol|	Responsable	|Observaciones|	Fecha|
|-------|------|----------------|-------------|------|
|1.0.0	|Desarrollador Integración|	Carlos Daniel Rivera Rangel|Versión Inicial|	27-03-2025|

