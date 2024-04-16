import os

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import StrOutputParser
from langchain_openai import AzureChatOpenAI

load_dotenv()

# 1. 定义提示语模板
prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

# 2. 初始化 AI 模型
chat = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_CHAT_MODEL"),
)

# 3. 定义响应解析器
output_parser = StrOutputParser()

# 4. 构建 chains
chain = prompt | chat | output_parser

while True:
    content = input(">> ")

    if content.strip() == "exit":
        break

    # 5. 调用 chain，这里 `content` 就是构建填充到提示语模板中的 `content`
    result = chain.invoke({"content": content})

    print("AI Answer: ", result)
