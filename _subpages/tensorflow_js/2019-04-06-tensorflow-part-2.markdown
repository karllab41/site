---
layout: post
title:  tensorflow in your browser
date: 2019-04-06 21:01:00
description: Getting your neural network to run on your website, starting with PoseNet
---

<html>

<head>
    <title>PoseNet - Camera Feed Demo</title>
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: black;
    }

    .footer-text {
        max-width: 600px;
        text-align: center;
        margin: auto;
    }

    @media only screen and (max-width: 600px) {
      .footer-text, .dg {
        display: none;
      }
    }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <div id="info" style="display:none">
    </div>
    <div id="loading">
        Loading the model...
    </div>

    <div id="main" style="display:none">
        <video id="video" playsinline="" style=" -moz-transform: scaleX(-1);
        -o-transform: scaleX(-1);
        -webkit-transform: scaleX(-1);
        transform: scaleX(-1);
        display: none;
        ">
        </video>
        <canvas id="output">
    </canvas></div>
    <div class="footer">
        <div class="footer-text">
            <p>
               You wanta POSE with THA POSE NET, MAAAAN? Check it out
                <br>
                <br> 
            </p>
        </div>
    </div>
    <script src="https://storage.googleapis.com/tfjs-models/demos/posenet/camera.d373f8d3.js"></script>
</body>

</html>
