#!/bin/bash


build_ruby() {
	docker build --no-cache -t chemotion-build:latest-ruby -f dckr-ruby .
}

build_node() {
	docker build --no-cache -t chemotion-build:latest-node -f dckr-node .
}

build_eln() {
	docker build --no-cache -t chemotion-build:latest-eln -f Dockerfile .
}

while [ -n "$1" ]; do 
	case "$1" in
		ruby)
			build_ruby
			;;
		node)
			build_node
			;;
		eln)
			build_eln
			;;
		all)
			build_ruby
			build_node
			build_eln
			;;
		*)
			echo "Ignoring: $1"
	esac
	shift
done


