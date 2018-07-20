# samoonprai-bot

## Steps to Reproduce the Project
1. pip install https://github.com/Jirayut558/spacymodel/raw/master/spacy-2.1.0.dev1.tar.gz
1. pip install https://raw.githubusercontent.com/Jirayut558/spacymodel/master/ay_model.tar.gz
1. pip install -r requirements


## Production Steps
1. Set environment variables by adding these:
    + **VERIFY_TOKEN** which is a plain string you set when connecting with the webhook of the Facebook App 
    + **PAGE_ACCESS_TOKEN** you can get it from Facebook for Developers -> Products -> Messenger -> Settings -> Token Generation -> Select a Page
    + Do not forget to set Webhook settings about these events:
        + **messages**
        + **messaging_postbacks**
1. Edit subscription of the Page's webhook like this:
    + **Callback URL**: \<URL\>/webhook
    + **Verify Token**: a plain text you set which must be matched with the environment variable in step 1
