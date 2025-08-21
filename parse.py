from openai import OpenAI
from openai import RateLimitError

client = OpenAI(api_key="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")


prompt_template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_openai(dom_chunks, parse_description):
    parsed_result = []

    for i, chunk in enumerate(dom_chunks, start=1):
        try:
            prompt = prompt_template.format(dom_content=chunk, parse_description=parse_description)
            
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [{"role": "system","content": "You are a data extractiion assistant."},
                            {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=1000
            )

            reply = response.choice[0].message["content"].strip()
            parsed_result.append(reply)
        
        except RateLimitError:
            return None, f"Quota exceeded on chunk {i}."
        except Exception as e:
            return None, f"OpenAI API failed on chunk {i}: {e}"
    return "\n".join(parsed_results),None



# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate

# model = OllamaLLM(model="llama3.2")

# def parse_with_ollama(dom_chunks, parse_description):
    # prompt = ChatPromptTemplate.from_template(template)
    # chain = prompt | model

    # parsed_results = []

    # for i, chunk in enumerate(dom_chunks,start=1):
        # try:
            # response = chain.invoke({"dom_content":chunk,"parse_description":parse_description})
            # parsed_result.append(response)
        # except Exception as e:
            # error_message=f"Error invoking chain on chunk {i}: {e}"
            # return None, error_message
        
    # return "\n".join(parsed_results), None
