# vibe-profiling
using GCC -finstrument-functions option to do performance profile various of C/C++ programs

This project enables function-level profiling using GCC's -finstrument-functions.
It provides detailed insights into execution flow, helping developers analyze performance, debug,
and optimize large-scale models like LLaMA for NLP tasks.

Currenly our profiling covers llama.cpp and pytorch

## Start

git clone https://github.com/ucas-linux/vibe-profiling.git

cd vibe-profiling

git submodule update --init --recursive

## profile llama.cpp

### build llama.cpp
sudo apt-get install elfutils libdw-dev


./build-binary.sh

### profiling llama.cpp
extern/llama.cpp/buildinstrument/bin/llama-cli -t 1 -m  ggml-org_gemma-3-1b-it-GGUF_gemma-3-1b-it-Q4_K_M.gguf

In other terminal

kill -sSIGUSR1 pid of llama-cli

## profiling pytorch

### install dependent software
```
sudo apt-get update
sudo apt-get install -y \
  git cmake ninja-build build-essential \
  python3 python3-dev python3-venv python3-pip \
  libopenblas-dev libomp-dev
```

cd extern/pytorch

git submodule update --init --recursive

python3 -m venv ~/venvs/torch-src

source ~/venvs/torch-src/bin/activate

pip install -r requirements.txt



### build pytorch

```
export CMAKE_BUILD_TYPE=Debug
export CMAKE_GENERATOR=Ninja
export USE_CUDA=0
export USE_ROCM=0
export USE_CUFILE=0
export USE_NCCL=0
export USE_DISTRIBUTED=0
export CMAKE_CXX_FLAGS=-finstrument-functions
export BUILT_TEST=0
```

python -m pip install --no-build-isolation -v -e .


### profiling pytorch
g++ -shared -fPIC src/profilepytorch.cpp -g3 -o src/profilepytorch.so -ldl -ldw -lelf

LD_PRELOAD=./src/profilepytorch.so python src/grad.py





