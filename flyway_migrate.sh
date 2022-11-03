#!/bin/bash


flyway migrate -locations=${FLYWAY_LOCATIONS:filesystem:./db/migrations} -configFiles=${FLYWAY_CONFIG_FILES:./flyway.conf}

