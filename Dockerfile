# Credits @NaytSeyd
FROM naytseyd/sedenbot:j1xlte

# Maintainer
MAINTAINER Ahmet Acikgoz <NaytSeyd@yandex.com>

# Zaman dilimini ayarla
ENV TZ=Europe/Istanbul

# Çalışma dizini
ENV PATH="/root/belali/bin:$PATH"
WORKDIR /root/belali

# Repoyu klonla
RUN git clone -b seden https://github.com/xpressqt/Telegram-UserBot /root/belali

# Oturum ve yapılandırmayı kopyala (varsa)
COPY ./sample_config.env ./sedenbot.session* ./config.env* /root/belali/

# Botu çalıştır
CMD ["python3","seden.py"]
