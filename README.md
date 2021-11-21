# ChatBot
HandsUp chatbot for clothing business websites (Copy right : I have used fashion bug website here)

#features
I have implemented as The bot can be used to
1.	Order clothes
2.	Cancel the order
3.	Return the order
4.	Refund the payment

#installation
1. anaconda 
2. rasa open source


#Rasa Policies I used, 
1.	TEDPolicy 
    -Max history: 5, epochs:200, constrain similarities: true, batch_size:50, max training samples: 300
2.	MemoizationPolicy
    -Max history: 7
3.	RulePolicy


#Dataset and stories for the chatbot
-because I couldn’t find the dataset for Tamil language,I have used for some clothes details from fashion bug business website. And I had to work more on writing own NLU data (approximately more than 400 lines only for NLU data).

-To implement the chatbot I just have used my own stories since, I had some experienced with real world chatbots. 

To improve the bot performance I have written more stories, NLU training data and domain data as well. I have also written some actions for user entries validation. I also had practiced with fallback actions. You can see in the code.


