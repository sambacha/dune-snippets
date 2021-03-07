#!/bin/sh
rm CHANGELOG*
rm VERSION*
export CI=true
npx semantic-release
