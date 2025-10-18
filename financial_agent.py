from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

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

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=OpenAIChat(id="gpt-4-turbo"),
    instructions=[
        "Combine insights from both agents.",
        "Always include sources.",
        "Use tables where appropriate."
    ],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response(
    "Summarize analyst recommendations and share the latest news for NVIDIA.",
    stream=True
)