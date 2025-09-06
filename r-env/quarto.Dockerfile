FROM ubuntu:24.04

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    r-base r-base-dev \
    libnlopt-dev

RUN R -e "install.packages('knitr', repos='https://cran.rstudio.com/')"
RUN R -e "install.packages('rmarkdown', repos='https://cran.rstudio.com/')"
RUN R -e "install.packages('renv')"


ARG QUARTO_VERSION=1.6.8

RUN curl -L -O https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb \
&& dpkg -i quarto-${QUARTO_VERSION}-linux-amd64.deb

EXPOSE 8080