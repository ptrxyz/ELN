################################################################################
# RUBY                                                                         #
################################################################################
FROM ubuntu:21.04 AS ruby
# set timezone
ARG TZ=Europe/Berlin
RUN ln -s /usr/share/zoneinfo/${TZ} /etc/localtime

# install system packages
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y --autoremove --fix-missing install \
    build-essential git \
    curl `# for pandoc` \
    libssl-dev libreadline-dev zlib1g-dev `# for building ruby`

# for the gems
RUN apt-get -y --autoremove --fix-missing install \
    cmake libpq-dev swig \
    libboost-serialization-dev \
    libboost-iostreams-dev \
    libboost-system-dev \
    libeigen3-dev \
    libmagickcore-dev \    
    python3-dev libsqlite3-dev

# install ruby
RUN cd /tmp && \
    curl https://cache.ruby-lang.org/pub/ruby/2.6/ruby-2.6.8.tar.bz2 2>/dev/null | tar xvj

RUN cd /tmp/ruby-2.6.8 && \
    ./configure --enable-shared --prefix /ruby && \
    make -j$(getconf _NPROCESSORS_ONLN) && \
    make install
RUN find /ruby/bin | xargs -i ln -s {} /bin/
RUN gem install bundler -v 1.17.3

# install the gems
COPY ./src /src
RUN cd /src && RAILS_ENV=production bundle install --jobs=$(getconf _NPROCESSORS_ONLN)

## hacky way to make cleanup of openbabel possible. should be obsolete
## as soon as https://github.com/ComPlat/openbabel-gem/pull/2 is merged.
#RUN cd /ruby/lib/ruby/gems/2.6.0/bundler/gems/openbabel-gem-3e25548fd95c/openbabel/build && \
#    cmake .. -DCMAKE_INSTALL_PREFIX=/openbabel/ -DBUILD_GUI=OFF -DENABLE_TESTS=OFF -DRUN_SWIG=ON -DRUBY_BINDINGS=ON
#RUN cd /ruby/lib/ruby/gems/2.6.0/bundler/gems/openbabel-gem-3e25548fd95c/openbabel/build && \
#    make -j$(getconf _NPROCESSORS_ONLN) && \
#    make install
#RUN tar cf /raw /openbabel 
#RUN cd /ruby/lib/ruby/gems/2.6.0/bundler/gems/openbabel-gem-3e25548fd95c/ && rm -rf openbabel && tar xf /raw 

################################################################################
# NODE                                                                         #
################################################################################
FROM ubuntu:21.04 AS node
# set timezone
ARG TZ=Europe/Berlin
RUN ln -s /usr/share/zoneinfo/${TZ} /etc/localtime

# install system packages
RUN apt-get -y update && apt-get -y upgrade

# wget: to download node
# git: for "npm install"
RUN apt-get -y install wget git 

ARG NODE_VERSION=v14.16.0
ARG NODE_STRING=node-${NODE_VERSION}-linux-x64
RUN wget -O /tmp/node.tar.gz https://nodejs.org/dist/${NODE_VERSION}/${NODE_STRING}.tar.gz
RUN cd / && tar xfvz /tmp/node.tar.gz
RUN mv ${NODE_STRING} /node
RUN PATH=/node/bin:$PATH npm install -g yarn
RUN find /node/bin/ | xargs -i ln -s {} /bin/

COPY ./src /src
RUN cd /src && yarn install --production --modules-folder /node/lib/node_modules

################################################################################
# MAIN                                                                         #
################################################################################
FROM ubuntu:21.04 AS main
# set the shell. we need `[[` and `echo -e`...
SHELL ["/bin/bash", "-c"]

# set timezone
ARG TZ=Europe/Berlin
RUN ln -s /usr/share/zoneinfo/${TZ} /etc/localtime

# locales
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
RUN echo -e "LANG=${LANG}\nLC_ALL=${LANG}" > /etc/locale.conf && \
    echo "${LANG} UTF-8" > /etc/locale.gen

# install system packages
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y --autoremove --fix-missing install \
    libboost-serialization1.74.0 \
    libboost-iostreams1.74.0 \
    curl `# for pandoc` \
    postgresql-client \
    inkscape `# this installs python3` \
    xvfb \
    imagemagick \
    locales \
    tini

RUN PANDOC_VERSION=2.10.1 && \
    pandoc_pkg="pandoc-${PANDOC_VERSION}-1-amd64.deb" && \
    curl -o /tmp/${pandoc_pkg} -L https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/${pandoc_pkg} && \
    dpkg -i /tmp/${pandoc_pkg} && rm /tmp/${pandoc_pkg}

# install ruby
COPY --from=ruby /ruby /ruby
COPY --from=node /node /node
ENV NODE_PATH=/node/lib/node_modules

# symlink the binaries to /bin
RUN find /ruby/bin /node/bin -not -type d | xargs -i ln -s {} /bin/

# sanity checking
RUN ruby -v && bundle -v && gem -v && rails -v && node -v && npm -v && npx -v && yarn -v   ``

# copy the app
COPY ./src /chemotion/app/
ENV RAILS_ENV=production
# RUN cd /chemotion/app && bundle install --jobs=$(getconf _NPROCESSORS_ONLN)
# RUN cd /chemotion/app && yarn install --production --modules-folder /node/lib/node_modules

# check dependencies 
COPY ./lddcheck /bin/lddcheck
RUN find /ruby/lib/ruby/gems/ /node/lib/node_modules -iname '*.so' -type f -exec lddcheck \{\} \; | tee /lddlog.txt | grep not | grep -v libRD | sort | uniq

# copy config template to image
RUN mkdir -p /shared /template
RUN for foldername in uploads log public config tmp; do echo "Exposing [${foldername}] ..."; \
    mkdir -p /chemotion/app/${foldername}; \
    mv /chemotion/app/${foldername} /template; \
    ln -s /shared/eln/${foldername} /chemotion/app/${foldername}; \
    done

RUN for filename in .env; do echo "Exposing [${filename}] ..."; \
    folder=$(dirname ${filename}); \
    fname=$(basename ${filename}); \
    mkdir -p /chemotion/app/${folder} /template/${folder} 2>/dev/null || true; \
    mv /chemotion/app/${filename} /template/${folder}/${fname} 2>/dev/null || true; \
    ln -s /shared/eln/${filename} /chemotion/app/${folder}/${fname}; \
    done

RUN mv /chemotion/app/.env.production.example /template/.env

# clean up some unnecessary files
RUN find /template /chemotion/app -iname '*.gitlab' -print -delete -or -iname '*.travis' -print -delete 

RUN mkdir -p /etc/scripts

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y --autoremove --fix-missing install \
    python3-click \
    python3-yaml

# Lines needed to be compatible with docker 1.26+ versions of tini
# as of Apr. 28, we use cmd.sh as init system.
RUN ln -s /usr/bin/tini /tini
RUN ln -s /etc/scripts/cmd.sh /init
ENTRYPOINT ["/usr/bin/tini", "--", "/init"]



#####

# info: stats ausgeben
# init: std config auf shared volume schreiben 
# upgrade: ...
# backup: backupen d. db, d. daten, d. config
# start-eln:      started das eln
# start-worker:   started den worker
# user-shell:     drop to user shell
# cmd | bash | shell | root-shell: drops to root shell



###


# config:
#   if (1stStart) exposeConfigFiles(STD.CONF)
#   if (followUpStart) pass
#   if (upgrade) CheckConfigIfCompatible()

# datenbank prüfen:
#   while (tryToConnect(db) != true and fail < 10); sleep 10; fail++; done
#   if (fail == 10) error "DB missing"

# if (istELN) bundle exec rails ...
# if (worker) bundle exec worker ...
