# reinforcement-learning
 
## Setup

```py
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Training
```py
PYTHONPATH=.:$PYTHONPATH python src/train_logistics.py
tensorboard --logdir ./data/tb # in another terminal
```

## Good Results

Result for 3x2x2:
```
./data/model/1706238544-satisfactoriness-tussle  # -28
./data/model/1706242653-jackfish-glecoma # -33
./data/model/1706282014-ogdoads-parabranchiat # -29
```

Result for 4x4x4:
```
1706462314-regive-prodromatic/A2C_1  # 23
```

Result
```
1706754719-oaks-filicin/A2C_1  # 24
1706729266-revisionist-unallegorical/A2C_1  # 25
```
