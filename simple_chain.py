# Import libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# load environment variables
load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0.2
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'Generative AI'})

print(result)

chain.get_graph().print_ascii()
