SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
pip install -r "${SCRIPT_DIR}/requirements.txt"
python "${SCRIPT_DIR}/{{cookiecutter.name}}.py" --config "${SCRIPT_DIR}/{{cookiecutter.name}}_config.yaml"
