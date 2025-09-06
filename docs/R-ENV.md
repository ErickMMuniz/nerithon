# General Docker commands

```
docker build -t nb-quarto quarto.Dockerfile .
```

``` 
docker run -it --rm -p 8080:8080 -v .:/app nb-quarto:latest
```

### References

    - https://williamhuey.github.io/posts/quarto-in-docker-container/