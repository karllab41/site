---
layout: post
title: Tensorflow.js and Web Content
date: 2019-04-06 11:12:00-1400
description: Learning Tensorflow.js from scratch
---

I vaguely have any idea of what Node.js is. Angular.

Having started at Google a few months ago, I made it through some of my struggles with their codelabs, and got used to doing them. In fact, the documentation is pretty good for known, and I was pleasantly surprised when I found [one for Tensorflow.js](https://codelabs.developers.google.com/codelabs/tensorflowjs-teachablemachine-codelab/index.html).

## Javascript Console

The first step is actually to get a Javascript console. I realized this after following the instructions in the codelab until the fifth step. After I'd done all that, nothing happened, so I went back, and re-read. 

So, this console thing you can through a variety of ways. Google developers use the Chrome stuff: https://developers.google.com/web/tools/chrome-devtools/console/get-started.

<html>
  <head>
    <!-- Load the latest version of TensorFlow.js -->
    <script src="https://unpkg.com/@tensorflow/tfjs"></script>
    <script src="https://unpkg.com/@tensorflow-models/mobilenet"></script>
  </head>
  <body>
    <div id="console"></div>
    <!-- Add an image that we will use to test -->
    <video autoplay playsinline muted id="webcam" width="224" height="224"></video>
    <!-- Load index.js after the content of the page -->
    <script src="assets/js/tensorflow_post/webcam.js"></script>
  </body>
</html>

