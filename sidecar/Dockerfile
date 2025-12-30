FROM php:8.2-apache

RUN apt-get update && apt-get install -y \
    git libxml2-dev libonig-dev \
    && docker-php-ext-install dom xml mbstring \
    && a2enmod rewrite \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html

# Create dummy lib to prevent 4get from loading real backend/fuckhtml
RUN mkdir -p dummy_lib/lib && \
    touch dummy_lib/lib/backend.php && \
    touch dummy_lib/lib/fuckhtml.php

COPY src/ /var/www/html/
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]
CMD ["apache2-foreground"]