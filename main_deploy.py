from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

# cloud 배포 시 .env를 같이 배포 하면 안됨. 클라우드 상에서 직접 입력 권장

#ChatOpenAI 초기화
llm = ChatOpenAI(model="gpt-4o-mini",  temperature=0.7)

#프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a helpful assistant."),
  ("user", "{input}")
])

#문자열 출력 파서
output_parser = StrOutputParser()

#LLM 체인 구성
chain = prompt | llm | output_parser

#제목
st.title("인공지능 시인")

#시 주제 입력 필드
content = st.text_input("시의 주제를 제시해주세요")
st.write("시의 주제는", content)

#시 작성 요청하기
if st.button("시 작성 요청하기"):
  with st.spinner('Wait for it...'):
      result = chain.invoke({"input": content + "에 대한 500자 짧은 시를 써줘"})
      st.write(result)