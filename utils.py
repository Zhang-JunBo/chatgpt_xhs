from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu


def generate_xiaohongshu(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result
#openai_api_key="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"
#print(generate_xiaohongshu("大模型", openai_api_key))