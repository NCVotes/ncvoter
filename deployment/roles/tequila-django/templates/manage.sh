# Shell script to run a management command
cd {{ source_dir }}
{{ venv_dir }}/bin/python {{ source_dir }}/{{ project_name }}/manage.py $@
