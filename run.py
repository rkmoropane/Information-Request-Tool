from openai import OpenAI
from decouple import config

import json
from information_request_tool import InformationRequestTool

congig = {
    "type_of_request": "[\"reservation_contacts - provides reservations information for services offered in both France and the French Antilles/Guyane, including contact numbers, open hours, and call rates for individual bookings and student preference accounts.\",\"cancellation_fee_invoice_request - handles requests for cancellation fee invoices, guiding the user on using electronic tickets as receipts, cancellation procedures, and necessary contacts.\",\"group_booking_affreightment_contact - offers information on group booking benefits for a minimum of 10 people traveling together, specific charter requests for official and business trips, and contact information for obtaining group rate quotes via an online form.\",\"refund_request - provides information and links for requesting refunds, including details for general and Pass Zen refund requests and guidance for package bookings through travel agencies.\",\"claim_request - gives access to filing a claim through a provided link to the claims form for handling complaints.\"]",
}


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
