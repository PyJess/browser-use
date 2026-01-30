import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import BrowserSession, Agent
from langchain_openai import ChatOpenAI
from Gen_Intent.GenInten import a_gen_instruction


# Feature 11 Check_Salvataggio_Richiesta

async def main():
    # feature_file_path = input("Enter the path to the file: ")
    # task= await a_gen_instruction( feature_file_path)
    # print(task)

    browser_session = BrowserSession(keep_alive=True)
    await browser_session.start()  
    # agent=Agent(task=task, 
    #             browser_session=browser_session, 
    #             llm=ChatOpenAI(model="gpt-4.1", temperature=0.1))

    agent = Agent(
        task="""- Navigate to "https://kinto-one-portal-es.tceu-kinto-stg.toyotaconnectedeurope.dev/"
        - Accept cookies if present
        - Select English language
        - Click Login Button 
        - Insert username@reply.it as email address
        - Show password
        - Insert Password01! as password
        - Continue 
        - Check if Login is successful
        - If Login is not successful, select Forgot Password
        - Insert the email address
        - Continue
""",
        browser_session=browser_session,
        llm=ChatOpenAI(model="gpt-4.1"),  
    )
    await agent.run()

asyncio.run(main())