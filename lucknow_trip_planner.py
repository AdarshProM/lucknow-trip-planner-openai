# Planning a Trip to Lucknow with OpenAI API
# Author: Adarsh Singh
# Description: AI-powered travel guide for Lucknow using GPT-4o-mini

import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Initialize the OpenAI client
# Set your API key as environment variable: OPENAI_API_KEY
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Define the conversation with system context
conversation = [
    {
        "role": "system",
        "content": "You are a travel guide designed to provide information about landmarks that tourists should explore in Lucknow, Uttar Pradesh. You speak in a concise manner."
    },
    {
        "role": "user",
        "content": "What is the most famous landmark in Lucknow?"
    },
    {
        "role": "assistant",
        "content": "The most famous landmark in Lucknow is Bada Imambara."
    },
]

# Define a list of tourist questions
questions = [
    "How far away is the Hazratganj from the Bada Imambara (in driving miles)?",
    "Where is the Hotel Taj Mahal?",
    "What are the must-see artworks at the Lucknow State Museum?",
]

print("=" * 60)
print("🏛️  AI Travel Guide: Planning a Trip to Lucknow")
print("=" * 60)

# Loop through each question to generate responses
for question in questions:

    print(f"\n📍 Question: {question}")
    print("-" * 40)

    # Format the user input
    input_dict = {"role": "user", "content": question}

    # Add to conversation history
    conversation.append(input_dict)

    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_tokens=100
    )

    # Extract and print the response
    resp = response.choices[0].message.content
    print(f"🤖 AI Guide: {resp}")

    # Add response to conversation history (multi-turn memory)
    resp_dict = {"role": "assistant", "content": resp}
    conversation.append(resp_dict)

print("\n" + "=" * 60)
print("✅ Trip planning complete! Enjoy Lucknow!")
print("=" * 60)
