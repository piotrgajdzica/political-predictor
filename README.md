# Political predictor

## Installation

```bash
pip install git+https://github.com/piotrgajdzica/political-predictor
```
## Requirements

* [Flair 0.4.4](https://github.com/flairNLP/flair)


## Sample usage

```python
from political_predictor.predictor import PoliticalViewsTagger
print(PoliticalViewsTagger().predict(['I agree with Trump about immigrants issue']))
```