# Useful commands

### Export env

```
conda env export --from-history | grep -v "^prefix: " > build/conda/environment.yml
```

### Remove env

```
conda env remove -n <ENV_NAME> --all
```
