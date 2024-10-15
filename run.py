from openai import OpenAI
from decouple import config

import json
from information_request_tool import InformationRequestTool

congig = {}


def setup_tools(verbose=True):
    tools = {}
    tool_descriptions = []
    to_use = [
        (InformationRequestTool, congig),

    ]
    for tool, configuration in to_use:
        instance = tool(configuration, verbose=verbose)
        tool_descriptions.append(instance.description)
        tools[instance.description["function"]["name"]] = instance.run
    return {"descriptions": tool_descriptions, "executable": tools}


def run_tool(tool_name, params, executable):
    print(f"tool: {tool_name}, {params}...")
    try:
        results = executable[tool_name](**params)

        return results["response"]
    except Exception as e:
        print(f"tool: Failed to run, {e}")
        return "tool failed"


if __name__ == "__main__":
    verbose = False

    client = OpenAI(api_key=config("OPENAI_API_KEY"))

    # Adding tools
    tool_data = setup_tools(verbose=verbose)
    tools = tool_data["descriptions"]

    def update_queries_with_tool(tool_results):
        for res in tool_results:
            queries.append(
                {
                    "tool_call_id": res.get("id", ""),
                    "role": "tool",
                    "name": res.get("name", ""),
                    "content": res.get("content", ""),
                }
            )

    queries = [
        {"role": "system", "content": "Your name is toolbox, you help test tools"}
    ]
    print("******************************************************\n")
    print(
        f"Bot: Welcome to tool box, I'm here to test your tools.\n to exit, just type 'exit'\n"
    )
    print("******************************************************\n")
    while True:
        print("-----------------------------------------------------------------------------------------------------------------------")
        query = input("\nYou: ")
        if query.lower() == "exit":
            print(f"Bot: Thank you for testing our tools, see you never!")
            break
        else:
            queries.extend([
                {"role": "user", "content": query},
                {'role': 'user', 'content': "email = 'rkmoropane@gmail.com', nom='Moropane'"}, 
                {'role': 'assistant', 'content': "understood"},
                ])
            response = client.chat.completions.create(
                model="gpt-4o-mini", messages=queries, tools=tools, tool_choice="auto"
            )

            response_message = response.choices[0].message
            if response_message.content:
                print(f"\nBot: {response_message.content}", flush=True)
            queries.append(response_message)
            tool_calls = response_message.tool_calls
            # check if the model wanted to call a function
            if tool_calls:
                if verbose:
                    print("## Tool calls made", flush=True)
                tool_responses = []
                for tool in tool_calls:
                    tool_name = tool.function.name
                    function_response = run_tool(
                        tool_name,
                        json.loads(tool.function.arguments),
                        tool_data["executable"],
                    )
                    tool_responses.append(
                        {"id": tool.id, "name": tool_name, "content": function_response}
                    )
                    if function_response != None:
                        print(
                            f"\n## Here is the function response:\n{function_response}\n"
                        )

                update_queries_with_tool(tool_responses)
                try:
                    second_response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=queries,
                    )
                    response_message = second_response.choices[0].message.content
                    print(f"\nBot: {response_message}\n")
                except Exception as e:
                    print(f"Error: {e}")
        print("-----------------------------------------------------------------------------------------------------------------------")
