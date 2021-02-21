import os
from django.contrib.gis.utils import LayerMapping
from .models import District


district_mapping = {
    'dist_id': 'DIST_ID',
    'district': 'DISTRICT',
    'zone_name': 'ZONE_NAME',
    'region': 'REGION',
    'diss': 'DISS',
    'xc': 'Xc',
    'yc': 'Yc',
    'geom': 'MULTIPOLYGON',
}

district_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/NP_75DWGS84.shp'))

def run(verbose = True):
    lm = LayerMapping(District, district_shp, district_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
