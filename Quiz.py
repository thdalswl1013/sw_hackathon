import streamlit as st
from PIL import Image
import time

def quiz():
    st.title("QUIZ")
    st.text("***********************************************************************************")
    
    st.text_area("Q1.",""" If you hold your pet in your arms when you go for a walk with your pet, you don't need a leash.
    (반려동물과 산책할 때 반려동물을 품에 안고 있다면, 목줄이 없어도 된다.)""")
    q1 = st.radio("",("O","X"))     # x
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q2.",""" Subsidies are available for those who adopt an animal that is being cared for by an animal protection center directly operated by a local government or entrusted with a designated animal protection center.
    (지방자치단체에서 직접 운영하거나 위탁 지정한 동물보호센터에서 보호 중인 동물을 입양한 경우에 지원금을 받을 수 있다.)""")
    q2 = st.radio("",("O","X "))    # o
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q3.",""" If you do not register your dog with the city/gu office, you will be fined up to 600,000 won.
    (본인이 기르는 반려견을 시·구청에 등록하지 않았다면 60만 원 이하의 과태료가 부과된다.)""")
    q3 = st.radio("",("O","X  "))   # o
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q4.",""" Fierce Dogs have the right as companion animals, so they can enter wherever other companion animals are allowed. 
    (맹견도 반려동물로써의 권리가 있으므로, 다른 반려동물들이 출입 가능한 모든 곳에 맹견 또한 출입이 가능하다.)""")
    q4 = st.radio("",("O","X   "))  # x
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q5.",""" In the case of a fierce dog causing physical harm to humans, it is possible to quarantine the dog with the consent of the owner.
    (맹견이 사람에게 신체적 피해를 주는 경우, 소유자의 동의를 얻으면, 맹견에 대한 격리조치가 가능하다.)""")
    q5 = st.radio("",("O","X    ")) # x
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q6.",""" If a person dies as a result of violating the use of a leash for a dog or violating a leash or muzzle for a dog, imprisonment for not more than 3 years or a fine of not more than 30 million won will be imposed. fine is imposed
    (반려견의 목줄 착용 위반 및 맹견의 목줄·입마개 착용 위반으로 인한 사고로 사람이 사망할 경우, 3년 이하의 징역 또는 3000만원 이하의 벌금이 부과되며 부상 시에는 2년 이하의 징역 또는 2000만원 이하의 벌금이 부과된다.)""")
    q6 = st.radio("",("O","X     "))    # o
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q7.",""" If you are adopting a new pet, it is preferable to have an “older” cat or dog rather than a kitten or puppy.
    (만약 애완동물을 새로 입양하려 한다면, 새끼 고양이나 새끼 강아지를 들이는 것보다 “좀 나이가 든” 고양이나 개를 들이는 것이 바람직하다.) """)
    q7 = st.radio("",("O","X      "))   # o
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q8.",""" 다음 빈칸에 들어갈 단어로 알맞은 것은?
    [                  ]는동물보호·복지 대국민 온라인 교육 플랫폼이다. 농식품부는 2018년부터 ‘동물보호복지 온라인’ 누리집을 통해 반려동물 관련업 종사자와 맹견소유자 등에게 의무교육을 제공해 왔다. 최근 반려동물을 양육하는 가구가 증가되는 상황을 고려, 의무교육프로그램 외에도 동물병원, 동물약국 등 다양한 정보를 포함하는 플랫폼으로 누리집을 전면 개편했다. [                  ]에는 수의사와 훈련사가 참여하는 반려견 입양 전 교육과 초등학생에게 생명 존중의 의미를 가르치는 인성교육 프로그램이 신설됐다. 아울러 동물병원, 동물약국, 미용업소, 위탁관리업소, 동물보호센터의 위치정보를 제공해 내 주변에서 이용 가능한 시설을 검색할 수 있는 편의 기능도 제공하고 있다.
    """)
    q8 = st.text_input('write answer', '')  # 동물사랑배움터
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q9.",""" 강아지의 중성화수술 권장 시기는 언제일까?
    """)
    q9 = st.radio("",("1) 생후 1개월 ~ 2개월","2) 생후 5개월 ~ 9개월","3) 생후 1년 ~ 2년","4) 생후 2년 ~ 3년","5) 생후 3년 ~ 4년"))
    # 2
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q10.",""" 다음 중 강아지가 먹으면 안되는 음식으로 옳지 않은 것은?
    """)
    q10 = st.radio("",("1) 초콜릿","2) 양파, 파, 마늘", "3) 계란", "4) 우유, 유제품", "5)호두, 아몬드, 마카다미아, 피스타치오 등의 견과류"))
    # 3
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q11.",""" 다음 중 강아지 입양에 대한 설명으로 옳지 않은 것은?
    """)
    q11 = st.radio("",("1) 강아지를 입양할 때는 외모가 내가 원하는 반려동물의 모습인지를 판단하는 것이 제일 중요하다."
    ,"2) 일반적으로 어미나 형제와 함께 충분한 시간을 보낸 후 생후 8-12주령에 입양하는게 가장 좋다."
    ,"3) 공공장소, 공원 등에서 구조되거나 유기된 애완동물은 유기동물보호소(동물보호센터)에 보호되는데 일정기간이 지나도 소유자가 나타나지 않으면 일반인이 분양받을수 있다."
    ,"4) 펫샵이나 동물판매업자에게 구입할경우 먼저 그 판매업소가 등록이 되어있는지 확인해야 한다."
    ,"5) 펫샵에서 구입할 경우 1차 이상 예방접종을 한 강아지인지, 건강한 상태인지 주의깊게 확인하는 것이 좋다."))
    # 1
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q12.",""" 다음 중 강아지 목욕/샤워에 대한 설명으로 옳지 않은 것은?
    """)
    q12 = st.radio("",("1) 강아지는 일주일에 한 번 이상 꼭 씻어야 한다.",
    "2) 가능하다면 좁은 공간에서 목욕시킨다."
    ,"3) 목욕 전 털을 빗겨 엉키고 엉겨 붙은 털을 정리해준다."
    ,"4) 손톱 정리가 필요하다면 목욕 전에 다듬는 것이 좋다."
    ,"5) 강아지의 귀가 젖으면 중이염의 위험이 높아지게 된다.솜을 귀에 넣어 목욕 시 외이도에 물이 들어가지 않도록 한다."))
    # 1
    st.text('-----------------------------------------------------------------------------------------------------')

    st.text_area("Q13.",""" 빈칸에 들어갈 말로 알맞은 것은? 
    개는 육식동물로서 몸의 근육을 유지하는데 필수적으로 [           ]이 필요하다. 강한 뼈와 건강한 치아를 위해서는 칼슘과 인, 충분한 비타민의 주의 깊은 균형이 필요하며, 지방과 오일은 활성 및 대형견을 위한 중요한 에너지원이 된다.
    고양이도 육식동물로서  [           ]이 필요한데, 개보다도 2배 이상 필요하다. 비타민A는 필요하지만 지나치면 해로울 수 있고, 비타민 같은 물질인 타우린은 눈과 심장질환예방에 좋다.
    """)
    q13 = st.text_input('write answer.', '')  # 단백질
    st.text('-----------------------------------------------------------------------------------------------------')

    score = 0
    if st.button('SUBMIT->'):     
        # 정답 계산
        col1, col2, col3= st.columns(3)
        with col1:
            st.subheader("your score is")
        time.sleep(1)
        with col2:
            st.subheader(".....")
        time.sleep(1)
        with col3:
            st.subheader("...")
        time.sleep(1)

        if q1 == "X":
            score += 1
        if q2 == "O":
            score += 1
        if q3 == "O":
            score += 1
        if q4 == "X   ":
            score += 1
        if q5 == "X    ":
            score += 1
        if q6 == "O":
            score += 1
        if q7 == "O":
            score += 2
        if q8 == "동물사랑배움터":
            score += 1
        if q9 == "2) 생후 5개월 ~ 9개월":
            score += 1
        if q10 == "3) 계란":
            score += 1
        if q11 == "1) 강아지를 입양할 때는 외모가 내가 원하는 반려동물의 모습인지를 판단하는 것이 제일 중요하다.":
            score += 1
        if q12 == "1) 강아지는 일주일에 한 번 이상 꼭 씻어야 한다.":
            score += 2
        if q13 == "단백질":
            score += 2

        st.title(score)

        if score <= 5:
            st.subheader("아직 부족합니다.")
            st.write("","아직 반려동물과 관련된 사전지식 및 상식이 많이 미흡한 상태이며, 좋은 반려인이 되기 위해서는 공부가 필요합니다. 오늘 틀렸던 문제들을 다시 한 번 살펴보고, 내가 몰랐던 점에 대해서 알아가고, 미흡했던 점에 대해 다시 공부하기 바랍니다.")
        elif score <= 10:
            st.subheader("멋집니다!")
            st.write("","반려동물을 키우기 위한 기본적인 지식은 갖춰져있으나, 좀 더 좋은 반려인이 되기 위해서는 조금 더 확장적인 지식이 필요합니다. 오늘 틀렸던 문제들을 다시 한 번 살펴보고, 내가 몰랐던 점에 대해 다시 알아가기 바랍니다.")
        elif score <=15:
            st.subheader("훌륭합니다!")
            st.write("","반려동물을 키우기 위해서 충분한 지식을 갖고있다고 보여집니다. 앞으로도 좋은 반려인으로 남아있길 바랍니다.")

        doggie = Image.open('static/doggie.png')
        st.image(doggie, width= 600)
