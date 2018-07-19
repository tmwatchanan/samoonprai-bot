train nlu
    - update data/AIYAIntentTemplate.xlsx
    - run "python bot.py train-nlu"

train-dialogue
    - update story in data/story.md
    - update domain.yml
    - run "python bot.py train-dialogue"

Install Rasa and Spacy ay-model:TH
RUN pip3 install https://github.com/Jirayut558/spacymodel/raw/master/spacy-2.1.0.dev1.tar.gz
RUN pip3 install https://raw.githubusercontent.com/Jirayut558/spacymodel/master/ay_model.tar.gz