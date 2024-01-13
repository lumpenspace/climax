#!/bin/bash
{
    for i in "$@"; do
        echo -en "file://$(realpath ${i})\n"
    done
} | xclip -i -sel c -rmlastnl -t text/uri-list
