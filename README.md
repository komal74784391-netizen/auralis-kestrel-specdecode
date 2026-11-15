# Kestrel

Official implementation of **Kestrel: Speculative Decoding under Strict Memory Budgets**.

## Installation

```bash
pip install -r requirements.txt
```

## Repository structure

```
src/model.py
src/scheduler.py
src/verifier.py
configs/default.yaml
train.py
eval.py
requirements.txt
```

## Training

Run `python train.py --config configs/default.yaml` to reproduce the main results.
Checkpoints and logs are written to `runs/`.

## Evaluation

Run `python eval.py --checkpoint runs/latest` to reproduce the benchmark tables.

## Citation

```bibtex
@inproceedings{misc,
  title = {Kestrel: Speculative Decoding under Strict Memory Budgets},
  booktitle = {Proceedings of the corresponding venue},
  year = {2025}
}
```

Note: the paper is currently under review at MLSys 2026.
