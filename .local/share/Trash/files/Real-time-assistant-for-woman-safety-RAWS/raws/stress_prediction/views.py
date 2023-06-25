from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import os
import csv
from csv import DictWriter
import random
from matplotlib import pyplot as plt, use
import numpy as np
import joblib
from sklearn.decomposition import KernelPCA

# Create your views here.
def index(request):
    return render(request,'index.html')


def new_data_user_input(user_data_yes_no):
    if user_data_yes_no=='Yes':
        return 1
    else:
        return 0

def prediction_stress(request):
    fname_back = request.POST.get('fname')
    lname_back = request.POST.get('lname')
    post_id_back = request.POST.get('post_id')
    subreddit_back = request.POST.get('subreddit')
    social_back = request.POST.get('social')
    confidence_back = request.POST.get('confidence')
    social_karnama_time_back = request.POST.get('social_karnama_time')
    question_1_back = request.POST.get('question_1')
    question_2_back = request.POST.get('question_2')
    question_3_back = request.POST.get('question_3')
    question_4_back = request.POST.get('question_4')
    question_5_back = request.POST.get('question_5')
    question_6_back = request.POST.get('question_6')
    question_7_back = request.POST.get('question_7')
    question_8_back = request.POST.get('question_8')
    question_9_back = request.POST.get('question_9')
    question_10_back = request.POST.get('question_10')
    question_11_back = request.POST.get('question_11')
    question_12_back = request.POST.get('question_12')
    question_13_back = request.POST.get('question_13')
    question_14_back = request.POST.get('question_14')
    question_15_back = request.POST.get('question_15')
    question_16_back = request.POST.get('question_16')
    question_17_back = request.POST.get('question_17')
    question_18_back = request.POST.get('question_18')
    question_19_back = request.POST.get('question_19')
    question_20_back = request.POST.get('question_20')
    question_21_back = request.POST.get('question_21')
    question_22_back = request.POST.get('question_22')
    question_23_back = request.POST.get('question_23')
    question_24_back = request.POST.get('question_24')
    question_25_back = request.POST.get('question_25')
    predict_text_back = request.POST.get('predict_text')
    print(predict_text_back)

    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    c = open(os.path.join(workpath, 'templates/train_model.sav'), 'rb')
    #print(c)

    #load the model
    model = joblib.load(c)

    user_data_set = []
    if subreddit_back == 'AlmostHomeLess':
        user_data_set.append(0)
    elif subreddit_back =='anxiety':
        user_data_set.append(1)
    elif subreddit_back=='assistance':
        user_data_set.append(2)
    elif subreddit_back=='domesticviolence':
        user_data_set.append(3)
    elif subreddit_back =='Financial_problem':
        user_data_set.append(4)
    elif subreddit_back=='food_pantry':
        user_data_set.append(5)
    elif subreddit_back == 'homeless':
        user_data_set.append(6)
    elif subreddit_back == 'Promotion_problem':
        user_data_set.append(7)
    elif subreddit_back=='ptsd':
        user_data_set.append(8)
    elif subreddit_back=='relationships':
        user_data_set.append(9)
    elif subreddit_back=='stress':
        user_data_set.append(10)
    else:
        user_data_set.append(11)
    
    user_data_set.append(social_back)
    user_data_set.append(confidence_back)
    user_data_set.append(social_karnama_time_back)

    user_data_set.append(new_data_user_input(question_1_back))
    user_data_set.append(new_data_user_input(question_2_back))
    user_data_set.append(new_data_user_input(question_3_back))
    user_data_set.append(new_data_user_input(question_4_back))
    user_data_set.append(new_data_user_input(question_5_back))
    user_data_set.append(new_data_user_input(question_6_back))
    user_data_set.append(new_data_user_input(question_7_back))
    user_data_set.append(new_data_user_input(question_8_back))
    user_data_set.append(new_data_user_input(question_9_back))
    user_data_set.append(new_data_user_input(question_10_back))
    user_data_set.append(new_data_user_input(question_11_back))
    user_data_set.append(new_data_user_input(question_12_back))
    user_data_set.append(new_data_user_input(question_13_back))
    user_data_set.append(new_data_user_input(question_14_back))
    user_data_set.append(new_data_user_input(question_15_back))
    user_data_set.append(new_data_user_input(question_16_back))
    user_data_set.append(new_data_user_input(question_17_back))
    user_data_set.append(new_data_user_input(question_18_back))
    user_data_set.append(new_data_user_input(question_19_back))
    user_data_set.append(new_data_user_input(question_20_back))
    user_data_set.append(new_data_user_input(question_21_back))
    user_data_set.append(new_data_user_input(question_22_back))
    user_data_set.append(new_data_user_input(question_23_back))
    user_data_set.append(new_data_user_input(question_24_back))
    user_data_set.append(new_data_user_input(question_25_back))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))
    user_data_set.append(format(random.uniform(0.0,20.0),".2f"))

    flidename = ['subreddit','social_timestamp','confidence','social_karma','question1','question2','question3','question4','question5','question6','question7','question8','question9','question10','question11','question12','question13','question14','question15','question16','question17','question18','question19','question20','question21','question22','question23','question24','question25','syntax_ari','lex_liwc_WC','lex_liwc_Analytic','lex_liwc_Clout','lex_liwc_Authentic','lex_liwc_Tone','lex_liwc_WPS','lex_liwc_Sixltr','lex_liwc_Diclex_liwc_function','lex_liwc_function','lex_liwc_pronoun','lex_liwc_ppron','lex_liwc_i','lex_liwc_we','lex_liwc_you','lex_liwc_shehe','lex_liwc_they','lex_liwc_ipron','lex_liwc_article','lex_liwc_prep','lex_liwc_auxverb','lex_liwc_adverb','lex_liwc_conj','lex_liwc_negate','lex_liwc_verb','lex_liwc_adj','lex_liwc_compare','lex_liwc_interrog','lex_liwc_number','lex_liwc_quant','lex_liwc_affect','lex_liwc_posemo','lex_liwc_negemo','lex_liwc_anx','lex_liwc_anger','lex_liwc_sad','lex_liwc_social','lex_liwc_family','lex_liwc_friend','lex_liwc_female','lex_liwc_male','lex_liwc_cogproc','lex_liwc_insight','lex_liwc_cause','lex_liwc_discrep','lex_liwc_tentat','lex_liwc_certain','lex_liwc_differ','lex_liwc_percept','lex_liwc_see','lex_liwc_hear','lex_liwc_feel','lex_liwc_bio','lex_liwc_body','lex_liwc_health','lex_liwc_sexual','lex_liwc_ingest','lex_liwc_drives','lex_liwc_affiliation','lex_liwc_achieve','lex_liwc_power','lex_liwc_reward','lex_liwc_risk','lex_liwc_focuspast','lex_liwc_focuspresent','lex_liwc_focusfuture','lex_liwc_relativ','lex_liwc_motion','lex_liwc_space','lex_liwc_time','lex_liwc_work','lex_liwc_leisure','lex_liwc_home','lex_liwc_money','lex_liwc_relig','lex_liwc_death','lex_liwc_informal','lex_liwc_swear','lex_liwc_netspeak','lex_liwc_assent','lex_liwc_nonflu','lex_liwc_filler','lex_liwc_AllPunc','lex_liwc_Period','lex_liwc_Comma','lex_liwc_Colon','lex_liwc_SemiC','lex_liwc_QMark','lex_liwc_Exclam','lex_liwc_Dash','lex_liwc_Quote','lex_liwc_Apostro','lex_liwc_Parenth','lex_liwc_OtherP','lex_dal_max_pleasantness','lex_dal_max_activation','lex_dal_max_imagery','lex_dal_min_pleasantness','lex_dal_min_activation','lex_dal_min_imagery','lex_dal_avg_activation','lex_dal_avg_imagery','lex_dal_avg_pleasantness','social_upvote_ratio','social_num_comments','syntax_fk_grade','sentiment']
    with open('stress_prediction/static/index/user_input_date.csv', 'w') as f:
      
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(flidename)
        write.writerow(user_data_set)
    
    user_dataset = pd.read_csv(r'stress_prediction/static/index/user_input_date.csv')

    X_train = user_dataset.iloc[:,:]
    X_train.dropna()

    #workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    #c = open(os.path.join(workpath, 'static/index/user_dataset.csv'), 'rb')

    #X_text = pd.read_csv(c)
    #X = X_text.drop(['post_id','text'], axis=1)
    #
    ##label encode
    #from sklearn.preprocessing import LabelEncoder
    #labelencoder = LabelEncoder()
    #X['subreddit'] = labelencoder.fit_transform(X['subreddit'])
    
    answer = model.predict(X_train)
    
    if answer>0:
        return render(request,'result_page.html',{'answer':'In Stress'})
    else:
        return render(request,'result_page.html',{'answer':'Not In Stress'})
