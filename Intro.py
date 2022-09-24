
import streamlit as st
from PIL import Image
import time


def intro():
    catdog_image = Image.open('catdog.png')
    st.image(catdog_image, width= 400)
    st.title("CCA Intro")
    st.write("",""" 농림축산식품부에 따르면 국내 반려동물 보유 가구 비율은 전체의 28.1%로 국민 4명 중 1명 이상이 반려동물을 키우고 있는 것으로 나타났습니다. 
    
     반려동물을 키우는 사람이 증가함에 따라, 반려동물에 대해 무지한 상태임에도 귀엽고 눈이 즐겁다는 이유 하나만으로 반려동물을 데려왔다가, 생각보다 해야할 일이 많음을 알게 된 후 파양 및 양육 포기를 하는 상황 또한 증가하고 있습니다. 
    
    < 2021년, 동물보호에 대한 국민 의식 조사 결과, 반려동물 양육자의 열 명 가운데 네 명이 반려동물의 양육 포기나 파양을 고려한 경험이 있는 것으로 나타났다. ‘2021년 동물보호에 대한 국민 의식 조사 결과’에 따르면 반려동물 양육자를 대상으로 반려동물의 양육을 포기하거나 파양하는 것을 고려한 경험이 있는지를 물어본 결과, 반려동물 양육자의 26.1%가 경험이 있는 것으로 나타났다. 양육 포기 또는 파양 고려 이유로는 ‘물건 훼손·짖음 등 동물의 행동 문제’가 27.8%로 가장 많았다. 이어 ‘예상보다 지출이 많음’(22.2%), ‘동물이 질병에 걸리거나 사고를 당함’(18.9%), ‘이사·취업 등 여건이 변화’(17.8%)의 순이었다. > """)
    report_image = Image.open('report.png')
    st.image(report_image, width= 500)
    st.write("",""" 위 내용은 농림축산식품부, ‘2021년 동물보호에 대한 국민의식조사’ 결과에 대한 기사의 일부분을 발췌한 것입니다. 
      이 기사 내용에 따르면, 물건 훼손, 짖음, 동물의 행동 문제, 예상보다 지출이 많음 등의 이유로 반려 동물 양육자 열 명 가운데 네 명이 반려동물의 양육 포기 및 파양을 고려해봤다고 합니다. 
      
    하지만, 파양 및 양육 포기를 고려하게 한 이러한 이유들은 모두 반려동물을 입양하기 전 충분히 고려했어야 할 사항이며, 입양 전 조금 더 신중히 생각해보았다면 당연하게 받아들였을 내용입니다. 
      
    이렇듯 불충분한 정보만을 가지고 반려동물을 입양하고, 쉽게 파양 및 양육 포기를 고려/실행하는 이러한 문제점을 해소하고자, 반려동물과 관련된 정보를 얻을 수 있는 웹사이트를 만들게 되었습니다.

    반려동물에 대해 알아야 할 지식이나 상식 등을 충분히 알고 있는지 본인조차도 모를 수 있기 때문에, 반려동물과 관련된 퀴즈를 통해 반려동물에 대한 나의 지식 및 상식이 어느 정도인지 확인할 수 있게 하고, 이렇게 퀴즈를 풀어봄으로써 본인이 몰랐던 부분을 보완하고 개선할 수 있을 것이라는 기대 효과가 있습니다. 
      
    더 나아가, 만약 입양 전에 이를 풀어본다면, 반려동물에 대한 사전 지식이 미흡한 상태에서 동물을 입양하는 문제를 사전에 방지할 수도 있을 것입니다.  """)
