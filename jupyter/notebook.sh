[ -f .python-version ] || pyenv local 3.6.9
[ -d venv ] || python -m venv venv
if ! `./venv/bin/pip freeze | grep -q jupyter`; then
    echo "!!"
    ./venv/bin/pip install jupyter
fi
./venv/bin/jupyter notebook
