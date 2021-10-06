# ST0263-002_Sebastian_Arboleda

# Autor: Sebastian Arboleda Botero

Entregas de Tópicos espaciales en telemática.

## Documentación Producto 1

Producto 1 Instalaciones de wordpress

## **Instalaciones**

**Docker:**

```bash
  $ sudo apt-get update

  $ sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release

  $ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

  $ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  $ sudo apt-get update

  $ sudo apt-get install docker-ce docker-ce-cli containerd.io

  $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

  $ sudo chmod +x /usr/local/bin/docker-compose
```

**Certbot:**

```bash
  $ sudo apt install snapd
  $ sudo snap install core; sudo snap refresh core
  $ sudo snap install --classic certbot
  $ sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

**Nginx:**

```bash
$ sudo apt install nginx
```

## **Configurar Certbot**

```bash
  $ sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.sudominio.com --manual --preferred-challenges dns-01 certonly

  $ mkdir /home/user/wordpress

  $ mkdir /home/user/wordpress/ssl

  $ sudo cp /etc/letsencrypt/live/sudominio.com/* /home/user/wordpress/ssl/
```

## **Clonar repositorio y configurar**

```bash
  $ git clone https://github.com/SarboledaB/ST0263-002_Sebastian_Arboleda.git

  $ cd ST0263-TE_Telematica/Proyecto2/Producto1/

  $ sudo cp docker-compose.yml /home/user/wordpress/

  $ sudo cp nginx.conf /home/user/wordpress/

  $ sudo cp ssl.conf /home/user/wordpress/

  $ cd /home/user/wordpress/

  $ sudo docker-compose up --build -d
```

Ahora debe probar desde un browser

```
https://sudominio.com o https://www.sudominio.com
```
