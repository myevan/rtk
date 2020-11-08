base=`cd $(dirname $0); pwd`
pushd $base
[ -f .python-version ] || pyenv local 3.6.9
[ -d venv ] || python -m venv venv
if ! `./venv/bin/pip freeze | grep -q jupyter`; then
    ./venv/bin/pip install jupyter
fi
popd
$base/venv/bin/jupyter notebook
