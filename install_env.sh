
if [$PYTHON_VERSION == "3.9"]; then
  conda create --name dev_autotuning python==3.9 
  conda activate dev_autotuning
else
  conda create --name dev_autotuning_py311 python==3.11 
  conda activate dev_autotuning_py311
fi
  pip install triton
  pip install -U --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/Triton-Nightly/pypi/simple/ triton-nightly
python -m pip install absl-py
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install tqdm