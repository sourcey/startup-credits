import json
import os

def test_polar_startup_program():
    catalog_path = '.github/sourcey-root-set.json'
    assert os.path.exists(catalog_path), 'Catalog file not found'
    with open(catalog_path, 'r') as f:
        data = json.load(f)
    
    vendors = data if isinstance(data, list) else data.get('vendors', data.get('items', []))
    polar = next((v for v in vendors if v.get('id') == 'polar' or v.get('name', '').lower() == 'polar'), None)
    
    assert polar is not None, 'Polar vendor record is missing from the catalog'
    assert 'polar.sh/startup-program' in str(polar), 'Polar startup program URL or reference missing'
