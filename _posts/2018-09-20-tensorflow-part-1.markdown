---
layout: post
title: Tensorflow.js and Web Content
date: 2018-09-20 11:12:00-1400
description: Learning Tensorflow.js from scratch
---

<html>
  <head>
    <!-- Load the latest version of TensorFlow.js -->
    <script src="https://unpkg.com/@tensorflow/tfjs"></script>
    <script src="https://unpkg.com/@tensorflow-models/mobilenet"></script>
    <!-- Add the k-nearest neighbor library -->
    <script src="https://unpkg.com/@tensorflow-models/knn-classifier"></script>
  </head>
  <body>
    <div id="console"></div>
    <!-- Add an image that we will use to test -->
    <video autoplay playsinline muted id="webcam" width="224" height="224"></video>
    <button id="class-a">Add A</button>
    <button id="class-b">Add B</button>
    <button id="class-c">Add C</button>
    <!-- Load index.js after the content of the page -->
    <script src="/assets/js/webtfvid.js"></script>
  </body>
</html>

