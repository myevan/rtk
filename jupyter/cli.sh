base=`cd $(dirname $0); pwd`
pushd $base
./venv/bin/python cli.py $*
popd
