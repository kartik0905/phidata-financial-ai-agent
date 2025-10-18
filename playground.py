from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
import phi
from phi.playground import Playground,serve_playground_app

load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the latest information.",
    model=OpenAIChat(id="gpt-4-turbo"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Financial AI Agent",
    model=OpenAIChat(id="gpt-4-turbo"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        )
    ],
    instructions=["Use Markdown tables for financial data."],
    show_tool_calls=True,
    markdown=True
)


app = Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)