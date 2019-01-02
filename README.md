# Weatherbot Tutorial (original video code)

This directory contains the full code of Weatherbot tutorial. You can use this code, modify it if you want, or you can test the models by simply loading the agent (run dialogue_management_model.py file).
Since this tutorial was recorded back in February 2018, it is using slightly older version of Rasa NLU and Rasa Core. If you prefer using the latest releases of these libraries check out
  [this](https://github.com/JustinaPetr/Weatherbot_Tutorial/tree/master/Full%20Code%20%5BLatest%20release%20of%20Rasa%20NLU%20and%20Rasa%20Core%5D) directory - it contains Weatherbot code and models compatible with the latest releases of Rasa NLU and Rasa Core (keep in mind that in some places the code will slightly differ from the one shown in the video).

Library versions used in the tutorial:

Rasa NLU version: 0.11.4

Rasa Core version: 0.8.2


## How to use this repo


### Training the NLU model

 To train and test the model run:  

``` python nlu_model.py ```

### Training the Rasa Core model

The biggest change in how Rasa Core model works is that custom action 'action_weather' now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Open a new terminal and train the Rasa Core model by running:  

``` python dialogue_management_model.py```  
 
3. Talk to the chatbot once it's loaded.  

### Starting the online training session:

The process of running the online session is very similar to training the Rasa Core model:
1. Make sure the custom actions server is running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Start the online training session by running:  

``` python train_online.py ```  

### Connecting a chatbot to Slack:
1. Configure the slack app as shown in the video (https://github.com/JustinaPetr/Weatherbot_Tutorial/tree/master/Full%20Code%20%5BLatest%20release%20of%20Rasa%20NLU%20and%20Rasa%20Core%5D)
2. Make sure custom actions server is running  
3. Start the agent by running run_app.py file (don't forget to provide the slack_token)  
4. Start the ngrok on the port 5004  
5. Provide the url: https://your_ngrok_url/webhooks/slack/webhook to 'Event Subscriptions' page of the slack configuration.  
6. Talk to you bot.  

