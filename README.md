# Yatin's Bot - Text to Speech Response

## Overview

This Project is an Generative AI Chat bot that answer to your requests in both text & Speech.
Built on Serverless architecture, using Aws Lambda, This application uses the power of **Amazon polly** to Synthesis Speech from text.

## AWS Architecture Diagram

![gpt-aws- (1)](https://github.com/YatinGarg07/yatin-bot/assets/73949161/5bb034b2-3e35-48ca-9ad4-1e82763fb175)


You can find the architecture diagram for this project in the `architecture` directory.

## Usage

1. **Frontend Interaction:**
   - User interacts with the frontend interface, such as a chat window or input field.
   - Frontend sends HTTP requests to the OpenAI API endpoint, including the user's message.
   - OpenAI API processes the request and generates a response based on the input message & sends back the response to the frontend.
   - Frontend sends HTTP requests to the AWS API endpoint, including the response received from OpenAI.

3. **Communication with AWS Backend (Serverless Architecture):**
   - API receives the response from the frontend and processes it.
   - API sends request to **AWS lambda** to generate an audio file from the text response using **Amazon Polly**.
   - Upon successful generation of the audio file, a response including the URL of the audio file stored in S3 Bucket to the frontend.

4. **Audio Playback in Frontend:**
   - Frontend receives the URL of the audio file as Response, plays the audio file directly from the provided URL.
  
     ![image](https://github.com/YatinGarg07/yatin-bot/assets/73949161/56bcffa6-7827-405b-9379-c6971ba8e30f)

 ## Listen yourself    
<div align="center">
  <video src="https://github.com/YatinGarg07/yatin-bot/assets/73949161/9a9cfbd1-8cb6-4062-be11-4e1278efba3e"/>
</div>     


## Tech Stack

### Cloud

- AWS Lambda
- Amazon Polly
- Amazon S3

### Core
- Node js
- Python
- Streamlit(For frontend)
