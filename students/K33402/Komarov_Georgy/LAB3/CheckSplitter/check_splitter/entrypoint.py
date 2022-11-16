import os
import subprocess

import django

django.setup()

from django.conf import settings
from django.core.management import call_command

print(f'Current path is: {os.path.abspath(".")}')

print('\nDjango settings:')
for attr in ['BASE_DIR', 'ALLOWED_HOSTS', ]:
    print('\t', attr, getattr(settings, attr, 'FAIL!'))

print('Collecting static files...')
call_command('collectstatic', interactive=False)

print('Compiling messages...')
call_command('compilemessages')

print('Applying migrations...')
call_command('migrate', interactive=False)

# Fixing permissions
subprocess.check_output(f'chown -R www-data:www-data {getattr(settings, "DATA_DIR")}', shell=True)

print('\n\nSetup completed!\n\n')
