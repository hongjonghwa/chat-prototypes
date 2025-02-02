from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from models import ChatRequestBody
import os
from langgraph.prebuilt import create_react_agent
import json
from fastapi.responses import StreamingResponse
import time
import logging

###### STEP 1. 상태(State) 정의 ######
class State(TypedDict):
    # 메시지 정의(list type 이며 add_messages 함수를 사용하여 메시지를 추가)
    messages: Annotated[list, add_messages]

class ChatAgent:
    
    def __init__(self):
        # self.order_repo: OrderRepository = OrderRepository()

        ###### STEP 2. 노드(Node) 정의 ######
        self.llm : ChatOpenAI = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key = os.environ.get("OPENAI_API_KEY"))

        # ##### STEP 3. 그래프(Graph) 정의, 노드 추가 ######
        # # 그래프 생성
        # graph_builder = StateGraph(State)
        # # 노드 이름, 함수 혹은 callable 객체를 인자로 받아 노드를 추가
        # graph_builder.add_node("chatbot", self._chatbot)

        # ###### STEP 4. 그래프 엣지(Edge) 추가 ######
        # # 시작 노드에서 챗봇 노드로의 엣지 추가
        # graph_builder.add_edge(START, "chatbot")

        # # 그래프에 엣지 추가
        # graph_builder.add_edge("chatbot", END)

        # ###### STEP 5. 그래프 컴파일(compile) ######
        # # 그래프 컴파일
        # self.graph = graph_builder.compile()

        self.graph = create_react_agent(model=self.llm, tools=[])

        ...


    # 챗봇 함수 정의
    def _chatbot(self, state: State):
        # 메시지 호출 및 반환

        return {"messages": [self.llm.invoke(state["messages"])]}
    


    def chat_stream(self, body: ChatRequestBody):
        inputs = {"messages": [("user", body.messages[-1].text.strip())]}
        def generate(inputs):
            for s in self.graph.stream(inputs, stream_mode="values"):
                message = s["messages"][-1]
                # logging.info(message)
                if isinstance(message, tuple):
                    print(message)
                else:
                    message.pretty_print()
                    if message.type == "ai":
                        yield f"data: {json.dumps({'text': f'{message.content} '})}\n\n"
                    elif message.type == "human":
                        yield ""  

        response = StreamingResponse(generate(inputs), media_type="text/event-stream")
        # response.headers["Content-Type"] = "text/event-stream"
        # response.headers["Cache-Control"] = "no-cache"
        # response.headers["Connection"] = "keep-alive"
        # response.headers["Access-Control-Allow-Origin"] = "*"

        return response