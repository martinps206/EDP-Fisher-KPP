import yaml

def load_parameters(path='data/parameters.yaml'):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)

    # Asegurar conversiones de tipo explícitas
    model = config['model']
    space = config['space_time']

    return {
        'D': float(model['D']),
        'r': float(model['r']),
        'K': float(model['K']),
    }, {
        'L': float(space['L']),
        'T': float(space['T']),
        'Nx': int(space['Nx']),
        'Nt': int(space['Nt']),
    }