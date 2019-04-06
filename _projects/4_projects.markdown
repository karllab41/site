---
layout: page
title: Some Tensorflow JS
description: First attempt
img: https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/SophieAndersonTakethefairfaceofWoman.jpg/220px-SophieAndersonTakethefairfaceofWoman.jpg
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
    <script src="https://storage.googleapis.com/tfjs-models/demos/posenet/737f311f31f1c925b2c718522b9c55a0.js"></script>
</body>

</html>
