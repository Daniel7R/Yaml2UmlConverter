import yaml

def generate_uml_class(schema_name, schema) -> str:
    """
    Generates the UML class representation for a provided schema.
    @
    """
    uml = f'class {schema_name} {{\n'
    properties = schema.get('properties', {})
    required_properties = schema.get('required', [])

    relationships = []
    
    for prop, prop_details in properties.items():
        prop_type = prop_details.get('type', 'string')  # Default is string
        # Handle $ref if use nested schemas
        if '$ref' in prop_details:
            ref_schema = prop_details['$ref'].split('/')[-1]  # Extract reference schema's name
            prop_type = ref_schema  # Property type to the referenced schema name
            relationships.append(f'{schema_name} --> {ref_schema}') 
        # Handle array types
        elif prop_type == 'array':
            items = prop_details.get('items', {})
            if '$ref' in items:
                ref_schema = items['$ref'].split('/')[-1]
                prop_type = f'List<{ref_schema}>'
                relationships.append(f'{schema_name} --> {ref_schema}') 
            elif 'type' in items:
                prop_type = f'List<{items["type"]}>'
            else:
                prop_type = 'List<string>'  # Default to List of strings if the type isn't defined
        
        required_indicator = " *" if prop in required_properties else "" 
        uml += f'    +{prop_type} {prop}{required_indicator}\n'
    
    uml += '}\n'
    for relation in relationships:
        uml += relation + '\n'

    return uml

def generate_uml(openapi_spec) -> str:
    """
    Generates a commplete UML diagram for an OpenAPI spec.
    """
    uml_classes = ""
    schemas = openapi_spec.get('components', {}).get('schemas', {})
    for schema_name, schema in schemas.items():
        uml_classes += generate_uml_class(schema_name, schema)
    
    return "@startuml\n" + uml_classes + "@enduml"

# Load OpenAPI spec from a YAML file
file_name="openapi.yaml"
try:
    with open(file_name, 'r') as file:
        openapi_spec = yaml.safe_load(file)
        if openapi_spec is None:
            raise Exception("File or content is not valid ")
except FileNotFoundError:
    print(f"Error: {file_name}")
    exit()
except ValueError as e:
    print(f"Error: {e}")
    exit()
except Exception as ex:
    print(f"Error: {ex}")
    exit()
uml_output = generate_uml(openapi_spec)
print(uml_output)