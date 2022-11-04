# python-script
Opinionated template of a stand-alone python script

Saves neurons and time by providing a template to write python scripts that have
input paths, configurations and outputs and that should be run as CLI.

# Usage
```bash
pip install cookiecutter
# navigate to the folder where you want to create the script
cookiecutter gh:fcossio/python-script
# enter the name and short description
bash <name>/run.sh
```

The logs are automatically configured to be saved in the <name>/output folder.
