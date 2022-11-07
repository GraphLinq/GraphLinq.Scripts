#!/bin/bash

echo
echo "Set variables in .env or command line usage: ./0-create.sh <HOST> <USER> <PASSWORD>"
echo

if [ -f .env ]
then
    echo ".env found!"
    export $(cat .env | xargs)

    if [ $HELPER_HOST ]
    then
        echo "HOST: $HELPER_HOST"
    else
        echo "HOST NOT FOUND"
        exit
    fi
    if [ $HELPER_USER ]
    then
        echo "USER: $HELPER_USER"
    else
        echo "USER NOT FOUND"
        exit
    fi
    if [ $HELPER_PASS ]
    then
        echo "PASS: $HELPER_PASS"
    else
        echo "PASS NOT FOUND"
        exit
    fi
    if [ $HELPER_DB ]
    then
        echo "DB: $HELPER_DB"
    else
        echo "DB NOT FOUND"
        exit
    fi

    #mysql -h $HELPER_HOST -u $HELP_USER -p$HELP_PASS $helper_db < tables.sql

else
    echo ".env not found - attempting to grab command line args"

    if [ $1 ]
    then
        echo "Host: $1"
    else
        echo "Host is missing!"
        exit
    fi

    if [ $2 ]
    then
        echo "User: $2"
    else
        echo "User is missing!"
        exit
    fi

    if [ $3 ]
    then
        echo "Password: $3"
    else
        echo "Password is missing!"
        exit
    fi
    if [ $3 ]
    then
        echo "Database: $4"
    else
        echo "Database is missing!"
        exit
    fi
    

    #mysql -h $1 -u $2 -p$3 $4 < tables.sql
fi