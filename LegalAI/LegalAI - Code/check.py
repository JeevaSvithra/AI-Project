import cohere
co = cohere.Client("Idet5MZLaP9o1PUu6YBud5xtYMBeQesbz0BgD8M5")
response = co.generate(
    model='c4ai-aya-23-8b',  # Example model
    prompt='Translate this text to Hindi.',
    max_tokens=50
)
print(response.generations[0].text)
