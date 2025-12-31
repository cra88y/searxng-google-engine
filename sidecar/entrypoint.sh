#!/bin/bash
set -e

if [ ! -d "/var/www/html/4get-repo" ]; then
    echo "📥 Warning: 4get-repo not found, cloning as fallback..."
    git clone --depth 1 https://git.lolcat.ca/lolcat/4get.git /var/www/html/4get-repo
    chown -R www-data:www-data /var/www/html/4get-repo
fi

exec "$@"