import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.functions import KernelArguments
from semantic_kernel.connectors.ai import PromptExecutionSettings
from semantic_kernel.prompt_template import InputVariable, PromptTemplateConfig

import os
from dotenv import load_dotenv

load_dotenv()


def azure_openai_settings_from_dot_env():
    deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    return deployment_name, api_key, endpoint


async def summary(report: str):
    deployment_name, api_key, endpoint = azure_openai_settings_from_dot_env()

    chat_completion_service = AzureChatCompletion(
        deployment_name=deployment_name,
        api_key=api_key,
        endpoint=endpoint,
        service_id="financial-report",
    )

    kernel = sk.Kernel()
    kernel.add_service(chat_completion_service)

    arguments = KernelArguments(
        report=report, settings=PromptExecutionSettings(max_tokens=5000)
    )
    analysis = """
        You are a financial analyst.
        You review financial reports and craft accurate executive summaries.
        Given the following report as a collection of tables in CSV format, craft a short summary.
        Your summary should be concise and informative.
        The executive summary should be no longer than 1 paragraphs and 500 words.
        Make it in the following format: Markdown.
        Here is the collection of tables you should analyze: {{$report}}
        """
    summary = await kernel.invoke_prompt(
        function_name="sample_zero",
        plugin_name="sample_plugin",
        prompt=analysis,
        arguments=arguments,
    )

    title = await kernel.invoke_prompt(
        function_name="sample_zero",
        plugin_name="sample_plugin",
        prompt="Find a title for this report: {{$report}}",
        arguments=KernelArguments(
            report=report, settings=PromptExecutionSettings(max_tokens=500)
        ),
    )

    return title, summary
