FROM mysql:8.0-debian

RUN apt-get update \
    && apt-get install -y --no-install-recommends locales \
    && echo "ja_JP.UTF-8 UTF-8" | tee /etc/locale.gen \
    && locale-gen ja_JP.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV LANG=ja_JP.UTF-8 \
    LANGUAGE=ja_JP:ja \
    LC_ALL=ja_JP.UTF-8
