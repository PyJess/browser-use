from langchain_openai import ChatOpenAI
import asyncio

async def a_invoke_model(gpt, msgs):
    return await gpt.ainvoke(msgs)

async def a_gen_instruction(feature_file_path):
    """Generate instructional text from a single test case."""

    with open("browser-use/Gen_Intent/system_prompt.txt", 'r') as file:
        system_prompt = file.read()
    with open("browser-use/Gen_Intent/user_prompt.txt", 'r') as file:
        user_prompt = file.read()
    with open(feature_file_path, 'r') as file:
        feature_file = file.read()

    user_prompt_filled = user_prompt.replace("{feature_file}", feature_file)

    gpt = ChatOpenAI(model="gpt-4.1", temperature=0.1)
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt_filled}]
    
    response = await a_invoke_model(gpt, messages)
    return response.content



async def main():
    feature_file_path = input("Enter the path to the file: ")
    print(await a_gen_instruction( feature_file_path))

if __name__ == "__main__":
    asyncio.run(main())