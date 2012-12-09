#!/bin/bash
FILENAME=$1
awk '!/xmlns|xs:schemaLocation/' $FILENAME > $FILENAME.parsed && mv $FILENAME.parsed $FILENAME
