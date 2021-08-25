#!/bin/sh -e


PACKAGE=$(basename `pwd`)

autoflake --recursive ${PACKAGE}
yapf -irp .
python setup.py sdist bdist_wheel --universal
twine upload dist/*
#${PREFIX}mkdocs gh-deploy --force

bash scripts/clean.sh