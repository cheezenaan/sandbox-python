# Install rye
FROM debian:bookworm-slim as builder

WORKDIR /opt


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    curl

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"    

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash


FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm
COPY --from=builder /opt/rye /opt/rye

ENV PYTHONUNBUFFERED True

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"    

RUN rye config --set-bool behavior.global-python=true && \
    rye config --set-bool behavior.use-uv=true

RUN chown -R vscode $RYE_HOME
