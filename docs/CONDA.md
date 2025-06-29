# Useful commands

### Export env 

```
conda env export | grep -v "^prefix: " > environment.yml
```

```
conda list --explicit > spec-file.txt
```

### Remove env

```
conda env remove -n <ENV_NAME> --all
```
