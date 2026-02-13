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
        task="""- Navigate to "https://www.poste.it/"
        - Accept cookies if present
        - Enter in "Area Personale"
        - Insert user.name as username
        - Show password
        - Insert Password01! as password
        - Click on "Accedi"
        - Verify that the login was successful or not
""",
        browser_session=browser_session,
        llm=ChatOpenAI(model="gpt-4.1"),  
    )
    history=await agent.run()
    print(history.model_actions())

asyncio.run(main())