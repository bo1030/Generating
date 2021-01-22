# Generating_maps
- Creating a map with satellite imagery
- server and application

## introduction
Generating_maps is a system that produces maps from aerial photographs through GAN.
there is 3 part(server, application, trainer).
trainer is for make models by Tensorflow
server make maps with image that application send and send maps to application.

## web crawler
collect map and aerial photographs by KAKAO maps.

    https://map.kakao.com/

## How To Crwaling
1. find locations with scale you want to collect
2. change the url
3. run the code

## training sets
1500 map and 1500 photographs are collected through web crawler

## training code
I referred to the Tensorflow document.

    https://www.tensorflow.org/tutorials/generative/pix2pix

## Server

## Application
