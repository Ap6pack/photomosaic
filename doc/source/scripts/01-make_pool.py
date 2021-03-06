import os
import photomosaic as pm


POOL_DIR = '/tmp/photomosaic-docs-pool/'
pm.rainbow_of_squares(POOL_DIR)
pool = pm.make_pool(os.path.join(POOL_DIR, '*.png'))
pm.export_pool(pool, os.path.join(POOL_DIR, 'pool.json'))
